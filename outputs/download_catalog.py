"""Download the public FUTNEXT catalog sequentially, retaining resumable page cache."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import shutil
import tempfile
import time

POSITIONS = {0:'GK',2:'RWB',3:'RB',5:'CB',7:'LB',8:'LWB',10:'CDM',12:'RM',14:'CM',16:'LM',18:'CAM',21:'CF',23:'RW',25:'ST',27:'LW'}
ROOT = Path(__file__).resolve().parent.parent

def extract_page(html):
    fragments = re.findall(r'self\.__next_f\.push\(\[1,("(?:\\.|[^"\\])*")\]\)', html)
    flight = ''.join(json.loads(fragment) for fragment in fragments)
    decoder = json.JSONDecoder()
    candidates = []
    for match in re.finditer(r'\{"count":', flight):
        try:
            value, _ = decoder.raw_decode(flight[match.start():])
        except ValueError:
            continue
        if isinstance(value, dict) and isinstance(value.get('players'), list) and 'currentPage' in value:
            candidates.append(value)
    if len(candidates) != 1:
        raise ValueError(f'Expected one catalog payload; found {len(candidates)}')
    return candidates[0]

def validate_page(page, number):
    if page['currentPage'] != number or page['count'] != len(page['players']):
        raise ValueError(f'Invalid page/count on page {number}')
    if not page['players'] or any(not isinstance(p.get('id'), int) for p in page['players']):
        raise ValueError(f'Missing player IDs on page {number}')

def fetch_page(number):
    with tempfile.TemporaryDirectory() as folder:
        body, headers = Path(folder)/'body', Path(folder)/'headers'
        for attempt in range(3):
            result = subprocess.run([shutil.which('curl') or shutil.which('curl.exe') or 'curl','--silent','--show-error','--location','--max-time','60','--dump-header',str(headers),'--output',str(body),'--write-out','%{http_code}','--header','Content-Type: application/json','--data-raw','{}',f'https://client-api.futnext.com/players?page={number}&locale=en'], capture_output=True, text=True)
            status = result.stdout.strip()
            if status in ('403','429'):
                detail = headers.read_text(errors='replace') if headers.exists() else ''
                retry_after = re.findall(r'(?im)^retry-after:\s*(.*)$', detail)
                raise RuntimeError(f'HTTP {status}; stopping. Retry-After: {retry_after or "not provided"}')
            if result.returncode == 0 and status == '200':
                return json.loads(body.read_text(encoding='utf-8'))
            if result.returncode == 0 and not status.startswith('5'):
                raise RuntimeError(f'HTTP {status} on page {number}')
            if attempt < 2:
                time.sleep(2 ** (attempt + 1))
        raise RuntimeError(f'Page {number} failed after three attempts: HTTP {status}; {result.stderr[:200]}')

def normalized(player):
    definition = player.get('definition', {})
    positions = player.get('positions', [])
    row = {'id':player['id'],'base_id':definition.get('id'),'name':definition.get('commonName') or ' '.join(filter(None,[definition.get('firstName'),definition.get('lastName')])),'rating':player.get('rating')}
    for key in ('rarity','club','nation','league'):
        row[key+'_id'] = player.get(key,{}).get('id')
        row[key] = player.get(key,{}).get('name')
    for label, preferred in [('position',True),('alternate_positions',False)]:
        selected = [p['id'] for p in positions if p.get('isPreferred') is preferred]
        row[label+'_ids'] = ';'.join(map(str,selected))
        row[label] = ';'.join(POSITIONS.get(p,str(p)) for p in selected)
    price = player.get('price') or {}
    row.update(price=price.get('cheapestPrice'),average_price=price.get('averagePrice'),price_timestamp=price.get('timeStamp'))
    return row

def write_json(path, value):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
    temporary.replace(path)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-pages',type=int,help='Limit new/existing pages for a pilot run')
    parser.add_argument('--refresh', action='store_true', help='Fetch every page again, ignoring the resumable cache')
    parser.add_argument('--delay',type=float,default=0.3)
    args = parser.parse_args()
    if args.max_pages is not None and args.max_pages < 1:
        parser.error('--max-pages must be positive')
    if args.delay < 0.3:
        parser.error('--delay must be at least 0.3 seconds')
    cache, out = ROOT/'work/catalog-cache', ROOT/'outputs'
    cache.mkdir(parents=True,exist_ok=True)
    out.mkdir(exist_ok=True)
    players, seen, fingerprints = [], set(), set()
    number, total, error, complete = 1, None, None, False
    try:
        while args.max_pages is None or number <= args.max_pages:
            path = cache/f'page-{number:04d}.json'
            cached = path.exists() and not args.refresh
            page = json.loads(path.read_text(encoding='utf-8')) if cached else fetch_page(number)
            validate_page(page,number)
            if total is not None and page['total'] != total:
                raise ValueError('Server total changed during download; retain cache and review before restarting')
            total = page['total']
            ids = [p['id'] for p in page['players']]
            fingerprint = hashlib.sha256(json.dumps(ids).encode()).hexdigest()
            if fingerprint in fingerprints or len(set(ids)) != len(ids) or seen.intersection(ids):
                raise ValueError(f'Repeated page or card ID on page {number}; no records silently discarded')
            fingerprints.add(fingerprint)
            seen.update(ids)
            players.extend(page['players'])
            if not cached:
                write_json(path,page)
            if number % 50 == 0 or number <= 2 or not page['hasNext']:
                print(f'Page {number}: {len(players)}/{total} cards',flush=True)
            if not page['hasNext']:
                if len(players) != total:
                    raise ValueError(f'Total mismatch: {len(players)} != {total}')
                complete = True
                break
            number += 1
            if not cached:
                time.sleep(args.delay)
    except (RuntimeError,ValueError,OSError) as exc:
        error = str(exc)
    if not complete:
        status = {'complete': False, 'error': error or 'Download stopped before the final page', 'records': len(players)}
        write_json(out/'catalog.status.json', status)
        print(json.dumps(status), flush=True)
        return 1
    rows = [normalized(p) for p in players]
    write_json(out/'catalog.raw.json',players)
    write_json(out/'catalog.json',rows)
    if rows:
        with (out/'catalog.csv').open('w',encoding='utf-8-sig',newline='') as stream:
            writer = csv.DictWriter(stream,fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    status = {'source':'https://client-api.futnext.com/players','fetched_at':datetime.now(timezone.utc).isoformat(),'complete':complete,'pages':len(fingerprints),'records':len(players),'unique_card_ids':len(seen),'declared_total':total,'error':error,'prices':'Public catalog snapshot; no separate price API calls'}
    write_json(out/'catalog.status.json',status)
    print(json.dumps(status),flush=True)
    return 1 if error else 0

if __name__ == '__main__':
    raise SystemExit(main())

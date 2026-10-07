# Explorador de jugadores EA FC

Catálogo con búsqueda, filtros por liga, equipo, nacionalidad, posición, género y rareza, paginación y exportación CSV. `index.html` contiene el catálogo comprimido y también se puede abrir directamente.

GitHub Actions descarga el catálogo completo de FUTNEXT cada hora, en el minuto 17, reconstruye la página y publica el resultado en GitHub Pages. También se ejecuta al subir cambios a `main` y manualmente desde Actions. GitHub puede retrasar las ejecuciones programadas.

Una descarga incompleta o fallida detiene la publicación y conserva la versión publicada. El género se infiere de la liga y el equipo; puede corregirse en el navegador.

El botón de actualización descarga directamente a ese navegador. Al abrir la página, se utiliza el catálogo publicado más reciente o la actualización local si es posterior. Para ver una nueva publicación en una pestaña ya abierta, recarga la página.

## Requisitos de publicación

En Settings → Pages debe elegirse GitHub Actions como origen. GitHub Pages en repositorios privados requiere un plan compatible. El repositorio no necesita hacerse público si la cuenta dispone de ese plan; la página publicada puede ser pública aunque el código sea privado.

## Generación local

Con Python 3.12 y curl instalados:

```sh
python outputs/download_catalog.py --refresh
python outputs/rebuild.py
```

Los archivos descargados y la caché se excluyen de Git. El flujo publica solo `index.html`.

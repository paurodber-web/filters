# Buscador de filtros de sniping

## Objetivo

Añadir a la página EAFC una vista que descubra combinaciones de filtros con varias cartas cuyo precio de referencia forme un grupo estrecho por encima de un mínimo configurable.

## Interfaz

- Nueva pestaña **Oportunidades** junto al explorador existente.
- Controles: precio mínimo X (monedas), mínimo de cartas (predeterminado 3), y un selector de tolerancia: fija en monedas (predeterminada y seleccionada inicialmente: 100 monedas) o porcentual (5 % inicial). Ambas tolerancias se pueden ajustar. También hay filtros opcionales de posición, nacionalidad, liga y equipo.
- Botón para buscar grupos y resultados ordenables por número de cartas o precio mínimo.
- Cada resultado muestra posición, nacionalidad, liga/equipo si se restringió, número de cartas, rango mínimo–máximo, mediana de precios y hora más reciente de los precios incluidos.
- Al abrir un resultado, la tabla existente muestra sus cartas y conserva sus acciones actuales.

## Criterio de agrupación

1. Primero se forma el grupo completo de cartas coincidentes usando posición principal o alternativa, nacionalidad y liga; el equipo opcional también restringe este grupo. Cada carta se cuenta una sola vez.
2. Se exige el mínimo de cartas sobre el grupo completo. No se quitan cartas por precio antes de contar ni antes de revisar el grupo.
3. Se calcula el precio más bajo de todas las cartas del grupo. Si alguna carta no tiene precio positivo, el grupo no se puede validar y se descarta. Si el precio más bajo no es estrictamente superior a X, se descarta el filtro completo, aunque otras cartas cuesten más. X nunca se usa para recortar el grupo.
4. Solo los grupos que superan el conteo y el precio mínimo pasan al análisis de similitud. Sus cartas se ordenan por precio ascendente y se forman bandas contiguas no solapadas, empezando por la más barata aún no asignada. En modo monedas, se añade la siguiente carta mientras `máximo - mínimo <= tolerancia en monedas`. En modo porcentaje, mientras `(máximo - mínimo) / mínimo <= tolerancia porcentual / 100`. Al superar el límite se cierra la banda y la siguiente carta inicia otra.
5. Solo se muestran las bandas con al menos el mínimo de cartas. El resultado conserva y muestra también el total y el precio más bajo del grupo completo que pasó el umbral X. La ordenación inicial favorece bandas con más cartas y después precios mínimos mayores.

## Datos y límites

Se usan `price` (precio más barato observado) y `price_timestamp` del catálogo ya descargado. La interfaz presentará las bandas como candidatas para revisar, no como beneficio garantizado: el catálogo no contiene operaciones cerradas, inventario de listados completo, coste de compra efectivo ni margen neto después de tasas.

## Integración y comprobación

El análisis se ejecuta en el navegador sobre el catálogo cargado y respeta los datos persistidos más recientes. No agrega solicitudes al API ni modifica la actualización programada. Comprobaciones: una banda que cumple umbral/tolerancia/mínimo aparece; una que falla cualquiera de ellos se excluye; las posiciones alternativas se reconocen sin duplicar cartas; abrir el resultado aplica correctamente sus filtros.

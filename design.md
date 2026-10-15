# Sistema de diseño web · Cinc Estrelles

**Documento de referencia para crear páginas nuevas con una identidad coherente y composiciones variadas.**  
Fuentes analizadas: `index (35).html` y `cinc-heroes-neteja-vic(2).html`.

## 1. Qué debe conseguir el sistema

Cada página debe sentirse parte de la misma marca por la tipografía, el color, la escala, el ritmo, el tono y la calidad de los detalles. La composición de cada sección debe responder a su contenido. No se debe resolver toda la web repitiendo tarjetas, columnas dobles o el mismo encabezado centrado.

La personalidad visual combina claridad de servicio, calma doméstica y una presencia empresarial actual. Debe sentirse cuidada y reconocible, sin caer en una estética de lujo, editorial, tecnológica o genérica.

## 2. Reglas de identidad

### Invariables

- Tipografía sans serif: **Plus Jakarta Sans**. Fallback: Arial, sans-serif.
- El contenido de los hero se redacta en catalán.
- Tinta azul marino para el texto principal; azul medio `#286D96` para acciones y énfasis puntuales.
- Fondos mayoritariamente blancos y azul hielo; lima como acento pequeño y luminoso.
- Titulares grandes, compactos, de peso medio-alto y con espaciado negativo.
- Márgenes amplios, alineación precisa y espacio suficiente alrededor de cada idea.
- Detalles gráficos sencillos y funcionales: líneas, numeración, etiquetas, flechas, separadores y controles.
- Movimiento breve y discreto; primero debe entenderse el contenido.

### Variables

- La estructura de cada sección.
- La proporción entre texto, imagen, datos e interacción.
- El uso de asimetría, ancho completo, columnas, listas, calendarios, formularios o composiciones tipográficas.
- La cantidad y el tratamiento de imágenes, según la historia de la página.
- El orden de los contenidos, según la intención de la página.

**Regla práctica:** mantener la identidad y variar el mecanismo visual. Una sección nueva no necesita “parecer otra caja” para pertenecer al mismo sitio.

## 3. Tokens visuales

### Colores

| Token | Valor | Uso |
|---|---:|---|
| Tinta | `#172C44` | Texto principal, títulos y fondos oscuros |
| Texto secundario | `#566779` | Párrafos secundarios y metadatos |
| Azul | `#286D96` | Botón principal, enlaces activos y énfasis; azul medio, sereno y menos saturado |
| Azul oscuro | `#1B5679` | Hover de acciones azules |
| Azul hielo | `#F1F6FA` | Fondo suave de sección |
| Azul pálido | `#E6EEFB` | Superficies destacadas y controles |
| Lima | `#D1EDC2` | Acento puntual, CTA o selección |
| Beige suave | `#EEE7DA` | Acento cálido, especialmente en el hero; usar con contraste suficiente |
| Verde tinta | `#355B2E` | Texto sobre lima cuando sea necesario |
| Blanco | `#FFFFFF` | Fondo y texto sobre tinta |
| Línea | `#D8E2EA` | Bordes y separadores |

**Proporción orientativa:** blanco y tonos hielo ocupan la mayor parte; la tinta sostiene el contraste; el azul aparece en puntos de acción y orientación; la lima se reserva para uno o dos acentos por vista. No usar todos los colores con el mismo peso.

### Color en títulos

- El título principal suele ir en tinta sobre fondos claros y en blanco sobre fondos oscuros.
- Se puede destacar **una palabra o una línea** en azul cuando ayude a fijar una idea o una ubicación. La palabra “Osona” del bloque de cobertura es una referencia de énfasis tipográfico.
- En secciones oscuras, el título permanece blanco; la lima se reserva para etiquetas, pequeños acentos o enlaces.
- En los hero, combinar blanco con un énfasis breve en beige suave `#EEE7DA`; comprobar el contraste sobre la fotografía.
- No alternar colores en cada palabra ni colorear títulos solo para decorar.
- Comprobar contraste y legibilidad en todos los tamaños.

### Tipografía y escala

Usar Plus Jakarta Sans en todo el sitio. La fuente se declara con peso variable o con los pesos necesarios disponibles. Mantener una voz tipográfica consistente; no introducir serif ni una segunda familia decorativa.

| Elemento | Referencia de tamaño | Peso / tratamiento |
|---|---:|---|
| H1 escritorio | `clamp(40px, 4.5vw, 70px)` | 600; interlineado 1.08; tracking `-.055em` |
| H1 móvil | `clamp(34px, 8.9vw, 53px)` | 600; interlineado 1.08; tracking `-.055em` |
| H2 | `clamp(34px, 3.8vw, 64px)` | 650; interlineado 1.13; tracking `-.045em` |
| H3 | `27px` | 650; ajustar fluidamente si el contexto lo requiere |
| H4 | `19px` | 650 |
| Texto base | `16px` | 450; interlineado 1.7 |
| Texto de apoyo | `14px` aprox. | 450; color secundario |
| Etiqueta / eyebrow | `10px` | 700; mayúsculas; tracking `.14em` |
| Botón | `12px` | 700 |
| Nota pequeña | `11px` | color secundario |

En móvil, reducir titulares de manera fluida y evitar saltos incómodos. No imponer saltos de línea rígidos en títulos largos. Mantener cada título en una o dos líneas cuando el contenido lo permita, sin comprimirlo hasta dificultar la lectura.

### Espaciado, contenedor y forma

- Unidad de espaciado: **8 px**. Escala base: `8, 16, 24, 32, 48, 72 px`.
- Contenedor: ancho máximo `1552px`; márgenes fluidos `clamp(20px, 4.5vw, 88px)`.
- Secciones: referencia vertical `clamp(70px, 7.7vw, 132px)`. Reducir solo cuando una pareja de bloques deba leerse como una unidad.
- Radios: 8 px general y 4 px en controles compactos. Evitar la acumulación de tarjetas muy redondeadas.
- Sombra: muy ligera, amplia y difusa (`0 16px 45px` a 8% aprox.). Usarla para separar capas, no como decoración general.
- Bordes: finos, de bajo contraste y útiles para agrupar información.
- En todas las secciones, cuidar igual que en los héroes de referencia la distancia entre grupos, la escala de los elementos dominantes, la alineación y el equilibrio entre espacio vacío y contenido. El espacio debe sentirse intencional, nunca como un hueco sin resolver.

## 4. Composición: cómo mantener variedad

Antes de maquetar una sección, definir su función en una frase y elegir un formato que la resuelva. Alternar formatos a lo largo de la página; no repetir el mismo patrón en dos secciones consecutivas.

### Formatos que la identidad puede admitir

- Titular y texto en una misma línea de lectura, alineados abajo.
- Manifiesto editorial breve con mucho aire y una sola frase dominante.
- Lista numerada o pasos con separadores, sin tarjetas.
- Comparativa con filas y etiquetas, no necesariamente dos paneles.
- Calendario o secuencia temporal.
- Configurador interactivo con resumen persistente.
- Sección oscura con declaraciones cortas y ritmo tipográfico.
- Composición fotográfica amplia con texto integrado o superpuesto con contraste suficiente.
- Formulario o campo de búsqueda incorporado a una composición geográfica o tipográfica.
- Preguntas agrupadas por tema con líneas divisorias.
- Cierre con una acción y un resumen contextual del servicio.

### Reglas de ritmo

- Alternar fondos blancos, hielo/pálidos, oscuros y lima con intención; no crear un patrón de franjas mecánico.
- No centrar todos los títulos. Elegir alineación según el contenido y alternarla cuando mejore el ritmo.
- No convertir cada servicio, beneficio o argumento en una tarjeta. Usar tarjetas solo cuando ayuden a comparar, seleccionar o interactuar.
- Evitar repetir la receta “eyebrow + título grande centrado + párrafo + tres cajas”.
- Dejar que imágenes, cifras, listas y controles cambien la silueta de la página.
- Mantener una jerarquía clara: cada sección debe tener un foco dominante y un siguiente paso comprensible.

### Acabado visual de referencia para todas las secciones

Las variantes 3, 4 y 5 del archivo de héroes son la referencia de **calidad visual para toda la página**, no solo para las cabeceras. Lo que se traslada a cada sección es el cuidado de la composición, la escala, el ritmo y el espaciado; no se replica el mismo layout ni sus recursos fotográficos.

- **Composición asimétrica, como en la variante 3:** se pueden combinar un elemento dominante, otro secundario y una nota breve en cualquier sección cuando la información lo justifique. El equilibrio viene de la escala y el espacio, no de centrarlo todo o encerrar cada cosa en una tarjeta.
- **Ritmo panorámico, como en la variante 4:** ordenar los elementos para que primero se entienda la idea y después se descubran imágenes, datos o detalles. Variar tamaños y alturas cuando aporte ritmo; cuidar especialmente la transición entre titular, texto, acción y visual.
- **Profundidad funcional, como en la variante 5:** usar capas, solapes o paneles flotantes para aportar contexto o utilidad. Cada capa debe tener un propósito, permanecer legible y no tapar el foco.

**Aplicación a cualquier sección:** dar presencia suficiente al elemento principal —imagen, titular, precio, selector, cita o dato—; separar visualmente grupos distintos; alinear con intención; limitar elementos secundarios; y usar recortes, fondos, líneas y formas como parte de una composición, no como decoración añadida. En secciones sin fotografía, la misma calidad se consigue con tipografía, datos, controles y espacio.

Los márgenes amplios no deben convertirse en huecos accidentales: cada pausa tiene que separar grupos o dejar respirar el foco. En móvil se conserva la jerarquía, se reordenan las piezas y se ajustan los solapes para que nada quede apretado ni cortado.

**No copiar literalmente:** la misma galería de tres imágenes, el mismo collage o la misma tarjeta flotante en todas las secciones. Cada sección debe elegir su propio mecanismo visual y desarrollarlo con el mismo cuidado.

## 5. Bloques de referencia que conviene conservar

Estos son los elementos del HTML con una personalidad visual suficientemente propia para reutilizarlos con fidelidad alta. En otras páginas se puede ajustar el texto, los datos o el color de fondo por contexto, pero debe conservarse su lógica de composición e interacción.

### A. Frecuencia con calendario (`#preus`)

**Preservar:** selector visible de frecuencia y descuento, acompañado por un calendario mensual que convierte la elección en algo tangible. La lectura combina elección, ejemplo temporal y navegación entre meses.

**Puede cambiar:** mes, contenido, número de opciones, densidad del calendario y detalles de precio.  
**No degradar a:** fila genérica de cinco tarjetas de precios sin relación temporal.

### B. Configurador con precio persistente (`#configura`)

**Preservar:** secuencia por pasos, controles claros, estimación que cambia con las elecciones y resumen de precio visible durante la configuración. El usuario entiende qué está eligiendo y cómo afecta al resultado.

**Puede cambiar:** preguntas, orden de pasos, controles y campos según el producto.  
**No degradar a:** formulario largo, calculadora aislada sin contexto o precio que desaparece al desplazarse.

### C. Estándares de servicio en fondo oscuro (`#per-que`)

**Preservar:** bloque de alto contraste, con declaraciones breves, numeración y una composición tipográfica que expresa la manera de trabajar. Funciona como pausa visual y elemento de marca.

**Puede cambiar:** número de principios y distribución interna, manteniendo el contraste y el tono.  
**No convertir en:** lista de iconos dentro de cajas oscuras.

### D. Política de materiales y contaminación cruzada (`#material`)

**Preservar:** el tema recibe una sección propia, explicado con claridad y tratado como una decisión de cuidado concreta. Debe incluir la elección sobre aspirador y mopa/equipo, quién los aporta y por qué.

**Puede cambiar:** el orden de explicación y la presentación de la elección.  
**No esconder en:** una nota al pie, una FAQ o un icono sin explicación.

### E. Cobertura geográfica tipográfica (`#zona`)

**Preservar:** nombre del territorio a escala grande como protagonista, acompañado de una frase local y un campo para indicar el municipio. La geografía se convierte en identidad visual en vez de ser una lista de localidades.

**Puede cambiar:** territorio, imagen de fondo integrada en las letras y tratamiento del formulario.  
**No reducir a:** una lista de municipios sin contexto.

### F. Cierre con resumen de solicitud (`#comencem`)

**Preservar:** CTA final sobre fondo lima, titular emocional breve y resumen visible del servicio/precio elegido. El botón continúa el flujo iniciado por el configurador.

**Puede cambiar:** copy, disposición en móvil y datos mostrados.  
**No dejar como:** una franja final con un botón genérico desconectado de la elección anterior.

### G. Hero como escena, no como plantilla

**Obligatorio:** imagen de borde a borde, a todo el ancho y alto del viewport (`100vw` × `100svh` como referencia), con `cover` y un encuadre que mantenga visible el punto focal. El hero no lleva gutters laterales que dejen franjas vacías.

**Header:** inicialmente transparente y superpuesto a la imagen. Al empezar el scroll pasa a un estado sticky; reduce de forma perceptible, pero moderada, su altura, padding y elementos de marca. La transición debe ser fluida y no provocar saltos de layout. Puede ganar un fondo claro translúcido o una superficie sólida discreta si hace falta para conservar legibilidad fuera del hero.

**Overlay y contenido:** usar una capa o gradiente tenue y localizado, no un velo oscuro uniforme. Debe conservar la fotografía y a la vez proporcionar contraste estable para titulares y texto en blanco y beige `#EEE7DA`. Colocar el texto sobre zonas de la imagen que mantengan ese contraste en escritorio y móvil; ajustar el gradiente al recorte responsivo.

**Acciones del hero:** el botón principal debe leerse sobre la foto con una superficie blanca o beige suave y texto tinta; una acción secundaria puede usar texto blanco o beige con un indicador claro. Mantener áreas táctiles cómodas, borde/foco visible y contraste suficiente. El azul del sistema sigue siendo el primario común del resto del sitio; estas variantes claras son específicas del hero.

**Puede cambiar:** la fotografía, el encuadre, la alineación del contenido y la geometría de la composición, siempre que se mantengan el fondo full bleed, la lectura limpia y los comportamientos del header y del overlay.

## 6. Elementos comunes de interfaz

### Botones y enlaces

- Botón primario en `#286D96` con texto blanco, radio de 7 px, altura mínima de 52 px, padding `18px 23px`, espacio amplio entre texto y flecha (`30px`), tamaño de texto `12px` y peso `700`.
- Hover del botón: azul `#1B5679` y elevación sutil de `2px`. Foco visible con contorno de `3px` en ocre `#C29148`, separado `5px` del control.
- Como segunda acción, preferir enlace de texto con flecha y buen espacio respecto al botón principal; evitar añadir otro botón relleno si no hace falta.
- Lima para acciones seleccionadas o llamadas especiales, no para todos los CTA.
- Flecha `↗` o similar puede señalar avance; dejar espacio suficiente para que se perciba como parte del botón y usarla de forma consistente.

### Etiquetas, numeración y divisores

- Eyebrows en mayúsculas, espaciado amplio y, cuando encaje, una pequeña línea horizontal.
- Numeración `01`, `02`, `03` para pasos o grupos; usarla para orientar, no como adorno repetitivo.
- Etiquetas sobre fondos pálidos con texto oscuro y forma compacta.
- Divisores de un píxel en línea suave para separar filas, preguntas o grupos.

### Campos y controles

Controles de tamaño cómodo, etiqueta visible, estado seleccionado evidente y foco accesible. El control debe explicar qué cambia. No depender solo del color para comunicar estados.

## 7. Movimiento y comportamiento

- Revelados de entrada suaves, en grupos pequeños y con escalonado leve. El contenido debe seguir disponible si JavaScript o la animación no se ejecutan.
- Duraciones de referencia: interacción rápida `200ms`, cambio de estado `350ms`, entrada `650ms`.
- Curva: `cubic-bezier(.22, 1, .36, 1)`.
- Priorizar `transform` y `opacity`; evitar animar dimensiones o propiedades que provoquen saltos de layout.
- Microinteracciones: cambios de estado claros en botones, selecciones, acordeones y precio. No añadir movimiento continuo ornamental.
- Respetar `prefers-reduced-motion` y permitir navegación completa con teclado.
- En el configurador, el resumen persistente debe evitar cubrir contenido y convertirse en una banda compacta en móvil.

## 8. Adaptación a móvil

- Una sola columna cuando las relaciones laterales dejen de ser legibles; reordenar contenido para preservar la historia de la sección.
- Mantener controles, botones y objetivos táctiles cómodos.
- Reducir espacios de forma progresiva, no eliminarlos. El aire es parte de la identidad.
- Recortar imágenes con intención y conservar el punto focal.
- No obligar a leer títulos diminutos, ni dejar palabras sueltas o titulares desbordados.
- La navegación, el resumen de precio, el calendario y las tablas deben seguir utilizables sin scroll horizontal accidental.

## 9. Accesibilidad y calidad

- Contraste suficiente entre texto y fondo; estados de foco visibles.
- Etiquetas conectadas a sus campos; controles con nombre accesible; acordeones y diálogos operables con teclado.
- Las imágenes informativas llevan texto alternativo útil; las decorativas quedan ocultas a tecnologías de asistencia.
- No comunicar precio, selección o estado exclusivamente con color.
- Usar HTML semántico y comprobar los estados vacíos, error, carga y selección.
- Las animaciones deben poder reducirse; ninguna información debe depender de que el usuario espere a una animación.

## 10. Lista de control antes de aprobar una página

1. ¿Se reconoce la identidad por tipografía, color, escala, aire y tono?
2. ¿Cada sección tiene una composición adecuada a su contenido?
3. ¿Se han evitado dos secciones consecutivas con el mismo layout?
4. ¿Los bloques de referencia mantienen su lógica distintiva cuando aparecen?
5. ¿Los colores de énfasis tienen una razón y no compiten entre sí?
6. ¿El usuario puede entender servicio, alcance, precio y siguiente paso sin esfuerzo?
7. ¿La página funciona a ancho móvil, con teclado y con movimiento reducido?
8. ¿Cada imagen, línea, caja o animación cumple una función concreta?

## 11. Instrucción breve para otro diseñador o IA

> Diseña una página nueva dentro del sistema de Cinc Estrelles. Conserva Plus Jakarta Sans, la paleta tinta/azul/hielo/lima, la escala tipográfica, el ritmo espacioso, los detalles funcionales y el tono claro y cercano descritos aquí. No reutilices un layout por defecto ni repitas cajas para cada contenido: decide la composición sección por sección y alterna formatos. Si incluyes el calendario de frecuencias, el configurador con precio persistente, el bloque oscuro de estándares, la política de materiales, la cobertura tipográfica o el cierre con resumen, conserva su mecanismo y su carácter visual. Lo demás puede variar mientras mantenga la identidad, la claridad y la calidad de acabado.

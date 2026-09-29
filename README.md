# Saloncito Aroa · Web

Landing page de **Saloncito Aroa**, centro de estética y bienestar en Piera (Barcelona).

Una sola página responsive (`index.html`) que une los dos diseños de referencia:

- **Escritorio**: cabecera con navegación, rejilla de servicios, historia, reseñas, reserva, tarjeta regalo, Instagram y contacto.
- **Móvil**: barra de navegación inferior con WhatsApp central, pestañas de servicios y reseñas deslizables, galería de imágenes.

Funciones: selector de idioma ES/CA, filtro de tratamientos por categoría, formulario de cita y tarjeta regalo que envían por WhatsApp, e indicador de abierto/cerrado según el horario.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `index.html` | La web |
| `assets/styles.css` | CSS de Tailwind compilado (generado, no editar a mano) |
| `tailwind.config.js` | Tokens del sistema de diseño (colores, tipografías, espaciados) |
| `DESIGN.md` | Guía del sistema de diseño "Serene Spa & Aesthetics" |
| `design/` | Exportaciones originales de escritorio y móvil, como referencia |

## Publicación

La web se publica en GitHub Pages: **https://saloncitoaroa.github.io/**

Para que la dirección sea la raíz de `saloncitoaroa.github.io` (sin `/saloncitoaroa/` al final), el repositorio debe llamarse exactamente `saloncitoaroa.github.io` (*Settings → General → Repository name*). Mientras se llame `saloncitoaroa`, la web queda en https://saloncitoaroa.github.io/saloncitoaroa/. Todas las rutas de `index.html` son relativas, así que funciona en ambos casos y también con un dominio propio en el futuro (se añadirá un archivo `CNAME`).

Cada push a `main` compila el CSS y despliega `index.html` y `assets/` (workflow `.github/workflows/pages.yml`). En *Settings → Pages*, la fuente debe ser **GitHub Actions**.

## Reseñas de Google

La valoración y el número de reseñas que muestra la web salen de `assets/reviews.json`. El workflow de publicación se ejecuta cada día (y en cada push a `main`) y, antes de publicar, `scripts/update-reviews.mjs` pide los datos actuales a Google Places API y reescribe ese archivo. Si falla o no hay clave, la web sigue mostrando los valores guardados en el repositorio (ahora 5,0 ★ y 48 reseñas).

Para activarlo:

1. En [Google Cloud Console](https://console.cloud.google.com/) crea un proyecto, activa **Places API (New)** y crea una clave de API (hace falta una cuenta de facturación, pero una consulta al día queda dentro del uso gratuito). Restringe la clave a *Places API (New)*.
2. En GitHub, *Settings → Secrets and variables → Actions*: crea el secreto `GOOGLE_PLACES_API_KEY` con la clave.
3. Opcional: la primera ejecución escribe en el log el Place ID del salón; guárdalo como variable `GOOGLE_PLACE_ID` en la misma pantalla para no depender de la búsqueda por nombre.

GitHub desactiva las tareas programadas si el repositorio pasa 60 días sin actividad; en ese caso se reactivan desde la pestaña *Actions*.

## Desarrollo

```bash
npm install
npm run dev     # recompila assets/styles.css al guardar
npm run build   # compilación minificada
```

Abre `index.html` en el navegador; no hace falta servidor. Después de cambiar clases en `index.html`, ejecuta `npm run build` y sube también `assets/styles.css`.

## Pendiente

- El logo ya es el definitivo (`assets/logo.png`). Las demás imágenes (fotos del local, Instagram, mapa) apuntan a URLs temporales de `lh3.googleusercontent.com` del diseño. Hay que sustituirlas por fotos reales guardadas en `assets/`.
- Confirmar tarifas, precios y textos con el salón.

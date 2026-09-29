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

La web se publica en GitHub Pages: https://yeray03izquierdo.github.io/saloncitoaroa/

Cada push a `main` compila el CSS y despliega `index.html` y `assets/` (workflow `.github/workflows/pages.yml`). En *Settings → Pages*, la fuente debe ser **GitHub Actions**.

## Desarrollo

```bash
npm install
npm run dev     # recompila assets/styles.css al guardar
npm run build   # compilación minificada
```

Abre `index.html` en el navegador; no hace falta servidor. Después de cambiar clases en `index.html`, ejecuta `npm run build` y sube también `assets/styles.css`.

## Pendiente

- Las imágenes (logo, fotos del local, Instagram, mapa) apuntan a URLs temporales de `lh3.googleusercontent.com` del diseño. Hay que sustituirlas por fotos reales guardadas en `assets/`.
- Confirmar tarifas, precios y textos con el salón.
git fetch origin claude/new-session-b41j28
git checkout claude/new-session-b41j28
ROOT=$(git commit-tree $(git hash-object -t tree /dev/null) -m "Initial commit")
git push origin $ROOT:refs/heads/main
git rebase --onto $ROOT --root
git push --force-with-lease origin claude/new-session-b41j28

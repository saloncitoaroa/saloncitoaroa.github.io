// Consulta la valoración y el número de reseñas de Google del salón y los
// guarda en assets/reviews.json, que la web lee al cargar.
//
// Necesita el secreto GOOGLE_PLACES_API_KEY (Places API "New").
// GOOGLE_PLACE_ID es opcional: si falta, se busca el negocio por nombre.
// Si algo falla, no toca el archivo y la web sigue con los últimos valores.

import { readFile, writeFile } from 'node:fs/promises';

const FILE = new URL('../assets/reviews.json', import.meta.url);
const QUERY = 'Saloncito Aroa, Carrer Piereta 3, Piera';
const key = process.env.GOOGLE_PLACES_API_KEY;
const placeId = process.env.GOOGLE_PLACE_ID;

async function fetchPlace() {
  const fields = ['id', 'displayName', 'rating', 'userRatingCount', 'googleMapsUri'];
  if (placeId) {
    const res = await fetch(`https://places.googleapis.com/v1/places/${encodeURIComponent(placeId)}`, {
      headers: { 'X-Goog-Api-Key': key, 'X-Goog-FieldMask': fields.join(',') },
    });
    if (!res.ok) throw new Error(`Place Details ${res.status}: ${await res.text()}`);
    return res.json();
  }
  const res = await fetch('https://places.googleapis.com/v1/places:searchText', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Goog-Api-Key': key,
      'X-Goog-FieldMask': fields.map(f => `places.${f}`).join(','),
    },
    body: JSON.stringify({ textQuery: QUERY, languageCode: 'es' }),
  });
  if (!res.ok) throw new Error(`Text Search ${res.status}: ${await res.text()}`);
  const place = (await res.json()).places?.[0];
  if (!place) throw new Error(`No se ha encontrado "${QUERY}"`);
  console.log(`Encontrado: ${place.displayName?.text} (Place ID ${place.id}). Guárdalo en la variable GOOGLE_PLACE_ID.`);
  return place;
}

if (!key) {
  console.log('Sin GOOGLE_PLACES_API_KEY: se mantienen los valores de assets/reviews.json.');
  process.exit(0);
}

try {
  const place = await fetchPlace();
  if (!Number.isInteger(place.userRatingCount) || typeof place.rating !== 'number') {
    throw new Error('La respuesta no trae rating/userRatingCount');
  }
  const current = JSON.parse(await readFile(FILE, 'utf8'));
  const data = {
    rating: Math.round(place.rating * 10) / 10,
    count: place.userRatingCount,
    url: place.googleMapsUri || current.url || '',
    updated: new Date().toISOString(),
  };
  await writeFile(FILE, JSON.stringify(data, null, 2) + '\n');
  console.log(`Reseñas actualizadas: ${data.rating} ★ · ${data.count} reseñas`);
} catch (err) {
  console.warn(`::warning::No se han podido actualizar las reseñas: ${err.message}`);
}

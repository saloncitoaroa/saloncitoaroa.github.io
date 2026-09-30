"""Genera aviso-legal.html, privacidad.html y cookies.html con la misma
cabecera y pie. Los textos están aquí; ejecuta `python3 scripts/legal-pages.py`
y después `npm run build` tras cambiarlos.

Los datos del titular que aún faltan se marcan con PENDIENTE(...) y se ven
resaltados en la página hasta que se rellenen en DATOS.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPDATED = "30 de septiembre de 2026"

# Datos del titular. Sustituye cada PENDIENTE(...) por el dato real.
DATOS = {
    "titular": "PENDIENTE(nombre y apellidos o razón social)",
    "nif": "PENDIENTE(NIF o CIF)",
    "domicilio": "PENDIENTE(domicilio fiscal)",
    "email": "PENDIENTE(email de contacto)",
    # Solo si el titular es una sociedad; déjalo vacío si es autónoma.
    "registro": "PENDIENTE(datos del Registro Mercantil, solo si es sociedad)",
}
CENTRO = "Carrer Piereta, 3, 08784 Piera (Barcelona)"
TELEFONO = "930 235 205"
WHATSAPP = "+34 669 264 120"


def dato(key):
    value = DATOS[key]
    if value.startswith("PENDIENTE("):
        return f'<mark class="legal-pending">{value[10:-1]}</mark>'
    return value


def page(slug, title, description, body):
    nav = "".join(
        f'<a class="hover:text-primary transition-colors{" text-primary font-medium" if s == slug else ""}" href="{s}.html">{t}</a>'
        for s, t in (("aviso-legal", "Aviso legal"), ("privacidad", "Privacidad"), ("cookies", "Cookies"))
    )
    html = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"/><meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>{title} · Saloncito Aroa</title>
<meta name="description" content="{description}"/>
<meta name="robots" content="noindex, follow"/>
<meta name="theme-color" content="#fff8f7"/>
<link rel="icon" type="image/png" href="assets/favicon.png"/><link rel="apple-touch-icon" href="assets/apple-touch-icon.png"/>
<link href="assets/styles.css" rel="stylesheet"/></head>
<body class="bg-surface font-body-md text-body-md text-on-surface antialiased">
<header class="bg-surface/85 shadow-[0_10px_30px_rgba(112,75,75,0.05)]"><div class="h-20 max-w-[1200px] mx-auto px-gutter flex items-center justify-between gap-space-sm">
<a class="flex items-center gap-space-xs shrink-0" href="./"><img alt="Logo Saloncito Aroa" class="h-12 w-auto object-contain" src="assets/logo.png"/><span class="font-headline-sm text-headline-sm text-primary">Saloncito Aroa</span></a>
<a class="inline-flex items-center gap-1 rounded-full bg-surface-container-low px-space-md py-space-xs font-label-md text-label-md uppercase text-primary hover:bg-primary hover:text-on-primary transition-all" href="./"><span class="material-symbols-outlined text-[18px]">arrow_back</span>Volver<span class="hidden sm:inline">&nbsp;a la web</span></a>
</div></header>
<main class="max-w-3xl mx-auto px-gutter py-space-xl">
<h1 class="font-headline-lg text-headline-lg-mobile md:text-headline-lg text-primary mb-2">{title}</h1>
<p class="font-body-sm text-body-sm text-on-surface-variant mb-space-lg">Última actualización: {UPDATED}</p>
<div class="legal">
{body.strip()}
</div>
</main>
<footer class="bg-surface-container-low"><div class="max-w-[1200px] mx-auto px-gutter py-space-md flex flex-col sm:flex-row items-center justify-between gap-space-sm font-label-md text-label-md text-on-surface-variant text-center">
<p>© 2026 Saloncito Aroa · {CENTRO}</p>
<nav class="flex flex-wrap justify-center gap-space-md">{nav}</nav>
</div></footer>
</body></html>
"""
    (ROOT / f"{slug}.html").write_text(html, encoding="utf-8")


registro = DATOS["registro"]
registro_html = f"<li><strong>Datos registrales:</strong> {dato('registro')}</li>" if registro else ""

page("aviso-legal", "Aviso legal",
     "Datos del titular y condiciones de uso de la web de Saloncito Aroa.", f"""
<h2>1. Titular de la web</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<ul>
<li><strong>Titular:</strong> {dato('titular')}</li>
<li><strong>NIF:</strong> {dato('nif')}</li>
<li><strong>Domicilio:</strong> {dato('domicilio')}</li>
<li><strong>Centro:</strong> Saloncito Aroa, {CENTRO}</li>
<li><strong>Teléfono:</strong> <a href="tel:930235205">{TELEFONO}</a> · WhatsApp: <a href="https://wa.me/34669264120">{WHATSAPP}</a></li>
<li><strong>Email:</strong> {dato('email')}</li>
{registro_html}
</ul>

<h2>2. Objeto</h2>
<p>Esta web presenta los servicios de estética y bienestar de Saloncito Aroa y permite pedir cita o encargar tarjetas regalo a través de WhatsApp o por teléfono. La web no realiza ventas ni cobros: cualquier reserva o compra se confirma directamente con el centro.</p>

<h2>3. Condiciones de uso</h2>
<p>El acceso a la web es gratuito y no requiere registro. Quien la visita se compromete a usarla de forma lícita y a no dañar su funcionamiento.</p>
<p>Los precios, promociones y descripciones de tratamientos son orientativos y pueden cambiar. Las condiciones aplicables son las que se confirmen en el centro al reservar.</p>

<h2>4. Propiedad intelectual</h2>
<p>Los textos, el logotipo, las fotografías y el diseño de esta web pertenecen a su titular o se usan con permiso, y no pueden copiarse ni reutilizarse sin autorización. Las tipografías Montserrat y Playfair Display se usan bajo la licencia SIL Open Font License y los iconos Material Symbols bajo la licencia Apache 2.0.</p>

<h2>5. Enlaces a otras webs</h2>
<p>La web enlaza con servicios externos (WhatsApp, Instagram y Google Maps). Al pulsar esos enlaces se sale de esta web y se aplican las condiciones y políticas de privacidad de cada servicio, de las que el titular no es responsable.</p>

<h2>6. Responsabilidad</h2>
<p>El titular procura que la información sea correcta y esté actualizada, pero no garantiza la ausencia de errores ni que la web esté disponible en todo momento, y no responde de los daños derivados de un uso indebido de la misma.</p>

<h2>7. Ley aplicable</h2>
<p>Este aviso legal se rige por la legislación española. Si eres consumidor, los conflictos se resolverán en los juzgados de tu domicilio.</p>
""")

page("privacidad", "Política de privacidad",
     "Cómo trata Saloncito Aroa los datos personales de sus clientes y de quienes visitan la web.", f"""
<h2>1. Responsable del tratamiento</h2>
<ul>
<li><strong>Responsable:</strong> {dato('titular')} (Saloncito Aroa)</li>
<li><strong>NIF:</strong> {dato('nif')}</li>
<li><strong>Dirección:</strong> {dato('domicilio')}</li>
<li><strong>Contacto para privacidad:</strong> {dato('email')} · Teléfono <a href="tel:930235205">{TELEFONO}</a></li>
</ul>

<h2>2. Qué datos tratamos</h2>
<p><strong>La web no recoge ni guarda datos personales.</strong> Los formularios de cita y de tarjeta regalo no envían nada a ningún servidor: solo preparan un mensaje que se abre en tu WhatsApp, y tú decides si lo envías.</p>
<p>Cuando nos contactas por WhatsApp, por teléfono o en el centro, tratamos los datos que nos facilitas:</p>
<ul>
<li>Nombre y teléfono.</li>
<li>Tratamiento, fecha y hora que solicitas, y las observaciones que nos escribas.</li>
<li>En las tarjetas regalo, el nombre de la persona que la recibe y la dedicatoria.</li>
<li>Si un tratamiento lo requiere, información de salud necesaria para realizarlo con seguridad (por ejemplo, alergias o contraindicaciones). Solo la pedimos cuando es imprescindible y con tu consentimiento expreso.</li>
</ul>

<h2>3. Para qué y con qué base legal</h2>
<ul>
<li><strong>Gestionar tus citas, consultas y tarjetas regalo</strong>, porque nos lo pides (ejecución de un contrato o de medidas precontractuales, art. 6.1.b del RGPD).</li>
<li><strong>Realizar los tratamientos con seguridad</strong> cuando necesitamos datos de salud, con tu consentimiento explícito (art. 9.2.a del RGPD).</li>
<li><strong>Facturación y obligaciones fiscales y contables</strong> (obligación legal, art. 6.1.c del RGPD).</li>
<li><strong>Enviarte promociones</strong>, solo si nos das tu consentimiento, que puedes retirar en cualquier momento (art. 6.1.a del RGPD).</li>
</ul>

<h2>4. Cuánto tiempo los conservamos</h2>
<p>Mientras seas cliente o no nos pidas que los borremos. Después, los datos necesarios para facturación se conservan durante los plazos que exige la ley (hasta 6 años) y el resto se elimina.</p>

<h2>5. Quién puede acceder a tus datos</h2>
<p>No cedemos tus datos a terceros, salvo obligación legal (por ejemplo, a Hacienda). Algunos proveedores los tratan por nuestra cuenta:</p>
<ul>
<li><strong>WhatsApp</strong> (Meta Platforms Ireland Ltd.), si nos escribes por esa vía. Puede implicar transferencias a EE. UU. amparadas por el Marco de Privacidad de Datos UE-EE. UU.</li>
<li><strong>GitHub Pages</strong> (GitHub, Inc.), que aloja esta web y puede registrar tu dirección IP por motivos de seguridad, también amparado por ese marco.</li>
<li>Nuestra gestoría, para la contabilidad y los impuestos.</li>
</ul>

<h2>6. Tus derechos</h2>
<p>Puedes pedir el acceso, la rectificación o la supresión de tus datos, oponerte a su tratamiento o pedir su limitación o portabilidad, y retirar tu consentimiento cuando quieras. Escríbenos a {dato('email')} o pásate por el centro, indicando qué derecho quieres ejercer.</p>
<p>Si crees que no hemos tratado bien tus datos, puedes reclamar ante la <a href="https://www.aepd.es" rel="noopener" target="_blank">Agencia Española de Protección de Datos</a>.</p>

<h2>7. Menores</h2>
<p>Si tienes menos de 14 años, necesitamos el consentimiento de tu madre, padre o tutor para tratar tus datos.</p>
""")

page("cookies", "Política de cookies",
     "Información sobre cookies y almacenamiento en la web de Saloncito Aroa.", """
<h2>1. Esta web no usa cookies</h2>
<p>Las cookies son pequeños archivos que algunas webs guardan en tu navegador. <strong>Esta web no instala ninguna cookie</strong>, ni propia ni de terceros, y no usa herramientas de analítica, publicidad ni redes sociales que te sigan. Por eso no te pedimos que aceptes cookies.</p>
<p>Las tipografías y los iconos se sirven desde la propia web, sin conectarse a servicios de terceros.</p>

<h2>2. Preferencia de idioma</h2>
<p>Si eliges el idioma (castellano o catalán), la web lo recuerda guardándolo en el almacenamiento local de tu navegador:</p>
<ul>
<li><strong>Nombre:</strong> <code>aroa_lang</code></li>
<li><strong>Para qué:</strong> mostrarte la web en el idioma que has elegido.</li>
<li><strong>Tipo:</strong> técnico y propio. No identifica a nadie ni se envía a ningún servidor.</li>
<li><strong>Duración:</strong> hasta que lo borres desde tu navegador.</li>
</ul>
<p>Al ser necesario para ofrecer una función que tú pides, está exento de consentimiento según el artículo 22.2 de la LSSI-CE.</p>

<h2>3. Enlaces a otros servicios</h2>
<p>Si pulsas los enlaces a WhatsApp, Instagram o Google Maps, sales de esta web y esos servicios pueden usar sus propias cookies, según sus políticas.</p>

<h2>4. Cómo borrar estos datos</h2>
<p>Puedes borrar el almacenamiento local y las cookies desde la configuración de privacidad de tu navegador (por ejemplo, en Safari: Ajustes → Privacidad → Gestionar datos de sitios web).</p>

<h2>5. Cambios</h2>
<p>Si en el futuro añadimos herramientas que usen cookies, como estadísticas de visitas, actualizaremos esta política y te pediremos permiso antes de activarlas.</p>
""")

print("Páginas legales generadas.")

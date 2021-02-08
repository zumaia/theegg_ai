# Tarea 41

# Para ejecutar:
***$ python tarea41.py***  
 
Solicitará la url de la página a analizar:
https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/


## Explicación de la tarea
### Entender que son las expresiones regulares y el manejo de estas con cierta solvencia

Las expresiones regulares o regex (regular expression) son patrones utilizados en programación para encontrar una determinada combinación de caracteres dentro de una cadena de texto. Se utilizan mucho en la gestión de la información de cualquier aplicativo. Todos los principales lenguajes de programación (C++, java, ruby, python, php, ...) utilizan expresiones regulares. En ocasiones, el desarrollador de aplicaciones de Inteligencia Artificial, debe trabajar con cadenas de texto para:

1.- La búsqueda de elementos particulares dentro de un largo texto. Por ejemplo, es posible que desee identificar todas las direcciones de correo electrónico existentes en un contenido muy extenso.  
2.- Para reemplazar, por ejemplo, un fichero de lenguaje de marcas de hipertexto (HTML) con unas etiquetas deficientes por otras correctas.  
3.- Para validar una contraseña o correo electrónico de un formulario. Por ejemplo, se puede querer verificar que una contraseña cumpla con ciertos criterios, tales como: una combinación de mayúsculas y minúsculas, dígitos, signos de puntuación. O para validar si un usuario que se registra a una página web a metido un correo electrónico correcto mediante la definición de unos patrones predeterminados: la existencia de un @, ...   
4.- Para automatizar ciertas acciones. Por ejemplo, es posible que se desee procesar ciertos archivos en un directorio, pero solo si cumplen unas condiciones predeterminadas.   
5.- Para reformatear texto. Por ejemplo, se pueden importar datos de un programa como archivo de texto, modificar su contenido y exportarlo a un editor de texto una vez corregido.   
6.- Para técnicas de scrapping. ATENTO! Esta técnica de análisis, captura e ingesta de datos se utilizan mucho para construir posteriormente soluciones de Inteligencia Artificial. Es una técnica que se utiliza en múltiples lenguajes de programación y existen diferentes librerías que nos ayudan en la construcción de este tipo de arañas (Para php la librería CURL, para python las librerías beautifulsoup o scrapy, para C++...).   
Ojo, no son lo mismo el crawling y el scraping; en este link se explican las diferencias.
En muchas ocasiones esta técnica de ingesta y análisis de datos se hace desde páginas web de terceros por lo que entenderás que tener ciertas nociones de HTML para el raspado o scrapping de contenido web será necesario para el desarrollo de soluciones de IA.  
7.- Para buscar coincidencias entre diferentes textos.

He aquí unas guías sobre la sintaxis utilizada para las expresiones regulares en diferentes lenguajes de programación:
1.- Para python: https://platzi.com/blog/expresiones-regulares-python/  
2.- Para javascript: https://www.arkaitzgarro.com/javascript/capitulo-11.html  
3.- Para php: https://diego.com.es/expresiones-regulares-en-php  
4.- Para ...  
  
Los alumnos podéis disponer en Internet de diferentes herramientas para probar vuestra sintaxis para expresiones regulares:
https://regex101.com/   
https://www.online-toolz.com/langs/es/tool-es-regexp-editor.html   
https://www.metriplica.com/informes-y-estudios-de-analitica-digital/recursos-herramientas-de-analitica/expresiones-regulares/  
Para esta tarea proponemos el siguiente ejercicio: el @egger mediante técnicas de Regex debe calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso del siguiente texto. La aplicación debe servir para cualquier otro texto:
   
"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."

Ref: https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/

NOTA:
1.- Para una de las ramas de la Inteligencia Artificial, la del Procesamiento del Lenguaje Natural, conocer estas técnicas va a ser útil ya que nos proveerá de una herramienta de analítica de texto muy avanzada. El PLN se utiliza para filtros de correo electrónico, asistentes inteligentes (Siri, Ok Google), traductores, llamadas telefónicas digitales, ...
2.- Para la ingestión de diferentes fuentes de datos durante el desarrollo soluciones de Machine Learning o Deep Learning el raspado de información también será necesario. Imagina que estás desarrollando una solución de predicción de venta de refrescos de una tienda de comestibles. Seguramente la meteorología es una variable que afecta directamente a este consumo. Pues bien, podrás obtener las previsiones meteorológicas a partir de páginas web de meteorología mediante técnicas de scrapping y utilizar este dato en tu modelo predictivo.

### HASHTAGS (etiquetas de ayuda para búsqueda de información relevante)
#### expresiones-regulares 
####Regex 
####procesamiento-del-lenguaje-natural 
####web-scrapping 
###LINKS DE INTERÉS
https://robologs.net/2019/05/05/como-utilizar-expresiones-regulares-regex-en-python/ https://geekflare.com/es/regular-expression-tester/  
https://www.metriplica.com/informes-y-estudios-de-analitica-digital/recursos-herramientas-de- analitica/expresiones-regulares/  
https://www.youtube.com/watch?v=M72lwALYRJU  

DICCIONARIO

expresiones-regulares | procesamiento-del-lenguaje-natural | scrapping | crawling
PUNTUACIÓN

Programación: 6
Redes: 1
Seguridad: 1
Algoritmia: 5


```python
# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
from collections import Counter
```


```python
# Solicitamos la url
print("Inserta una url: por ej:(http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/)")
url = input()
```

    Inserta una url: por ej:(http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/)


     http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/



```python
# LLamamos la url para obtenerlos datos
# url = 'http://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/'
r = requests.get(url)
# Debemos recibir código 200 de OK
r.status_code
```




    200




```python
# Parseamos la url
s = BeautifulSoup(r.content, "html.parser") 
s
```




    
    <!DOCTYPE html>
    
    <html lang="es">
    <head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-132776453-1"></script>
    <script>
      		window.dataLayer = window.dataLayer || [];
      		function gtag(){dataLayer.push(arguments);}
      		gtag('js', new Date());
    		gtag('config', 'UA-132776453-1');
    	</script>
    <!-- Fin - Google Analytics -->
    <meta charset="utf-8"/>
    <meta content="ie=edge" http-equiv="x-ua-compatible"/>
    <meta content="width=device-width, initial-scale=1" name="viewport"/>
    <link href="http://pegameunviaje.com/xmlrpc.php" rel="pingback"/>
    <link href="http://gmpg.org/xfn/11" rel="profile"/>
    <!-- TradeDoubler site verification 3088857 -->
    <!-- TradeDoubler site verification 3083380 -->
    <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document,"script","https://chimpstatic.com/mcjs-connected/js/users/4d19b098916be503a0374effd/71184098868193f14df22a0df.js");</script>
    <title>3 anécdotas divertidas de mis viajes - Pégame un viaje</title>
    <!-- This site is optimized with the Yoast SEO plugin v13.4.1 - https://yoast.com/wordpress/plugins/seo/ -->
    <meta content="max-snippet:-1, max-image-preview:large, max-video-preview:-1" name="robots"/>
    <link href="https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/" rel="canonical"/>
    <meta content="es_ES" property="og:locale"/>
    <meta content="article" property="og:type"/>
    <meta content="3 anécdotas divertidas de mis viajes - Pégame un viaje" property="og:title"/>
    <meta content="Siempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido" property="og:description"/>
    <meta content="https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/" property="og:url"/>
    <meta content="Pégame un viaje" property="og:site_name"/>
    <meta content="Slider" property="article:tag"/>
    <meta content="Viajes" property="article:section"/>
    <meta content="2017-11-02T21:57:10+00:00" property="article:published_time"/>
    <meta content="2019-01-28T17:26:06+00:00" property="article:modified_time"/>
    <meta content="2019-01-28T17:26:06+00:00" property="og:updated_time"/>
    <meta content="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n.jpg" property="og:image"/>
    <meta content="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n.jpg" property="og:image:secure_url"/>
    <meta content="960" property="og:image:width"/>
    <meta content="960" property="og:image:height"/>
    <meta content="summary_large_image" name="twitter:card"/>
    <meta content="Siempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido" name="twitter:description"/>
    <meta content="3 anécdotas divertidas de mis viajes - Pégame un viaje" name="twitter:title"/>
    <meta content="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n.jpg" name="twitter:image"/>
    <script class="yoast-schema-graph yoast-schema-graph--main" type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://pegameunviaje.com/#website","url":"https://pegameunviaje.com/","name":"P\u00e9game un viaje","inLanguage":"es","description":"Muy buenas, soy Pablo! Y si os apetece ver las aventurillas que voy teniendo por aqu\u00ed y viajar un poco conmigo, \u00e9ste es vuestro sitio!!","potentialAction":[{"@type":"SearchAction","target":"https://pegameunviaje.com/?s={search_term_string}","query-input":"required name=search_term_string"}]},{"@type":"ImageObject","@id":"https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/#primaryimage","inLanguage":"es","url":"https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n.jpg","width":960,"height":960},{"@type":"WebPage","@id":"https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/#webpage","url":"https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/","name":"3 an\u00e9cdotas divertidas de mis viajes - P\u00e9game un viaje","isPartOf":{"@id":"https://pegameunviaje.com/#website"},"inLanguage":"es","primaryImageOfPage":{"@id":"https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/#primaryimage"},"datePublished":"2017-11-02T21:57:10+00:00","dateModified":"2019-01-28T17:26:06+00:00","author":{"@id":"https://pegameunviaje.com/#/schema/person/bca07c426fd8a6a2238569acfb080a33"},"potentialAction":[{"@type":"ReadAction","target":["https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/"]}]},{"@type":["Person"],"@id":"https://pegameunviaje.com/#/schema/person/bca07c426fd8a6a2238569acfb080a33","name":"Pablo Gonz\u00e1lez","image":{"@type":"ImageObject","@id":"https://pegameunviaje.com/#authorlogo","inLanguage":"es","url":"http://0.gravatar.com/avatar/0c4a2e014d7a1e32dce52cb4db6caad2?s=96&d=mm&r=g","caption":"Pablo Gonz\u00e1lez"},"sameAs":[]}]}</script>
    <!-- / Yoast SEO plugin. -->
    <script type="text/javascript">console.log('PixelYourSite Free version 7.1.7');</script>
    <link href="//fonts.googleapis.com" rel="dns-prefetch"/>
    <link href="//s.w.org" rel="dns-prefetch"/>
    <link href="https://pegameunviaje.com/feed/" rel="alternate" title="Pégame un viaje » Feed" type="application/rss+xml"/>
    <link href="https://pegameunviaje.com/comments/feed/" rel="alternate" title="Pégame un viaje » Feed de los comentarios" type="application/rss+xml"/>
    <link href="https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/feed/" rel="alternate" title="Pégame un viaje » Comentario 3 anécdotas divertidas de mis viajes del feed" type="application/rss+xml"/>
    <!-- This site uses the Google Analytics by ExactMetrics plugin v6.0.2 - Using Analytics tracking - https://www.exactmetrics.com/ -->
    <script data-cfasync="false" type="text/javascript">
    	var em_version         = '6.0.2';
    	var em_track_user      = true;
    	var em_no_track_reason = '';
    	
    	var disableStr = 'ga-disable-UA-132776453-1';
    
    	/* Function to detect opted out users */
    	function __gaTrackerIsOptedOut() {
    		return document.cookie.indexOf(disableStr + '=true') > -1;
    	}
    
    	/* Disable tracking if the opt-out cookie exists. */
    	if ( __gaTrackerIsOptedOut() ) {
    		window[disableStr] = true;
    	}
    
    	/* Opt-out function */
    	function __gaTrackerOptout() {
    	  document.cookie = disableStr + '=true; expires=Thu, 31 Dec 2099 23:59:59 UTC; path=/';
    	  window[disableStr] = true;
    	}
    
    	if ( 'undefined' === typeof gaOptout ) {
    		function gaOptout() {
    			__gaTrackerOptout();
    		}
    	}
    	
    	if ( em_track_user ) {
    		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    			(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    			m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    		})(window,document,'script','//www.google-analytics.com/analytics.js','__gaTracker');
    
    window.ga = __gaTracker;		__gaTracker('create', 'UA-132776453-1', 'auto');
    		__gaTracker('set', 'forceSSL', true);
    		__gaTracker('send','pageview');
    		__gaTracker( function() { window.ga = __gaTracker; } );
    	} else {
    		console.log( "" );
    		(function() {
    			/* https://developers.google.com/analytics/devguides/collection/analyticsjs/ */
    			var noopfn = function() {
    				return null;
    			};
    			var noopnullfn = function() {
    				return null;
    			};
    			var Tracker = function() {
    				return null;
    			};
    			var p = Tracker.prototype;
    			p.get = noopfn;
    			p.set = noopfn;
    			p.send = noopfn;
    			var __gaTracker = function() {
    				var len = arguments.length;
    				if ( len === 0 ) {
    					return;
    				}
    				var f = arguments[len-1];
    				if ( typeof f !== 'object' || f === null || typeof f.hitCallback !== 'function' ) {
    					console.log( 'Función desactivada __gaTracker(' + arguments[0] + " ....) porque no estás siendo rastreado. " + em_no_track_reason );
    					return;
    				}
    				try {
    					f.hitCallback();
    				} catch (ex) {
    
    				}
    			};
    			__gaTracker.create = function() {
    				return new Tracker();
    			};
    			__gaTracker.getByName = noopnullfn;
    			__gaTracker.getAll = function() {
    				return [];
    			};
    			__gaTracker.remove = noopfn;
    			window['__gaTracker'] = __gaTracker;
    			window.ga = __gaTracker;		})();
    		}
    </script>
    <!-- / Google Analytics by ExactMetrics -->
    <script type="text/javascript">
    			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/12.0.0-1\/svg\/","svgExt":".svg","source":{"concatemoji":"http:\/\/pegameunviaje.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.3.2"}};
    			!function(e,a,t){var r,n,o,i,p=a.createElement("canvas"),s=p.getContext&&p.getContext("2d");function c(e,t){var a=String.fromCharCode;s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,e),0,0);var r=p.toDataURL();return s.clearRect(0,0,p.width,p.height),s.fillText(a.apply(this,t),0,0),r===p.toDataURL()}function l(e){if(!s||!s.fillText)return!1;switch(s.textBaseline="top",s.font="600 32px Arial",e){case"flag":return!c([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])&&(!c([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!c([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]));case"emoji":return!c([55357,56424,55356,57342,8205,55358,56605,8205,55357,56424,55356,57340],[55357,56424,55356,57342,8203,55358,56605,8203,55357,56424,55356,57340])}return!1}function d(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(i=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},o=0;o<i.length;o++)t.supports[i[o]]=l(i[o]),t.supports.everything=t.supports.everything&&t.supports[i[o]],"flag"!==i[o]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[i[o]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(r=t.source||{}).concatemoji?d(r.concatemoji):r.wpemoji&&r.twemoji&&(d(r.twemoji),d(r.wpemoji)))}(window,document,window._wpemojiSettings);
    		</script>
    <style type="text/css">
    img.wp-smiley,
    img.emoji {
    	display: inline !important;
    	border: none !important;
    	box-shadow: none !important;
    	height: 1em !important;
    	width: 1em !important;
    	margin: 0 .07em !important;
    	vertical-align: -0.1em !important;
    	background: none !important;
    	padding: 0 !important;
    }
    </style>
    <link href="http://pegameunviaje.com/wp-includes/css/dist/block-library/style.min.css?ver=5.3.2" id="wp-block-library-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/plugins/js_composer/assets/lib/bower/font-awesome/css/font-awesome.min.css?ver=5.1.1" id="font-awesome-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.1.7" id="contact-form-7-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/plugins/cookie-law-info/public/css/cookie-law-info-public.css?ver=1.8.7" id="cookie-law-info-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/plugins/cookie-law-info/public/css/cookie-law-info-gdpr.css?ver=1.8.7" id="cookie-law-info-gdpr-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://fonts.googleapis.com/css?family=Lato%3A400%2C700%2C900%7CRoboto%3A400%2C400i%2C500%2C700%7CLora%3A400i%7CRancho%3A400" id="cheerup-fonts-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/themes/cheerup/style.css?ver=4.0.0" id="cheerup-core-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/plugins/mapplic/css/magnific-popup.css" id="magnific-popup-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/themes/cheerup/css/fontawesome/css/font-awesome.min.css?ver=4.0.0" id="cheerup-font-awesome-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-content/themes/cheerup/css/skin-travel.css?ver=4.0.0" id="cheerup-skin-css" media="all" rel="stylesheet" type="text/css"/>
    <style id="cheerup-skin-inline-css" type="text/css">
    @import url('https://fonts.googleapis.com/css?family=Playfair+Display%3A|Source+Sans+Pro%3A400|Source+Sans+Pro%3A600|Source+Sans+Pro%3A700');
    
    
    .main-footer .bg-wrap:before { opacity: 0.2; }
    
    .main-footer .bg-wrap:before { background-image: url(https://pegameunviaje.com/wp-content/uploads/2019/01/zkPICT1404.jpg);background-repeat: no-repeat; background-position: center center; background-size: cover; }
    
    .main-head > .inner { background-image: url(https://pegameunviaje.com/wp-content/uploads/2019/08/cabecera-pegame-un-viaje-1.jpg); background-position: top center;;background-repeat: no-repeat; background-position: center center; background-size: cover; }
    
    .sidebar .widget-title { font-family: "Playfair Display", Arial, sans-serif; }
    
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    input[type="submit"],
    button,
    input[type="button"],
    .button,
    .modern-quote cite,
    .top-bar-content,
    .search-action .search-field,
    .main-head .title,
    .navigation,
    .tag-share,
    .post-share-b .service,
    .author-box,
    .comments-list .comment-content,
    .post-nav .label,
    .main-footer.dark .back-to-top,
    .lower-footer .social-icons,
    .main-footer .social-strip .social-link,
    .main-footer.bold .links .menu-item,
    .main-footer.bold .copyright,
    .archive-head,
    .cat-label a,
    .section-head,
    .post-title-alt,
    .post-title,
    .block-heading,
    .block-head-b,
    .small-post .post-title,
    .likes-count .number,
    .post-meta,
    .grid-post-b .read-more-btn,
    .list-post-b .read-more-btn,
    .post-footer .read-more,
    .post-footer .social-share,
    .post-footer .social-icons,
    .large-post-b .post-footer .author a,
    .products-block .more-link,
    .main-slider,
    .slider-overlay .heading,
    .large-slider,
    .large-slider .heading,
    .grid-slider .category,
    .grid-slider .heading,
    .carousel-slider .category,
    .carousel-slider .heading,
    .grid-b-slider .heading,
    .bold-slider,
    .bold-slider .heading,
    .main-pagination,
    .main-pagination .load-button,
    .page-links,
    .post-content .read-more,
    .widget-about .more,
    .widget-posts .post-title,
    .widget-posts .posts.full .counter:before,
    .widget-cta .label,
    .social-follow .service-link,
    .widget-twitter .meta .date,
    .widget-twitter .follow,
    .widget_categories,
    .widget_product_categories,
    .widget_archive,
    .mobile-menu,
    .woocommerce .main .button,
    .woocommerce .quantity .qty,
    .woocommerce nav.woocommerce-pagination,
    .woocommerce-cart .post-content,
    .woocommerce .woocommerce-ordering,
    .woocommerce-page .woocommerce-ordering,
    .woocommerce ul.products,
    .woocommerce.widget,
    .woocommerce div.product,
    .woocommerce #content div.product,
    .woocommerce-cart .cart-collaterals .cart_totals .button,
    .woocommerce .checkout .shop_table thead th,
    .woocommerce .checkout .shop_table .amount,
    .woocommerce-checkout #payment #place_order,
    .top-bar .posts-ticker,
    .post-content h1,
    .post-content h2,
    .post-content h3,
    .post-content h4,
    .post-content h5,
    .post-content h6,
    
    .related-posts.grid-2 .post-title,
    .related-posts .post-title,
    .block-heading .title,
    .single-cover .featured .post-title,
    .single-creative .featured .post-title,
    .single-magazine .post-top .post-title,
    .author-box .author > a,
    .section-head .title,
    .comments-list .comment-author,
    .sidebar .widget-title,
    .upper-footer .widget .widget-title
     { font-family: "Source Sans Pro", Arial, sans-serif; }
    
    h3:contains('Contact Form') {
    display: none;
    }
    </style>
    <script type="text/javascript">
    /* <![CDATA[ */
    var exactmetrics_frontend = {"js_events_tracking":"true","download_extensions":"zip,mp3,mpeg,pdf,docx,pptx,xlsx,rar","inbound_paths":"[{\"path\":\"\\\/go\\\/\",\"label\":\"affiliate\"},{\"path\":\"\\\/recommend\\\/\",\"label\":\"affiliate\"}]","home_url":"https:\/\/pegameunviaje.com","hash_tracking":"false"};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-content/plugins/google-analytics-dashboard-for-wp/assets/js/frontend.min.js?ver=6.0.2" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var Sphere_Plugin = {"ajaxurl":"https:\/\/pegameunviaje.com\/wp-admin\/admin-ajax.php"};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-includes/js/jquery/jquery.js?ver=1.12.4-wp" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var Cli_Data = {"nn_cookie_ids":[],"cookielist":[]};
    var log_object = {"ajax_url":"https:\/\/pegameunviaje.com\/wp-admin\/admin-ajax.php"};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-content/plugins/cookie-law-info/public/js/cookie-law-info-public.js?ver=1.8.7" type="text/javascript"></script>
    <link href="https://pegameunviaje.com/wp-json/" rel="https://api.w.org/"/>
    <link href="https://pegameunviaje.com/xmlrpc.php?rsd" rel="EditURI" title="RSD" type="application/rsd+xml"/>
    <link href="http://pegameunviaje.com/wp-includes/wlwmanifest.xml" rel="wlwmanifest" type="application/wlwmanifest+xml"/>
    <meta content="WordPress 5.3.2" name="generator"/>
    <link href="https://pegameunviaje.com/?p=1132" rel="shortlink"/>
    <link href="https://pegameunviaje.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F" rel="alternate" type="application/json+oembed"/>
    <link href="https://pegameunviaje.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F&amp;format=xml" rel="alternate" type="text/xml+oembed"/>
    <!-- Facebook Pixel Code -->
    <script type="text/javascript">
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
    n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
    document,'script','https://connect.facebook.net/en_US/fbevents.js');
    </script>
    <!-- End Facebook Pixel Code -->
    <script type="text/javascript">
      fbq('init', '531385824478910', [], {
        "agent": "wordpress-5.3.2-2.0.1"
    });
    </script><script type="text/javascript">
      fbq('track', 'PageView', []);
    </script>
    <!-- Facebook Pixel Code -->
    <noscript>
    <img alt="fbpx" height="1" src="https://www.facebook.com/tr?id=531385824478910&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
    </noscript>
    <!-- End Facebook Pixel Code -->
    <!--[if lte IE 9]><link rel="stylesheet" type="text/css" href="http://pegameunviaje.com/wp-content/plugins/js_composer/assets/css/vc_lte_ie9.min.css" media="screen"><![endif]--><script type="text/javascript">console.warn('PixelYourSite: no pixel configured.');</script>
    <link href="https://pegameunviaje.com/wp-content/uploads/2020/03/cropped-travel-32x32.png" rel="icon" sizes="32x32"/>
    <link href="https://pegameunviaje.com/wp-content/uploads/2020/03/cropped-travel-192x192.png" rel="icon" sizes="192x192"/>
    <link href="https://pegameunviaje.com/wp-content/uploads/2020/03/cropped-travel-180x180.png" rel="apple-touch-icon-precomposed"/>
    <meta content="https://pegameunviaje.com/wp-content/uploads/2020/03/cropped-travel-270x270.png" name="msapplication-TileImage"/>
    <noscript><style type="text/css"> .wpb_animate_when_almost_visible { opacity: 1; }</style></noscript>
    </head>
    <body class="post-template-default single single-post postid-1132 single-format-standard right-sidebar skin-travel wpb-js-composer js-comp-ver-5.1.1 vc_responsive">
    <div class="main-wrap">
    <header class="main-head search-alt head-nav-below alt top-below" id="main-head">
    <div class="inner">
    <div class="wrap logo-wrap cf">
    <div class="title">
    <a href="https://pegameunviaje.com/" rel="home" title="Pégame un viaje">
    <span class="text-logo">Pégame un viaje</span>
    </a>
    </div>
    </div>
    </div>
    <div class="top-bar dark cf">
    <div class="top-bar-content" data-sticky-bar="1">
    <div class="wrap cf">
    <span class="mobile-nav"><i class="fa fa-bars"></i></span>
    <ul class="social-icons cf">
    <li><a class="fa fa-facebook" href="https://www.facebook.com/pegameunviaje/" target="_blank"><span class="visuallyhidden">Facebook</span></a></li>
    <li><a class="fa fa-twitter" href="https://twitter.com/pegameunviaje" target="_blank"><span class="visuallyhidden">Twitter</span></a></li>
    <li><a class="fa fa-instagram" href="https://www.instagram.com/pegameunviaje/" target="_blank"><span class="visuallyhidden">Instagram</span></a></li>
    <li><a class="fa fa-youtube" href="https://www.youtube.com/channel/UCURHrB8MvZmoDLbfSxP0SoQ" target="_blank"><span class="visuallyhidden">YouTube</span></a></li>
    </ul>
    <nav class="navigation dark">
    <div class="menu-menueventoenero-container"><ul class="menu" id="menu-menueventoenero"><li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-1106" id="menu-item-1106"><a href="https://pegameunviaje.com">Inicio</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1107" id="menu-item-1107"><a href="https://pegameunviaje.com/videos/">Vídeos</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1466" id="menu-item-1466"><a href="https://pegameunviaje.com/para-ti/">Para ti</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1406" id="menu-item-1406"><a href="https://pegameunviaje.com/mapa/">Mapa</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1476" id="menu-item-1476"><a href="https://pegameunviaje.com/blog/">Blog</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1321" id="menu-item-1321"><a href="https://pegameunviaje.com/sobre-mi/">Sobre mí</a></li>
    <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1110" id="menu-item-1110"><a href="https://pegameunviaje.com/contacto/">Contacto</a></li>
    </ul></div> </nav>
    <div class="actions">
    <div class="search-action cf">
    <form action="https://pegameunviaje.com/" class="search-form" method="get">
    <button class="search-submit" type="submit"><i class="fa fa-search"></i></button>
    <input class="search-field" name="s" placeholder="Search" required="" type="search" value=""/>
    </form>
    </div>
    </div>
    </div>
    </div>
    </div>
    </header> <!-- .main-head -->
    <div class="main wrap">
    <div class="ts-row cf">
    <div class="col-8 main-content cf">
    <article class="the-post post-1132 post type-post status-publish format-standard has-post-thumbnail category-viajes tag-slider" id="post-1132">
    <header class="post-header cf">
    <div class="post-meta">
    <span class="post-cat">
    <a class="category" href="https://pegameunviaje.com/category/viajes/">Viajes</a>
    </span>
    <h1 class="post-title">
    			3 anécdotas divertidas de mis viajes			
    		</h1>
    <a class="date-link" href="https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/"><time class="post-date">noviembre 2, 2017</time></a>
    </div>
    <div class="featured">
    <a class="image-link" href="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n.jpg"><img alt="" class="attachment-cheerup-main size-cheerup-main wp-post-image" height="515" sizes="(max-width: 770px) 100vw, 770px" src="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n-770x515.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n-770x515.jpg 770w, https://pegameunviaje.com/wp-content/uploads/2017/11/27972742_2016040548658824_6307450843043682114_n-270x180.jpg 270w" title="3 anécdotas divertidas de mis viajes" width="770"/> </a>
    </div>
    </header><!-- .post-header -->
    <div class="post-content description cf">
    <p>Siempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido curioso recoger <strong>algunas de las anécdotas más curiosas </strong>que me han pasado estando <strong>de viaje</strong> para contártelas al detalle.</p>
    <p> <strong>1. El conductor interesado </strong><br/></p>
    <p>En Filippiada, en Grecia, tuve que hacer autoestop con una amiga para moverme hasta una localidad cercana. No había autobús ni ningún otro medio de transporte. Después de un buen rato con el pulgar arriba, paró un coche. <strong>Pero lejos de lo que te imaginas, no fue nuestra salvación.</strong><br/></p>
    <p style="text-align:left">El conductor redujo la velocidad y atendió a la petición de mi compañera, que sujetaba un cartel en el que habíamos escrito el nombre de nuestro destino. Pero de pronto se dio cuenta de algo con lo que no contaba.</p>
    <p>Mi turno de hacer autoestop ya había pasado, y mientras ella hacía el suyo yo descansaba en un muro a la sombra, a unos cuantos metros de distancia. Ella se acercó feliz hasta donde estaba yo para decirme que un coche había parado, y cuando el conductor descubrió que yo iba en el pack… ¡PUM! Acelerón y aquí no ha pasado nada.<br/></p>
    <p><strong>2. El Blablacar más «crack»</strong><br/></p>
    <p>Cuando me di cuenta ya era tarde; un despiste me había hecho bajar del autobús olvidando mi maleta en la bodega. De pronto me entró el agobio porque faltaban muy pocos minutos para que un tipo con el que había contactado a través de Blablacar viniera a recogerme con su coche (el autobús no me dejaba en mi parada definitiva, todavía me quedaban más de dos horas de camino). Pensé: <strong>«Si no tengo la maleta, ¿qué hago?</strong>, ¿me quedo en esta ciudad a buscarla o me subo al coche con él y ya arreglaré este asunto?».<br/></p>
    <p>Localicé a la empresa de autobuses y me dijo que mi maleta ya estaba en Catania, en Sicilia, y que si quería la podían dejar en una oficina de por allí para que no siguiera dando vueltas. Les dije que sí.  En ese momento llegó Graziano con su coche, el señor con el que había quedado para que me llevara al sur de la isla. </p>
    <blockquote class="wp-block-quote"><p>Si no tengo la maleta, ¿qué hago? -pensé muuuy agobiado</p></blockquote>
    <p>Abrí la puerta y le dije lo que me pasaba: «Hola, Graziano. Tengo un problema y no me voy a poder ir contigo porque me he dejado la maleta en el bus». <strong>Contra todo pronóstico, sonrió y me dijo: «¡Anda, sube! Vamos a buscarla»</strong>. Y eso hizo. Condujo hasta Catania, aparcó el coche y me acompañó a cuatro oficinas distintas para dar con mi equipaje. <br/></p>
    <p><strong>3. El mejor calefactor para una congelación</strong><br/></p>
    <p>En Strandhill, Irlanda, se cruzó en mi camino Chris, <strong>un señor de los que inspiran</strong> y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento…<br/></p>
    <p>Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. <strong>Aunque tenía un «pequeño» problema</strong>: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.</p>
    <p>Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. </p>
    <p><strong>Y eso hice, fui para allá y la cogí.</strong> Aunque el neopreno no me lo pudo prestar, y no porque se negara… Lamentablemente le sacaba unos 15 cm de altura.</p>
    <p>Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.<br/></p>
    <p>El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.</p>
    <p>Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar,  y hasta cantamos juntos la canción de Annie. </p>
    <p>Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero… seguro que a ti también te han pasado cosas así.</p>
    <p>Si tienes un hueco, pásate por mis redes y cuéntamelas, que seguro que me alegras el día.</p>
    <p>Ah, por cierto… Por suerte, como sabes, siempre empuño la cámara, así que puedes ver grabadas todas estas anécdotas (y dos más bastante curiosas) en el vídeo que te dejo a continuación: </p>
    <p><br/></p>
    <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
    <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="433" src="https://www.youtube.com/embed/DiZGeI2cOOA?start=403&amp;feature=oembed" width="770"></iframe>
    </div></figure>
    </div><!-- .post-content -->
    <div class="the-post-foot cf">
    <div class="tag-share cf">
    <div class="post-tags"><a href="https://pegameunviaje.com/tag/slider/" rel="tag">Slider</a></div>
    <div class="post-share">
    <div class="post-share-icons cf">
    <span class="counters">
    <a class="likes-count fa fa-heart-o" data-id="1132" href="#" title=""><span class="number">5</span></a>
    </span>
    <a class="link" href="http://www.facebook.com/sharer.php?u=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F" target="_blank" title="Share on Facebook"><i class="fa fa-facebook"></i></a>
    <a class="link" href="http://twitter.com/home?status=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F" target="_blank" title="Share on Twitter"><i class="fa fa-twitter"></i></a>
    <a class="link" href="http://plus.google.com/share?url=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F" target="_blank" title="Share on Google+"><i class="fa fa-google-plus"></i></a>
    <a class="link" href="http://pinterest.com/pin/create/button/?url=https%3A%2F%2Fpegameunviaje.com%2F3-anecdotas-divertidas-de-mis-viajes%2F&amp;media=https%3A%2F%2Fpegameunviaje.com%2Fwp-content%2Fuploads%2F2017%2F11%2F27972742_2016040548658824_6307450843043682114_n.jpg" target="_blank" title="Share on Pinterest"><i class="fa fa-pinterest-p"></i></a>
    </div>
    </div>
    </div>
    </div>
    <div class="author-box">
    <div class="image"><img alt="" class="avatar avatar-82 photo" height="82" src="http://0.gravatar.com/avatar/0c4a2e014d7a1e32dce52cb4db6caad2?s=82&amp;d=mm&amp;r=g" srcset="http://0.gravatar.com/avatar/0c4a2e014d7a1e32dce52cb4db6caad2?s=164&amp;d=mm&amp;r=g 2x" width="82"/></div>
    <div class="content">
    <span class="author">
    <span>Author</span>
    <a href="https://pegameunviaje.com/author/admin-2/" rel="author" title="Entradas de Pablo González">Pablo González</a> </span>
    <p class="text author-bio"></p>
    <ul class="social-icons">
    <li>
    <a class="fa fa-facebook" href="https://www.facebook.com/pegameunviaje/" title="Facebook">
    <span class="visuallyhidden">Facebook</span></a>
    </li>
    <li>
    <a class="fa fa-twitter" href="https://www.twitter.com/pegameunviaje/" title="Twitter">
    <span class="visuallyhidden">Twitter</span></a>
    </li>
    <li>
    <a class="fa fa-instagram" href="https://www.instagram.com/pegameunviaje/" title="Instagram">
    <span class="visuallyhidden">Instagram</span></a>
    </li>
    </ul>
    </div>
    </div>
    <section class="related-posts grid-3">
    <h4 class="section-head"><span class="title">Related Posts</span></h4>
    <div class="ts-row posts cf">
    <article class="post col-4">
    <a class="image-link" href="https://pegameunviaje.com/la-bufadora-el-segundo-geiser-mas-grande-del-mundo/" title="La Bufadora, el segundo géiser más grande del mundo">
    <img alt="" class="image wp-post-image" height="180" sizes="(max-width: 270px) 100vw, 270px" src="https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-270x180.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-270x180.jpg 270w, https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-770x515.jpg 770w" title="La Bufadora, el segundo géiser más grande del mundo" width="270"/> </a>
    <div class="content">
    <h3 class="post-title"><a class="post-link" href="https://pegameunviaje.com/la-bufadora-el-segundo-geiser-mas-grande-del-mundo/">La Bufadora, el segundo géiser más grande del mundo</a></h3>
    <div class="post-meta">
    <time class="post-date" datetime="2019-03-06T19:45:03+01:00">marzo 6, 2019</time>
    </div>
    </div>
    </article>
    <article class="post col-4">
    <a class="image-link" href="https://pegameunviaje.com/que-ver-en-argel-argelia/" title="Qué ver en Argel | Argelia en el mapa">
    <img alt="" class="image wp-post-image" height="180" sizes="(max-width: 270px) 100vw, 270px" src="https://pegameunviaje.com/wp-content/uploads/2019/02/1234gt-270x180.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2019/02/1234gt-270x180.jpg 270w, https://pegameunviaje.com/wp-content/uploads/2019/02/1234gt-770x515.jpg 770w" title="Qué ver en Argel | Argelia en el mapa" width="270"/> </a>
    <div class="content">
    <h3 class="post-title"><a class="post-link" href="https://pegameunviaje.com/que-ver-en-argel-argelia/">Qué ver en Argel | Argelia en el mapa</a></h3>
    <div class="post-meta">
    <time class="post-date" datetime="2019-02-12T09:59:20+01:00">febrero 12, 2019</time>
    </div>
    </div>
    </article>
    <article class="post col-4">
    <a class="image-link" href="https://pegameunviaje.com/7-cosas-que-tienes-que-saber-antes-de-ir-a-las-cataratas-del-niagara/" title="7 cosas que tienes que saber antes de ir a las Cataratas del Niágara">
    <img alt="" class="image wp-post-image" height="180" sizes="(max-width: 270px) 100vw, 270px" src="https://pegameunviaje.com/wp-content/uploads/2019/01/consejos-cataratas-del-niagara-1-270x180.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2019/01/consejos-cataratas-del-niagara-1-270x180.jpg 270w, https://pegameunviaje.com/wp-content/uploads/2019/01/consejos-cataratas-del-niagara-1-770x515.jpg 770w" title="7 cosas que tienes que saber antes de ir a las Cataratas del Niágara" width="270"/> </a>
    <div class="content">
    <h3 class="post-title"><a class="post-link" href="https://pegameunviaje.com/7-cosas-que-tienes-que-saber-antes-de-ir-a-las-cataratas-del-niagara/">7 cosas que tienes que saber antes de ir a las Cataratas del Niágara</a></h3>
    <div class="post-meta">
    <time class="post-date" datetime="2019-01-22T22:58:19+01:00">enero 22, 2019</time>
    </div>
    </div>
    </article>
    </div>
    </section>
    <div class="comments">
    <div class="comments-area" id="comments">
    <div class="comment-respond" id="respond">
    <h3 class="comment-reply-title" id="reply-title"><span class="section-head"><span class="title">Write A Comment</span></span> <small><a href="/3-anecdotas-divertidas-de-mis-viajes/#respond" id="cancel-comment-reply-link" rel="nofollow" style="display:none;">Cancel Reply</a></small></h3><form action="http://pegameunviaje.com/wp-comments-post.php" class="comment-form" id="commentform" method="post"><div class="fields">
    <div class="inline-field">
    <input aria-required="true" id="author" name="author" placeholder="Name" required="" type="text" value=""/>
    </div>
    <div class="inline-field">
    <input aria-required="true" id="email" name="email" placeholder="Email" required="" type="text" value=""/>
    </div>
    <div class="inline-field">
    <input id="url" name="url" placeholder="Website" type="text" value=""/>
    </div>
    <div class="reply-field cf">
    <textarea aria-required="true" cols="45" id="comment" name="comment" placeholder="Enter your comment here.." required="" rows="7"></textarea>
    </div>
    </div><p class="form-submit"><input class="submit" id="comment-submit" name="submit" type="submit" value="Post Comment"/> <input id="comment_post_ID" name="comment_post_ID" type="hidden" value="1132"/>
    <input id="comment_parent" name="comment_parent" type="hidden" value="0"/>
    </p></form> </div><!-- #respond -->
    </div><!-- #comments -->
    </div>
    </article> <!-- .the-post -->
    </div>
    <aside class="col-4 sidebar" data-sticky="1">
    <div class="inner theiaStickySidebar">
    <ul>
    <li class="widget widget-cta" id="bunyad-widget-cta-1">
    <h5 class="widget-title"><span>Destinos TOP</span></h5>
    <div class="cta-box">
    <a href="https://www.youtube.com/playlist?list=PLmeG4xkphTZVvsWI7rUPOn0A2M0-NoFj0&amp;fbclid=IwAR24VOkqI9Qlz7TXdcX6eA7H7wRQxre7u1eKzrIJ3FoXL7Tzb3QHtXQtnsI">
    <img alt="Argelia" src="https://pegameunviaje.com/wp-content/uploads/2019/01/argelia.png"/>
    <span class="label">Argelia</span>
    </a>
    </div>
    <div class="cta-box">
    <a href="https://www.youtube.com/playlist?list=PLmeG4xkphTZVXkE9ArCavrFX3-tBBkUc3&amp;disable_polymer=true">
    <img alt="Mexico" src="https://pegameunviaje.com/wp-content/uploads/2019/01/mexico.png"/>
    <span class="label">Mexico</span>
    </a>
    </div>
    <div class="cta-box">
    <a href="https://www.youtube.com/playlist?list=PLmeG4xkphTZWVJHPiFnq9OdfVShwAGzMY&amp;disable_polymer=true">
    <img alt="Italia" src="https://pegameunviaje.com/wp-content/uploads/2019/01/italia.png"/>
    <span class="label">Italia</span>
    </a>
    </div>
    </li>
    <li class="widget_text widget widget_custom_html" id="custom_html-5"><div class="textwidget custom-html-widget"><a href="https://www.intermundial.es/?utm_source=pegameunviaje" rel="noopener noreferrer" target="_blank">
    <img alt="intermundialXpegameunviaje" src="https://pegameunviaje.com/wp-content/uploads/2019/04/intermundial.jpg"/>
    </a></div></li>
    <li class="widget widget_mc4wp_form_widget" id="mc4wp_form_widget-5"><h5 class="widget-title"><span>Newsletter</span></h5><script>(function() {
    	window.mc4wp = window.mc4wp || {
    		listeners: [],
    		forms: {
    			on: function(evt, cb) {
    				window.mc4wp.listeners.push(
    					{
    						event   : evt,
    						callback: cb
    					}
    				);
    			}
    		}
    	}
    })();
    </script><!-- Mailchimp for WordPress v4.7.6 - https://wordpress.org/plugins/mailchimp-for-wp/ --><form class="mc4wp-form mc4wp-form-1270" data-id="1270" data-name="Suscríbete a mi newsletter" id="mc4wp-form-1" method="post"><div class="mc4wp-form-fields"><p style="text-align: center"> 
      Si estas interesado en conocer mis andaduras, déjame por aquí tu correo electrónico para no perderte nada.
      <br/><br/>
    <input name="EMAIL" required="" type="email"/>
    </p>
    <p style="text-align: center">
    <input type="submit" value="Suscribirme"/>
    </p></div><label style="display: none !important;">Deja vacío este campo si eres humano: <input autocomplete="off" name="_mc4wp_honeypot" tabindex="-1" type="text" value=""/></label><input name="_mc4wp_timestamp" type="hidden" value="1612804876"/><input name="_mc4wp_form_id" type="hidden" value="1270"/><input name="_mc4wp_form_element_id" type="hidden" value="mc4wp-form-1"/><div class="mc4wp-response"></div></form><!-- / Mailchimp for WordPress Plugin --></li>
    <li class="widget widget-about" id="bunyad-widget-about-7">
    <h5 class="widget-title"><span>Sobre mí</span></h5>
    <div class="author-image image-circle">
    <img alt="About Me" src="https://pegameunviaje.com/wp-content/uploads/2019/01/foto-2.jpg">
    </img></div>
    <div class="text about-text"><p>Mi objetivo es recorrer el mundo para descubrir historias, personas y rincones. Y te lo pienso contar todo.</p>
    </div>
    </li>
    <li class="widget_text widget widget_custom_html" id="custom_html-3"><div class="textwidget custom-html-widget"><div style="background-color: #e61a25; padding: 10px; color: #fff; background-image: linear-gradient(to bottom,rgba(255,255,255,.2) 0,rgba(255,255,255,.01) 100%); background-repeat: repeat-x; padding: 20px;">
    <h5 align="center" style="font-size: 20px; margin-bottom: 0; font-weight: 700; line-height: 25px; margin-bottom: 10px; color: #fff;">
    		Suscríbete en YouTube
    		</h5>
    <p align="center" style="font-size: 13px;">
    		Más de 6.000 personas se han sumado ya a las ‘videoaventuras’ de Pégame un viaje
    	</p>
    <div align="center" style="padding-bottom:10px;">
    <a class="vc_general vc_btn3 vc_btn3-size-md vc_btn3-shape-rounded vc_btn3-style-modern vc_btn3-color-danger customize-unpreviewable" href="https://www.youtube.com/channel/UCURHrB8MvZmoDLbfSxP0SoQ">
    <i class="fa fa-youtube"></i> 
    			Ir al Canal
    		</a>
    </div>
    </div>
    </div></li>
    <li class="widget widget-social" id="bunyad-widget-social-1">
    <h5 class="widget-title"><span>Sígueme en las redes</span></h5>
    <div class="social-icons">
    <a class="social-link" href="https://www.facebook.com/pegameunviaje/" target="_blank"><i class="fa fa-facebook"></i>
    <span class="visuallyhidden">Facebook</span></a>
    <a class="social-link" href="https://twitter.com/pegameunviaje" target="_blank"><i class="fa fa-twitter"></i>
    <span class="visuallyhidden">Twitter</span></a>
    <a class="social-link" href="https://www.instagram.com/pegameunviaje/" target="_blank"><i class="fa fa-instagram"></i>
    <span class="visuallyhidden">Instagram</span></a>
    <a class="social-link" href="https://www.youtube.com/channel/UCURHrB8MvZmoDLbfSxP0SoQ" target="_blank"><i class="fa fa-youtube"></i>
    <span class="visuallyhidden">YouTube</span></a>
    </div>
    </li>
    </ul>
    </div>
    </aside>
    </div> <!-- .ts-row -->
    </div> <!-- .main -->
    <footer class="main-footer dark stylish stylish-b">
    <section class="mid-footer cf">
    			Instagram no ha devuelto un 200.<p class="clear"><a class="" href="//instagram.com/explore/tags/pegameunviaje/" rel="me" target="_blank">¡Sígueme!</a></p> </section>
    <div class="bg-wrap">
    <section class="upper-footer">
    <div class="wrap">
    <ul class="widgets ts-row cf">
    <li class="widget column col-4 widget_media_video" id="media_video-3"><h5 class="widget-title">Sobre mí</h5><div class="wp-video" style="width:100%;"><!--[if lt IE 9]><script>document.createElement('video');</script><![endif]-->
    <video class="wp-video-shortcode" controls="controls" id="video-1132-1" preload="metadata"><source src="https://www.youtube.com/watch?v=TOnPfwxrC9g&amp;_=1" type="video/youtube"/><a href="https://www.youtube.com/watch?v=TOnPfwxrC9g">https://www.youtube.com/watch?v=TOnPfwxrC9g</a></video></div></li>
    <li class="widget column col-4 widget-posts" id="bunyad-posts-widget-2">
    <h5 class="widget-title">Últimas publicaciones</h5>
    <ul class="posts cf meta-below">
    <li class="post cf">
    <a class="image-link" href="https://pegameunviaje.com/la-bufadora-el-segundo-geiser-mas-grande-del-mundo/">
    <img alt="" class="attachment-cheerup-thumb size-cheerup-thumb wp-post-image" height="67" sizes="(max-width: 87px) 100vw, 87px" src="https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-87x67.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-87x67.jpg 87w, https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-370x285.jpg 370w, https://pegameunviaje.com/wp-content/uploads/2019/03/Imagen1-260x200.jpg 260w" title="La Bufadora, el segundo géiser más grande del mundo" width="87"/> </a>
    <div class="content">
    <a class="post-title" href="https://pegameunviaje.com/la-bufadora-el-segundo-geiser-mas-grande-del-mundo/" title="La Bufadora, el segundo géiser más grande del mundo">La Bufadora, el segundo géiser más grande del mundo</a>
    <div class="post-meta">
    </div>
    </div>
    </li>
    <li class="post cf">
    <a class="image-link" href="https://pegameunviaje.com/rosarito-bajacalifornia-mexico/">
    <img alt="" class="attachment-cheerup-thumb size-cheerup-thumb wp-post-image" height="67" sizes="(max-width: 87px) 100vw, 87px" src="https://pegameunviaje.com/wp-content/uploads/2019/03/Sin-título-1-87x67.jpg" srcset="https://pegameunviaje.com/wp-content/uploads/2019/03/Sin-título-1-87x67.jpg 87w, https://pegameunviaje.com/wp-content/uploads/2019/03/Sin-título-1-370x285.jpg 370w, https://pegameunviaje.com/wp-content/uploads/2019/03/Sin-título-1-260x200.jpg 260w" title="Rosarito, el rincón de México donde se rodó Titanic" width="87"/> </a>
    <div class="content">
    <a class="post-title" href="https://pegameunviaje.com/rosarito-bajacalifornia-mexico/" title="Rosarito, el rincón de México donde se rodó Titanic">Rosarito, el rincón de México donde se rodó Titanic</a>
    <div class="post-meta">
    </div>
    </div>
    </li>
    </ul>
    </li>
    <li class="widget column col-4 widget_mc4wp_form_widget" id="mc4wp_form_widget-3"><h5 class="widget-title">Newsletter</h5><script>(function() {
    	window.mc4wp = window.mc4wp || {
    		listeners: [],
    		forms: {
    			on: function(evt, cb) {
    				window.mc4wp.listeners.push(
    					{
    						event   : evt,
    						callback: cb
    					}
    				);
    			}
    		}
    	}
    })();
    </script><!-- Mailchimp for WordPress v4.7.6 - https://wordpress.org/plugins/mailchimp-for-wp/ --><form class="mc4wp-form mc4wp-form-1270" data-id="1270" data-name="Suscríbete a mi newsletter" id="mc4wp-form-2" method="post"><div class="mc4wp-form-fields"><p style="text-align: center"> 
      Si estas interesado en conocer mis andaduras, déjame por aquí tu correo electrónico para no perderte nada.
      <br/><br/>
    <input name="EMAIL" required="" type="email"/>
    </p>
    <p style="text-align: center">
    <input type="submit" value="Suscribirme"/>
    </p></div><label style="display: none !important;">Deja vacío este campo si eres humano: <input autocomplete="off" name="_mc4wp_honeypot" tabindex="-1" type="text" value=""/></label><input name="_mc4wp_timestamp" type="hidden" value="1612804878"/><input name="_mc4wp_form_id" type="hidden" value="1270"/><input name="_mc4wp_form_element_id" type="hidden" value="mc4wp-form-2"/><div class="mc4wp-response"></div></form><!-- / Mailchimp for WordPress Plugin --></li> </ul>
    </div>
    </section>
    <div class="social-strip">
    <ul class="social-icons">
    </ul>
    </div>
    <section class="lower-footer cf">
    <div class="wrap">
    <div class="bottom cf">
    <p class="copyright">Copyright © 2019 Pégame un viaje. <a href="/politica-de-cookies">Política de cookies.</a> <a href="/politica-de-privacidad">Poltica de privacidad.</a></p>
    <div class="to-top">
    <a class="back-to-top" href="#"><i class="fa fa-angle-up"></i> Top</a>
    </div>
    </div>
    </div>
    </section>
    </div>
    </footer>
    </div> <!-- .main-wrap -->
    <div class="mobile-menu-container off-canvas">
    <a class="close" href="#"><i class="fa fa-times"></i></a>
    <div class="logo">
    </div>
    <ul class="mobile-menu"></ul>
    </div>
    <div id="cookie-law-info-bar"><h5 class="cli_messagebar_head">Bienvenido al blog. Dame solo un segundo!</h5><span>Utilizamos cookies para almacenar información (como tus preferencias personales al visitar el sitio web). Consulta más info aquí si quieres antes de aceptar. <br>
    <a class="cli_settings_button" role="button" style="margin:5px 20px 5px 20px;" tabindex="0">Leer más</a><a class="medium cli-plugin-button cli-plugin-main-button cookie_action_close_header cli_action_button" data-cli_action="accept" id="cookie_action_close_header" role="button" style="display:inline-block;  margin:5px; " tabindex="0">Aceptar</a></br></span></div><div id="cookie-law-info-again" style="display:none;"><span id="cookie_hdr_showagain">Privacidad y Política de cookies</span></div><div aria-hidden="true" aria-labelledby="cliSettingsPopup" class="cli-modal" id="cliSettingsPopup" role="dialog" tabindex="-1">
    <div class="cli-modal-dialog" role="document">
    <div class="cli-modal-content cli-bar-popup">
    <button class="cli-modal-close" id="cliModalClose" type="button">
    <svg class="" viewbox="0 0 24 24"><path d="M19 6.41l-1.41-1.41-5.59 5.59-5.59-5.59-1.41 1.41 5.59 5.59-5.59 5.59 1.41 1.41 5.59-5.59 5.59 5.59 1.41-1.41-5.59-5.59z"></path><path d="M0 0h24v24h-24z" fill="none"></path></svg>
    <span class="wt-cli-sr-only">Cerrar</span>
    </button>
    <div class="cli-modal-body">
    <div class="cli-container-fluid cli-tab-container">
    <div class="cli-row">
    <div class="cli-col-12 cli-align-items-stretch cli-px-0">
    <div class="cli-privacy-overview">
    <h4>Privacy Overview</h4>
    <div class="cli-privacy-content">
    <div class="cli-privacy-content-text">This website uses cookies to improve your experience while you navigate through the website. Out of these cookies, the cookies that are categorized as necessary are stored on your browser as they are as essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may have an effect on your browsing experience.</div>
    </div>
    <a class="cli-privacy-readmore" data-readless-text="Mostrar menos" data-readmore-text="Mostrar más"></a> </div>
    </div>
    <div class="cli-col-12 cli-align-items-stretch cli-px-0 cli-tab-section-container">
    <div class="cli-tab-section">
    <div class="cli-tab-header">
    <a class="cli-nav-link cli-settings-mobile" data-target="necessary" data-toggle="cli-toggle-tab" role="button" tabindex="0">
                                Necesarias 
                            </a>
    <span class="cli-necessary-caption">Siempre activado</span> </div>
    <div class="cli-tab-content">
    <div class="cli-tab-pane cli-fade" data-id="necessary">
    <p>Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.</p>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="cli-modal-backdrop cli-fade cli-settings-overlay"></div>
    <div class="cli-modal-backdrop cli-fade cli-popupbar-overlay"></div>
    <script type="text/javascript">
      /* <![CDATA[ */
      cli_cookiebar_settings='{"animate_speed_hide":"500","animate_speed_show":"500","background":"#FFF","border":"#b1a6a6c2","border_on":false,"button_1_button_colour":"#000","button_1_button_hover":"#000000","button_1_link_colour":"#fff","button_1_as_button":true,"button_1_new_win":false,"button_2_button_colour":"#333","button_2_button_hover":"#292929","button_2_link_colour":"#444","button_2_as_button":false,"button_2_hidebar":false,"button_3_button_colour":"#000","button_3_button_hover":"#000000","button_3_link_colour":"#fff","button_3_as_button":true,"button_3_new_win":false,"button_4_button_colour":"#000","button_4_button_hover":"#000000","button_4_link_colour":"#62a329","button_4_as_button":false,"font_family":"inherit","header_fix":false,"notify_animate_hide":true,"notify_animate_show":false,"notify_div_id":"#cookie-law-info-bar","notify_position_horizontal":"right","notify_position_vertical":"bottom","scroll_close":false,"scroll_close_reload":false,"accept_close_reload":false,"reject_close_reload":false,"showagain_tab":false,"showagain_background":"#fff","showagain_border":"#000","showagain_div_id":"#cookie-law-info-again","showagain_x_position":"100px","text":"#000","show_once_yn":false,"show_once":"10000","logging_on":false,"as_popup":false,"popup_overlay":true,"bar_heading_text":"Bienvenido al blog. Dame solo un segundo!","cookie_bar_as":"banner","popup_showagain_position":"bottom-right","widget_position":"left"}';
      /* ]]> */
    </script><script>(function() {function maybePrefixUrlField() {
    	if (this.value.trim() !== '' && this.value.indexOf('http') !== 0) {
    		this.value = "http://" + this.value;
    	}
    }
    
    var urlFields = document.querySelectorAll('.mc4wp-form input[type="url"]');
    if (urlFields) {
    	for (var j=0; j < urlFields.length; j++) {
    		urlFields[j].addEventListener('blur', maybePrefixUrlField);
    	}
    }
    })();</script><link href="http://pegameunviaje.com/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.13-9993131" id="mediaelement-css" media="all" rel="stylesheet" type="text/css"/>
    <link href="http://pegameunviaje.com/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=5.3.2" id="wp-mediaelement-css" media="all" rel="stylesheet" type="text/css"/>
    <script src="http://pegameunviaje.com/wp-includes/js/comment-reply.min.js?ver=5.3.2" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var wpcf7 = {"apiSettings":{"root":"https:\/\/pegameunviaje.com\/wp-json\/contact-form-7\/v1","namespace":"contact-form-7\/v1"}};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-content/plugins/contact-form-7/includes/js/scripts.js?ver=5.1.7" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-content/plugins/mapplic/js/magnific-popup.js" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var Bunyad = {"custom_ajax_url":"\/3-anecdotas-divertidas-de-mis-viajes\/"};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-content/themes/cheerup/js/bunyad-theme.js?ver=4.0.0" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-content/themes/cheerup/js/jquery.slick.js?ver=4.0.0" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-content/themes/cheerup/js/jarallax.js?ver=4.0.0" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-content/themes/cheerup/js/jquery.sticky-sidebar.js?ver=4.0.0" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-includes/js/wp-embed.min.js?ver=5.3.2" type="text/javascript"></script>
    <script type="text/javascript">
    var mejsL10n = {"language":"es","strings":{"mejs.install-flash":"Est\u00e1s usando un navegador que no tiene Flash activo o instalado. Por favor, activa el componente del reproductor Flash o descarga la \u00faltima versi\u00f3n desde https:\/\/get.adobe.com\/flashplayer\/","mejs.fullscreen-off":"Salir de pantalla completa","mejs.fullscreen-on":"Ver en pantalla completa","mejs.download-video":"Descargar el v\u00eddeo","mejs.fullscreen":"Pantalla completa","mejs.time-jump-forward":["Saltar %1 segundo hacia adelante","Salta hacia adelante %1 segundos"],"mejs.loop":"Alternar bucle","mejs.play":"Reproducir","mejs.pause":"Pausa","mejs.close":"Cerrar","mejs.time-slider":"Control de tiempo","mejs.time-help-text":"Usa las teclas de direcci\u00f3n izquierda\/derecha para avanzar un segundo y las flechas arriba\/abajo para avanzar diez segundos.","mejs.time-skip-back":["Saltar atr\u00e1s 1 segundo","Retroceder %1 segundos"],"mejs.captions-subtitles":"Pies de foto \/ Subt\u00edtulos","mejs.captions-chapters":"Cap\u00edtulos","mejs.none":"Ninguna","mejs.mute-toggle":"Desactivar el sonido","mejs.volume-help-text":"Utiliza las teclas de flecha arriba\/abajo para aumentar o disminuir el volumen.","mejs.unmute":"Activar el sonido","mejs.mute":"Silenciar","mejs.volume-slider":"Control de volumen","mejs.video-player":"Reproductor de v\u00eddeo","mejs.audio-player":"Reproductor de audio","mejs.ad-skip":"Saltar el anuncio","mejs.ad-skip-info":["Saltar en 1 segundo","Saltar en %1 segundos"],"mejs.source-chooser":"Selector de origen","mejs.stop":"Parar","mejs.speed-rate":"Tasa de velocidad","mejs.live-broadcast":"Transmisi\u00f3n en vivo","mejs.afrikaans":"Afrik\u00e1ans","mejs.albanian":"Albano","mejs.arabic":"\u00c1rabe","mejs.belarusian":"Bielorruso","mejs.bulgarian":"B\u00falgaro","mejs.catalan":"Catal\u00e1n","mejs.chinese":"Chino","mejs.chinese-simplified":"Chino (Simplificado)","mejs.chinese-traditional":"Chino (Tradicional)","mejs.croatian":"Croata","mejs.czech":"Checo","mejs.danish":"Dan\u00e9s","mejs.dutch":"Holand\u00e9s","mejs.english":"Ingl\u00e9s","mejs.estonian":"Estonio","mejs.filipino":"Filipino","mejs.finnish":"Fin\u00e9s","mejs.french":"Franc\u00e9s","mejs.galician":"Gallego","mejs.german":"Alem\u00e1n","mejs.greek":"Griego","mejs.haitian-creole":"Creole haitiano","mejs.hebrew":"Hebreo","mejs.hindi":"Indio","mejs.hungarian":"H\u00fangaro","mejs.icelandic":"Island\u00e9s","mejs.indonesian":"Indonesio","mejs.irish":"Irland\u00e9s","mejs.italian":"Italiano","mejs.japanese":"Japon\u00e9s","mejs.korean":"Coreano","mejs.latvian":"Let\u00f3n","mejs.lithuanian":"Lituano","mejs.macedonian":"Macedonio","mejs.malay":"Malayo","mejs.maltese":"Malt\u00e9s","mejs.norwegian":"Noruego","mejs.persian":"Persa","mejs.polish":"Polaco","mejs.portuguese":"Portugu\u00e9s","mejs.romanian":"Rumano","mejs.russian":"Ruso","mejs.serbian":"Serbio","mejs.slovak":"Eslovaco","mejs.slovenian":"Esloveno","mejs.spanish":"Espa\u00f1ol","mejs.swahili":"Swahili","mejs.swedish":"Sueco","mejs.tagalog":"Tagalo","mejs.thai":"Tailand\u00e9s","mejs.turkish":"Turco","mejs.ukrainian":"Ukraniano","mejs.vietnamese":"Vietnamita","mejs.welsh":"Gal\u00e9s","mejs.yiddish":"Yiddish"}};
    </script>
    <script src="http://pegameunviaje.com/wp-includes/js/mediaelement/mediaelement-and-player.min.js?ver=4.2.13-9993131" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-includes/js/mediaelement/mediaelement-migrate.min.js?ver=5.3.2" type="text/javascript"></script>
    <script type="text/javascript">
    /* <![CDATA[ */
    var _wpmejsSettings = {"pluginPath":"\/wp-includes\/js\/mediaelement\/","classPrefix":"mejs-","stretching":"responsive"};
    /* ]]> */
    </script>
    <script src="http://pegameunviaje.com/wp-includes/js/mediaelement/wp-mediaelement.min.js?ver=5.3.2" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-includes/js/mediaelement/renderers/vimeo.min.js?ver=4.2.13-9993131" type="text/javascript"></script>
    <script src="http://pegameunviaje.com/wp-content/plugins/mailchimp-for-wp/assets/js/forms.min.js?ver=4.7.6" type="text/javascript"></script>
    <!-- start Simple Custom CSS and JS -->
    <script type="text/javascript">
    
    
    //Traducciones
    jQuery("a.read-more-btn").text('Seguir leyendo');
    jQuery("span.author span").text("Autor");
    jQuery("span.title:contains('Related Posts')").text("Recomendaciones");
    jQuery("span.title:contains('Write A Comment')").text("Deja tu comentario");
    jQuery("a.view-all").text("Ver todo")
    
    //CTAs Sidebar: cambio para que se abran en otra pestaña
    jQuery(".cta-box a").attr("target", "_blank")
    
    // Sidebar: newsletter
    jQuery("#bunyad-widget-subscribe-7 input").attr("placeholder", "Introduzca aquí su email")
    
    //Mensaje pre-comentarios
    jQuery("p.logged-in-as").css("display", "none");
    
    //Formulario
    jQuery("form input[name='nombre'], form input[name='email'], form input[name='asunto']").css("width","100%");
    
    // Mapa
    jQuery("article#post-162").css("width", "100%");
    
    // Cookies
    jQuery(".cli_settings_button").attr("href", "https://www.pegameunviaje.com/politica-de-cookies");
    jQuery(".cli_settings_button").removeClass("cli_settings_button");
    </script>
    <!-- end Simple Custom CSS and JS -->
    </body>
    </html>




```python
# Obtenemos el texto espedifico
texto = []
for text in s.find_all('div',{'class':'post-content description cf'}):
    b = text
    texto.append(b)
```


```python
texto
```




    [<div class="post-content description cf">
     <p>Siempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido curioso recoger <strong>algunas de las anécdotas más curiosas </strong>que me han pasado estando <strong>de viaje</strong> para contártelas al detalle.</p>
     <p> <strong>1. El conductor interesado </strong><br/></p>
     <p>En Filippiada, en Grecia, tuve que hacer autoestop con una amiga para moverme hasta una localidad cercana. No había autobús ni ningún otro medio de transporte. Después de un buen rato con el pulgar arriba, paró un coche. <strong>Pero lejos de lo que te imaginas, no fue nuestra salvación.</strong><br/></p>
     <p style="text-align:left">El conductor redujo la velocidad y atendió a la petición de mi compañera, que sujetaba un cartel en el que habíamos escrito el nombre de nuestro destino. Pero de pronto se dio cuenta de algo con lo que no contaba.</p>
     <p>Mi turno de hacer autoestop ya había pasado, y mientras ella hacía el suyo yo descansaba en un muro a la sombra, a unos cuantos metros de distancia. Ella se acercó feliz hasta donde estaba yo para decirme que un coche había parado, y cuando el conductor descubrió que yo iba en el pack… ¡PUM! Acelerón y aquí no ha pasado nada.<br/></p>
     <p><strong>2. El Blablacar más «crack»</strong><br/></p>
     <p>Cuando me di cuenta ya era tarde; un despiste me había hecho bajar del autobús olvidando mi maleta en la bodega. De pronto me entró el agobio porque faltaban muy pocos minutos para que un tipo con el que había contactado a través de Blablacar viniera a recogerme con su coche (el autobús no me dejaba en mi parada definitiva, todavía me quedaban más de dos horas de camino). Pensé: <strong>«Si no tengo la maleta, ¿qué hago?</strong>, ¿me quedo en esta ciudad a buscarla o me subo al coche con él y ya arreglaré este asunto?».<br/></p>
     <p>Localicé a la empresa de autobuses y me dijo que mi maleta ya estaba en Catania, en Sicilia, y que si quería la podían dejar en una oficina de por allí para que no siguiera dando vueltas. Les dije que sí.  En ese momento llegó Graziano con su coche, el señor con el que había quedado para que me llevara al sur de la isla. </p>
     <blockquote class="wp-block-quote"><p>Si no tengo la maleta, ¿qué hago? -pensé muuuy agobiado</p></blockquote>
     <p>Abrí la puerta y le dije lo que me pasaba: «Hola, Graziano. Tengo un problema y no me voy a poder ir contigo porque me he dejado la maleta en el bus». <strong>Contra todo pronóstico, sonrió y me dijo: «¡Anda, sube! Vamos a buscarla»</strong>. Y eso hizo. Condujo hasta Catania, aparcó el coche y me acompañó a cuatro oficinas distintas para dar con mi equipaje. <br/></p>
     <p><strong>3. El mejor calefactor para una congelación</strong><br/></p>
     <p>En Strandhill, Irlanda, se cruzó en mi camino Chris, <strong>un señor de los que inspiran</strong> y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento…<br/></p>
     <p>Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. <strong>Aunque tenía un «pequeño» problema</strong>: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.</p>
     <p>Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. </p>
     <p><strong>Y eso hice, fui para allá y la cogí.</strong> Aunque el neopreno no me lo pudo prestar, y no porque se negara… Lamentablemente le sacaba unos 15 cm de altura.</p>
     <p>Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.<br/></p>
     <p>El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.</p>
     <p>Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar,  y hasta cantamos juntos la canción de Annie. </p>
     <p>Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero… seguro que a ti también te han pasado cosas así.</p>
     <p>Si tienes un hueco, pásate por mis redes y cuéntamelas, que seguro que me alegras el día.</p>
     <p>Ah, por cierto… Por suerte, como sabes, siempre empuño la cámara, así que puedes ver grabadas todas estas anécdotas (y dos más bastante curiosas) en el vídeo que te dejo a continuación: </p>
     <p><br/></p>
     <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
     <iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="433" src="https://www.youtube.com/embed/DiZGeI2cOOA?start=403&amp;feature=oembed" width="770"></iframe>
     </div></figure>
     </div>]




```python
# Utilizamos el regex para eliminar los valores que no nos sirven
lista_palab = re.sub(r"<.+?>", "", str(texto))
lista_palab
```




    '[\nSiempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido curioso recoger algunas de las anécdotas más curiosas que me han pasado estando de viaje para contártelas al detalle.\n 1. El conductor interesado \nEn Filippiada, en Grecia, tuve que hacer autoestop con una amiga para moverme hasta una localidad cercana. No había autobús ni ningún otro medio de transporte. Después de un buen rato con el pulgar arriba, paró un coche. Pero lejos de lo que te imaginas, no fue nuestra salvación.\nEl conductor redujo la velocidad y atendió a la petición de mi compañera, que sujetaba un cartel en el que habíamos escrito el nombre de nuestro destino. Pero de pronto se dio cuenta de algo con lo que no contaba.\nMi turno de hacer autoestop ya había pasado, y mientras ella hacía el suyo yo descansaba en un muro a la sombra, a unos cuantos metros de distancia. Ella se acercó feliz hasta donde estaba yo para decirme que un coche había parado, y cuando el conductor descubrió que yo iba en el pack… ¡PUM! Acelerón y aquí no ha pasado nada.\n2. El Blablacar más «crack»\nCuando me di cuenta ya era tarde; un despiste me había hecho bajar del autobús olvidando mi maleta en la bodega. De pronto me entró el agobio porque faltaban muy pocos minutos para que un tipo con el que había contactado a través de Blablacar viniera a recogerme con su coche (el autobús no me dejaba en mi parada definitiva, todavía me quedaban más de dos horas de camino). Pensé: «Si no tengo la maleta, ¿qué hago?, ¿me quedo en esta ciudad a buscarla o me subo al coche con él y ya arreglaré este asunto?».\nLocalicé a la empresa de autobuses y me dijo que mi maleta ya estaba en Catania, en Sicilia, y que si quería la podían dejar en una oficina de por allí para que no siguiera dando vueltas. Les dije que sí. \xa0En ese momento llegó Graziano con su coche, el señor con el que había quedado para que me llevara al sur de la isla. \nSi no tengo la maleta, ¿qué hago? -pensé muuuy agobiado\nAbrí la puerta y le dije lo que me pasaba: «Hola, Graziano. Tengo un problema y no me voy a poder ir contigo porque me he dejado la maleta en el bus». Contra todo pronóstico, sonrió y me dijo: «¡Anda, sube! Vamos a buscarla». Y eso hizo. Condujo hasta Catania, aparcó el coche y me acompañó a cuatro oficinas distintas para dar con mi equipaje. \n3. El mejor calefactor para una congelación\nEn Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento…\nStrandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.\nTodo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. \nY eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara… Lamentablemente le sacaba unos 15 cm de altura.\nLuego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.\nEl caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.\nChris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar,  y hasta cantamos juntos la canción de Annie. \nSé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero… seguro que a ti también te han pasado cosas así.\nSi tienes un hueco, pásate por mis redes y cuéntamelas, que seguro que me alegras el día.\nAh, por cierto… Por suerte, como sabes, siempre empuño la cámara, así que puedes ver grabadas todas estas anécdotas (y dos más bastante curiosas) en el vídeo que te dejo a continuación: \n\n\n\n\n]'




```python
# Eliminamos los saltos de línea
mytext = "".join(lista_palab.split("\n"))
mytext
```




    '[Siempre pasa. Si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. Yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. Hoy me ha parecido curioso recoger algunas de las anécdotas más curiosas que me han pasado estando de viaje para contártelas al detalle. 1. El conductor interesado En Filippiada, en Grecia, tuve que hacer autoestop con una amiga para moverme hasta una localidad cercana. No había autobús ni ningún otro medio de transporte. Después de un buen rato con el pulgar arriba, paró un coche. Pero lejos de lo que te imaginas, no fue nuestra salvación.El conductor redujo la velocidad y atendió a la petición de mi compañera, que sujetaba un cartel en el que habíamos escrito el nombre de nuestro destino. Pero de pronto se dio cuenta de algo con lo que no contaba.Mi turno de hacer autoestop ya había pasado, y mientras ella hacía el suyo yo descansaba en un muro a la sombra, a unos cuantos metros de distancia. Ella se acercó feliz hasta donde estaba yo para decirme que un coche había parado, y cuando el conductor descubrió que yo iba en el pack… ¡PUM! Acelerón y aquí no ha pasado nada.2. El Blablacar más «crack»Cuando me di cuenta ya era tarde; un despiste me había hecho bajar del autobús olvidando mi maleta en la bodega. De pronto me entró el agobio porque faltaban muy pocos minutos para que un tipo con el que había contactado a través de Blablacar viniera a recogerme con su coche (el autobús no me dejaba en mi parada definitiva, todavía me quedaban más de dos horas de camino). Pensé: «Si no tengo la maleta, ¿qué hago?, ¿me quedo en esta ciudad a buscarla o me subo al coche con él y ya arreglaré este asunto?».Localicé a la empresa de autobuses y me dijo que mi maleta ya estaba en Catania, en Sicilia, y que si quería la podían dejar en una oficina de por allí para que no siguiera dando vueltas. Les dije que sí. \xa0En ese momento llegó Graziano con su coche, el señor con el que había quedado para que me llevara al sur de la isla. Si no tengo la maleta, ¿qué hago? -pensé muuuy agobiadoAbrí la puerta y le dije lo que me pasaba: «Hola, Graziano. Tengo un problema y no me voy a poder ir contigo porque me he dejado la maleta en el bus». Contra todo pronóstico, sonrió y me dijo: «¡Anda, sube! Vamos a buscarla». Y eso hizo. Condujo hasta Catania, aparcó el coche y me acompañó a cuatro oficinas distintas para dar con mi equipaje. 3. El mejor calefactor para una congelaciónEn Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento…Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no porque se negara… Lamentablemente le sacaba unos 15 cm de altura.Luego, en la playa, un alemán me solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar,  y hasta cantamos juntos la canción de Annie. Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de Irlanda con un señor que acaba de conocer? Pero… seguro que a ti también te han pasado cosas así.Si tienes un hueco, pásate por mis redes y cuéntamelas, que seguro que me alegras el día.Ah, por cierto… Por suerte, como sabes, siempre empuño la cámara, así que puedes ver grabadas todas estas anécdotas (y dos más bastante curiosas) en el vídeo que te dejo a continuación: ]'




```python
# Modificamos a minusculas
text_low = mytext.lower()
```


```python
# Mostramos
text_low
```




    '[siempre pasa. si ya te cruzas con situaciones atípicas cuando estás en tu ciudad, cuando sales de ella a veces se arman unas que no veas. yo creo que es porque vives mucho más en mucho menos tiempo y porque fuera de tu zona habitual las cosas a menudo resultan extrañas. hoy me ha parecido curioso recoger algunas de las anécdotas más curiosas que me han pasado estando de viaje para contártelas al detalle. 1. el conductor interesado en filippiada, en grecia, tuve que hacer autoestop con una amiga para moverme hasta una localidad cercana. no había autobús ni ningún otro medio de transporte. después de un buen rato con el pulgar arriba, paró un coche. pero lejos de lo que te imaginas, no fue nuestra salvación.el conductor redujo la velocidad y atendió a la petición de mi compañera, que sujetaba un cartel en el que habíamos escrito el nombre de nuestro destino. pero de pronto se dio cuenta de algo con lo que no contaba.mi turno de hacer autoestop ya había pasado, y mientras ella hacía el suyo yo descansaba en un muro a la sombra, a unos cuantos metros de distancia. ella se acercó feliz hasta donde estaba yo para decirme que un coche había parado, y cuando el conductor descubrió que yo iba en el pack… ¡pum! acelerón y aquí no ha pasado nada.2. el blablacar más «crack»cuando me di cuenta ya era tarde; un despiste me había hecho bajar del autobús olvidando mi maleta en la bodega. de pronto me entró el agobio porque faltaban muy pocos minutos para que un tipo con el que había contactado a través de blablacar viniera a recogerme con su coche (el autobús no me dejaba en mi parada definitiva, todavía me quedaban más de dos horas de camino). pensé: «si no tengo la maleta, ¿qué hago?, ¿me quedo en esta ciudad a buscarla o me subo al coche con él y ya arreglaré este asunto?».localicé a la empresa de autobuses y me dijo que mi maleta ya estaba en catania, en sicilia, y que si quería la podían dejar en una oficina de por allí para que no siguiera dando vueltas. les dije que sí. \xa0en ese momento llegó graziano con su coche, el señor con el que había quedado para que me llevara al sur de la isla. si no tengo la maleta, ¿qué hago? -pensé muuuy agobiadoabrí la puerta y le dije lo que me pasaba: «hola, graziano. tengo un problema y no me voy a poder ir contigo porque me he dejado la maleta en el bus». contra todo pronóstico, sonrió y me dijo: «¡anda, sube! vamos a buscarla». y eso hizo. condujo hasta catania, aparcó el coche y me acompañó a cuatro oficinas distintas para dar con mi equipaje. 3. el mejor calefactor para una congelaciónen strandhill, irlanda, se cruzó en mi camino chris, un señor de los que inspiran y se posicionan como referente. fue una pieza fundamental en un momento de pura congelación. te cuento…strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas olas. y allí estaba yo también. después de unos meses viviendo en una ciudad sin costa, mis ganas por hacer un poco de surfing estaban por las nubes. aunque tenía un «pequeño» problema: no tenía equipo, ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.todo se puso a rodar enseguida. escribí a un famoso surfista de la zona y recibí una respuesta increíble. «mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. ven cuando quieras», me dijo. y eso hice, fui para allá y la cogí. aunque el neopreno no me lo pudo prestar, y no porque se negara… lamentablemente le sacaba unos 15 cm de altura.luego, en la playa, un alemán me solucionó el tema del neopreno. me prestó uno que había por su maletero, uno muy fino, de los que uso yo en el mediterráneo en otoño o primavera. y claro, era invierno y estábamos en irlanda.el caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios congelados. me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando semidesnudo, se me acercó chris. «está fría el agua, eh», apuntó este fenómeno.chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar hasta allí. sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que se encarga de pensar,  y hasta cantamos juntos la canción de annie. sé que esto último puede sonar raro, ¿quién canta annie semidesudo y congelado en un paseo de irlanda con un señor que acaba de conocer? pero… seguro que a ti también te han pasado cosas así.si tienes un hueco, pásate por mis redes y cuéntamelas, que seguro que me alegras el día.ah, por cierto… por suerte, como sabes, siempre empuño la cámara, así que puedes ver grabadas todas estas anécdotas (y dos más bastante curiosas) en el vídeo que te dejo a continuación: ]'




```python
# Generamos 2 str
word_count = 0
char_count = 0
# Dividimos los str
split_string = text_low.split()

# contamos las palabras
word_count = len(split_string)

# contamos los carácteres
for word in split_string:
    char_count += len(word)

# Mostramos
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))
```

    Total words : 861
    Total characters : 3853



```python
# Agrupamos y contamos
counts = Counter(split_string)
print("\nLas 10 mas comunes : \n")
counts.most_common(10)
```

    
    Las 10 mas comunes : 
    





    [('de', 38),
     ('que', 32),
     ('y', 30),
     ('en', 28),
     ('el', 24),
     ('me', 23),
     ('la', 23),
     ('un', 18),
     ('a', 17),
     ('no', 13)]




```python
print("\nTotal characters : \n {} \n".format(counts) +"\n")
```

    
    Total characters : 
     Counter({'de': 38, 'que': 32, 'y': 30, 'en': 28, 'el': 24, 'me': 23, 'la': 23, 'un': 18, 'a': 17, 'no': 13, 'con': 12, 'para': 11, 'se': 9, 'una': 8, 'había': 8, 'mi': 7, 'por': 7, 'yo': 6, 'más': 6, 'ya': 5, 'te': 5, 'porque': 5, 'hasta': 5, 'lo': 5, 'los': 5, 'cuando': 4, 'las': 4, 'coche': 4, 'su': 4, 'si': 3, 'ella': 3, 'es': 3, 'pasado': 3, 'al': 3, 'conductor': 3, 'hacer': 3, 'autobús': 3, 'ni': 3, 'pronto': 3, 'unos': 3, 'estaba': 3, 'del': 3, 'maleta': 3, 'muy': 3, 'tengo': 3, 'señor': 3, 'está': 3, 'tu': 2, 'mucho': 2, 'zona': 2, 'cosas': 2, 'ha': 2, 'anécdotas': 2, 'han': 2, 'estando': 2, 'autoestop': 2, 'después': 2, 'pero': 2, 'fue': 2, 'cuenta': 2, 'hacía': 2, 'acercó': 2, 'donde': 2, 'blablacar': 2, 'era': 2, 'dos': 2, 'maleta,': 2, '¿qué': 2, 'ciudad': 2, 'o': 2, 'este': 2, 'catania,': 2, 'allí': 2, 'dije': 2, 'momento': 2, 'puerta': 2, 'le': 2, 'eso': 2, 'como': 2, 'siempre': 2, 'mis': 2, 'aunque': 2, 'tenía': 2, 'tienes': 2, 'uno': 2, 'cabeza': 2, 'paseo': 2, 'seguro': 2, '[siempre': 1, 'pasa.': 1, 'cruzas': 1, 'situaciones': 1, 'atípicas': 1, 'estás': 1, 'ciudad,': 1, 'sales': 1, 'veces': 1, 'arman': 1, 'unas': 1, 'veas.': 1, 'creo': 1, 'vives': 1, 'menos': 1, 'tiempo': 1, 'fuera': 1, 'habitual': 1, 'menudo': 1, 'resultan': 1, 'extrañas.': 1, 'hoy': 1, 'parecido': 1, 'curioso': 1, 'recoger': 1, 'algunas': 1, 'curiosas': 1, 'viaje': 1, 'contártelas': 1, 'detalle.': 1, '1.': 1, 'interesado': 1, 'filippiada,': 1, 'grecia,': 1, 'tuve': 1, 'amiga': 1, 'moverme': 1, 'localidad': 1, 'cercana.': 1, 'ningún': 1, 'otro': 1, 'medio': 1, 'transporte.': 1, 'buen': 1, 'rato': 1, 'pulgar': 1, 'arriba,': 1, 'paró': 1, 'coche.': 1, 'lejos': 1, 'imaginas,': 1, 'nuestra': 1, 'salvación.el': 1, 'redujo': 1, 'velocidad': 1, 'atendió': 1, 'petición': 1, 'compañera,': 1, 'sujetaba': 1, 'cartel': 1, 'habíamos': 1, 'escrito': 1, 'nombre': 1, 'nuestro': 1, 'destino.': 1, 'dio': 1, 'algo': 1, 'contaba.mi': 1, 'turno': 1, 'pasado,': 1, 'mientras': 1, 'suyo': 1, 'descansaba': 1, 'muro': 1, 'sombra,': 1, 'cuantos': 1, 'metros': 1, 'distancia.': 1, 'feliz': 1, 'decirme': 1, 'parado,': 1, 'descubrió': 1, 'iba': 1, 'pack…': 1, '¡pum!': 1, 'acelerón': 1, 'aquí': 1, 'nada.2.': 1, '«crack»cuando': 1, 'di': 1, 'tarde;': 1, 'despiste': 1, 'hecho': 1, 'bajar': 1, 'olvidando': 1, 'bodega.': 1, 'entró': 1, 'agobio': 1, 'faltaban': 1, 'pocos': 1, 'minutos': 1, 'tipo': 1, 'contactado': 1, 'través': 1, 'viniera': 1, 'recogerme': 1, '(el': 1, 'dejaba': 1, 'parada': 1, 'definitiva,': 1, 'todavía': 1, 'quedaban': 1, 'horas': 1, 'camino).': 1, 'pensé:': 1, '«si': 1, 'hago?,': 1, '¿me': 1, 'quedo': 1, 'esta': 1, 'buscarla': 1, 'subo': 1, 'él': 1, 'arreglaré': 1, 'asunto?».localicé': 1, 'empresa': 1, 'autobuses': 1, 'dijo': 1, 'sicilia,': 1, 'quería': 1, 'podían': 1, 'dejar': 1, 'oficina': 1, 'siguiera': 1, 'dando': 1, 'vueltas.': 1, 'les': 1, 'sí.': 1, 'ese': 1, 'llegó': 1, 'graziano': 1, 'coche,': 1, 'quedado': 1, 'llevara': 1, 'sur': 1, 'isla.': 1, 'hago?': 1, '-pensé': 1, 'muuuy': 1, 'agobiadoabrí': 1, 'pasaba:': 1, '«hola,': 1, 'graziano.': 1, 'problema': 1, 'voy': 1, 'poder': 1, 'ir': 1, 'contigo': 1, 'he': 1, 'dejado': 1, 'bus».': 1, 'contra': 1, 'todo': 1, 'pronóstico,': 1, 'sonrió': 1, 'dijo:': 1, '«¡anda,': 1, 'sube!': 1, 'vamos': 1, 'buscarla».': 1, 'hizo.': 1, 'condujo': 1, 'aparcó': 1, 'acompañó': 1, 'cuatro': 1, 'oficinas': 1, 'distintas': 1, 'dar': 1, 'equipaje.': 1, '3.': 1, 'mejor': 1, 'calefactor': 1, 'congelaciónen': 1, 'strandhill,': 1, 'irlanda,': 1, 'cruzó': 1, 'camino': 1, 'chris,': 1, 'inspiran': 1, 'posicionan': 1, 'referente.': 1, 'pieza': 1, 'fundamental': 1, 'pura': 1, 'congelación.': 1, 'cuento…strandhill': 1, 'playa': 1, 'mar': 1, 'ruge': 1, 'bien,': 1, 'lleno': 1, 'surfistas': 1, 'busca': 1, 'buenas': 1, 'olas.': 1, 'también.': 1, 'meses': 1, 'viviendo': 1, 'sin': 1, 'costa,': 1, 'ganas': 1, 'poco': 1, 'surfing': 1, 'estaban': 1, 'nubes.': 1, '«pequeño»': 1, 'problema:': 1, 'equipo,': 1, 'tabla,': 1, 'neopreno,': 1, 'tampoco': 1, 'ninguna': 1, 'tienda': 1, 'alquilarlo.todo': 1, 'puso': 1, 'rodar': 1, 'enseguida.': 1, 'escribí': 1, 'famoso': 1, 'surfista': 1, 'recibí': 1, 'respuesta': 1, 'increíble.': 1, '«mi': 1, 'casa': 1, 'calle': 1, 'x,': 1, 'abierta': 1, 'tabla': 1, 'esquina.': 1, 'ven': 1, 'quieras»,': 1, 'dijo.': 1, 'hice,': 1, 'fui': 1, 'allá': 1, 'cogí.': 1, 'neopreno': 1, 'pudo': 1, 'prestar,': 1, 'negara…': 1, 'lamentablemente': 1, 'sacaba': 1, '15': 1, 'cm': 1, 'altura.luego,': 1, 'playa,': 1, 'alemán': 1, 'solucionó': 1, 'tema': 1, 'neopreno.': 1, 'prestó': 1, 'maletero,': 1, 'fino,': 1, 'uso': 1, 'mediterráneo': 1, 'otoño': 1, 'primavera.': 1, 'claro,': 1, 'invierno': 1, 'estábamos': 1, 'irlanda.el': 1, 'caso': 1, 'salí': 1, 'agua': 1, 'previsto': 1, 'manos,': 1, 'labios': 1, 'congelados.': 1, 'empecé': 1, 'cambiar': 1, 'mismo': 1, 'contorneaba': 1, 'costa': 1, 'y,': 1, 'semidesnudo,': 1, 'chris.': 1, '«está': 1, 'fría': 1, 'agua,': 1, 'eh»,': 1, 'apuntó': 1, 'fenómeno.chris': 1, 'superaba': 1, '65': 1, 'años': 1, 'todos': 1, 'días': 1, 'recorrido': 1, 'decenas': 1, 'kilómetros': 1, 'llegar': 1, 'allí.': 1, 'sus': 1, 'gracietas': 1, 'buena': 1, 'conversación': 1, 'hicieron': 1, 'apartar': 1, 'frío': 1, 'parte': 1, 'encarga': 1, 'pensar,': 1, 'cantamos': 1, 'juntos': 1, 'canción': 1, 'annie.': 1, 'sé': 1, 'esto': 1, 'último': 1, 'puede': 1, 'sonar': 1, 'raro,': 1, '¿quién': 1, 'canta': 1, 'annie': 1, 'semidesudo': 1, 'congelado': 1, 'irlanda': 1, 'acaba': 1, 'conocer?': 1, 'pero…': 1, 'ti': 1, 'también': 1, 'así.si': 1, 'hueco,': 1, 'pásate': 1, 'redes': 1, 'cuéntamelas,': 1, 'alegras': 1, 'día.ah,': 1, 'cierto…': 1, 'suerte,': 1, 'sabes,': 1, 'empuño': 1, 'cámara,': 1, 'así': 1, 'puedes': 1, 'ver': 1, 'grabadas': 1, 'todas': 1, 'estas': 1, '(y': 1, 'bastante': 1, 'curiosas)': 1, 'vídeo': 1, 'dejo': 1, 'continuación:': 1, ']': 1}) 
    
    


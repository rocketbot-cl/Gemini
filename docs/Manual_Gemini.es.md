



# Gemini

Este módulo te permite trabajar con la API de inteligencia artificial de Google Gemini

*Read this in other languages: [English](Manual_Gemini.md), [Português](Manual_Gemini.pr.md), [Español](Manual_Gemini.es.md)*

![banner](imgs/Banner_Gemini.jpg)
## Como instalar este módulo

Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.



## Cómo usar este módulo

Para usar este módulo, necesitamos obtener la clave API de Gemini. Sigue estos pasos:

1. Ve a la [página de claves API de Gemini](https://aistudio.google.com/app/apikey). Asegúrate de estar conectado con tu cuenta de Google.
2. Haz clic en el botón "Crear clave API".
3. Copia la clave API generada.
4. Usa esta clave API en el módulo para la autenticación y acceso a los servicios de Gemini.

### Si deseas conectar con un Agente de Gemini:

¿Cuándo usarlo?
Tu cliente creó un Agente en Vertex AI (Agent Engine/Agent Builder). Requiere credenciales de Google Cloud (no API key). Permite conectar por agent_name y chatear con su memoria/knowledge (PDFs, datastores, etc.).

Datos que te pide el comando connect:

1. Project Id: Entra a Google Cloud Console → Home (Panel) y copia el ID del proyecto (no el nombre).
2. Location: la región donde creaste el agente o donde usarás Vertex (normalmente us-central1 si no definieron otra).
3. Agent Name: Si lo creaste desde 
Agent Builder / Agent Engine, el ID aparece en la ficha del agente. También puedes obtenerlo desde la URL o panel de detalles del agente. Copia el resource name completo (incluye projects/.../locations/.../agents/...).

Importante: en modo agente NO subes el archivo desde Rocketbot; debe estar en el knowledge del agente (Vertex).


## Descripción de los comandos

### Conectar a Gemini

Conecta a la API de Google Gemini
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|API Key|API Key|AIza....|
|Modelo|Modelo de Gemini a usar|gemini-2.0-flash|
|Asignar resultado a variable|Variable donde se almacenará el modelo de Gemini|resultado|

### Generar Contenido

Genera contenido proporcionando un prompt de la información que deseas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido|¿Qué es Rocketbot?|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

### Leer Imagen

Genera contenido proporcionando una imagen de la ruta de archivo que desees
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido a partir de la imagen|¿Qué puedes ver en la imagen?|
|Imagen|Archivo que se utilizará como prompt para generar el contenido. Los tipos permitidos son png, jpeg, jpg, webp, bmp, heic y heif.|Selecciona un archivo|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

### Generar Contenido Desde txt

Genera contenido proporcionando un archivo .txt de la información que deseas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido|¿Qué lees en el archivo txt?|
|Archivo|Archivo que se utilizará como prompt para generar el contenido|Selecciona un archivo|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

### Generar Contenido Desde pdf

Genera contenido proporcionando un archivo .pdf de la información que deseas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido|¿Qué lees en el archivo pdf?|
|Archivo|Archivo que se utilizará como prompt para generar el contenido|Selecciona un archivo|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

### Generar Contenido Desde Audio

Genera contenido proporcionando un archivo de audio de la información que deseas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido|¿Qué escuchar en el audio?|
|Archivo|Archivo que se utilizará como prompt para generar el contenido|Selecciona un archivo|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

### Generar Contenido Desde Video

Genera contenido proporcionando un archivo de video de la información que deseas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Prompt|Texto que se utilizará como prompt para generar el contenido|¿Qué  contiene el video?|
|Archivo|Archivo que se utilizará como prompt para generar el contenido|Selecciona un archivo|
|Esquema de respuesta (opcional)|Formato del contenido generado (opcional). 
Los posibles tipos son "string", "number", "integer", "boolean" y "array". 
Para indicar un objeto anidado, se puede usar otro diccionario con la misma estructura.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Devolver lista de elementos|Marcar si se quiere que la respuesta sea un arreglo de objetos siguiendo el esquema dado|Checkbox|
|Timeout (segundos)|Tiempo máximo en segundos que se esperará por la respuesta de Gemini. Por default son 60 segundos.|60|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la ejecución|result|

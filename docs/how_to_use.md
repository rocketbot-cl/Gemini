## How to use this module

To use this module, we need to obtain the API key from Gemini. Follow these steps:

1. Go to the [Gemini API Key page](https://aistudio.google.com/app/apikey). Ensure you are logged in with your Google account.
2. Click on the "Create API key" button.
3. Copy the generated API key.
4. Use this API key in the module for authentication and access to Gemini services.

### If you want to connect to a Gemini Agent:

When to use it?
Your client created an Agent in Vertex AI (Agent Engine/Agent Builder). It requires Google Cloud credentials (not API keys). It allows you to connect via agent_name and chat with its memory/knowledge (PDFs, datastores, etc.).

Information requested by the connect command:

1. Project ID: Go to the Google Cloud Console → Home (Dashboard) and copy the project ID (not the name).
2. Location: The region where you created the agent or where you will use Vertex (usually us-central1 if you haven't defined another).
3. Agent Name: If you created it from Agent Builder/Agent Engine, the ID appears in the agent's tab. You can also get it from the URL or the agent's details panel. Copy the full resource name (include projects/.../locations/.../agents/...).

Important: In agent mode, DO NOT upload the file from Rocketbot; must be in the agent's knowledge (Vertex).

---

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
3. Agent Name: Si lo creaste desde Agent Builder / Agent Engine, el ID aparece en la ficha del agente. También puedes obtenerlo desde la URL o panel de detalles del agente. Copia el resource name completo (incluye projects/.../locations/.../agents/...).

Importante: en modo agente NO subes el archivo desde Rocketbot; debe estar en el knowledge del agente (Vertex).

---

## Como usar este módulo

Para usar este módulo, precisamos obter a chave API do Gemini. Siga estes passos:

1. Vá para a [página de chave API do Gemini](https://aistudio.google.com/app/apikey). Certifique-se de estar logado com sua conta do Google.
2. Clique no botão "Criar chave API".
3. Copie a chave API gerada.
4. Use essa chave API no módulo para autenticação e acesso aos serviços do Gemini.

### Se você deseja se conectar a um Agente Gemini:

Quando usar?
Seu cliente criou um Agente no Vertex AI (Agent Engine/Agent Builder). Requer credenciais do Google Cloud (não chaves de API). Permite que você se conecte via agent_name e converse com sua memória/conhecimento (PDFs, datastores, etc.).

Informações solicitadas pelo comando connect:

1. ID do Projeto: Acesse o Console do Google Cloud → Página Inicial (Painel) e copie o ID do projeto (não o nome).
2. Local: A região onde você criou o agente ou onde usará o Vertex (geralmente us-central1, caso não tenha definido outro).
3. Nome do Agente: Se você o criou no Agent Builder/Agent Engine, o ID aparece na aba do agente. Você também pode obtê-lo na URL ou no painel de detalhes do agente. Copie o nome completo do recurso (incluindo projects/.../locations/.../agents/...).

Importante: No modo agente, NÃO carregue o arquivo do Rocketbot; deve ser do conhecimento do agente (Vertex).
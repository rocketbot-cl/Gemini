



# Gemini
  
Este módulo permite trabalhar com a API de IA do Google Gemini  

*Read this in other languages: [English](Manual_Gemini.md), [Português](Manual_Gemini.pr.md), [Español](Manual_Gemini.es.md)*
  
![banner](imgs/Banner_Gemini.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  

## Como usar este módulo

Para usar este módulo, precisamos obter a chave API do Gemini. Siga estes passos:

1. Vá para a [página de chave API do Gemini](https://aistudio.google.com/app/apikey). Certifique-se de estar logado com sua conta do Google.
2. Clique no botão "Criar chave API".
3. Copie a chave API gerada.
4. Use essa chave API no módulo para autenticação e acesso aos serviços do Gemini.
## Descrição do comando

### Conectar ao Gemini
  
Conecte-se à API do Google Gemini
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Chave da API|Chave da API|AIza....|
|Atribuir resultado à variável|Variável onde o resultado da conexão será armazenado|result|

### Gerar Conteúdo
  
Gere conteúdo fornecendo um prompt das informações que deseja
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto que será usado como prompt para gerar o conteúdo|O que é Rocketbot?|
|Atribuir resultado à variável|Variável onde o resultado da execução será armazenado|result|

### Ler Imagem
  
Gere conteúdo fornecendo um prompt com uma rota de arquivo que você deseja
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto que será usado como prompt para gerar o conteúdo desde à imagem|O que é você pode olhar na imagem?|
|Imagem|Arquivo que será usado como prompt para gerar o conteúdo|Selecione um arquivo|
|Atribuir resultado à variável|Variável onde o resultado da execução será armazenado|result|

### Gerar Conteúdo Desde txt
  
Gere conteúdo fornecendo um arquivo .txt das informações que deseja
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto que será usado como prompt para gerar o conteúdo|O que você lê no arquivo txt?|
|Arquivo|Arquivo que será usado como prompt para gerar o conteúdo|Selecione um arquivo|
|Atribuir resultado à variável|Variável onde o resultado da execução será armazenado|result|

### Gerar Conteúdo Desde pdf
  
Gere conteúdo fornecendo um arquivo .pdf das informações que deseja
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto que será usado como prompt para gerar o conteúdo|O que você lê no arquivo pdf?|
|Arquivo|Arquivo que será usado como prompt para gerar o conteúdo|Selecione um arquivo|
|Atribuir resultado à variável|Variável onde o resultado da execução será armazenado|result|

### Gerar Conteúdo Desde Audio
  
Gere conteúdo fornecendo um arquivo de audio das informações que deseja
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Prompt|Texto que será usado como prompt para gerar o conteúdo|O que você ouve no áudio?|
|Arquivo|Arquivo que será usado como prompt para gerar o conteúdo|Selecione um arquivo|
|Atribuir resultado à variável|Variável onde o resultado da execução será armazenado|result|

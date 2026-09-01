



# Gemini

This module allows you to work with the Google Gemini AI API

*Read this in other languages: [English](Manual_Gemini.md), [Português](Manual_Gemini.pr.md), [Español](Manual_Gemini.es.md)*

![banner](imgs/Banner_Gemini.jpg)
## How to install this module

To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.

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
3. Agent Name: If you 
created it from Agent Builder/Agent Engine, the ID appears in the agent's tab. You can also get it from the URL or the agent's details panel. Copy the full resource name (include projects/.../locations/.../agents/...).

Important: In agent mode, DO NOT upload the file from Rocketbot; must be in the agent's knowledge (Vertex).


## Description of the commands

### Connect to Gemini

Connect to the Google Gemini API
|Parameters|Description|example|
| --- | --- | --- |
|API Key|API Key|AIza....|
|Model|Gemini model to use|gemini-3.6-flash|
|Assign result to variable|Variable where the Gemini model is to be stored|result|

### Generate Content

Generate content by providing a prompt of the information you want
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content|What is Rocketbot?|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

### Read Image

Generate content by providing a prompt with a file route you want
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content from the image|What can you see in the image?|
|Image|File that will be used as a prompt to generate the content|Select a file|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

### Generate Content From txt

Generate content by providing a .txt file of the information you want
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content|What do you read in the txt file?|
|File|File that will be used as a prompt to generate the content|Select a file|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

### Generate Content From pdf

Generate content by providing a .pdf file of the information you want
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content|What do you read in the pdf file?|
|File|File that will be used as a prompt to generate the content|Select a file|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

### Generate Content From Audio

Generate content by providing an audio file of the information you want
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content|What do you listen in the audio?|
|File|File that will be used as a prompt to generate the content|Select a file|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

### Generate Content From Video

Generate content by providing a video file of your desired information
|Parameters|Description|example|
| --- | --- | --- |
|Prompt|Text that will be used as a prompt to generate the content|What the video containso?|
|File|File that will be used as a prompt to generate the content|Select a file|
|Response schema (optional)|Format of the generated content (optional). 
The possible types are "string", "number", "integer", "boolean" and "array". 
To indicate a nested object, you can use another dictionary with the same structure.|{ "name": "string", "number": "number", "sub_object": {...}}|
|Return list of items|Check if you want the response to be an array of objects following the given schema|Checkbox|
|Timeout (seconds)|Maximum time in seconds to wait for the Gemini response. Default is 60 seconds.|60|
|Assign result to variable|Variable where the execution result will be stored|result|

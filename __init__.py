
# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import PIL.Image
import os, sys, platform
from time import sleep

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'Gemini' + os.sep + 'libs' + os.sep

system_name = platform.system().lower()

if system_name == "windows":
    cur_path_platform = os.path.join(cur_path, 'win' + os.sep)
    if cur_path_platform in sys.path:
        sys.path.remove(cur_path_platform)
    sys.path.insert(0, cur_path_platform)


elif system_name == "darwin":
    cur_path_macos = os.path.join(cur_path, 'macos' + os.sep)
    if cur_path_macos in sys.path:
        sys.path.remove(cur_path_macos)
    sys.path.insert(0, cur_path_macos)
    try:
        from gemini_mock_classes import load_mock_classes
        load_mock_classes()
    except Exception as e:
        PrintException()
        raise e 

import g_typing_extensions

if not hasattr(g_typing_extensions, "Sentinel"):
    class _CompatSentinel:
        def __new__(cls, name, /, *, module=None):
            obj = super().__new__(cls)
            obj._name = name
            obj._module = module
            return obj

        def __repr__(self):
            return self._name

    g_typing_extensions.Sentinel = _CompatSentinel
    if hasattr(g_typing_extensions, "__all__") and "Sentinel" not in g_typing_extensions.__all__:
        g_typing_extensions.__all__.append("Sentinel")

sys.modules["typing_extensions"] = g_typing_extensions
import google.generativeai as genai # type: ignore
global mod_model_Gemini


try:
    if not mod_model_Gemini: #type:ignore
        mod_model_Gemini = None
except NameError:
    mod_model_Gemini = None

module = GetParams("module")


global parse_into_gemini_schema, gemini_schema_mapper
gemini_schema_mapper = {
    "string": str,
    "integer": int,
    "number": float, 
    "boolean": bool,
    "array": list,
}

def parse_into_gemini_schema(schema, class_name="Schema"):
    
    parsed_schema = {}

    for key, value in schema.items():
        if isinstance(value, dict):
            sub_class_name = f"Schema_{key}"
            parsed_schema[key] = parse_into_gemini_schema(schema=value, class_name=sub_class_name)
        else:
            parsed_schema[key] = gemini_schema_mapper.get(value.strip().lower(), str)

    return g_typing_extensions.TypedDict(class_name, parsed_schema)



def get_response_with_schema(schema, is_list, content, timeout):
    import ast

    dict_schema: dict = ast.literal_eval(schema)
    if type(dict_schema) != dict:
        raise Exception("Response schema could not be parsed")

    Final_schema = parse_into_gemini_schema(dict_schema)
    config={"response_mime_type": "application/json", "response_schema": list[Final_schema] if is_list else Final_schema}


    return mod_model_Gemini.generate_content(content, generation_config=config, request_options={"timeout": timeout})

try:
    if module == "connect":
        try:
            api_key = GetParams("api_key")
            result = GetParams("result") 
            model_name = GetParams("model_name") or "gemini-2.0-flash"

            genai.configure(api_key=api_key)
            # get_model = genai.get_model("models/gemini-1.5-flash-latest")  # Modelo retirado
            # mod_model_Gemini = genai.GenerativeModel("gemini-1.5-flash")    # Modelo retirado
            #mod_model_Gemini = genai.GenerativeModel("gemini-2.0-flash")  # Actualización
            mod_model_Gemini = genai.GenerativeModel(model_name)
            
            SetVar(result, True)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module != "connect" and not mod_model_Gemini:
        raise Exception("Please connect to Gemini AI before using this module")

    if module == "generate_content":
        try:

            prompt = GetParams("prompt")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            result = GetParams("result")
            timeout = int(GetParams("timeout") or "60")
            
            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            response = get_response_with_schema(schema, is_list, prompt, timeout) if schema else mod_model_Gemini.generate_content(prompt, request_options={"timeout": timeout})
            
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_image":
        try:
            path = GetParams("image")
            prompt = GetParams("prompt")
            result = GetParams("result")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            timeout = int(GetParams("timeout") or "60")

            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            if not path.endswith((".png", ".jpeg", ".jpg", ".webp",".heic", ".heif", ".bmp")):
                raise Exception("File format not supported by Gemini AI using this module")
                
            file_image = PIL.Image.open(path)

            response = get_response_with_schema(schema, is_list, [prompt, file_image], timeout) if schema else mod_model_Gemini.generate_content([prompt, file_image], request_options={"timeout": timeout})
            
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_txt":
        try:
            path = GetParams("file")
            result = GetParams("result")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            timeout = int(GetParams("timeout") or "60")

            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            text = open(path,'r').read()
            
            response = get_response_with_schema(schema, is_list, text, timeout) if schema else mod_model_Gemini.generate_content(text, request_options={"timeout": timeout})

            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_pdf":
        try:
            path = GetParams("file")
            prompt = GetParams("prompt")
            result = GetParams("result")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            timeout = int(GetParams("timeout") or "60")

            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            if not path.endswith(".pdf"):
                raise Exception("Not .pdf formats not supported for pdf extraction")
            
            sample_pdf = genai.upload_file(path)

            response = get_response_with_schema(schema, is_list, [prompt, sample_pdf], timeout) if schema else mod_model_Gemini.generate_content([prompt, sample_pdf], request_options={"timeout": timeout})
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_audio":
        try:
            path = GetParams("file")
            prompt = GetParams("prompt")
            result = GetParams("result")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            timeout = int(GetParams("timeout") or "60")

            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            if not path.endswith((".wav", ".mp3", ".aiff",".aac", ".ogg", ".flac")):
                raise Exception("File format not supported by Gemini AI using this module")
            
            file = genai.upload_file(path)

            response = get_response_with_schema(schema, is_list, [file, prompt], timeout) if schema else mod_model_Gemini.generate_content([file, prompt], request_options={"timeout": timeout})
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
    
    #TODO
    if module == "generate_content_from_video":
        try:
            path = GetParams("file")
            prompt = GetParams("prompt")
            result = GetParams("result")
            schema = GetParams("schema")
            is_list = GetParams("is_list")
            timeout = int(GetParams("timeout") or "60")
            
            if isinstance(is_list, str):
                is_list = is_list.strip().lower() in ["true", "1", "yes"]
            else:
                is_list = bool(is_list)

            # if not path.endswith("mp4"):
            #     raise Exception("File format not supported by Gemini AI using this module")
            
            file = genai.upload_file(path, mime_type='video/mp4')

            while file.state.name == "PROCESSING":
                sleep(5)
                file = genai.get_file(file.name)
            #print(file)
            response = get_response_with_schema(schema, is_list, [file, prompt], timeout) if schema else mod_model_Gemini.generate_content([file, prompt], request_options={"timeout": timeout})
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
    
        
except Exception as e:
    PrintException()
    raise e
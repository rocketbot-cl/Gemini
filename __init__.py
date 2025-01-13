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
import os, sys
from time import sleep

GetParams = GetParams # type: ignore
SetVar = SetVar # type: ignore
PrintException = PrintException # type: ignore

base_path = tmp_global_obj["basepath"] # type: ignore
cur_path = base_path + 'modules' + os.sep + 'Gemini' + os.sep + 'libs' + os.sep


if cur_path not in sys.path:
    sys.path.append(cur_path)

import google.generativeai as genai # type: ignore

global mod_model_Gemini


try:
    if not mod_model_Gemini: #type:ignore
        mod_model_Gemini = None
except NameError:
    mod_model_Gemini = None

module = GetParams("module")

try:
    if module == "connect":
        try:
            api_key = GetParams("api_key")
            result = GetParams("result")

            genai.configure(api_key=api_key)
            get_model = genai.get_model("models/gemini-1.5-flash-latest")
            mod_model_Gemini = genai.GenerativeModel("gemini-1.5-flash")
            SetVar(result, True)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module != "connect" and not mod_model_Gemini:
        raise Exception("Please connect to Gemini AI before using this module")

    if module == "generate_content":
        try:
            prompt = GetParams("prompt")
            result = GetParams("result")

            response = mod_model_Gemini.generate_content(prompt)
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_image":
        try:
            path = GetParams("image")
            prompt = GetParams("prompt")
            result = GetParams("result")

            if not path.endswith((".png", ".jpeg", ".webp",".heic", ".heif")):
                raise Exception("File format not supported by Gemini AI using this module")
                
            file_image = PIL.Image.open(path)

            response = mod_model_Gemini.generate_content([prompt, file_image])
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_txt":
        try:
            path = GetParams("file")
            result = GetParams("result")
            text = open(path,'r').read()
            response = mod_model_Gemini.generate_content(text)
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_pdf":
        try:
            path = GetParams("file")
            prompt = GetParams("prompt")
            result = GetParams("result")
            if not path.endswith(".pdf"):
                raise Exception("Not .pdf formats not supported for pdf extraction")
            
            sample_pdf = genai.upload_file(path)

            response = mod_model_Gemini.generate_content([prompt, sample_pdf])
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
        
    if module == "generate_content_from_audio":
        try:
            path = GetParams("file")
            prompt = GetParams("prompt")
            result = GetParams("result")
            if not path.endswith((".wav", ".mp3", ".aiff",".aac", ".ogg", ".flac")):
                raise Exception("File format not supported by Gemini AI using this module")
            
            file = genai.upload_file(path)

            response = mod_model_Gemini.generate_content([file, prompt])
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
            # if not path.endswith("mp4"):
            #     raise Exception("File format not supported by Gemini AI using this module")
            
            file = genai.upload_file(path, mime_type='video/mp4')

            while file.state.name == "PROCESSING":
                sleep(5)
                file = genai.get_file(file.name)
            print(file)
            response = mod_model_Gemini.generate_content([file, prompt])
            SetVar(result, response.text)

        except Exception as e:
            SetVar(result, False)
            raise e
    
        
except Exception as e:
    PrintException()
    raise e
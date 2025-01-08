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
import os, sys

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
        
    
        
except Exception as e:
    PrintException()
    raise e
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Dict
from fastapi.responses import JSONResponse
import uvicorn
import os
from dotenv import load_dotenv
import json
import time

from module_link.get_text_link import get_cv_text_linkedin

from utils.process_json import procesar_json_vacante
from create_vacancy.create_vacancy import create_vacancy
from calculate_score.calculate_score import calculate_score

load_dotenv()

app = FastAPI()


class RequestData(BaseModel):
    url_perfil: str

class RequestDataScore(BaseModel):
    url_perfil: str
    json_data: dict

API_KEY_AUTH = os.getenv('API_KEY_AUTH')

if API_KEY_AUTH is None:
    raise Exception("API_KEY_AUTH not configured in .env file")

def get_api_key(api_key_auth: str = Header(...)):
    if api_key_auth != API_KEY_AUTH:
        raise HTTPException(status_code=403, detail="Unauthorized")
    return api_key_auth

@app.post("/texto/linkedin")
async def analizar(request_data: RequestData, api_key_auth: str = Depends(get_api_key)):
    try:
        url_perfil = request_data.url_perfil
    
        resultado = get_cv_text_linkedin(url_perfil)
        #print(json.dumps({"text_linkedin": resultado}))
        print(JSONResponse(content={"text_linkedin": resultado}, status_code=200))
        return JSONResponse(content={"text_linkedin": resultado}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/linkedin/score")
async def analizar(request_data: RequestDataScore, api_key_auth: str = Depends(get_api_key)):
    try:
        request_data = request_data.dict()

        if 'json_data' in request_data and request_data['json_data']: # este es el camino de la solicitud existe
        
            json_vacante = request_data['json_data']
            vacante = procesar_json_vacante(json_vacante)
        
        else: # el camino de cuando no hay solicitud
        
            nivel = request_data["seniority"]
            rol = request_data["position"]        
            vacante = create_vacancy(nivel, rol)
                        
        url_perfil = request_data['url_perfil']
        
        cv_text = get_cv_text_linkedin(url_perfil)
        
        respuesta = calculate_score(cv_text, vacante)
        
        return JSONResponse(content=respuesta, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@app.post("/probar")
async def analizar(request_data: RequestData, api_key_auth: str = Depends(get_api_key)):
    try:
        request_data = request_data.dict()
        url_perfil = request_data['url_perfil']

        resultado = url_perfil.split('/')
        time.sleep(10)
        print(json.dumps({"text_linkedin": resultado}))
        return JSONResponse(content={"text_linkedin": resultado}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=3600)
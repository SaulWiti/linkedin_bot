from utils.process_json import procesar_json_vacante

from create_vacancy.create_vacancy import create_vacancy
from cv_to_text.cv_to_text import cv_to_text
from calculate_score.calculate_score import calculate_score

def link_score(request)->dict:
    
    try:
        data = request.get_json()
        
        if 'json_data' in data and data['json_data']: # este es el camino de la solicitud existe
        
            json_vacante = data['json_data']
            vacante = procesar_json_vacante(json_vacante)
        
        else: # el camino de cuando no hay solicitud
        
            nivel = data["seniority"]
            rol = data["position"]        
            vacante = create_vacancy(nivel, rol)
                        
        pdf_url = data['pdf_url']
        
        cv_text = cv_to_text(pdf_url)
        
        respuesta = calculate_score(cv_text, vacante)
        
        return respuesta, 200
                
    except Exception as e:
        return {'start': 0, 'score': 0, 'justificacion': f'Error {e}'}, 500
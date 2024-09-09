from .calculate_score_utils import seniority, stack, estudios, lagunas_laborales, estabilidad_laboral, evaluacion_final, proces_data
from concurrent.futures import ThreadPoolExecutor

def calculate_score(cv_text:str, vacante:str)->dict:

    try:
        with ThreadPoolExecutor(max_workers=3) as executor:
            # Programar las funciones para que se ejecuten en paralelo
            resp_seniority = executor.submit(seniority, cv_text, vacante)
            resp_stack = executor.submit(stack, cv_text, vacante)
            resp_estudios = executor.submit(estudios, cv_text, vacante)

            # Esperar a que las funciones terminen y obtener sus resultados
            resp_seniority = resp_seniority.result()
            resp_stack = resp_stack.result()
            resp_estudios = resp_estudios.result()

        with ThreadPoolExecutor(max_workers=2) as executor:
            # Programar las funciones para que se ejecuten en paralelo
            resp_lagunas = executor.submit(lagunas_laborales, cv_text)
            resp_estabilidad = executor.submit(estabilidad_laboral, cv_text)

            # Esperar a que las funciones terminen y obtener sus resultados
            resp_lagunas = resp_lagunas.result()
            resp_estabilidad = resp_estabilidad.result()

        resp_final = evaluacion_final(resp_seniority, resp_stack, resp_estudios, resp_lagunas, resp_estabilidad)

        json_respuesta = proces_data(resp_final, resp_seniority, resp_stack, resp_estudios, resp_lagunas, resp_estabilidad)

        return json_respuesta

    except Exception as e:
        return {'start': 0, 'score': 0.0, 'justificacion': f"Error: {e}"}
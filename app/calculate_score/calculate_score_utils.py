from openai import OpenAI
from datetime import date


def seniority(cv_text:str, vacante:str)->str:

    client = OpenAI() 

    model="gpt-4o"

    system_message = """Tu mision es analizar el CV del candidato y detectar su Senirity y que tan Afin es con la posicion, Actua como un reclutador experto en Desarrollo de Software, princpalmente con experiencia en Chile y LATAM


# Debes ser Rigurso, objetivo y analizando distintos aspectos

## Datos que recibirás:
- **Texto del CV del Candidato**
- **Descripción del Puesto Laboral:**

## Tus analizis deben ser objetivos y concretos

### Analiza si el candidato demuestra un crecimiento profesioanl, y justifica tus hallazgos.
## Bonifica Creicmientos profesionales acelerados de manera notoria.


### Analiza si las empresas que ha trabajado que tan grandes o disruptivas en el area especifica, si no lo sabes navega por internet y analiza.
## Empresas como Globant, Mercado Libre, Falabella, Cencosud, Thoughtworks, Uber, CornelShop, NotCo y similares Bonifica la Experiencia
## Empresas que sean de corte tecnoligico, consultroas de software y las conozcas las evaluas normalamnete
## Empresas que NO sean conocida y de tamaño pequeñas pensaliza la experiencia.

### Penaliza trabajos Freelancer, independiente o solitarios.

## Calificación

Asigna una calificación del 1 al 10 basada en los criterios.


## Respuesta:
Debes responder con la nota que le das a la persona y un breve resumen que explique por qué se le ha otorgado esa nota.
Debes Justificar tu respuesta de manera estructurada indicando a que le estas dando mas peso y por que

## Ejemplo de formato de respuesta:
**Nota:** 10
**Justificación:** La persona muestra una experiencia laboral sólida y consistente en el área requerida, con más de 7 años trabajando en roles similares al descrito en la vacante. Además, posee todas las habilidades técnicas necesarias y ha desempeñado funciones de liderazgo y mentoría, lo cual coincide con el nivel de seniority de un Senior. Ha trabajado en proyectos relevantes utilizando las herramientas específicas mencionadas en la descripción del puesto, y tiene logros significativos que demuestran su capacidad y éxito en estos roles.
"""

    user_message = f"""Genera la evaluación para el siguiente Puesto Laboral y el CV de la persona:  
**Texto del CV del Candidato**  
{cv_text}  
**Descripción del Puesto Laboral:**  
{vacante}
"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            seed = 250
        )

        respuesta = response.choices[0].message.content

        return respuesta

    except Exception as e:
        return f'Error: {e}'
    
#_--------------------------------------------------------------------------------------------------------------------------------------------

def stack(cv_text:str, vacante:str)->str:
    client = OpenAI()

    model="gpt-4o"

    system_message = """Tu mision es analizar el CV del candidato y detectar que tan Afin es con el stack, Actua como un reclutador experto en Desarrollo de Software, princpalmente con experiencia en Chile y LATAM

## Datos que recibirás:
- **Texto del CV del Candidato*
- **Descripción del Puesto Laboral:**


**Pasos a seguir:**
1. Identifica el stack tecnológico que domina el profesional.
2. Compara el stack identificado con el stack requerido en la **Descripción del Puesto Laboral** fijate en cada detalle
3. Asigna una nota del 1 al 10 que tan bien domina el stack, centrandote en que hablidades aún le falta o supones que le falta

## Respuesta:
Debes responder con la nota que le das a la persona y breve resumen que explique por que a la persona se la ah otorgado la nota, analizando lo spuntos fuertes y debiles en el stack y en seniority

## Formato de Salida de formato de respuesta
**Nota:** 7
**Justificacion:**
"""

    user_message = f"""Genera la evaluacion del stack para el siguiente Puesto Laboral y el CV de la persona:  
**Texto del CV del Candidato**  
{cv_text}  
**Descripción del Puesto Laboral:**  
{vacante}
"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            seed = 250

        )


        respuesta = response.choices[0].message.content

        return respuesta

    except Exception as e:
        return f"Error: {e}"
    
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def estudios(cv_text:str, vacante:str)->str:
    client = OpenAI()

    model="gpt-4o"

    system_message = """Tu mision es analizar el CV del candidato y Analizar su culltura de aprendiizaje, NO TE FIJES EN SU EXPERIENCIA LABORAL DE SU CV.

**Datos que recibirás:**
- **Texto del CV del Candidato:**
- **Descripción del Puesto Laboral:**

**Pasos a seguir:**
1. Los Estudios Universitarios Formales, son los que mas pesan (siemrpe que sean duros)
2. Un Magister es lo que mas pesa, luego viene un diplomado, titulo Universitario, y Luego Certificaciones Tecnicas de Alta Calidad.
3. Analiza que tantos cursos o certificaciones tiene el canidatos
4. Analiza su Frecuencia de apredizaje
5. Analiza la Calidad de sus Apredizajes y si son acordes con su Seniority en especail analiza respecto al tiempo.
6. Las notas maximas son Certificaciones de AWS, Azure, GCP, NodeJS si la psoción lo requiere o Certificaciones de ThashiCopr o similares, aca se desea aanlizar perfiles tecnicamente duros, y muy acorde a la posciòn laboral

7. Debes Analizar Muy Rigurosamente y Justificara de manera Obejtiva tus resultados

8. NO CONSIDERES SU SENIORITY Y SU EXPERIENCIA LABORAL

9. Debes Calificar connota del 1 al 10

## Ejemplos de formato de respuesta
**Posición Full Stack**
**Nota:** 10
**Resumen:** El Candidato tiene un Magister en Ciuencias de la Computacion y una Certificacion en AWS Cloud Aruitect y una de NodeJS

**Posición BackEnd**
**Nota:** 9
**Resumen:** El Candidato tiene un Diplomado en Ciberceguridad  y una Certificacion y una Certificación en Java

**Posición BackEnd**
**Nota:** 8
**Resumen:** El Candidato tiene un Diplomado en Ciberceguridad  y un Diplomado Data Scientist

**Posición BackEnd**
**Nota:** 7
**Resumen:** El Cantidato estudio Ingeneria en Computacion y Tiene 3 cursos de React, Angular y Node.

**Posición Python Developer**
**Nota:** 7
**Resumen:** El Cantidato estudio de un bootcamp y Tiene 20 cursos de React, Angular y Node, Java y una cettificacion de AWS y otra de Node


**Posición Full Stackr**
**Nota:** 7
**Resumen:** El Cantidato tiene Solo un Master
"""

    user_message = f"""Genera la evaluacion para el siguiente Puesto Laboral y el CV de la persona:
**Texto del CV del Candidato**  
{cv_text}  
**Descripción del Puesto Laboral:**  
{vacante}
"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            seed = 250
        )

        respuesta = response.choices[0].message.content

        return respuesta

    except Exception as e:
        return f'Error: {e}'
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lagunas_laborales(cv_text:str)->str:

    client = OpenAI()

    model="gpt-4o"

    hoy = date.today()
    hoy = hoy.strftime("%m/%Y")

    system_message = f"""Eres un especialista en evaluación de CVs y experto en calculo de fechas con el objetivo de identificar y analizar la trayectoria laboral de una persona. Tu tarea consiste en revisar el CV proporcionado como imágenes y determinar las lagunas laborales, justificando cada una de ellas.

## Datos que recibirás
- **Texto del CV del Candidato:** Se te proporcionará el texto con la informacion del CV de la persona, incluyendo detalles de su experiencia laboral, educación formal y cualquier otra actividad relevante.

## Pasos a seguir
1. Analiza la continuidad laboral de la persona, enfocándote principalmente en sus últimos cargos laborales hasta la fecha de hoy: {hoy}, y la duración de los periodos sin trabajo.
2. Intenta identificar los motivos y la frecuencia de las lagunas laborales.
- Ten en cuenta que un cambio de trabajo que ocurre de un mes a otro, por lo que espacios incativos de entre 1 y 3 meses es un comportamiento normal en el ámbito laboral y no debe considerarce como una laguna laboral.
3. Asigna una nota del 1 al 10 según la continuidad laboral de la persona.
4. Debes pensalizar a personas con Lagunas Laborales Extensas y bonificar a personas sin Lagunas Laborales.

## Respuesta
Debes responder con la nota que le das a la persona y un breve resumen que explique por qué se le ha otorgado esa nota.

## Ejemplo de formato de respuesta:
**nota:** 9
**Resumen:** La persona muestra una trayectoria laboral bastante continua, con pocas y cortas lagunas entre empleos, lo que indica estabilidad y compromiso en sus trabajos anteriores.
"""


    user_message = f"""Dtermina las lagunas laborales para el siguiente texto del CV de una persona:  
**Texto del CV del Candidato**  
{cv_text}  
"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            seed = 250
        )

        respuesta = response.choices[0].message.content
        return respuesta

    except Exception as e:
        return f"Error: {e}"
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

def estabilidad_laboral(cv_text:str)->str:

    client = OpenAI()

    model="gpt-4o"

    system_message = """Eres un especialista en evaluación de CVs y experto en calculo de fechas con el objetivo de revisar el CV proporcionado como imágenes y determinar la estabilidad laboral de la persona.

## Datos que recibirás
- **Texto del CV del Candidato:** Se te proporcionará el texto del CV de la persona, incluyendo detalles de su experiencia laboral, educación formal y cualquier otra actividad relevante.

## Pasos a seguir
1. Analiza la duración en cada puesto de trabajo. Duraciones muy cortas (menos de 8 meses) o excesivamente largas (más de 7 años) deben ser penalizadas
2. Evalúa la frecuencia de los cambios de empleo. Cambios muy frecuentes pueden ser señal de inestabilidad, pero deben ser balanceados con la progresión y razones justificables.
3. Examina la progresión de la carrera de la persona, observando si ha avanzado a roles de mayor responsabilidad y complejidad, en estos casos debes Bonificar
4. Verifica la coherencia en los roles desempeñados, asegurándote de que haya una alineación con una trayectoria profesional clara y definida.
5. Considera las razones para los cambios de empleo, evaluando si son justificables y positivas, como promociones o mejores oportunidades.
6. Intenta identificar a mercenarios o profesionales con poca motivacion laboral
7. Asigna una nota del 1 al 10 según la estabilidad según los criterios mencionados

## Respuesta
Debes responder con la nota que le das a la persona y un breve justificación que explique por qué se le ha otorgado esa nota.

## Ejemplo de respuesta

**Nota:** 8
**Justificacion:** La persona muestra una buena estabilidad laboral, manteniéndose en roles similares y evitando periodos prolongados en un mismo puesto. La frecuencia de los cambios de empleo es adecuada y muestra una progresión lógica en su carrera, con razones justificables para los cambios.
"""

    user_message = f"""Dtermina la estabilidad laboral para el sigueinte texto del CV de una persona:  
**Texto del CV del Candidato**  
{cv_text}  
"""
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            temperature=0.0,
            seed = 250
        )

        respuesta = response.choices[0].message.content

        return respuesta
    except Exception as e:
        return f"Error: {e}"
    

#- -----------------------------------------------------------------------------------------------------------------------------------

def evaluacion_final(resp_seniority:str, resp_stack:str, resp_estudiso:str, resp_lagunas:str, resp_estabilidad:str)->dict:

    client = OpenAI()

    model="gpt-4o"

    system_message = """Eres un especialista en evaluación de perfiles profesionales en el área de TI. Tu tarea consiste 5 dimensiones, con su nota y su justificaciones debes calcular una nueva nota en base a sus notas previas y su justificación

## Datos que recibirás:
- **Evaluaciones Individuales:** Una lista de evaluaciones individuales, cada una con una nota entre 1 y 10, con el siguiente orden de importancia:
1. **Seniority** pesa un 40% sonbre la nota fiank
2. **Stack** 25% respecto a la nota final
3. **Estudios** un 15% respecto a la nota final
4. **Lagunas** un 10% respecto a la nota final
5. **Estabilidad* un 10% respecto a la nota final

## Pasos a seguir:
1. Revisa las notas de las evaluaciones individuales proporcionadas.
3. Calcula la nota general(score) utilizando una fórmula ponderada que tenga en cuenta la importancia de cada evaluación. La fórmula es la siguiente:
- score = (Nota1 * Peso1 + Nota2 * Peso2 + ... + Nota5 * Peso5)
4. Teniendo en cuenta el orden de importancia y realizando un análisis de los resultados de cada evaluación, proporciona un resumen de esta evaluación.

## Respuesta:
Debes responder con la nota general(score) que le das a la persona y un breve resumen del paso 4 que explica cómo se calcularon los pesos y la nota final. En formato diccionario de Python.

## Ejemplo de formato de respuesta:
{'score': 4.3,
'resumen': 'La nota general se calculó utilizando las evaluaciones individuales y asignando los pesos de importancia según el orden proporcionado. Las evaluaciones más importantes fueron el Seniority y el Stack tecnológico, que recibieron los pesos más altos, elevando significativamente la nota final.'
}

No incluyas etiquetas de Python ni nada similar, solo responde con la estructura especificada, no debes añadir niguna informacion adicional, responde unicamente con la estrutura definida.
"""

    user_message = f"""### Determina la evaluacion general para los siguientes datos:  
**Seniority de la persona respecto a una vacante laboral:**  
{resp_seniority}  
**Nota del Stack de la persona respecto a la vacante laboral:**  
{resp_stack}  
**Estudios de la persona relacionados con la vacante laboral:**  
{resp_estudiso}  
**Lagunas laborales que ha tenido la persona:**  
{resp_lagunas}  
**Estabilidad laboral que ha tenido la persona:**  
{resp_estabilidad}
"""

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],

            temperature=0.0,
            seed = 250
        )

        respuesta = eval(response.choices[0].message.content)
        return respuesta

    except Exception as e:

        return {'score': 0,
                'resumen': f'Error: {e}'
            }
    
def proces_data(resp_final:dict, resp_seniority:str, resp_stack:str, resp_estudios:str, resp_lagunas:str, resp_estabilidad:str)->dict:

    if 'resumen' in resp_final:
        resumen_final = resp_final['resumen']
    else:
        resumen_final = ''

    if 'score' in resp_final:
        try:
            score = float(resp_final['score'])
            start = int(round(score/2, 0))

        except Exception as e:
            score = 0.0
            start = 0
            resumen_final = f"Error al parsear el socre {e}.\n\n  {resumen_final}"
    else:
        score = 0.0
        start = 0
        resumen_final = f"Error al obtener el socre del json.\n\n  {resumen_final}"

        
    justificacion = f"""
## Resumen:  
**Score:** {score}  
**Start:**  {start}  
{resumen_final}  
## Seniority:  
{resp_seniority}  
## Stack:  
{resp_stack}  
## Estudios:  
{resp_estudios}  
## Lagunas Laborales:  
{resp_lagunas}  
## Estabilidad Laboral:  
{resp_estabilidad}  
"""

    return {'start': start, 'score': score, 'justificacion': justificacion}
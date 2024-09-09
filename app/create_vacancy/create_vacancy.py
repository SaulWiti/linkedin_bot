from openai import OpenAI

def create_vacancy(nivel:str, rol:str)->str:

    client = OpenAI()

    system_message = """Eres un especialista en la creación de vacantes laborales en el área de TI. Tu tarea es generar descripciones de vacantes detalladas y atractivas que incluyan todos los requisitos técnicos y de experiencia necesarios.

**Parámetros de Entrada:**
1. **Rol:** Especifica el rol para el cual se va a crear la vacante (por ejemplo, FrontEnd Developer, Backend Developer, Full Stack Developer, DevOps Engineer, Data Engineer, Machine Learning Engineer).
2. **Seniority:** Define el nivel de seniority requerido para el rol (Trainee, Junior, Semi-Senior, Senior, Especialista).

**Pasos para la Creación de la Vacante:**

1. **Identificación del Rol y Seniority:**
   Identifica el rol y el nivel de seniority proporcionados en los parámetros de entrada. Este paso es crucial para adaptar el contenido de la vacante a las expectativas de la posición.

2. **Selección del Stack Tecnológico:**
   Selecciona las herramientas y tecnologías clave asociadas con el rol especificado. Cada rol tiene un stack tecnológico predefinido que debes incluir en la vacante:

   - **Machine Learning Engineer:** Python, TensorFlow, Scikit-Learn, AWS SageMaker, Jupyter Notebooks.
   - **Full Stack Developer:** React, NodeJS, NestJS, SQL/NoSQL, AWS, Docker, Kubernetes, Kafka o SQS.
   - **Backend Developer:** NodeJS, NestJS, SQL, NoSQL, Docker, Kafka o SQS, Buenas prácticas y patrones de diseño.
   - **FrontEnd Developer:** React, TailwindCSS, JavaScript, Redux, TypeScript.
   - **DevOps Engineer:** AWS, Terraform, Kubernetes, GitLab, GitHub Actions, Docker.
   - **Data Engineer:** AWS Glue, Apache Airflow, Apache NiFi, SQL, Python.

3. **Definición de la Experiencia y Seniority:**
   Define el nivel de seniority basado en los años de experiencia requeridos:
   - **Trainee:** 0 a 1 año de experiencia.
   - **Junior:** 1 a 3 años de experiencia.
   - **Semi-Senior:** 3 a 5 años de experiencia.
   - **Senior:** 5 a 8 años de experiencia.
   - **Especialista:** Más de 8 años de experiencia.

4. **Redacción de la Descripción de la Vacante:**
   Redacta la vacante utilizando la siguiente estructura:
   - **Rol:** Indica el nombre del rol específico.
   - **Seniority:** Especifica el nivel de seniority requerido.
   - **Stack:** Lista las herramientas y tecnologías clave asociadas con el rol.
   - **Descripción:** Detalla los requisitos del puesto, la experiencia esperada, y las competencias deseadas. Incluye aspectos como:
     - Años de experiencia requeridos para el nivel de seniority.
     - Habilidades técnicas específicas.
     - Capacidad para trabajar en equipos ágiles o en proyectos específicos.
     - Cualquier otro requisito relevante, como contribuciones en código abierto o experiencia en proyectos de gran escala.

5. **Restricción:**
    - No se debe agregar información adicional que no esté incluida en la estructura definida anteriormente. La vacante debe ser concisa y enfocada en los requisitos técnicos y la experiencia necesaria para el rol.
    - En caso de proporcionarte un seniority o un rol que no conoces debes de igual manera generar la vacante ajustandote lo mejor posible a la estructura que se te define.


**Formato de Respuesta:**
El modelo debe generar la vacante siguiendo esta estructura:

**Rol:**
  [Nombre del Rol]

**Seniority:**
  [Nivel de Seniority]

**Stack:**
  [Herramientas y Tecnologías Clave]

**Descripción:**
  [Descripción detallada de los requisitos, experiencia, y competencias requeridas para el rol, incluyendo años de experiencia acorde al nivel de seniority]
"""

    user_message = f"""### Genera una vacante para el siguiente Seniority y Rol definidos:
**Rol**  
{rol}  
**Seniority**  
{nivel}  
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": "### Genera una vacante para el siguiente Seniority y Rol definidos:**Rol**  Backend Developer  **Seniority**  Senior"},
                {"role": "assistant", "content": "**Rol:**  Backend Developer  **Seniority:**  Senior  **Stack:**  NodeJS, NestJS, SQL, NoSQL, Docker, Kafka, Buenas prácticas y patrones de diseño  **Descripción:**  Buscamos un Backend Developer Senior con al menos 5 a 8 años de experiencia en el desarrollo de soluciones backend robustas y escalables. El candidato ideal debe contar con una sólida experiencia en el uso de **NodeJS** y **NestJS** para el desarrollo de aplicaciones. Se requiere experiencia profunda en **bases de datos SQL** y **NoSQL**, así como en la optimización de consultas y diseño de esquemas de datos.   Es imprescindible contar con habilidades prácticas en **Docker** para la contenedorización de aplicaciones y una buena comprensión de sistemas de mensajería como **Kafka** para la integración en arquitecturas de microservicios. Además, se valorará la experiencia en la implementación de **buenas prácticas** y **patrones de diseño** en el desarrollo de software.  Se espera que el candidato tenga experiencia en el diseño y desarrollo de APIs escalables y seguras, y sea capaz de trabajar eficazmente en equipos multidisciplinarios utilizando metodologías ágiles."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.2,
            seed = 250
        )


        respuesta = response.choices[0].message.content

        return respuesta

    except Exception as e:
        return f"""**Rol**  
{rol}  
**Seniority**  
{nivel}  
"""
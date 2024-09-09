from selenium import webdriver

from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

import time

import random

import re

from openai import OpenAI

from bs4 import BeautifulSoup, NavigableString, Tag

from urllib.parse import unquote

from fake_useragent import UserAgent

from dotenv import load_dotenv
from os import getenv


def is_perfil(texto_html):

  client = OpenAI()

  system_message = f"""**Tarea: Identificación de Tipo de Página de LinkedIn**

  **Objetivo:**
  Determinar si el texto extraído de un HTML de LinkedIn corresponde al perfil de una persona o a una página de login, registro u otra que no sea un perfil personal.

  **Materiales Proveídos:**
  - **Texto HTML Extraído:** Contenido textual del HTML de LinkedIn que puede incluir perfiles personales, páginas de login, registro u otras páginas.

  **Instrucciones Detalladas:**

  1. **Análisis del Texto HTML:**
    - Examina el texto HTML proporcionado para identificar elementos típicos de un perfil personal de LinkedIn (e.g., nombre, experiencia laboral, educación, habilidades, recomendaciones).

  2. **Identificación del Tipo de Página:**
    - Si el texto contiene información característica de un perfil personal (nombre, título profesional, resumen, experiencia laboral, etc.), clasifícalo como un perfil de persona.
    - Si el texto contiene elementos típicos de páginas de login, registro u otros (formularios de autenticación, botones de registro, términos de servicio, etc.), clasifícalo como no perfil de persona.

  3. **Formato de Respuesta:**
    - La respuesta debe ser un valor booleano: **True** si el texto corresponde a un perfil personal y **False** si corresponde a una página de login, registro u otra que no sea un perfil personal.

  **Ejemplo de Estructura de Salida:**
  True

  No incluyas etiquetas de Python ni nada similar, solo responde con la estructura especificada.
  """

  user_message = f"""Genera la respuesta para el siguiente texto extraido del html:  
  {texto_html}
  """
  try:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content":  user_message}
        ],
        temperature=0.0,
        top_p = 1,
        seed = 250
    )

    respuesta = response.choices[0].message.content
    respuesta = eval(respuesta)

  except:
      respuesta = False
    
  return respuesta

def extraer_texto_etiquetas(html_string):

    etiquetas_texto = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a']

    soup = BeautifulSoup(html_string, 'lxml')

    def obtener_texto(etiqueta):
        texto = ''
        for elemento in etiqueta.descendants:
            if isinstance(elemento, NavigableString):
                texto += str(elemento)
            elif isinstance(elemento, Tag) and elemento.name in etiquetas_texto:
                texto += obtener_texto(elemento)
        return texto

    texto = ''
    for etiqueta in soup.find_all(etiquetas_texto):
        texto += obtener_texto(etiqueta) + ' '

    texto = texto.strip()

    texto = re.sub(r'\s+', ' ', texto)
    
    return texto

def procesar_url(url_perfil):
    
    url_perfil = unquote(url_perfil)
    
    url_perfil = url_perfil[:-1] if url_perfil[-1] == '/' else url_perfil

    return url_perfil


def get_html_text(url_perfil):
    print('Empieza')
    url_perfil = procesar_url(url_perfil)
    print(url_perfil)

    #profile_path = '/app/module_link/spf0s97m.default-release' # para docker
    profile_path = '/module_link/spf0s97m.default-release' # localmente
    profile_path = "C:/Users/Zaid96/AppData/Local/Mozilla/Firefox/Profiles/spf0s97m.default-release"
    profile_path = "spf0s97m.default-release"
    options = Options()

    options.add_argument("--headless")
    options.add_argument(f'-profile {profile_path}')
    #options.add_argument("--marionette-port 2828")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    #options.add_argument("--disable-features=NetworkService")
    #options.add_argument("--incognito")
    #options.add_argument("--disable-extensions")
    #options.add_argument("--disable-popup-blocking")
    #options.add_argument("--disable-infobars")
    #options.add_argument("--disable-notifications")
    ua = UserAgent()
    options.add_argument(f"user-agent={ua.random}")
    print('Opciones cargadas')
    
    con = 2
    
    while con:

        con -= 1
        print('While', con)
        try:
            
            driver = webdriver.Firefox(options=options)
            print('driver cargado')

            # Navegar a Google
            driver.get('https://www.google.com')

            time.sleep(random.uniform(3,7))

        
            # Encontrar y hacer clic en el botón "Aceptar todo"
            try:
   
                crokie_google = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'L2AGLb')))
                
                if crokie_google: crokie_google.click()

            except Exception as e:
                print(f"No se encontró el botón de aceptar cookies")

            #time.sleep(random.randint(time_min_esp,time_max_esp))

            # Realizar una búsqueda en Google
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, 'q'))
            )

            # Desplazamiento
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Movimiento del ratón
            ActionChains(driver).move_to_element(search_box).perform()
            
            time.sleep(random.uniform(1,2))

            # realizar busqueda
            search_box.send_keys(url_perfil)
            search_box.send_keys(Keys.ENTER)

            print('busqueda realizada')

            time.sleep(random.uniform(8,12))

            # Hacer clic en el primer resultado de búsqueda
            first_result = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.g a'))
            )

            # Desplazamiento
            
            # Movimiento del ratón
            ActionChains(driver).move_to_element(first_result).perform()

            time.sleep(random.uniform(0,1))

            first_result.click()

            print('click en el primer elemento')
            
            time.sleep(random.uniform(15,20))

            html_general_content = driver.page_source

            print('html obtenido')

            texto_html = extraer_texto_etiquetas(html_general_content)

            print(texto_html)
            print('texto obtenido')

            if is_perfil(texto_html):
                driver.quit()    
                return texto_html
            
            print('No es perfil')
            driver.quit()
        except Exception as e:
            print(f'Exception scraping: {e}')

            try:
              driver.quit()
            except:
              continue

    return None


def model_get_cv(text_link):
  
  client = OpenAI()

  system_message = """Dado un texto extraído de un perfil de LinkedIn, organiza y presenta la información en el formato de un currículum vítae (CV) estructurado. Asegúrate de incluir las siguientes secciones si la información está disponible: Información de contacto, Perfil, Experiencia, Educación, Licencias y Certificaciones, Conocimientos y Aptitudes, Recomendaciones, Publicaciones, Cursos, Reconocimientos y Premios, Idiomas.
"""

  user_message = f"""Realiza el análisis el siguiente texto:  
1. **Texto Linkedin**  
- {text_link}   
"""
  try:
    response = client.chat.completions.create(
          model="gpt-4o",
          messages=[
              {"role": "system", "content": system_message},
              {"role": "user", "content": user_message}
          ],
          temperature=0.0,
          max_tokens=4096,
          seed = 250
        )

    respuesta = response.choices[0].message.content

    return respuesta
  except:
    return None
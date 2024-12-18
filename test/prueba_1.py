import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:8000/texto/linkedin"

def link_to_text(url_perfil):
    
    #url = getenv("URL_LINKEDIN")
    print(url)
    # Define los datos en formato JSON que quieres enviar
    data = {
        "url_perfil": url_perfil
    }

    headers = {
        "Content-Type": "application/json",
        "api-key-auth": getenv("API_KEY_AUTH")
    }
    
    print("Envia", getenv("API_KEY_AUTH"))

    try:
        response = requests.post(url=url, json=data, timeout=3600, headers=headers)
        
        respuesta = response.json()
        
        print(respuesta)

        return respuesta['text_linkedin']
    
    except Exception as e:
        return f"Error: {e}"
        
print(link_to_text("https://www.linkedin.com/in/sa%C3%BAl-d%C3%ADaz-matos-7190971bb"))
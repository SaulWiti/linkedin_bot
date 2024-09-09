from bs4 import BeautifulSoup

def procesar_json_vacante(json_vacante:dict)->str:

    if 'rol' in json_vacante:
        rol = ', '.join(json_vacante['rol'])
    else:
        rol = ''

    if 'stack' in json_vacante:
        stack = ', '.join(json_vacante['stack'])
    else:
        stack = ''

    if 'nivel' in json_vacante:
        nivel = json_vacante['nivel']
    else:
        nivel = ''

    if "descripcion" in json_vacante:
        try:
            soup = BeautifulSoup(json_vacante["descripcion"], "html.parser")
            description = soup.get_text(separator="\n")
        except Exception as e:
            description = json_vacante["descripcion"]
    else:
        description = ""

    vacante = f"""
**Rol:**
{rol}

**Seniority**
{nivel}

**Stack:**
{stack}

**Descripcion :**
{description}
"""

    return vacante
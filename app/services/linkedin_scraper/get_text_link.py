from .get_text_link_utils import get_html_text, model_get_cv


async def get_cv_text_linkedin(url_perfil):
    
    try:
        texto_html = await get_html_text(url_perfil)
        
        if texto_html:
            cv_text = await model_get_cv(texto_html)
        
            return cv_text
        return None
    except:
        return None 
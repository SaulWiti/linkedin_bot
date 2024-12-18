from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
import uvicorn

from services.linkedin_scraper.get_text_link import get_cv_text_linkedin
from core.auth import get_api_key
from schemas.shema import RequestData

app = FastAPI()

@app.post("/texto/linkedin")
async def analizar(request_data: RequestData, api_key_auth: str = Depends(get_api_key)):
    try:
        url_perfil = request_data.url_perfil    

        resultado = await get_cv_text_linkedin(url_perfil)

        return JSONResponse(content={"text_linkedin": resultado}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, timeout_keep_alive=3600)
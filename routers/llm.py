from fastapi import APIRouter, HTTPException
from schemas import TextoUsuario
import httpx


router = APIRouter(
    prefix="/llm",
    tags=["llm"]
)


@router.get("/")
def home():
    return {"message": "Hola LLM"}


@router.post("/analizar-emocion")
async def analizar_emocion(datos: TextoUsuario):

    prompt = f"""
    Analiza las emociones presentes en este texto:

    {datos.texto}

    Devuelve:
    - Emociones identificadas.
    - Intensidad del 1 al 10.
    - Explicación breve.
    """

    try:
        async with httpx.AsyncClient(timeout=120) as client:

            respuesta = await client.post(
                "https://oai.endpoints.kepler.ai.cloud.ovh.net/v1/chat/completions",
                json={
                    "model": "Qwen3.5-397B-A17B",
                    "messages": [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "stream": False
                }
            )

            respuesta.raise_for_status()

            resultado = respuesta.json()

            return {
                "analisis": resultado["choices"][0]["message"]["content"]
            }

    except httpx.HTTPError as error:
        raise HTTPException(
            status_code=502,
            detail=f"Error al conectar con el LLM: {error}"
        )

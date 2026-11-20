from fastapi import APIRouter

router = APIRouter(
    prefix="/llm",
    tags=["llm"]
)


@router.get("/")
def home():
    return {"message": "Hola LLM"}

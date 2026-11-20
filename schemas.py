from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int | None = None # Este id forma parte del ejercicio de CRUD
    name: str = Field(min_length=3) # Longitud mínima de 3 caracteres
    description: str | None = None
    price: float = Field(gt=0) # Greater Than 0
    stock: int = Field(ge=0) # Greater or Equal to 0
    
class TextoUsuario(BaseModel):
    texto: str


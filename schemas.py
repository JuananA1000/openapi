from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(min_length=3) # Longitud mínima de 3 caracteres
    description: str | None = None
    price: float = Field(gt=0) # Greater Than 0
    stock: int = Field(gt=0)

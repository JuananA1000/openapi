from fastapi import FastAPI
from schemas import Product

app = FastAPI()

''' 
    Introducción a FastAPI
'''

@app.get("/")
def home():
    # FastAPI retorna un Diccionario, pero automáticamente lo convierte a JSON mediante un parseo interno.
    return {"message": "Hola caracolo"}


''' 
    Rutas con Parámetros
'''

@app.get("/products")
def get_products(limit: int = 10):
    return {
        "products": [],
        "limit": limit
    }

@app.get("/products/{product_id}")
# El tipado en python es opcional
def get_product(product_id: int, include_desc: bool = False):
    return {"id": product_id, "include_desc": include_desc}


''' 
    Modelos y Validación
'''
# La respuesta es 201 porque se está creando un recurso nuevo, en este caso un producto.
@app.post("/products", status_code=201)
def create_product(product: Product): # Product viene del fichero schemas.py
    return product
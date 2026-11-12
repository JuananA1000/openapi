from fastapi import FastAPI

app = FastAPI()

''' 
    INTRODUCCION A FASTAPI
'''

@app.get("/")
def home():
    # FastAPI retorna un Diccionario, pero automáticamente lo convierte a JSON mediante un parseo interno.
    return {"message": "Hola caracolo"}


''' 
    RUTAS CON PARAMETROS
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

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

# @app.get("/products")
# def get_products(limit: int = 10):
#     return {
#         "products": [],
#         "limit": limit
#     }

# @app.get("/products/{product_id}")
# # El tipado en python es opcional
# def get_product(product_id: int, include_desc: bool = False):
#     return {"id": product_id, "include_desc": include_desc}


''' 
    Modelos y Validación
'''

# La respuesta es 201 porque se está creando un recurso nuevo, en este caso un producto.
# @app.post("/products", status_code=201)
# def create_product(product: Product): # Product viene del fichero schemas.py
#     return product


''' 
    CRUD (Create, Read, Update, Delete)
'''
products: dict[int, Product] = {} # Diccionario vacío para almacenar los producto
next_id = 1 # Variable para almacenar el siguiente id disponible

@app.post("/products", status_code=201)
def create_product(product: Product):
    global next_id
    product.id = next_id # Asignar el siguiente id disponible al producto
    products[next_id] = product # Almacenar el producto en el diccionario
    next_id += 1 # Incrementar el siguiente id disponible
    return product

@app.get("/products")
def get_products(limit: int = 10):
    return  list(products.values())[:limit]

@app.get("/products/{product_id}")
# El tipado en python es opcional
def get_product(product_id: int):
    return products.get(product_id)

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return products.pop(product_id, None) # Elimina el producto del diccionario y lo retorna, si no existe retorna None
from fastapi import FastAPI, HTTPException
from schemas import Product

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hola caracolo"}


products: dict[int, Product] = {}
next_id = 1


@app.post("/products", status_code=201)
def create_product(product: Product):
    global next_id
    product.id = next_id
    products[next_id] = product
    next_id += 1
    return product


@app.get("/products")
def get_products(limit: int = 10):
    return list(products.values())[:limit]


@app.get("/products/{product_id}")
def get_product(product_id: int):
    return products.get(product_id)


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    product = products.pop(product_id, None)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


def get_product(product_id: int, include_desc: bool = False):
    product = {"id": product_id, "include_desc": include_desc}

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

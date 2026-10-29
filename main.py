from fastapi import FastAPI
from models import Products

app = FastAPI()

@app.get("/")
def greet():
    return "Hi there"

products = [
    Products(id=1, name="Swish", price=99.9),
    Products(id=2, name="toing", price=80.9),
    Products(id=3, name="Zepto", price=45.50),
]

@app.get("/products")
def getproducts():
    return products

@app.get("/product/{id}")
def getProductsById(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"

@app.post("/product")
def addProduct(product:Products):
    products.append(product)
    return product

@app.put("/product")
def updateProduct(id: int, product:Products):
    for i in range (len(products)):
        if products[i].id == id:
            products[i] = product
            return "Updated successfully"

    
@app.delete("/product")
def deleteproduct(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return {"message": "Product deleted"}
    return "Product not found"

from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app= FastAPI()

@app.get("/")
def home():
    return "Welcome to FastAPI Series!"

@app.get('/products')
def get_products():
    return products

# path params
@app.get('/product/{product_id}')
def get_one_porduct(product_id:int):

    for oneproduct in products:
        if oneproduct.get("id")==product_id:
            return oneproduct
    return {
        "error":"Product not found for this ID."}

    
# query params
# for limited 2-3 but what if 300 then we werite no
@app.get("/greet")
def greet_user(name:str,age:int):
    return {
        "greet":f"Hello {name}, How are you? and you are {age} years old."
    }
  
@app.get("/greet")
def greet_user2(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet":f"Hello {query_params.get('name')}, How are you? and you are {query_params.get('age')} years old."
    }
    
# 5th notes start here
# different types of HTTP methods
## how to validate data==DTOS- Data Transfer Objects
@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"status":"Product Created Successfully.","data":products}

@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):
    
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index]=product_data.model_dump()
            return {
                    "status":"Product Updated Successfully",
                    "product":product_data
                }    
    return {
        "error":"Product not Found for this ID."
    }

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return{
                "status":"Product Deleted Successfully.",
                "product":deleted_product
            }
    return {"error": "Product not found for this ID"}

if __name__ == "__main__":
    home()
    get_products()
    get_one_porduct()

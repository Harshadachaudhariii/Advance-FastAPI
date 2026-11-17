from fastapi import FastAPI, Request
from mockData import products

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
      
if __name__ == "__main__":
    home()
    get_products()
    get_one_porduct()

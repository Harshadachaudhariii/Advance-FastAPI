from fastapi import FastAPI

app= FastAPI()
# Create your first FastAPI server and get endpoints
@app.get("/")
def home():
    return "Welcome to FastAPI Series!"

@app.get("/contact")
def contact():
    return "Contact with us any time."
def main():
    home()
    
if __name__ == "__main__":
    main()

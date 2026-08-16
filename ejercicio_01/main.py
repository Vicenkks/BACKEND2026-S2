from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"mensaje": "API funcionando"}


@app.get("/saludo")
def saludo():
    return {"mensaje": "Hola Backend"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int


@app.post("/productos")
def crear_producto(producto: Producto):
    return producto
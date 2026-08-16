from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Producto(BaseModel):
    nombre: str = Field(min_length=2)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


@app.post("/productos")
def crear_producto(producto: Producto):
    return producto
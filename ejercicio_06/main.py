from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Producto(BaseModel):
    nombre: str = Field(min_length=2)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


productos = {}
siguiente_id = 1


@app.post("/productos")
def crear_producto(producto: Producto):
    global siguiente_id

    nuevo = producto.model_dump()

    nuevo["id"] = siguiente_id

    productos[siguiente_id] = nuevo

    siguiente_id += 1

    return nuevo
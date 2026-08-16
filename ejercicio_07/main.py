from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# --------------------
# Modelo
# --------------------

class Producto(BaseModel):
    nombre: str = Field(min_length=2)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


# --------------------
# Almacenamiento
# --------------------

productos = {}
siguiente_id = 1


def generar_id():
    global siguiente_id

    nuevo_id = siguiente_id
    siguiente_id += 1

    return nuevo_id


# --------------------
# READ
# --------------------

@app.get("/productos")
def listar_productos():
    return list(productos.values())


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    if producto_id not in productos:
        return {"error": "Producto no encontrado"}

    return productos[producto_id]


# --------------------
# CREATE
# --------------------

@app.post("/productos")
def crear_producto(producto: Producto):

    nuevo_id = generar_id()

    nuevo = producto.model_dump()
    nuevo["id"] = nuevo_id

    productos[nuevo_id] = nuevo

    return nuevo


# --------------------
# UPDATE
# --------------------

@app.put("/productos/{producto_id}")
def actualizar_producto(
    producto_id: int,
    producto: Producto
):

    if producto_id not in productos:
        return {"error": "Producto no encontrado"}

    actualizado = producto.model_dump()
    actualizado["id"] = producto_id

    productos[producto_id] = actualizado

    return actualizado


# --------------------
# DELETE
# --------------------

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int):

    if producto_id not in productos:
        return {"error": "Producto no encontrado"}

    return productos.pop(producto_id)
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Libro(BaseModel):
    titulo: str = Field(min_length=2)
    autor: str
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


libros = {}
siguiente_id = 1




def generar_id():
    global siguiente_id

    nuevo_id = siguiente_id
    siguiente_id += 1

    return nuevo_id


@app.get("/libros")
def listar_libros():
    return list(libros)


@app.get("/libros/{libro_id}")
def obtener_libros(libro_id: int):
    if libro_id not in libros:
        return {"Libro no encontrado"}
    return libros[libro_id]
    
# GET /libros/{libro_id}



# POST /libros
@app.post("/libros")
def crear_libros(libro: Libro):
    nueva_id = generar_id()

    nuevo = libro.model_dump()
    nuevo["id"] = nueva_id

    libros[nueva_id] = nuevo
    return nuevo



# PUT /libros/{libro_id}
@app.put("/libros/{libro_id}")
def actualizar_libros(
    libro_id: int,
    libro: Libro
):

    if libro_id not in libros:
        return {"error": "Libro no encontrado"}

    actualizado = libro.model_dump()
    actualizado["id"] = libro_id

    libro[libro_id] = actualizado

    return actualizado



# DELETE /libros/{libro_id}

@app.delete("/libros/{libro_id}")
def eliminar_libros(libro_id: int):

    if libro_id not in libros:
        return {"error": "Libro no encontrado"}

    return libros.pop(libro_id)

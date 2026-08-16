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


# TODO
# GET /libros


# TODO
# GET /libros/{libro_id}


# TODO
# POST /libros


# TODO
# PUT /libros/{libro_id}


# TODO
# DELETE /libros/{libro_id}
from fastapi import FastAPI

app = FastAPI()


@app.get("/productos/{producto_id}")
def obtener_producto(producto_id: int):
    return {
        "id": producto_id
    }
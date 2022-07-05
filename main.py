import traceback

from fastapi import FastAPI

import services
from dto import Compra

app = FastAPI()


@app.post("/passageiro/{id_passageiro}/reserva/")
def reserva_passagem(id_passageiro: int, compra: Compra):
    try:
        id_passagem = services.reservar_passagem(id_passageiro, compra)
        return {'id_passagem': id_passagem}
    except Exception as e:
        traceback.format_exc()
        raise e

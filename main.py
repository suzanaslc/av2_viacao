import traceback

from fastapi import FastAPI
from pydantic import BaseModel

from src import services

app = FastAPI()


class Compra(BaseModel):
    localSaida: str
    localDestino: str


@app.post("/passageiro/{id_passageiro}/reserva/{id_onibus}")
def reserva_passagem(id_passageiro: int, id_onibus: int, compra: Compra):
    try:
        id_passagem = services.reservar_passagem(id_passageiro, id_onibus, compra)
        return {'id_passagem': id_passagem}
    except Exception as e:
        traceback.format_exc()
        raise e

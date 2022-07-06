import traceback

from fastapi import FastAPI, HTTPException

import services
from dto import Compra, PassageiroDto

app = FastAPI()


@app.post("/passageiro/{id_passageiro}/reserva")
def reserva_passagem(id_passageiro: int, compra: Compra):
    try:
        id_passagem = services.reservar_passagem(id_passageiro, compra)
        return {'resultado': "sucesso"}
    except Exception as e:
        traceback.format_exc()
        raise HTTPException(status_code=404, detail="Local não encontrado")


@app.post("/passageiro")
def cadastrar_passageiro(passageiro: PassageiroDto):
    try:
        id_passageiro = services.cadastrar_passageiro(passageiro)
        return {"resultado": "sucesso"}
    except Exception as e:
        traceback.format_exc()
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")

from pydantic import BaseModel


class Compra(BaseModel):
    localSaida_id: int
    localDestino_id: int
    onibus_id: int


class PassageiroDto(BaseModel):
    nome: str
    rg: str

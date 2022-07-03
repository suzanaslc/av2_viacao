import traceback

from main import Compra
from src.models import Passageiro, Onibus


def reservar_passagem(id_passageiro: int, id_onibus: int, compra: Compra):
    try:
        passageiro = Passageiro.get_by_id(id_passageiro)
        onibus = Onibus.get_by_id(id_onibus)
        rota = onibus.rota
        if rota.localSaida is compra.localSaida and rota.localDestino is compra.localDestino:
            preco = rota.preco * (1 - (rota.desconto / 100))
        else:
            for parada in rota.paradas:
                parada
    except Exception as e:
        traceback.format_exc()
        raise e

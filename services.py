import traceback

from peewee import IntegrityError

from dto import Compra, PassageiroDto
from models import Passageiro, Onibus, Reserva, Local, Parada, db


def possui_lugares_disponiveis(saida, paradas):
    for parada in paradas:
        if parada.local == saida:
            if parada.lugares == 0:
                return False
            return True
    return False


def determinar_preco(saida, destino, paradas, preco):
    if paradas[0].local == saida and paradas[-1].local == destino:
        return preco * 0.9
    saida_index = 0
    destino_index = 0
    for parada in paradas:
        if parada.local == saida:
            saida_index = parada.posicao
        if parada.local == destino:
            destino_index = parada.posicao
    if saida_index >= destino_index or saida_index == 0 or destino_index == 0:
        raise Exception("Entrada ou saida inválidos")
    return preco * ((destino_index - saida_index) / len(paradas))


def ocupar_lugar(saida, destino, paradas):
    saida_posicao = 0
    destino_posicao = 0
    for parada in paradas:
        if parada.local == saida:
            saida_posicao = parada.posicao
        if parada.local == destino:
            destino_posicao = parada.posicao
    if destino_posicao == saida_posicao or destino_posicao == 0 or saida_posicao == 0:
        raise Exception("Erro ao ocupar lugares")
    db.execute_sql("UPDATE parada SET lugares=lugares-1 WHERE posicao <= %s AND posicao >= %s",
                   (destino_posicao, saida_posicao))
    db.commit()


def salvar_reserva(passageiro: Passageiro, saida: Local, destino: Local, onibus: Onibus, preco: float):
    reserva = Reserva(passageiro=passageiro, localSaida=saida, localDestino=destino, onibus=onibus, preco=preco)
    reserva.save()
    return reserva


def reservar_passagem(id_passageiro: int, compra: Compra):
    try:
        passageiro = Passageiro.get_by_id(id_passageiro)
        onibus = Onibus.get_by_id(compra.onibus_id)
        paradas = Parada.select().where(Parada.onibus == onibus).order_by(Parada.posicao)
        saida = Local.get_by_id(compra.localSaida_id)
        destino = Local.get_by_id(compra.localDestino_id)
        if possui_lugares_disponiveis(saida, paradas):
            preco_padrao = onibus.preco
            ocupar_lugar(saida, destino, paradas)
            preco = determinar_preco(saida, destino, paradas, preco_padrao)
            return salvar_reserva(passageiro, saida, destino, onibus, preco)
        else:
            raise Exception("Sem lugares disponiveis")
    except Exception as e:
        traceback.format_exc()
        raise e


def cadastrar_passageiro(passageiroDto: PassageiroDto):
    try:
        passageiro = Passageiro(nome=passageiroDto.nome, rg=passageiroDto.rg)
        passageiro.save()
    except IntegrityError as e:
        traceback.format_exc()
        raise e

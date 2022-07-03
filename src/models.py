from peewee import PostgresqlDatabase, Model, CharField, DoubleField, IntegerField, ForeignKeyField

from playhouse.postgres_ext import ArrayField

db = PostgresqlDatabase(database='xptotec', user='postgres', password='1234')


class BaseModel(Model):
    class Meta:
        database = db


class Rota(BaseModel):
    localSaida = CharField()
    localDestino: CharField()
    paradas: ArrayField(field_class=CharField)
    preco = DoubleField()
    desconto = DoubleField()


class Onibus(BaseModel):
    lugares = IntegerField()
    tipo = CharField()
    rota = ForeignKeyField(Rota)


class Passageiro(BaseModel):
    nome = CharField()
    rg = CharField()


class Reserva(BaseModel):
    passageiro = Passageiro
    localSaida = CharField()
    localDestino = CharField()
    subtotal = DoubleField()

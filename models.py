from peewee import PostgresqlDatabase, Model, CharField, DoubleField, IntegerField, ForeignKeyField

db = PostgresqlDatabase(database='xptotec', user='postgres', password='1234')


class BaseModel(Model):
    class Meta:
        database = db


class Local(BaseModel):
    cidade = CharField()
    estado = CharField(max_length=2)


class Onibus(BaseModel):
    lugares = IntegerField()
    tipo = CharField()
    preco = DoubleField()


class Parada(BaseModel):
    onibus = ForeignKeyField(Onibus)
    local = ForeignKeyField(Local)
    lugares = IntegerField()
    posicao = IntegerField()


class Passageiro(BaseModel):
    nome = CharField()
    rg = CharField()


class Reserva(BaseModel):
    passageiro = ForeignKeyField(Passageiro)
    localSaida = ForeignKeyField(Local)
    localDestino = ForeignKeyField(Local)
    onibus = ForeignKeyField(Onibus)
    preco = DoubleField()


# if db.table_exists('rota') is not None:
#     db.create_tables(BaseModel.__subclasses__())
#     passageiro = Passageiro(nome="Suzana", rg="1234")
#     passageiro.save()
#     rio = Local(cidade="Rio de Janeiro", estado="RJ")
#     espirito_santo = Local(cidade="Espírito Santo", estado="ES")
#     salvador = Local(cidade="Salvador", estado="BA")
#     recife = Local(cidade="Recife", estado="PE")
#     rio.save()
#     espirito_santo.save()
#     salvador.save()
#     recife.save()
#     onibus = Onibus(lugares=32, tipo="Leito", preco=100.0)
#     onibus.save()
#     parada1 = Parada(onibus=onibus, local=rio, lugares=32, posicao=1)
#     parada1.save()
#     parada2 = Parada(onibus=onibus, local=espirito_santo, lugares=32, posicao=2)
#     parada2.save()
#     parada3 = Parada(onibus=onibus, local=salvador, lugares=32, posicao=3)
#     parada3.save()
#     parada4 = Parada(onibus=onibus, local=recife, lugares=32, posicao=4)
#     parada4.save()

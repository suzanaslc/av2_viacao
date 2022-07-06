from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def testar_reserva_inicio_fim():
    response = client.post(
        "/passageiro/1/reserva",
        json={"localSaida_id": 1,
              "localDestino_id": 4,
              "onibus_id": 1}
    )
    assert response.status_code == 200


def testar_reserva_inicio_parada():
    response = client.post(
        "/passageiro/1/reserva",
        json={"localSaida_id": 1,
              "localDestino_id": 3,
              "onibus_id": 1}
    )
    assert response.status_code == 200


def testar_reserva_parada_fim():
    response = client.post(
        "/passageiro/1/reserva",
        json={"localSaida_id": 2,
              "localDestino_id": 4,
              "onibus_id": 1}
    )
    assert response.status_code == 200


def testar_reserva_paradas():
    response = client.post(
        "/passageiro/1/reserva",
        json={"localSaida_id": 2,
              "localDestino_id": 3,
              "onibus_id": 1}
    )
    assert response.status_code == 200


def testar_parada_inexistente():
    response = client.post(
        "/passageiro/1/reserva",
        json={"localSaida_id": 1,
              "localDestino_id": 5,
              "onibus_id": 1}
    )
    assert response.status_code == 404


def testar_cadastro():
    response = client.post(
        "/passageiro",
        json={"nome": "Paula",
              "rg": "123456",
              }
    )
    assert response.status_code == 200


def testar_cadastro_ja_existe():
    response = client.post(
        "/passageiro",
        json={"nome": "Suzana",
              "rg": "1234",
              }
    )
    assert response.status_code == 400

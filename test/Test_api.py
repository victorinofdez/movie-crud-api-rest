#  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Comprueba que la ruta / responde   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_inicio_status_code():

    response = client.get("/")

    assert response.status_code == 200

# Comprueba el contenido de la respuesta de /  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_inicio_contenido():

    response = client.get("/")

    data = response.json()

    assert "mensaje" in data
    
    assert data["mensaje"] == "Bienvenido a Pitufin Movie"

    assert data["documentacion"] == "/docs"

    assert data["documentacion_alternativa"] == "/redoc"

# Comprueba que la ruta /estado   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_estado_status_code():

    response = client.get("/estado")

    assert response.status_code == 200

# Comprueba el mensaje del estado del   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

def test_estado_contenido():

    response = client.get("/estado")

    data = response.json()

    assert "estado" in data

    assert data["estado"] == "todo funciona Perfectamente valgame dios"

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

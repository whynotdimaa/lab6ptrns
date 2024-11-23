# test_smart_home.py
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_security_arm():
    response = client.get("/security/arm")
    assert response.status_code == 200
    assert response.json() == {"status": "Security system armed."}

def test_control_lighting():
    response = client.get("/lighting/on")
    assert response.status_code == 200
    assert response.json() == {"status": "Lighting action 'on' executed."}

def test_set_temperature():
    response = client.get("/climate/set/22")
    assert response.status_code == 200
    assert response.json() == {"status": "Temperature set to 22°C."}

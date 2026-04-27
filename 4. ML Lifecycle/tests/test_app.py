from application import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_predict_endpoint():
    client = app.test_client()
    payload = {
        "Temperature": 30,
        "RH": 40,
        "Ws": 10,
        "Rain": 0,
        "FFMC": 85,
        "DMC": 20,
        "ISI": 5,
        "Classes": 1,
        "Region": 1,
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.get_json()

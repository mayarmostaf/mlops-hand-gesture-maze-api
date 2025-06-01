import pytest
from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hand gesture recognition API is up."}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict():
    # Sample 42 values: [x1, y1, x2, y2, ..., x21, y21]
    test_data = {
        "landmarks": [
            262.67, 257.30, 257.42, 247.11, 246.88, 241.71, 236.38, 241.45, 230.08, 243.95,
            238.13, 233.23, 225.65, 247.25, 226.06, 255.87, 228.16, 260.38, 236.88, 238.05,
            226.11, 252.71, 229.43, 260.45, 232.64, 265.25, 236.29, 244.32, 225.11, 256.21,
            227.39, 263.65, 230.75, 268.07, 236.51, 251.71, 223.35, 255.49, 215.04, 258.11,
            208.01, 259.61
        ]
    }

    response = client.post("/predict", json=test_data)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], str)

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'api'))

from index import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello from CI/CD demo!"

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../LAB_TEST06')        
from main import app

client = TestClient(app)

def test_post_students_insert(db):
    response = client.post(
        "/students/",
        json={
            "name": "string2",
            "description": "string",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "string2"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_put_students_insert(db):
    response = client.put(
        "/students/6233fe1661c220f21379f8a2",
        json={
            "name": "update",
            "description": "string2",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string2"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_delete_students_insert(db):
    response = client.delete(
        "/students/6233fe1661c220f21379f8a2"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
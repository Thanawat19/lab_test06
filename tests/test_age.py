from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../lab_test06')        
from main import app

client = TestClient(app)

def test_year_api():
    input = "2543"
    output = 22
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_year_zero_api():
    input = "0"
    output = "your input too less"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_year_less_zero_api():
    input = "-1"
    output = "your input too less"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_year_over_api():
    input = "2566"
    output = "your input too over"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}
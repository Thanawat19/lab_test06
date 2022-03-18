from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../LAB_TEST06')
from main import app

client = TestClient(app)

def test_post_todo_insert(db):
    assert True
import json
from fastapi.testclient import TestClient
from web_exercise1 import app
"""
Run: python web_exercise1_test.py
"""
client = TestClient(app)


def test_post():
    data = json.dumps({"value": 10})
    r = client.post("/42?query=5", data=data)
    print(r.json())
    assert r.json()["path"] == 42
    assert r.json()["query"] == 5
    assert r.json()["body"] == {"value": 10}

if __name__ == "__main__":
    test_post()
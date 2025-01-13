from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

class Value(BaseModel):
    value:int

# define POST method
@app.post("/{path}")
async def exercise_function(path: int, query: int, body:Value):
    return {"path": path, "query": query, "body": body}




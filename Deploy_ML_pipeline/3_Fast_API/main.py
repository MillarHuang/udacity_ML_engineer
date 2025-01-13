from fastapi import FastAPI

# Instantiate the app(FastAPI class)
app = FastAPI()

# Define a function that returns a simple greeting in Json format, which has a decorator that defines GET method
# Define a GET on the specified endpoint.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}
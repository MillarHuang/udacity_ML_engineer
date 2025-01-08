import requests
import json

data = {"name":"Kit","tags":['Books','Towels'],
        "item_id":23}
r = requests.post("https://udacit-web-test.onrender.com/items/", data = json.dumps(data))
print(r.json())

g = requests.get("https://udacit-web-test.onrender.com/items/23?count=5")
print(g.json())
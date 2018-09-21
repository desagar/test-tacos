import requests

req = requests.get('http://129.213.75.222:8081/api/v1/stores')

req.raise_for_status()
if req.headers["Content-Type"] != "application/json":
  raise Exception("Expected JSON, got content type " + req.headers["Content-Type"])

respJson = req.json()

assert len(respJson) == 3, "Expected 3 stores from Tacos API"
storeNames = list(map(lambda x: str(x["name"]), respJson))
print storeNames
assert "Silly Tacos" in storeNames, "Silly Tacos missing!"
assert "Chilly Willy" in storeNames, "Chilly Willy missing!"
assert "Silly Tacos" in storeNames, "Silly Tacos missing!"

import requests

# Define la URL de destino
url = "http://127.0.0.1:8001/marie/outbox"

# Define el JSON que deseas enviar
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "UpdateClass",
  "id": "http://127.0.0.1:8001/marie/activities/a2b2c2d2",
  "actor": "http://127.0.0.1:8001/marie/",
  "to": ["http://127.0.0.1:8000/freddie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/freddie/classes/a1b2c3",
    "name": "House",
    "summary": "Represents a class for houses.",
    "attributes": []
  }
}

# Envía la solicitud POST con el JSON
response = requests.post(url, json=json_data)

# Verifica la respuesta
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
import requests

# Define la URL de destino
url = "http://127.0.0.1:8001/marie/outbox"

# Define el JSON que deseas enviar
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "CreateClass",
  "id": "http://127.0.0.1:8001/marie/activities/a1b2c3",
  "actor": "http://127.0.0.1:8001/marie/",
  "to": ["http://127.0.0.1:8000/freddie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8001/marie/classes/a1b2c3book",
    "name": "Book",
    "summary": "Represents a class for books.",
    "attributes": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8001/marie/classes/attrs/a1b1c1",
        "name": "name",
        "summary": "The name of the book.",
        "elementType": "str"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8001/marie/classes/attrs/a2b2c3",
        "name": "pages",
        "summary": "The pages of the book.",
        "elementType": "int"
      }
    ]
  }
}

# Envía la solicitud POST con el JSON
response = requests.post(url, json=json_data)

# Verifica la respuesta
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
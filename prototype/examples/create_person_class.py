import requests

url = "http://127.0.0.1:8000/userA/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/userA/activities/a4c6t8",
  "actor": "http://127.0.0.1:8000/userA/",
  "to": ["http://127.0.0.1:8001/userB/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/userA/classes/c7l8s9",
    "name": "Person",
    "attributes": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/userA/properties/p8b1c1",
        "name": "name",
        "elementType": "str"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/userA/properties/a2tt2c3",
        "name": "age",
        "elementType": "int"
      }
    ]
  },
  "target": "http://127.0.0.1:8000/userA/domainmodel/a1b2c3",
  "timestamp": "2025-05-11T15:32:15Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
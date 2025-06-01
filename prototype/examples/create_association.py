import requests

url = "http://127.0.0.1:8000/userA/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/userA/activities/a1c2t3",
  "actor": "http://127.0.0.1:8000/userA/",
  "to": ["http://127.0.0.1:8001/userB/"],
  "object": {
    "type": "BinaryAssociation",
    "id": "http://127.0.0.1:8000/userA/associations/a1s2d3",
    "name": "relationship",
    "ends": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/userA/property/e1n2d3",
        "name": "person",
        "elementType": "http://127.0.0.1:8000/userA/classes/c7l8s9",
        "multiplicity": "1"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/userA/properties/e5n7d9",
        "name": "pets",
        "elementType": "http://127.0.0.1:8000/userA/classes/a1b2c3",
        "multiplicity": "0..*"
      }
    ],
  },
  "target": "http://127.0.0.1:8000/userA/domainmodel/a1b2c3",
  "timestamp": "2025-05-11T20:31:45Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
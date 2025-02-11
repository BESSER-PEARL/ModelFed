import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/a1c2t3",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "BinaryAssociation",
    "id": "http://127.0.0.1:8000/freddie/associations/a1s2d3",
    "name": "relationship",
    "ends": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/property/e1n2d3",
        "name": "end1",
        "elementType": "http://127.0.0.1:8000/freddie/classes/a1b2c3",
        "multiplicity": "0..1"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/properties/e5n7d9",
        "name": "end2",
        "elementType": "http://127.0.0.1:8000/freddie/classes/c7l8s9",
        "multiplicity": "1",
        "isComposite": True,
      }
    ],
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3",
  "timestamp": "2024-02-11T15:44:45Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
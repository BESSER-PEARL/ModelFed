import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/a4c6t8",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/freddie/classes/c7l8s9",
    "name": "Building",
    "attributes": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/properties/p8b1c1",
        "name": "name",
        "elementType": "str"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/properties/a2tt2c3",
        "name": "year",
        "elementType": "int"
      }
    ],
    "methods": [
      {
        "type": "Method",
        "id": "http://127.0.0.1:8000/freddie/methods/m8t1d1",
        "name": "close",
        "elementType": "boolean",
        "parameters": [
          {
            "type": "Parameter",
            "id": "http://127.0.0.1:8000/freddie/parameters/p8t1d1",
            "name": "origin",
            "elementType": "date"
          }
        ]
      }
    ]
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
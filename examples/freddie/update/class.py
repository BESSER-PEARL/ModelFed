import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Update",
  "id": "http://127.0.0.1:8000/freddie/activities/a2b2c2",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/freddie/classes/a1b2c3",
    "name": "Museum",
    "summary": "Represents a class for museums.",
    "attributes": [
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/classes/attrs/a1b1c1",
        "name": "name",
        "summary": "The name of the library.",
        "elementType": "str"
      },
      {
        "type": "Property",
        "id": "http://127.0.0.1:8000/freddie/classes/attrs/a2b2c3",
        "name": "location",
        "summary": "The location of the library.",
        "elementType": "str"
      }
    ]
  }
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
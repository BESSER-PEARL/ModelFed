import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/a1b2c3",
  "actor": "http://127.0.0.1:8001/marie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Class",
    "id": "http://127.0.0.1:8000/freddie/classes/a1b2c3",
    "name": "Library",
    "summary": "Represents a class for libraries."
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/p4c6k8",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Package",
    "id": "http://127.0.0.1:8000/freddie/packages/p7a8k9",
    "name": "packageA",
    "owner": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3",
    "classes": [
        "http://127.0.0.1:8000/freddie/classes/a1b2c3",
        "http://127.0.0.1:8000/freddie/classes/c7l8s9"
    ]
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3",
  "timestamp": "2024-02-11T15:39:45Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
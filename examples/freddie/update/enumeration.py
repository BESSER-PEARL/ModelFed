import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://BESSER-PEARL.github.io/Modelverse/ns/modelverse.jsonld"
  ],
  "type": "Update",
  "id": "http://127.0.0.1:8000/freddie/activities/up1en0u30",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Enumeration",
    "id": "http://127.0.0.1:8000/freddie/enumerations/e1n2u3",
    "name": "New_Category"
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3",
  "timestamp": "2024-04-11T15:10:45Z"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
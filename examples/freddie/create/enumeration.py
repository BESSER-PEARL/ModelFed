import requests

url = "http://127.0.0.1:8000/freddie/outbox"

# JSON activity definition
json_data = {
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Create",
  "id": "http://127.0.0.1:8000/freddie/activities/e10n20u30",
  "actor": "http://127.0.0.1:8000/freddie/",
  "to": ["http://127.0.0.1:8001/marie/"],
  "object": {
    "type": "Enumeration",
    "id": "http://127.0.0.1:8000/freddie/enumerations/e1n2u3",
    "name": "Category",
    "literals": [
        {
            "type": "EnumerationLiteral",
            "id": "http://www.modeling-platform/enumerationliteral/l1m2n3",
            "name": "Public",
            "value": "1",
        },
        {
            "type": "EnumerationLiteral",
            "id": "http://www.modeling-platform/enumerationliteral/l1i2t3",
            "name": "Academic",
            "value": "2",
        }
    ]
  },
  "target": "http://127.0.0.1:8000/freddie/domainmodel/a1b2c3"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
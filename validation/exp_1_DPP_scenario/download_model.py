import requests

url = "http://127.0.0.1:8000/generate_model"

# JSON activity definition
json_data = {
  "model_id": "http://127.0.0.1:8000/admin/domainmodel/digital_product_passport",
  "file_path": "output_model/dpp_besser_model.py"
}

# Send the request
response = requests.post(url, json=json_data)
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")
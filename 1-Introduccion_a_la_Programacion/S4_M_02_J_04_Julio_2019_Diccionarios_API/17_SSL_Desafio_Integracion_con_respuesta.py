import json
import requests

def request(requested_url):
    headers = {
        "cache-control": "no-cache",
        "Postman-Token": "2defb9f3-9b11-499b-be4f-82505a2f8e1a",
    }
    response = requests.request("GET", requested_url, headers=headers)
    return json.loads(response.text)

prices = request("https://api.coindesk.com/v1/bpi/historical/close.json")["bpi"]
#print(data)

selected_data = [k for k, v in prices.items() if v < 5000]
print(selected_data)

under_5000 = [v for v in prices.values() if v < 5000]
data_inv = {v:k for k, v in prices.items()}
selected_data = [data_inv[k] for k in under_5000]
print(selected_data)
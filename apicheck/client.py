import requests

endpoint_url = "http://127.0.0.1:8000/todos/all/update/1/"

# message = requests.get(endpoint_url)

# print(message.json())

delMes = requests.put(endpoint_url, json={"task": "The Rooooooooooooook!! by Levy Rozman", "completion": True})

print(delMes.json(), delMes.status_code)
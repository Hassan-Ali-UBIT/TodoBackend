import requests

endpoint_url = "http://127.0.0.1:8000/todos/all/1/"

# message = requests.get(endpoint_url)

# print(message.json())

delMes = requests.get(endpoint_url)

print(delMes.json(), delMes.status_code)
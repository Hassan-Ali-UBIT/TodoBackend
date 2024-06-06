import requests
from getpass import getpass

auth_endpoint = "http://127.0.0.1:8000/todos/auth/"

username = input("What is the username: ")
password = getpass("What is the password: ")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response)

if auth_response.status_code == 200:
    token = auth_response.json()["token"]

    headers = {
        "Authorization": f"Token {token}"
    }
    endpoint_url = "http://127.0.0.1:8000/todos/"

    response = requests.get(endpoint_url, headers=headers)

    print(response.json())

# else:
#     print("Some Weird Shit happened yo")

# message = requests.get(endpoint_url)

# print(message.json())

# delMes = requests.get(endpoint_url)

# print(delMes.json(), delMes.status_code)
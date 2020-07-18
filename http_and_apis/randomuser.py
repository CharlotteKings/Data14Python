import requests

address = "https://randomuser.me/"
req_response = requests.get(address)

print(req_response)
import requests
import json
from pprint import pprint
# address = "https://api.postcodes.io/postcodes/DY9 0YHJIJ"
# req_response = requests.get(address)
# #
# print(req_response)  # Prints HTTP status code [200] means OK
# print(type(req_response))  # = <class 'requests.models.Response'>
# # print(req_response.status_code)  # If status is not returned and want it
# # print(req_response.headers)    # Python turns it into a dictionary but was originally a json file
# #
# # pprint(req_response.content)  # returns bytes
# pprint(req_response.json())
#
# # Get dictionary within dictionary result
# result = req_response.json()['result']
# print(result['codes']['nuts'])

#
#
dict_body = {'postcodes': ["B7 4BB", "OX49 5NU","M32 0JG"]}
json_body = json.dumps(dict_body)
headers = {'Content-type': 'application/json'}

address = "https://api.postcodes.io/postcodes/"
req_response = requests.post(address,headers=headers,data=json_body)

pprint(req_response.json()['result'])
#
# # Print the postcode, eastings, northings and NUTS code for each result
#
#
#
# for postcode in req_response.json()['result']:
#     result = postcode['result']
#     print(f" Postcode = {postcode['query']}, eastings = {result['eastings']}, northings = {result['northings']}and NUTS code = {result['codes']['nuts']}")

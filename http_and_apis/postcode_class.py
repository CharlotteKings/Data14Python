import requests
import json

class Postcode:

    def __init__(self,postcode):
        self.postcode = postcode
        self.address = "https://api.postcodes.io/postcodes/"+ self.postcode
        self.req_response = requests.get(self.address)
        self.result = self.req_response.json()['result']
        self.codes = self.result['codes']
        self.eastings = self.result['eastings']
        self.northings = self.result['northings']


    def get_address(self):
        return self.result



my_house = Postcode("DY9 0YH")
# wrong_house = Postcode("abcdefg")
print(my_house.req_response)
print(my_house.get_address())
print(my_house.codes['nuts'])

postcode_list = ["DY9 0YH", "CV1 2BP", "CV2 3LT", "CV1 5FB"]
postcode_objects = []

# for postcode in postcode_list:


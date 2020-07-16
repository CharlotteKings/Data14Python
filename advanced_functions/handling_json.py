import json
from pprint import pprint  # Pretty print
# # Returns this 'pretty'
# # Returns things in alphabetical order
#
# # GETTING INFO OUT OF JSON
# with open("film.json", "r") as jsonfile:
#     film = json.load(jsonfile)
#
# pprint(film)  # Returned as a dictionary


# DICTIONARY TO STRING - dump
film = {
    "name": "The Godfather",
    "length": 178,
    "release_year": 1972
}

print(json.dumps(film))
print(type(json.dumps(film)))

# NEW FILE  - dumps
with open("godfather.json","w") as jsonfile:
    json.dump(film,jsonfile)
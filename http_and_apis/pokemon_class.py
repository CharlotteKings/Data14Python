import requests
import json
from pprint import pprint

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.address = "https://pokeapi.co/api/v2/pokemon/"+ self.pokemon_name
        self.req_response = requests.get(self.address)
        self.result = self.req_response.json()
        self.abilities_list = []
        self.abilities_url = []
        self.abilities_effects_list = []

    def abilities_and_effects(self):
        abilities = self.result['abilities']
        for ability in abilities:
            pokemon_ablility = ability['ability']
            self.abilities_list.append(pokemon_ablility['name'])
            self.abilities_url.append(pokemon_ablility['url'])
        for url in self.abilities_url:
            get_effect = requests.get(url)
            response = get_effect.json()["effect_entries"]
            for row in response:
                if row['language']['name'] == 'en':
                    append_with = row['short_effect']
                    self.abilities_effects_list.append(append_with)
        return self.abilities_list , self.abilities_effects_list


    def appened_to_txt_file(self):
        with open("pokemon_stats.txt", "a") as pokeapi:
            if len(self.abilities_list) == 1:
                pokeapi.writelines(f"{self.pokemon_name} only ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
            elif len(abilities_list) == 2:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
            elif len(abilities_list) == 3:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} third ability is: {self.list_of_abilities_names[2]}, and the effect {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
            elif len(abilities_list) == 4:
                pokeapi.writelines(f"{self.pokemon_name} first ability is: {self.list_of_abilities_names[0]}, and the effect {self.list_of_effect[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} second ability is: {self.list_of_abilities_names[1]}, and the effect {self.list_of_effect[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} third ability is: {self.list_of_abilities_names[2]}, and the effect {self.list_of_effect[2]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.pokemon_name} fourth ability is: {self.list_of_abilities_names[3]}, and the effect {self.list_of_effect[3]}")
                pokeapi.writelines("\n")






pikachu = Pokemon("pikachu")

#print(pikachu.abilities_and_effects())
#pprint(pikachu.result)
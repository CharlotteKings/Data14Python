import requests
import json
from config_manager import base_url
from pprint import pprint

class Pokemon:
    def __init__(self, pokemon_name):
        self.pokemon_name = pokemon_name
        self.address = "https://pokeapi.co/api/v2/pokemon/" + self.pokemon_name  # base_url()
        self.req_response = requests.get(self.address)
        self.result = self.req_response.json()
        self.abilities_list = []
        self.abilities_url = []
        self.abilities_effects_list = []
        self.base_stat = []
        self.base_stat_name = []
        self.moves = []


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
        return self.abilities_list, self.abilities_effects_list


    def get_base_stats(self):
        stats = self.result['stats']
        for stat in stats:
            stats_info = stat['base_stat']
            self.base_stat.append(stats_info)
            stats_name = stat['stat']['name']
            self.base_stat_name.append(stats_name)
        return self.base_stat, self.base_stat_name


    def get_moves(self):  # need to fix
        moves_key = self.result['moves']
        for move in moves_key:
            move_name = move['move']['name']
            self.moves.append(move_name)
        return self.moves


    def write_pokemon(self):
        with open(f"{self.pokemon_name}.txt", "a")as opened_file:
            opened_file.writelines(f"Ability, Effects: {list(map(lambda a,b:(a,b) ,self.abilities_list, self.abilities_effects_list))} \n")
            opened_file.writelines(f"Base Stat, Base Stat Name: {list(map(lambda a,b:(a,b) ,self.base_stat, self.base_stat_name))} \n")
            opened_file.writelines(f"Moves : {self.moves} \n")



pikachu = Pokemon("pikachu")
pikachu.get_base_stats()
pikachu.abilities_and_effects()
pikachu.get_moves()
pikachu.write_pokemon()
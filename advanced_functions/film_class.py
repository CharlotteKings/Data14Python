import json

class Film:

    def __init__(self, title, year, rated):
        self.title = film_dict['title']
        self.year = year
        self.rated = rated


    def read_film(self):
        with open("film.json", "r") as jsonfile:
            film_dict = json.load(jsonfile)
            print(film)

new_film = Film()
new_film.read_film()
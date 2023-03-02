import requests
from pprint import pprint
import json


LINK = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
hero_list = ('Hulk', 'Captain America', 'Thanos')

def get_sh():
    url = LINK
    response = requests.get(url)
    return response.json()

max_int = 0
most_int_hero = ''

for hero in get_sh():
    if hero['name'] in hero_list:
        # print(hero['name'])
        # print(hero['powerstats']['intelligence'])
        if hero['powerstats']['intelligence'] > max_int:
            max_int = hero['powerstats']['intelligence']
            most_int_hero = hero['name']

print(f'Most intelligent hero is {most_int_hero} with intelligence: {max_int}')
import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'YOUR_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create_poke = {
    "name": "Кохаку2",
    "photo_id": 2
}

body_change_poke = {
    "pokemon_id": "45777",
    "name": "Хитоми",
    "photo_id": 2
}

body_catch_poke = {
    "pokemon_id": "45777"
}


'''create_poke = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_poke)
print(create_poke.text)'''

'''change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_poke)
print(change_name.text)'''

catch_poke = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_poke)
print(catch_poke.text)

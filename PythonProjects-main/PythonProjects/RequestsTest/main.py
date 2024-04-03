import requests


response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json ={
    "name": "generate",
    "photo": "generate"
},headers = {'Content-Type':'application/json','trainer_token':'9613abb177c2913fc6f8c2482b6e201a'})
print(response.text)

response_change_name = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {"pokemon_id": "6027",
    "name": "pikachu","photo": "https://dolnikov.ru/pokemons/albums/025.png"},headers = {'Content-Type':'application/json','trainer_token':'9613abb177c2913fc6f8c2482b6e201a'})
print(response_change_name.text)

response_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball',json = {
    "pokemon_id": "6027"},headers = {'Content-Type':'application/json','trainer_token':'9613abb177c2913fc6f8c2482b6e201a'})
print(response_pokeball.text)

### Токен вводится в файле key.py ###
import requests
from key import TOKEN
### Задаем переменные ###
URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type':'application/json'}
trainer_token = {'trainer_token' : TOKEN}
pokemon_id = 0
body = {
    'name': 'Mona',
    'photo': 'https://dolnikov.ru/pokemons/albums/906.png'
}
### Создание покемона ###
response = requests.post(url= f'{URL}/pokemons', headers = HEADERS | trainer_token, json = body)
print(response,response.text)
### Забераем покемона в переменную ###
pokemon_id = response.json()['id']
print(pokemon_id)
### Смена имени покемона ###
response = requests.put(url= f'{URL}/pokemons', headers = HEADERS | trainer_token, json = {
    'pokemon_id' : f'{pokemon_id}',
    'name': 'MonaChan',
    'photo': 'https://dolnikov.ru/pokemons/albums/906.png'
})
print(response,response.text)
### Прячем покемона в покебол ###
response = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADERS | trainer_token, json = {
    'pokemon_id' : f'{pokemon_id}'
})
print(response,response.text)
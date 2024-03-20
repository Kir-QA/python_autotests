### Имя тренера и ID находится в файле key.py ###
import requests
import pytest
from key import TRAINER_ID, TRAINER_NAME
###Зададим необходимые переменные###
URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json'}
query = {'trainer_id' : TRAINER_ID}
### Проверь, что ответ запрос GET /trainers приходит с кодом 200 ###
def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = query)
    assert response.status_code == 200
### Проверь, что в ответе приходит строчка с именем твоего тренера ###
def test_name():
    response = requests.get(url = f'{URL}/trainers', params = query)
    assert response.json()['data'][0]['trainer_name'] == TRAINER_NAME
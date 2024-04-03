import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '9613abb177c2913fc6f8c2482b6e201a'

def test_status_code():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 2564})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id' : 2564})
    assert response.json()['trainer_name'] == 'Irina'

import pytest
import requests
import yaml

with open("config.yaml") as f:
    infodata = yaml.safe_load(f)

url = infodata["url"]


@pytest.fixture()
def autorization():
    result = requests.post(url=url, data={"username": "kitty89", "password": "61d96a3985"})
    return result.json()['token']

@pytest.fixture()
def create_newpost():
    result = requests.post(url=url, headers={"X-Auth-Token": autorization}, data={
        "username": "kitty89", 
        "password": "61d96a3985", 
        "title": "My cats", 
        "description": "Murring", 
        "content": "Cats can mur"})
    return result.json()['description']

@pytest.fixture()
def real_post_id():
    return 90526

@pytest.fixture()
def new_description():
    return "Murring"


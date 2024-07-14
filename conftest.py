import pytest
from data import Data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture(scope='function')
def get_bun_data():
    return Data.bun

@pytest.fixture(scope='function')
def get_sause_data():
    return Data.sauce

@pytest.fixture(scope='function')
def get_filling_data():
    return Data.filling

@pytest.fixture(scope='function')
def get_bun(get_bun_data):
    return Bun(name=get_bun_data.name, price=get_bun_data.price)

@pytest.fixture(scope='function')
def get_sause(get_sause_data):
    # return Data.sauce
    return Ingredient(name=get_sause_data.name, price=get_sause_data.price, ingredient_type=get_sause_data.ingredient_type)
        
@pytest.fixture(scope='function')
def get_filling(get_filling_data):
    # return Data.filling
    return  Ingredient(name=get_filling_data.name, price=get_filling_data.price, ingredient_type=get_filling_data.ingredient_type)

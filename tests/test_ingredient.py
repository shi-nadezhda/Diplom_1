import pytest
from praktikum.ingredient import Ingredient
from data import Data   
    

class TestIngredient:         
    @pytest.mark.parametrize('ingredient', [Data.sauce, Data.filling])
    # У ингредиента есть тип (начинка или соус), название и цена.
    def test_ingredient_has_price_and_type(self, ingredient):
        current_ingredient = Ingredient(name=ingredient.name, price=ingredient.price, ingredient_type=ingredient.ingredient_type)
        
        assert current_ingredient.get_price() == ingredient.price 
        assert current_ingredient.get_type() == ingredient.ingredient_type 
        assert current_ingredient.get_name() == ingredient.name 
  
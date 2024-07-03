from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock

class Data:
    bun = Mock()
    bun.name = "Флюоресцентная булка R2-D3"
    bun.price = 988
    
    sauce = Mock()
    sauce.name = "Соус Spicy-X"
    sauce.price =  90
    sauce.ingredient_type = INGREDIENT_TYPE_SAUCE

    filling = Mock()
    filling.name = "Биокотлета из марсианской Магнолии"
    filling.price =  424
    filling.ingredient_type = INGREDIENT_TYPE_FILLING

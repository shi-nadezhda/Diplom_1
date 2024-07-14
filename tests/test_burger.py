from praktikum.burger import Burger
from praktikum.bun import Bun


class TestBurger:
    # В бургер можно добавить булочки
    def test_set_buns_success(self, get_bun_data):
        bun = Bun(name=get_bun_data.name, price=get_bun_data.price)
        burger = Burger()
        burger.set_buns(bun)
        
        assert burger.bun == bun
        
        
    # В бургер можно добавить ингридиенты
    def test_add_ingredient_success(self, get_sause):
        burger = Burger()
        burger.add_ingredient(get_sause)
        
        assert get_sause in burger.ingredients 
        
        
    # Ингредиенты можно удалять
    def test_remove_ingredient_success(self, get_filling, get_sause):
        burger = Burger()
        burger.add_ingredient(get_sause)
        burger.add_ingredient(get_filling)
        burger.remove_ingredient(0)
        
        assert get_sause not in burger.ingredients and len(burger.ingredients) == 1
                 
                     
    # Ингредиенты можно перемещать
    def test_move_ingredient_success(self, get_filling, get_sause):
        burger = Burger()
        burger.add_ingredient(get_sause)
        burger.add_ingredient(get_filling)
        burger.move_ingredient(0, 1)
        
        assert burger.ingredients[0] == get_filling
        assert burger.ingredients[1] == get_sause 

        
    # Можно распечать чек с информацией о бургере
    def test_get_receipt_success(self, get_bun_data, get_sause_data, get_filling_data, get_bun, get_filling, get_sause):
        burger = Burger()
        
        burger.set_buns(get_bun)
        burger.add_ingredient(get_sause)
        burger.add_ingredient(get_filling)
        
        price = burger.get_price()
        check = burger.get_receipt()
        
        burger_check = [
            get_bun_data.name, 
            f"{get_sause_data.ingredient_type.lower()} {get_sause_data.name}",
            f"{get_filling_data.ingredient_type.lower()} {get_filling_data.name}",
            f"Price: {str(price)}"
        ]
        
        for text in burger_check:
            assert text in check

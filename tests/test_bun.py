from praktikum.bun import Bun


class TestBun:
    # Булочке можно дать название
    def test_get_name_success(self, get_bun_data):
        bun = Bun(name = get_bun_data.name, price = get_bun_data.price)
        assert bun.get_name() == get_bun_data.name
    
    
    # Булочке можно назначить цену
    def test_get_price_success(self, get_bun_data):
        bun = Bun(name = get_bun_data.name, price = get_bun_data.price)
        assert bun.get_price() == get_bun_data.price
   
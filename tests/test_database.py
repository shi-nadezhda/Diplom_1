from praktikum.database import Database 
  
    
class TestDatabase:
    def test_available_buns(self):
        db = Database()
        bun = db.buns[0]
        
        assert bun in db.available_buns()
        
        
    def test_available_ingredients(self):
        db = Database()
        ingredient = db.ingredients[0]
        
        assert ingredient in db.available_ingredients()        
 
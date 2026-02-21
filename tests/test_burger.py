from praktikum.burger import Burger
from praktikum.database import Database
from tests.helper import get_price
from tests.testdata import RECEIPT


class TestBurger:
    def test_set_buns(self, db: Database):
        burger = Burger()
        bun = db.available_buns()[0]
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self, db: Database):
        burger = Burger()
        ing = db.available_ingredients()[0]
        burger.add_ingredient(ing)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ing
    
    def test_remove_ingredient(self, db: Database):
        burger = Burger()
        ing = db.available_ingredients()[0]
        burger.add_ingredient(ing)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    def test_move_ingredient(self, db: Database):
        burger = Burger()
        ings = db.available_ingredients()
        burger.add_ingredient(ings[0])
        burger.add_ingredient(ings[1])
        burger.move_ingredient(1,0)
        assert burger.ingredients[0] == ings[1]
        assert burger.ingredients[1] == ings[0]

    def test_get_price(self, db: Database):
        burger = Burger()
        bun = db.available_buns()[0]
        burger.set_buns(bun)
        ings = db.available_ingredients()
        burger.add_ingredient(ings[0])
        burger.add_ingredient(ings[1])
        assert burger.get_price() == get_price(burger)        

    def test_get_receipt(self, db: Database):
        burger = Burger()
        bun = db.available_buns()[0]
        burger.set_buns(bun)
        ings = db.available_ingredients()
        burger.add_ingredient(ings[0])
        burger.add_ingredient(ings[1])

        assert burger.get_receipt() == RECEIPT        
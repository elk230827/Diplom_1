from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from tests.testdata import RECEIPT


class TestBurger:
    @pytest.mark.parametrize("bun", Database().available_buns())
    def test_set_buns(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    @pytest.mark.parametrize("ing", Database().available_ingredients())
    def test_add_ingredient(self, ing):
        burger = Burger()
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

    def test_get_price_mock(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        burger.set_buns(bun)
        ing = Mock()
        ing.get_price.return_value = 10

        burger.add_ingredient(ing)
        burger.add_ingredient(ing)
        
        assert burger.get_price() == 220        


    def test_get_receipt(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        bun.get_name.return_value = "black bun"
        burger.set_buns(bun)
        ing = Mock()
        ing.get_price.return_value = 10
        ing.get_name.return_value = "hot sauce"
        ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(ing)
        burger.add_ingredient(ing)

        assert burger.get_receipt() == RECEIPT        

    
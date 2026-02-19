from praktikum.burger import Burger


def get_price(burger: Burger):
    price = burger.bun.get_price() * 2 
    for i in burger.ingredients:
        price = price + i.get_price() 
    return price
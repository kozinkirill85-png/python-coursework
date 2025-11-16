import pytest
from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

def test_category_add_product_valid():
    category = Category("Категория", "Описание", [])
    product = Product("P", "", 100.0, 2)
    category.add_product(product)
    assert len(category._Category__products) == 1  # если приватный атрибут __products

def test_category_add_product_invalid():
    category = Category("Категория", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("Not a product")

def test_category_add_smartphone():
    category = Category("Смартфоны", "Описание", [])
    smartphone = Smartphone("S", "", 100.0, 2, 90.0, "M", 128, "Black")
    category.add_product(smartphone)
    assert len(category._Category__products) == 1

def test_category_add_lawn_grass():
    category = Category("Трава", "Описание", [])
    grass = LawnGrass("G", "", 5.0, 10, "US", "5 дней", "Green")
    category.add_product(grass)
    assert len(category._Category__products) == 1
import pytest
from src.product import Product
from src.category import Category


def test_category_init():
    product1 = Product("Samsung", "256GB", 180000.0, 5)
    product2 = Product("iPhone", "512GB", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание"

    # Проверяем, что в строке есть оба продукта
    assert "Samsung" in category.products
    assert "iPhone" in category.products

    # Проверяем, что в строке есть 2 продукта (по количеству "шт.")
    assert category.products.count("шт.") == 2

    assert category.category_count == 1
    assert category.product_count == 2


def test_category_counters():
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product("Samsung", "256GB", 180000.0, 5)
    product2 = Product("iPhone", "512GB", 210000.0, 8)
    category1 = Category("Смартфоны", "Описание", [product1, product2])

    product3 = Product("TV", "QLED", 123000.0, 7)
    category2 = Category("Телевизоры", "Описание", [product3])

    assert Category.category_count == 2
    assert Category.product_count == 3

def test_category_str():
    p1 = Product("P1", "", 100.0, 3)
    p2 = Product("P2", "", 200.0, 2)
    category = Category("Категория", "Описание", [p1, p2])
    assert str(category) == "Категория, количество продуктов: 5 шт."
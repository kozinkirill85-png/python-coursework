import pytest
from src.product import Product


def test_product_init():
    product = Product("Samsung", "256GB", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5

def test_product_str():
    product = Product("Test Product", "Description", 100.0, 5)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."

def test_product_add():
    p1 = Product("P1", "", 100.0, 2)
    p2 = Product("P2", "", 50.0, 4)
    assert p1 + p2 == 400.0  # 100*2 + 50*4 = 200 + 200

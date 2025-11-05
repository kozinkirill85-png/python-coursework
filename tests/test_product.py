import pytest
from src.product import Product


def test_product_init():
    product = Product("Samsung", "256GB", 180000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 180000.0
    assert product.quantity == 5

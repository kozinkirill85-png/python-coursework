import pytest
from src.product import Product
from src.smartphone import Smartphone

def test_product_creation_logging(capfd):
    """Проверяем, что при создании продукта выводится сообщение в консоль"""
    product = Product("P1", "Description", 100.0, 2)
    captured = capfd.readouterr()
    assert captured.out.strip() == "Product(P1, Description, 100.0, 2)"

def test_product_inherits_base_product():
    """Проверяем, что Product наследуется от BaseProduct"""
    from src.base_product import BaseProduct
    assert issubclass(Product, BaseProduct)

def test_product_str():
    product = Product("Test Product", "Description", 100.0, 5)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."

def test_product_add_same_type():
    p1 = Product("P1", "", 100.0, 2)
    p2 = Product("P2", "", 50.0, 4)
    assert p1 + p2 == 400.0

def test_product_add_different_type():
    p = Product("P", "", 100.0, 2)
    s = Smartphone("S", "", 200.0, 1, 90.0, "Model", 128, "Black")
    with pytest.raises(TypeError):
        p + s
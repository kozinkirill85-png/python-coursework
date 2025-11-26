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


def test_product_invalid_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Описание", 1000.0, 0)

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Описание", 1000.0, -5)


def test_product_create_with_zero_quantity():
    """Проверка, что при создании продукта с нулевым количеством выбрасывается ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Description", 100.0, 0)


def test_product_create_with_negative_quantity():
    """Проверка, что при создании продукта с отрицательным количеством выбрасывается ValueError."""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Description", 100.0, -1)


def test_product_price_setter_positive():
    """Проверка, что сеттер цены корректно устанавливает положительное значение."""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0


def test_product_price_setter_negative():
    """Проверка, что сеттер цены не позволяет установить нулевое или отрицательное значение."""
    product = Product("Test", "Desc", 100.0, 5)
    product.price = -10.0  # Это должно вывести сообщение, но не вызывать ошибку
    assert product.price == 100.0  # Цена не должна измениться


def test_product_addition():
    """Проверка сложения двух продуктов (общая стоимость)."""
    product1 = Product("A", "Desc", 100.0, 2)
    product2 = Product("B", "Desc", 50.0, 3)
    total = product1 + product2
    assert total == 350.0  # 100*2 + 50*3 = 200 + 150 = 350


def test_product_str():
    """Проверка строкового представления продукта."""
    product = Product("Test", "Desc", 100.0, 5)
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."
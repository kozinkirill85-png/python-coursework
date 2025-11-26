import pytest
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass
from src.category import Category
from src.exceptions import ZeroQuantityError
from src.product import Product


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


def test_category_middle_price():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    category = Category("Смартфоны", "Категория смартфонов", [product1, product2])
    assert category.middle_price() == (180000.0 + 210000.0) / 2


def test_category_middle_price_empty():
    """Проверка, что средняя цена равна 0.0, если в категории нет товаров."""
    category = Category("Electronics", "All gadgets", [])
    assert category.middle_price() == 0.0


def test_category_add_product_invalid_type():
    """Проверка, что при передаче не-продукта в add_product выбрасывается TypeError."""
    category = Category("Electronics", "All gadgets", [])

    with pytest.raises(TypeError, match="Ожидается объект Product, получено: str"):
        category.add_product("Not a product")


def test_category_products_property():
    """Проверка свойства products (строковое представление списка товаров)."""
    product1 = Product("A", "Desc", 100.0, 2)
    product2 = Product("B", "Desc", 50.0, 3)
    category = Category("Test", "Desc", [product1, product2])

    expected = "A, 100.0 руб. Остаток: 2 шт.\nB, 50.0 руб. Остаток: 3 шт.\n"
    assert category.products == expected


def test_category_str():
    """Проверка строкового представления категории."""
    product1 = Product("A", "Desc", 100.0, 2)
    product2 = Product("B", "Desc", 50.0, 3)
    category = Category("Electronics", "All gadgets", [product1, product2])

    assert str(category) == "Electronics, количество продуктов: 5 шт."
import pytest
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

def test_product_add_same_type():
    p1 = Product("P1", "", 100.0, 2)
    p2 = Product("P2", "", 50.0, 4)
    assert p1 + p2 == 400.0

def test_product_add_different_type():
    p = Product("P", "", 100.0, 2)
    s = Smartphone("S", "", 200.0, 1, 90.0, "Model", 128, "Black")
    with pytest.raises(TypeError):
        p + s

def test_smartphone_add_same_type():
    s1 = Smartphone("S1", "", 100.0, 2, 90.0, "M1", 128, "Black")
    s2 = Smartphone("S2", "", 50.0, 4, 85.0, "M2", 64, "White")
    assert s1 + s2 == 400.0

def test_lawn_grass_add_same_type():
    g1 = LawnGrass("G1", "", 10.0, 5, "RU", "7 дней", "Green")
    g2 = LawnGrass("G2", "", 5.0, 10, "US", "5 дней", "Dark Green")
    assert g1 + g2 == 100.0

def test_smartphone_add_different_type():
    s = Smartphone("S", "", 100.0, 2, 90.0, "M", 128, "Black")
    g = LawnGrass("G", "", 5.0, 10, "US", "5 дней", "Green")
    with pytest.raises(TypeError):
        s + g

# src/exceptions.py
class ZeroQuantityError(Exception):
    """Исключение для случая добавления товара с нулевым количеством."""
    pass
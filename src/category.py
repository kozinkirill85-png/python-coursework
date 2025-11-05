from typing import List
from .product import Product


class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Автоматическое обновление счётчиков
        Category.category_count += 1
        Category.product_count += len(products)

from typing import List
from .exceptions import ZeroQuantityError
from .product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products.copy() if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        # Проверка типа — если не Product, TypeError вылетит наружу
        if not isinstance(product, Product):
            raise TypeError(f"Ожидается объект Product, получено: {type(product).__name__}")

        try:
            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
            self.__products.append(product)
            print("Товар успешно добавлен.")
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self):
        if not self.__products:
            return 0.0
        total_price = sum(product.price for product in self.__products)
        return total_price / len(self.__products)
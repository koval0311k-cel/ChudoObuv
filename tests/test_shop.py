# ============================================================
# Практическое занятие №8. Модульные тесты для shop.py.
# Файл: tests/test_shop.py
# Запуск: python -m unittest discover -s tests
# ============================================================

import unittest
import sys
import os

# Добавляем корень проекта в sys.path, чтобы импортировать shop.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shop import (
    get_low_stock,
    search_advanced,
    total_sum,
    cart_total,
    add_to_cart,
    remove_from_cart,
    update_quantity,
)


# ============================================================
# Задание 2. Тесты для функций каталога
# ============================================================

class TestGetLowStock(unittest.TestCase):
    """Тесты для функции get_low_stock (3 теста)."""

    def test_empty_list(self):
        """Пустой список товаров — пустой результат."""
        self.assertEqual(get_low_stock([]), [])

    def test_no_low_stock(self):
        """Все товары с достаточным остатком — пустой результат."""
        products = [
            {'name': 'A', 'sizes': {40: 10}},
            {'name': 'B', 'sizes': {41: 5}},
        ]
        self.assertEqual(get_low_stock(products), [])

    def test_one_low_stock(self):
        """Один товар с низким остатком — он и возвращается."""
        products = [
            {'name': 'A', 'sizes': {40: 1}},
            {'name': 'B', 'sizes': {40: 10}},
        ]
        result = get_low_stock(products)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'A')


class TestSearchAdvanced(unittest.TestCase):
    """Тесты для функции search_advanced (3 теста)."""

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом."""
        self.products = [
            {'name': 'Кроссовки Run', 'category': 'Обувь', 'price': 8990.0},
            {'name': 'Кроссовки Trail', 'category': 'Обувь', 'price': 11990.0},
            {'name': 'Футболка Sport', 'category': 'Одежда', 'price': 2490.0},
            {'name': 'Рюкзак City', 'category': 'Аксессуары', 'price': 4590.0},
        ]

    def test_search_by_name_only(self):
        """Поиск только по названию."""
        result = search_advanced(self.products, 'кросс')
        self.assertEqual(len(result), 2)

    def test_search_by_category(self):
        """Поиск по названию + категории."""
        result = search_advanced(self.products, 'кросс', category='Обувь')
        self.assertEqual(len(result), 2)

    def test_search_by_price_range(self):
        """Поиск по названию + диапазону цен."""
        result = search_advanced(
            self.products, 'кросс', min_price=9000, max_price=12000
        )
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['name'], 'Кроссовки Trail')


class TestTotalSum(unittest.TestCase):
    """Тесты для функции total_sum (2 теста)."""

    def test_empty_cart(self):
        """Пустая корзина — сумма 0."""
        self.assertEqual(total_sum([]), 0)

    def test_cart_with_items(self):
        """Корзина с товарами — сумма price * quantity."""
        cart = [
            {'price': 1000, 'quantity': 2},
            {'price': 500, 'quantity': 3},
        ]
        self.assertEqual(total_sum(cart), 3500)


# ============================================================
# Задание 3. Тесты с ожидаемыми ошибками
# ============================================================

class TestAddToCart(unittest.TestCase):
    """Тесты для функции add_to_cart."""

    def test_invalid_size(self):
        """Добавление товара с несуществующим размером."""
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}}]
        cart = []
        result, message = add_to_cart(cart, products, 1, 99, 1)
        self.assertFalse(result)
        self.assertIn('размер', message.lower())

    def test_successful_add(self):
        """Успешное добавление товара."""
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}}]
        cart = []
        result, message = add_to_cart(cart, products, 1, 40, 2)
        self.assertTrue(result)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 2)

    def test_add_existing_increases_quantity(self):
        """Повторное добавление увеличивает количество."""
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}}]
        cart = []
        add_to_cart(cart, products, 1, 40, 2)
        add_to_cart(cart, products, 1, 40, 1)
        self.assertEqual(len(cart), 1)
        self.assertEqual(cart[0]['quantity'], 3)

    def test_exceed_stock(self):
        """Превышение остатка на складе."""
        products = [{'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 2}}]
        cart = []
        result, message = add_to_cart(cart, products, 1, 40, 5)
        self.assertFalse(result)


class TestDivisionByZero(unittest.TestCase):
    """Тест с ожидаемым исключением."""

    def test_division_by_zero(self):
        """Деление на ноль вызывает ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0


# ============================================================
# Задание 5. Тестирование корзины
# ============================================================

class TestCart(unittest.TestCase):
    """Тесты для функций корзины."""

    def setUp(self):
        self.products = [
            {'id': 1, 'name': 'A', 'price': 100, 'sizes': {40: 5}},
            {'id': 2, 'name': 'B', 'price': 200, 'sizes': {41: 3}},
        ]

    def test_remove_from_cart(self):
        """Удаление позиции из корзины."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        result, message = remove_from_cart(cart, 1, 40)
        self.assertTrue(result)
        self.assertEqual(len(cart), 0)

    def test_remove_nonexistent(self):
        """Удаление несуществующей позиции."""
        cart = []
        result, message = remove_from_cart(cart, 99, 99)
        self.assertFalse(result)

    def test_update_quantity(self):
        """Изменение количества."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        result, message = update_quantity(cart, self.products, 1, 40, 4)
        self.assertTrue(result)
        self.assertEqual(cart[0]['quantity'], 4)

    def test_update_quantity_exceed(self):
        """Изменение количества сверх остатка."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)
        result, message = update_quantity(cart, self.products, 1, 40, 100)
        self.assertFalse(result)

    def test_cart_total(self):
        """Подсчёт суммы корзины."""
        cart = []
        add_to_cart(cart, self.products, 1, 40, 2)  # 2 * 100 = 200
        add_to_cart(cart, self.products, 2, 41, 1)  # 1 * 200 = 200
        self.assertEqual(cart_total(cart), 400)

    def test_cart_total_empty(self):
        """Пустая корзина — сумма 0."""
        self.assertEqual(cart_total([]), 0)


# ============================================================
# Запуск
# ============================================================

if __name__ == '__main__':
    unittest.main()
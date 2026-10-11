"""Интеграционные тесты: полный цикл работы магазина."""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.storage import load_products, save_orders, load_orders
from src.cart import add_to_cart, cart_total
from src.orders import create_order


class TestIntegration(unittest.TestCase):
    """Проверка взаимодействия модулей."""

    def setUp(self):
        self.products = load_products('data/products.json')
        self.cart = []
        self.orders_file = 'data/test_orders.json'

    def tearDown(self):
        if os.path.exists(self.orders_file):
            os.remove(self.orders_file)

    def test_full_cycle(self):
        """Полный цикл: каталог → корзина → заказ → JSON → загрузка."""
        # 1. Товары загружены
        self.assertGreater(len(self.products), 0)

        # 2. Добавляем товар в корзину
        result, msg = add_to_cart(self.cart, self.products, 1, 40, 2)
        self.assertTrue(result, msg)
        self.assertEqual(len(self.cart), 1)

        # 3. Создаём заказ
        order = create_order(self.cart, 'Тестовый клиент', self.products)
        self.assertIsNotNone(order)
        self.assertEqual(order['client'], 'Тестовый клиент')
        self.assertGreater(order['total'], 0)

        # 4. Сохраняем заказ в JSON
        save_orders([order], self.orders_file)
        self.assertTrue(os.path.exists(self.orders_file))

        # 5. Загружаем заказ из JSON
        loaded = load_orders(self.orders_file)
        self.assertEqual(len(loaded), 1)

        # 6. Проверяем, что сумма совпадает
        self.assertEqual(loaded[0]['total'], order['total'])

    def test_cart_total_after_order(self):
        """После оформления заказа корзина очищается."""
        add_to_cart(self.cart, self.products, 2, 39, 1)
        self.assertEqual(cart_total(self.cart), 7490.0)

        order = create_order(self.cart, 'Клиент', self.products)
        self.assertIsNotNone(order)
        self.assertEqual(len(self.cart), 0)
        self.assertEqual(cart_total(self.cart), 0)

    def test_order_reduces_stock(self):
        """Оформление заказа уменьшает остатки на складе."""
        product = next(p for p in self.products if p['id'] == 1)
        before = product['sizes'].get(40, 0)

        add_to_cart(self.cart, self.products, 1, 40, 1)
        create_order(self.cart, 'Клиент', self.products)

        after = product['sizes'].get(40, 0)
        self.assertEqual(after, before - 1)


if __name__ == '__main__':
    unittest.main()
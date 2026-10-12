"""Работа с JSON: сохранение и загрузка данных."""

import json
import os


def load_products(filename='data/products.json'):
    """Загружает каталог товаров из JSON."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        products = json.load(f)
    # Преобразуем ключи размеров обратно в int, если возможно
    for p in products:
        new_sizes = {}
        for key, value in p['sizes'].items():
            try:
                new_sizes[int(key)] = value
            except ValueError:
                new_sizes[key] = value
        p['sizes'] = new_sizes
    return products


def save_products(products, filename='data/products.json'):
    """Сохраняет каталог товаров в JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)


def save_orders(orders, filename='data/orders.json'):
    """Сохраняет список заказов в JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)


def load_orders(filename='data/orders.json'):
    """Загружает заказы из JSON."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
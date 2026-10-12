# ============================================================
# Проект «СпортТовары». Отработка Python.
# Файл shop.py — бизнес-логика интернет-магазина.
# Все задания 1–12 выполнены в одном файле.
# ============================================================

import json
import os
from datetime import datetime


# ============================================================
# ЗАДАНИЕ 1. Формирование каталога
# ============================================================

products = [
    {'id': 1, 'name': 'Кроссовки Run', 'category': 'Обувь', 'brand': 'Nike',
     'price': 8990.0, 'sizes': {40: 2, 41: 3, 42: 1}, 'rating': 4.7, 'created_at': '2024-09-15'},
    {'id': 2, 'name': 'Кеды Classic', 'category': 'Обувь', 'brand': 'Adidas',
     'price': 7490.0, 'sizes': {39: 1, 40: 1, 41: 1}, 'rating': 4.5, 'created_at': '2024-09-20'},
    {'id': 3, 'name': 'Футболка Sport', 'category': 'Одежда', 'brand': 'Puma',
     'price': 2490.0, 'sizes': {'S': 5, 'M': 7, 'L': 4}, 'rating': 4.8, 'created_at': '2024-08-10'},
    {'id': 4, 'name': 'Шорты Run', 'category': 'Одежда', 'brand': 'Reebok',
     'price': 1990.0, 'sizes': {'S': 3, 'M': 6, 'L': 2}, 'rating': 4.2, 'created_at': '2024-09-01'},
    {'id': 5, 'name': 'Рюкзак City', 'category': 'Аксессуары', 'brand': 'Nike',
     'price': 4590.0, 'sizes': {'OneSize': 8}, 'rating': 4.6, 'created_at': '2024-09-25'},
    {'id': 6, 'name': 'Кепка Sport', 'category': 'Аксессуары', 'brand': 'Adidas',
     'price': 1590.0, 'sizes': {'OneSize': 12}, 'rating': 4.1, 'created_at': '2024-07-15'},
    {'id': 7, 'name': 'Куртка Wind', 'category': 'Одежда', 'brand': 'The North Face',
     'price': 12990.0, 'sizes': {'M': 2, 'L': 3, 'XL': 1}, 'rating': 4.9, 'created_at': '2024-09-28'},
    {'id': 8, 'name': 'Носки Sport (3 пары)', 'category': 'Аксессуары', 'brand': 'Puma',
     'price': 890.0, 'sizes': {'OneSize': 20}, 'rating': 4.0, 'created_at': '2024-08-20'},
    {'id': 9, 'name': 'Кроссовки Trail', 'category': 'Обувь', 'brand': 'Salomon',
     'price': 11990.0, 'sizes': {41: 2, 42: 2, 43: 1}, 'rating': 4.8, 'created_at': '2024-09-30'},
    {'id': 10, 'name': 'Бутылка для воды', 'category': 'Аксессуары', 'brand': 'Nike',
     'price': 1290.0, 'sizes': {'OneSize': 15}, 'rating': 4.3, 'created_at': '2024-09-05'},
]


# ============================================================
# ЗАДАНИЕ 2. Функции-помощники
# ============================================================

def total_quantity(product):
    """Суммарное количество единиц товара по всем размерам."""
    return sum(product['sizes'].values())


def avg_price(products):
    """Средняя цена по каталогу."""
    if not products:
        return 0.0
    return round(sum(p['price'] for p in products) / len(products), 2)


def get_categories(products):
    """Множество уникальных категорий."""
    return set(p['category'] for p in products)


def get_brands(products):
    """Отсортированный список уникальных брендов."""
    return sorted(set(p['brand'] for p in products))


def is_low_stock(product, threshold=3):
    """True, если общее количество товара ≤ порога."""
    return total_quantity(product) <= threshold


def get_low_stock(products, threshold=3):
    """
    Возвращает список товаров с суммарным количеством ≤ threshold,
    отсортированный по возрастанию количества.
    """
    low = [p for p in products if total_quantity(p) <= threshold]
    return sorted(low, key=lambda p: total_quantity(p))


# ============================================================
# ЗАДАНИЕ 3. Сортировка и топы
# ============================================================

def demo_sorting():
    top_by_price = sorted(products, key=lambda p: p['price'], reverse=True)[:3]
    print("Топ-3 товара по цене:")
    for p in top_by_price:
        print(f"  {p['name']} — {p['price']} руб.")

    sorted_by_rating = sorted(products, key=lambda p: (-p['rating'], p['price']))
    print("\nТовары по рейтингу:")
    for p in sorted_by_rating:
        print(f"  {p['rating']} — {p['name']} ({p['price']} руб.)")

    sorted_by_date = sorted(products,
                            key=lambda p: datetime.strptime(p['created_at'], '%Y-%m-%d'),
                            reverse=True)
    print("\nТовары по дате (сначала новые):")
    for p in sorted_by_date:
        print(f"  {p['created_at']} — {p['name']}")

    sorted_by_name = sorted(products, key=lambda p: p['name'])
    print("\nТовары по алфавиту:")
    for p in sorted_by_name:
        print(f"  {p['name']}")


# ============================================================
# ЗАДАНИЕ 4. Фильтрация
# ============================================================

def demo_filtering():
    cheap_and_high_rated = [p for p in products if p['price'] < 5000 and p['rating'] >= 4.5]
    print("\nТовары дешевле 5000 руб. и с рейтингом ≥ 4.5:")
    for p in cheap_and_high_rated:
        print(f"  {p['name']} — {p['price']} руб.")

    shoes_or_accessories = [p for p in products if p['category'] in ('Обувь', 'Аксессуары')]
    print("\nТовары «Обувь» или «Аксессуары»:")
    for p in shoes_or_accessories:
        print(f"  {p['name']}")

    has_size_42 = [p for p in products if 42 in p['sizes']]
    print("\nТовары с размером 42:")
    for p in has_size_42:
        print(f"  {p['name']}")

    low_stock = get_low_stock(products)
    print("\nТовары с низким остатком:")
    for p in low_stock:
        print(f"  {p['name']} — {total_quantity(p)} шт.")


# ============================================================
# ЗАДАНИЕ 5. Поиск
# ============================================================

def search_by_name(products, query):
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]


def search_by_brand(products, brand):
    brand = brand.lower()
    return [p for p in products if p['brand'].lower() == brand]


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    query = query.lower()
    result = []
    for p in products:
        if query not in p['name'].lower():
            continue
        if category is not None and p['category'] != category:
            continue
        if min_price is not None and p['price'] < min_price:
            continue
        if max_price is not None and p['price'] > max_price:
            continue
        result.append(p)
    return result


def highlight(products):
    return [p['name'] for p in products if total_quantity(p) <= 3]


def demo_search():
    print("\nПоиск 'кросс':")
    for p in search_by_name(products, 'кросс'):
        print(f"  {p['name']}")
    print("\nПоиск бренда 'nike':")
    for p in search_by_brand(products, 'nike'):
        print(f"  {p['name']}")


# ============================================================
# ЗАДАНИЕ 6. Группировка и агрегация
# ============================================================

def count_by_category(products):
    result = {}
    for p in products:
        result[p['category']] = result.get(p['category'], 0) + 1
    return result


def total_stock_by_brand(products):
    result = {}
    for p in products:
        result[p['brand']] = result.get(p['brand'], 0) + total_quantity(p)
    return result


def avg_rating_by_category(products):
    sums = {}
    counts = {}
    for p in products:
        cat = p['category']
        sums[cat] = sums.get(cat, 0) + p['rating']
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(sums[cat] / counts[cat], 2) for cat in sums}


def top_brand_by_stock(products):
    stock = total_stock_by_brand(products)
    if not stock:
        return None
    return max(stock, key=stock.get)


def demo_grouping():
    print("\nКоличество по категориям:")
    for cat, count in count_by_category(products).items():
        print(f"  {cat}: {count}")
    print("\nСток по брендам:")
    for brand, qty in total_stock_by_brand(products).items():
        print(f"  {brand}: {qty}")
    print(f"\nТоп-бренд: {top_brand_by_stock(products)}")


# ============================================================
# ЗАДАНИЕ 7. Корзина
# ============================================================

def find_product_by_id(products, product_id):
    for p in products:
        if p['id'] == product_id:
            return p
    return None


def add_to_cart(cart, products, product_id, size, quantity):
    product = find_product_by_id(products, product_id)
    if product is None:
        return False, f"Товар с id={product_id} не найден"

    if size not in product['sizes']:
        return False, f"Размер {size} отсутствует у товара '{product['name']}'"

    available = product['sizes'][size]
    if quantity <= 0:
        return False, "Количество должно быть больше 0"

    already_in_cart = 0
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            already_in_cart = item['quantity']
            break

    if already_in_cart + quantity > available:
        return False, f"Недостаточно товара. Доступно: {available}"

    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True, "Количество увеличено"

    cart.append({
        'product_id': product_id,
        'name': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity,
    })
    return True, f"Товар '{product['name']}' добавлен"


def remove_from_cart(cart, product_id, size):
    for i, item in enumerate(cart):
        if item['product_id'] == product_id and item['size'] == size:
            cart.pop(i)
            return True, "Позиция удалена"
    return False, "Позиция не найдена"


def update_quantity(cart, products, product_id, size, new_qty):
    product = find_product_by_id(products, product_id)
    if product is None:
        return False, "Товар не найден"
    if size not in product['sizes']:
        return False, f"Размер {size} отсутствует"
    if new_qty <= 0:
        return remove_from_cart(cart, product_id, size)
    if new_qty > product['sizes'][size]:
        return False, f"Недостаточно товара. Доступно: {product['sizes'][size]}"
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] = new_qty
            return True, f"Количество изменено на {new_qty}"
    return False, "Позиция не найдена"


def cart_total(cart):
    return sum(item['price'] * item['quantity'] for item in cart)


def cart_to_string(cart):
    if not cart:
        return "Корзина пуста"
    lines = ["Корзина:"]
    for item in cart:
        lines.append(f"  {item['name']}, размер {item['size']}, "
                     f"{item['quantity']} шт. × {item['price']} = "
                     f"{item['quantity'] * item['price']} руб.")
    lines.append(f"Итого: {cart_total(cart)} руб.")
    return "\n".join(lines)


# ============================================================
# ЗАДАНИЕ 8. Оформление заказа
# ============================================================

orders = []
order_counter = [0]


def create_order(cart, client_name, products):
    if not cart:
        return None
    order_counter[0] += 1
    order_id = order_counter[0]
    items = []
    for item in cart:
        items.append({
            'product_id': item['product_id'],
            'name': item['name'],
            'size': item['size'],
            'quantity': item['quantity'],
            'price': item['price'],
            'sum': item['price'] * item['quantity'],
        })
        product = find_product_by_id(products, item['product_id'])
        if product and item['size'] in product['sizes']:
            product['sizes'][item['size']] -= item['quantity']
            if product['sizes'][item['size']] <= 0:
                del product['sizes'][item['size']]

    order = {
        'order_id': order_id,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'client': client_name,
        'items': items,
        'total': sum(i['sum'] for i in items),
    }
    orders.append(order)
    cart.clear()
    return order


def print_order(order):
    if order is None:
        print("Заказ пуст")
        return
    print(f"Заказ №{order['order_id']} от {order['date']}")
    print(f"Клиент: {order['client']}")
    for item in order['items']:
        print(f"  {item['name']}, размер {item['size']}, "
              f"{item['quantity']} шт. × {item['price']} = {item['sum']} руб.")
    print(f"Итого: {order['total']} руб.")


def demo_cart_and_orders():
    cart = []
    print("\n--- Добавление товаров ---")
    print(add_to_cart(cart, products, 1, 40, 2))
    print(add_to_cart(cart, products, 1, 40, 1))
    print(add_to_cart(cart, products, 1, 99, 1))
    print(add_to_cart(cart, products, 3, 'M', 2))
    print(add_to_cart(cart, products, 3, 'M', 10))
    print("\n" + cart_to_string(cart))

    print("\n--- Изменение количества ---")
    print(update_quantity(cart, products, 1, 40, 5))
    print(update_quantity(cart, products, 3, 'M', 1))
    print("\n" + cart_to_string(cart))

    print("\n--- Удаление позиции ---")
    print(remove_from_cart(cart, 1, 40))
    print("\n" + cart_to_string(cart))

    print("\n--- Оформление заказов ---")
    add_to_cart(cart, products, 1, 41, 2)
    add_to_cart(cart, products, 5, 'OneSize', 1)
    print_order(create_order(cart, 'Иванов И.И.', products))

    add_to_cart(cart, products, 3, 'S', 2)
    add_to_cart(cart, products, 8, 'OneSize', 3)
    print_order(create_order(cart, 'Петров П.П.', products))

    add_to_cart(cart, products, 9, 42, 1)
    add_to_cart(cart, products, 10, 'OneSize', 2)
    print_order(create_order(cart, 'Сидоров С.С.', products))


# ============================================================
# ЗАДАНИЕ 9. Аналитика по заказам
# ============================================================

def orders_by_client(orders, client_name):
    return [o for o in orders if o['client'] == client_name]


def orders_by_period(orders, start_date, end_date):
    result = []
    for o in orders:
        order_date = o['date'][:10]
        if start_date <= order_date <= end_date:
            result.append(o)
    return result


def total_revenue(orders):
    return sum(o['total'] for o in orders)


def best_selling_product(orders):
    counter = {}
    for order in orders:
        for item in order['items']:
            counter[item['name']] = counter.get(item['name'], 0) + item['quantity']
    if not counter:
        return None
    return max(counter, key=counter.get)


def average_order_total(orders):
    if not orders:
        return 0.0
    return round(total_revenue(orders) / len(orders), 2)


def total_sum(products):
    """Сумма цен с учётом количества."""
    return sum(p['price'] * p['quantity'] for p in products)


def demo_analytics():
    print(f"\nВсего заказов: {len(orders)}")
    print(f"Общая выручка: {total_revenue(orders)} руб.")
    print(f"Средняя сумма: {average_order_total(orders)} руб.")
    print(f"Самый продаваемый: {best_selling_product(orders)}")


# ============================================================
# ЗАДАНИЕ 11. JSON
# ============================================================

def save_orders(orders, filename='orders.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)
    print(f"Заказы сохранены в {filename}")


def load_orders(filename='orders.json'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# ============================================================
# ЗАДАНИЕ 12. Валидация
# ============================================================

def safe_int_input(prompt, default=0):
    try:
        return int(input(prompt))
    except ValueError:
        print("Некорректный ввод.")
        return default


# ============================================================
# ЗАДАНИЕ 10. CLI
# ============================================================

def print_menu():
    print("\n" + "=" * 40)
    print("МЕНЮ МАГАЗИНА «СПОРТТОВАРЫ»")
    print("=" * 40)
    print("1 - Показать каталог")
    print("2 - Отфильтровать по категории")
    print("3 - Поиск по названию")
    print("4 - Показать товары с низким остатком")
    print("5 - Добавить в корзину")
    print("6 - Показать корзину")
    print("7 - Оформить заказ")
    print("8 - Показать все заказы")
    print("9 - Аналитика")
    print("0 - Выход")
    print("=" * 40)


def show_catalog():
    print("\n--- КАТАЛОГ ---")
    for p in products:
        print(f"  [{p['id']}] {p['name']} ({p['category']}, {p['brand']}) — "
              f"{p['price']} руб., рейтинг {p['rating']}, "
              f"всего {total_quantity(p)} шт.")


def filter_by_category_cli():
    cat = input("Введите категорию: ").strip()
    filtered = [p for p in products if p['category'].lower() == cat.lower()]
    if not filtered:
        print("Товаров не найдено.")
        return
    for p in filtered:
        print(f"  {p['name']} — {p['price']} руб.")


def search_cli():
    query = input("Введите часть названия: ").strip()
    found = search_by_name(products, query)
    if not found:
        print("Ничего не найдено.")
        return
    for p in found:
        print(f"  [{p['id']}] {p['name']} — {p['price']} руб.")


def low_stock_cli():
    low = get_low_stock(products)
    if not low:
        print("Нет товаров с низким остатком.")
        return
    for p in low:
        print(f"  {p['name']} — {total_quantity(p)} шт.")


def add_to_cart_cli(cart):
    show_catalog()
    pid = safe_int_input("Введите id товара: ")
    product = find_product_by_id(products, pid)
    if product is None:
        print("Товар не найден.")
        return
    print(f"Доступные размеры: {list(product['sizes'].keys())}")
    size_raw = input("Введите размер: ").strip()
    try:
        size = int(size_raw)
    except ValueError:
        size = size_raw
    qty = safe_int_input("Введите количество: ", default=1)
    result, message = add_to_cart(cart, products, pid, size, qty)
    print(message)


def show_cart_cli(cart):
    print("\n" + cart_to_string(cart))


def create_order_cli(cart):
    if not cart:
        print("Корзина пуста.")
        return
    print("\n" + cart_to_string(cart))
    client = input("Введите имя клиента: ").strip() or "Без имени"
    order = create_order(cart, client, products)
    print("\nЗаказ оформлен:")
    print_order(order)


def show_orders_cli():
    if not orders:
        print("Заказов пока нет.")
        return
    for o in orders:
        print_order(o)
        print()


def analytics_cli():
    if not orders:
        print("Заказов нет.")
        return
    print(f"\nВсего заказов: {len(orders)}")
    print(f"Общая выручка: {total_revenue(orders)} руб.")
    print(f"Средняя сумма: {average_order_total(orders)} руб.")
    print(f"Самый продаваемый: {best_selling_product(orders)}")


def main():
    print("Добро пожаловать в магазин «СпортТовары»!")
    cart = []
    while True:
        print_menu()
        choice = safe_int_input("Ваш выбор: ", default=-1)
        if choice == 1:
            show_catalog()
        elif choice == 2:
            filter_by_category_cli()
        elif choice == 3:
            search_cli()
        elif choice == 4:
            low_stock_cli()
        elif choice == 5:
            add_to_cart_cli(cart)
        elif choice == 6:
            show_cart_cli(cart)
        elif choice == 7:
            create_order_cli(cart)
        elif choice == 8:
            show_orders_cli()
        elif choice == 9:
            analytics_cli()
        elif choice == 0:
            if orders:
                save_orders(orders)
            print("До свидания!")
            break
        else:
            print("Неверный пункт.")


# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == '__main__':
    # Раскомментируй нужное для демонстрации заданий 3–9:
    # demo_sorting()
    # demo_filtering()
    # demo_search()
    # demo_grouping()
    # demo_cart_and_orders()
    # demo_analytics()

    # Запуск CLI (Задание 10):
    main()
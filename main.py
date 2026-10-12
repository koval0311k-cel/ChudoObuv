"""Главный файл приложения «СпортТовары».

Использует модули из src/ для работы с каталогом, корзиной, заказами и аналитикой.
"""

from src.storage import load_products, save_orders, load_orders
from src.catalog import (
    get_low_stock, search_by_name, search_advanced,
    total_quantity, count_by_category, avg_rating_by_category,
    top_brand_by_stock,
)
from src.cart import (
    add_to_cart, remove_from_cart, update_quantity,
    cart_total, cart_to_string, find_product_by_id,
)
from src.orders import create_order, print_order
from src.analytics import total_revenue, best_selling_product, average_order_total


# ---------- Глобальные данные ----------

products = load_products('data/products.json')
orders = load_orders('data/orders.json')
cart = []


# ---------- CLI ----------

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


def safe_int_input(prompt, default=0):
    try:
        return int(input(prompt))
    except ValueError:
        print("Некорректный ввод.")
        return default


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


def add_to_cart_cli():
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


def show_cart_cli():
    print("\n" + cart_to_string(cart))


def create_order_cli():
    if not cart:
        print("Корзина пуста.")
        return
    print("\n" + cart_to_string(cart))
    client = input("Введите имя клиента: ").strip() or "Без имени"
    order = create_order(cart, client, products)
    orders.append(order)
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
            add_to_cart_cli()
        elif choice == 6:
            show_cart_cli()
        elif choice == 7:
            create_order_cli()
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


if __name__ == '__main__':
    main()
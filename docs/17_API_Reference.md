API Reference — Справочник функций проекта «СпортТовары»
Дата: [9-10-2026]
Автор: [Коваль Андрей Михайлович]

Модуль src/catalog.py
total_quantity(product)
Суммарное количество единиц товара по всем размерам.

Параметры:

product (dict) — словарь товара с ключом sizes.

Возвращает:

int — сумма значений словаря sizes.

Пример:
product = {'name': 'A', 'sizes': {40: 2, 41: 3}}
print(total_quantity(product)) # 5

avg_price(products)
Средняя цена по каталогу, округлённая до 2 знаков.

Параметры:

products (list[dict]).

Возвращает:

float.

Пример:
print(avg_price(products)) # 5430.0

get_categories(products)
Множество уникальных категорий.

Параметры:

products (list[dict]).

Возвращает:

set[str].

Пример:
print(get_categories(products)) # {'Обувь', 'Одежда', 'Аксессуары'}

get_brands(products)
Отсортированный список уникальных брендов.

Параметры:

products (list[dict]).

Возвращает:

list[str].

Пример:
print(get_brands(products))

is_low_stock(product, threshold=3)
Проверка: является ли товар низким по остатку.

Параметры:

product (dict).

threshold (int, по умолчанию 3).

Возвращает:

bool.

Пример:
print(is_low_stock({'sizes': {40: 1}})) # True

get_low_stock(products, threshold=3)
Список товаров с низким остатком, отсортированный по возрастанию количества.

Параметры:

products (list[dict]).

threshold (int, по умолчанию 3).

Возвращает:

list[dict].

Пример:
low = get_low_stock(products)
for p in low:
print(p['name'])

search_by_name(products, query)
Поиск товаров по подстроке в названии.

Параметры:

products (list[dict]).

query (str).

Возвращает:

list[dict].

Пример:
result = search_by_name(products, 'кросс')

search_by_brand(products, brand)
Поиск товаров по бренду.

Параметры:

products (list[dict]).

brand (str).

Возвращает:

list[dict].

Пример:
result = search_by_brand(products, 'nike')

search_advanced(products, query, category=None, min_price=None, max_price=None)
Комбинированный поиск с опциональными фильтрами.

Параметры:

products (list[dict]).

query (str).

category (str | None, по умолчанию None).

min_price (float | None, по умолчанию None).

max_price (float | None, по умолчанию None).

Возвращает:

list[dict].

Пример:
result = search_advanced(products, 'кросс', category='Обувь', min_price=8000)

highlight(products)
Список названий товаров с низким остатком.

Параметры:

products (list[dict]).

Возвращает:

list[str].

Пример:
print(highlight(products))

count_by_category(products)
Словарь {категория: количество товаров}.

Параметры:

products (list[dict]).

Возвращает:

dict[str, int].

Пример:
print(count_by_category(products))

total_stock_by_brand(products)
Словарь {бренд: суммарное количество единиц}.

Параметры:

products (list[dict]).

Возвращает:

dict[str, int].

Пример:
print(total_stock_by_brand(products))

avg_rating_by_category(products)
Словарь {категория: средний рейтинг}.

Параметры:

products (list[dict]).

Возвращает:

dict[str, float].

Пример:
print(avg_rating_by_category(products))

top_brand_by_stock(products)
Бренд с наибольшим суммарным количеством единиц.

Параметры:

products (list[dict]).

Возвращает:

str | None.

Пример:
print(top_brand_by_stock(products)) # 'Puma'

Модуль src/cart.py
find_product_by_id(products, product_id)
Находит товар по id.

Параметры:

products (list[dict]).

product_id (int).

Возвращает:

dict | None.

Пример:
p = find_product_by_id(products, 1)

add_to_cart(cart, products, product_id, size, quantity)
Добавляет товар в корзину с проверками.

Параметры:

cart (list[dict]).

products (list[dict]).

product_id (int).

size (int | str).

quantity (int).

Возвращает:

tuple[bool, str].

Пример:
result, msg = add_to_cart(cart, products, 1, 40, 2)

Возможные ошибки:

Товар не найден.

Размер отсутствует.

Количество ≤ 0.

Недостаточно товара.

remove_from_cart(cart, product_id, size)
Удаляет позицию из корзины.

Параметры:

cart (list[dict]).

product_id (int).

size (int | str).

Возвращает:

tuple[bool, str].

Пример:
result, msg = remove_from_cart(cart, 1, 40)

update_quantity(cart, products, product_id, size, new_qty)
Изменяет количество с проверкой остатка.

Параметры:

cart (list[dict]).

products (list[dict]).

product_id (int).

size (int | str).

new_qty (int).

Возвращает:

tuple[bool, str].

Пример:
result, msg = update_quantity(cart, products, 1, 40, 5)

cart_total(cart)
Сумма позиций корзины.

Параметры:

cart (list[dict]).

Возвращает:

float.

Пример:
print(cart_total(cart))

cart_to_string(cart)
Многострочное текстовое представление корзины.

Параметры:

cart (list[dict]).

Возвращает:

str.

Пример:
print(cart_to_string(cart))

Модуль src/orders.py
create_order(cart, client_name, products)
Превращает корзину в заказ. Уменьшает остатки. Очищает корзину.

Параметры:

cart (list[dict]).

client_name (str).

products (list[dict]).

Возвращает:

dict | None.

Пример:
order = create_order(cart, 'Иванов И.И.', products)

print_order(order)
Печатает заказ в консоль.

Параметры:

order (dict | None).

Возвращает:

Ничего.

Пример:
print_order(order)

orders_by_client(orders, client_name)
Список заказов клиента.

Параметры:

orders (list[dict]).

client_name (str).

Возвращает:

list[dict].

Пример:
print(orders_by_client(orders, 'Иванов И.И.'))

orders_by_period(orders, start_date, end_date)
Заказы за период (YYYY-MM-DD).

Параметры:

orders (list[dict]).

start_date (str).

end_date (str).

Возвращает:

list[dict].

Пример:
print(orders_by_period(orders, '2026-01-01', '2026-12-31'))

Модуль src/analytics.py
total_revenue(orders)
Общая выручка по всем заказам.

Параметры:

orders (list[dict]).

Возвращает:

float.

Пример:
print(total_revenue(orders))

best_selling_product(orders)
Товар, который чаще всего заказывали.

Параметры:

orders (list[dict]).

Возвращает:

str | None.

Пример:
print(best_selling_product(orders))

average_order_total(orders)
Средняя сумма заказа.

Параметры:

orders (list[dict]).

Возвращает:

float.

Пример:
print(average_order_total(orders))

total_sum(products)
Сумма цен с учётом количества.

Параметры:

products (list[dict]).

Возвращает:

float.

Пример:
print(total_sum(cart))

Модуль src/storage.py
load_products(filename='data/products.json')
Загружает каталог товаров из JSON.

Параметры:

filename (str, по умолчанию 'data/products.json').

Возвращает:

list[dict].

Пример:
products = load_products()

save_products(products, filename='data/products.json')
Сохраняет каталог товаров в JSON.

Параметры:

products (list[dict]).

filename (str, по умолчанию 'data/products.json').

Возвращает:

Ничего.

Пример:
save_products(products)

save_orders(orders, filename='data/orders.json')
Сохраняет список заказов в JSON.

Параметры:

orders (list[dict]).

filename (str, по умолчанию 'data/orders.json').

Возвращает:

Ничего.

Пример:
save_orders(orders)

load_orders(filename='data/orders.json')
Загружает заказы из JSON.

Параметры:

filename (str, по умолчанию 'data/orders.json').

Возвращает:

list[dict].

Пример:
orders = load_orders()
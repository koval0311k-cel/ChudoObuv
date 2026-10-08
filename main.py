# ============================================================
# Практическая работа №5. Основы Python в VS Code.
# Структуры данных для предметной области «Чудо Обувь»
# ============================================================

# ---------- Задание 1. Первая программа ----------
print("Приложение Чудо обувь запущено")
print("Добро пожаловать!")


# ---------- Задание 2. Переменные, print, for ----------

# Объявляем переменные разных типов
login = "admin"
last_name = "Админов"
price = 8990.0
quantity = 5
in_stock = True

# Выводим их через print
print("логин:", login)
print("Фамилия:", last_name)
print("Цена:", price, "руб.")
print("Количество:", quantity)
print("В наличии:", in_stock)

# Список размеров и перебор через for
sizes = [36.0, 37.0, 38.0, 39.0]

print("\nДоступные размеры:")
for size in sizes:
    print("-", size)

# Перебор через range с индексами
print("\nНомера по порядку:")
for i in range(len(sizes)):
    print(i + 1, "-", sizes[i])

# Условие if / elif / else
if quantity <= 3:
    print("\nМало на складе")
elif quantity <= 10:
    print("\nДостаточно на складе")
else:
    print("\nМного на складе")


# ---------- Задание 3. Списки и словари ----------

# Список словарей — пользователи системы
users = [
    {'login': 'admin', 'last_name': 'Админов', 'role': 'администратор'},
    {'login': 'manager', 'last_name': 'Менеджеров', 'role': 'менеджер'},
    {'login': 'user', 'last_name': 'Пользователев', 'role': 'авторизованный'},
]

print("\nПользователи системы:")
for u in users:
    print(f"Логин: {u['login']}, фамилия: {u['last_name']}, роль: {u['role']}")

# Список словарей — каталог товаров
products = [
    {
        'id': 1,
        'name': 'Air Max',
        'price': 8990.0,
        'quantity': 5,
        'sizes': {36.0: 1, 37.0: 2, 38.0: 2},
    },
    {
        'id': 2,
        'name': 'Superstar',
        'price': 7490.0,
        'quantity': 3,
        'sizes': {37.0: 1, 38.0: 1, 39.0: 1},
    },
    {
        'id': 3,
        'name': 'Runfalcon',
        'price': 5990.0,
        'quantity': 10,
        'sizes': {36.0: 3, 37.0: 4, 38.0: 3},
    },
]

print("\nКаталог товаров:")
for p in products:
    total = sum(p['sizes'].values())
    print(f"{p['name']} — {p['price']} руб., всего на складе: {total} шт.")


# ---------- Задание 4. Функции ----------

def find_user(login):
    """Ищет пользователя по логину. Возвращает словарь или None."""
    for u in users:
        if u['login'] == login:
            return u
    return None


def total_sum(items):
    """Считает итоговую сумму заказа: цена * количество по каждой позиции."""
    total = 0
    for item in items:
        total += item['price'] * item['quantity']
    return total


# Проверяем find_user
result = find_user('admin')
if result:
    print(f"\nНайден пользователь: {result['last_name']}")
else:
    print("\nПользователь не найден")

# Проверяем total_sum на корзине
cart = [
    {'name': 'Air Max', 'price': 8990.0, 'quantity': 2},
    {'name': 'Superstar', 'price': 7490.0, 'quantity': 1},
]

print(f"\nИтоговая сумма заказа: {total_sum(cart)} руб.")


# ---------- Задание 5. Сортировка и фильтрация ----------

# Сортировка по цене (возрастание)
sorted_by_price = sorted(products, key=lambda p: p['price'])
print("\nТовары по возрастанию цены:")
for p in sorted_by_price:
    print(f"{p['name']} - {p['price']} руб.")

# Фильтрация товаров с низким остатком (≤ 3 шт.)
low_stock = [p for p in products if sum(p['sizes'].values()) <= 3]
print("\nТовары с низким остатком (≤ 3 шт.):")
for p in low_stock:
    print(p['name'])


# ---------- Задание 6. Поиск по каталогу ----------

def search_products(query):
    """Поиск товаров по подстроке в названии (без учёта регистра)."""
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]


def filter_by_price(products, min_price, max_price):
    """Фильтр товаров по диапазону цен."""
    return [p for p in products if min_price <= p['price'] <= max_price]


# Проверяем поиск
found = search_products('max')
print("\nРезультаты поиска 'max':")
for p in found:
    print(p['name'])

# Проверяем фильтр по цене
result = filter_by_price(products, 5000, 8000)
print("\nТовары от 5000 до 8000 руб.:")
for p in result:
    print(f"{p['name']} — {p['price']} руб.")


# ---------- Задание 7. Мини-задача «Корзина» ----------

def add_to_cart(cart, product, size, quantity):
    """Добавляет товар в корзину."""
    cart.append({
        'product': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity,
    })


def remove_from_cart(cart, name):
    """Удаляет все позиции с указанным названием товара."""
    cart[:] = [item for item in cart if item['product'] != name]


def change_quantity(cart, name, new_qty):
    """Меняет количество для позиции с указанным названием."""
    for item in cart:
        if item['product'] == name:
            item['quantity'] = new_qty
            break


# Собираем корзину
cart = []
add_to_cart(cart, products[0], 36.0, 2)   # Air Max
add_to_cart(cart, products[1], 37.0, 1)   # Superstar

print("\nКорзина:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, "
          f"{item['quantity']} шт. × {item['price']} = "
          f"{item['quantity'] * item['price']} руб.")

print(f"\nИтого: {total_sum(cart)} руб.")

# Меняем количество и удаляем позицию
change_quantity(cart, 'Air Max', 3)
remove_from_cart(cart, 'Superstar')

print("\nПосле изменений:")
for item in cart:
    print(f"{item['product']}, размер {item['size']}, {item['quantity']} шт.")
print(f"Итого: {total_sum(cart)} руб.")


# ---------- Задание 8. Самостоятельно ----------

# 1. Добавляем ещё два товара в каталог
products.append({
    'id': 4,
    'name': 'Pegasus',
    'price': 9990.0,
    'quantity': 4,
    'sizes': {38.0: 2, 39.0: 2},
})
products.append({
    'id': 5,
    'name': 'Ultraboost',
    'price': 11990.0,
    'quantity': 6,
    'sizes': {40.0: 3, 41.0: 3},
})


# 2. Функция get_sizes(product) — список доступных размеров
def get_sizes(product):
    """Возвращает список доступных размеров товара."""
    return list(product['sizes'].keys())


# 3. Функция get_total_quantity(product) — общее количество единиц
def get_total_quantity(product):
    """Возвращает суммарное количество единиц товара по всем размерам."""
    return sum(product['sizes'].values())


# 4. Сортировка товаров по названию (алфавит)
print("\nТовары по алфавиту:")
for p in sorted(products, key=lambda p: p['name']):
    print(p['name'])


# 5. Фильтр товаров дешевле 6000 руб.
cheap = [p for p in products if p['price'] < 6000]
print("\nТовары дешевле 6000 руб.:")
for p in cheap:
    print(f"{p['name']} — {p['price']} руб.")


# 6. Вывод всех товаров через while
print("\nВсе товары (через while):")
i = 0
while i < len(products):
    p = products[i]
    print(f"{p['name']} — {p['price']} руб., "
          f"размеры: {get_sizes(p)}, всего: {get_total_quantity(p)} шт.")
    i += 1
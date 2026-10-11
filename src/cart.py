"""Работа с корзиной."""


def find_product_by_id(products, product_id):
    """Находит товар по id."""
    for p in products:
        if p['id'] == product_id:
            return p
    return None


def add_to_cart(cart, products, product_id, size, quantity):
    """Добавляет товар в корзину с проверками."""
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
    """Удаляет позицию из корзины."""
    for i, item in enumerate(cart):
        if item['product_id'] == product_id and item['size'] == size:
            cart.pop(i)
            return True, "Позиция удалена"
    return False, "Позиция не найдена"


def update_quantity(cart, products, product_id, size, new_qty):
    """Изменяет количество с проверкой остатка."""
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
    """Сумма позиций корзины."""
    return sum(item['price'] * item['quantity'] for item in cart)


def cart_to_string(cart):
    """Многострочное представление корзины."""
    if not cart:
        return "Корзина пуста"
    lines = ["Корзина:"]
    for item in cart:
        lines.append(f"  {item['name']}, размер {item['size']}, "
                     f"{item['quantity']} шт. × {item['price']} = "
                     f"{item['quantity'] * item['price']} руб.")
    lines.append(f"Итого: {cart_total(cart)} руб.")
    return "\n".join(lines)
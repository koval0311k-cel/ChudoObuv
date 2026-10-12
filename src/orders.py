"""Работа с заказами."""

from datetime import datetime
from src.cart import find_product_by_id


def create_order(cart, client_name, products):
    """Превращает корзину в заказ. Уменьшает остатки."""
    if not cart:
        return None

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
        'order_id': int(datetime.now().timestamp()),
        'date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'client': client_name,
        'items': items,
        'total': sum(i['sum'] for i in items),
    }
    cart.clear()
    return order


def print_order(order):
    """Печатает заказ."""
    if order is None:
        print("Заказ пуст")
        return
    print(f"Заказ №{order['order_id']} от {order['date']}")
    print(f"Клиент: {order['client']}")
    for item in order['items']:
        print(f"  {item['name']}, размер {item['size']}, "
              f"{item['quantity']} шт. × {item['price']} = {item['sum']} руб.")
    print(f"Итого: {order['total']} руб.")


def orders_by_client(orders, client_name):
    """Список заказов клиента."""
    return [o for o in orders if o['client'] == client_name]


def orders_by_period(orders, start_date, end_date):
    """Заказы за период (YYYY-MM-DD)."""
    result = []
    for o in orders:
        order_date = o['date'][:10]
        if start_date <= order_date <= end_date:
            result.append(o)
    return result
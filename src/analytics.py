"""Аналитика по заказам."""


def total_revenue(orders):
    """Общая выручка по всем заказам."""
    return sum(o['total'] for o in orders)


def best_selling_product(orders):
    """Товар, который чаще всего заказывали."""
    counter = {}
    for order in orders:
        for item in order['items']:
            counter[item['name']] = counter.get(item['name'], 0) + item['quantity']
    if not counter:
        return None
    return max(counter, key=counter.get)


def average_order_total(orders):
    """Средняя сумма заказа."""
    if not orders:
        return 0.0
    return round(total_revenue(orders) / len(orders), 2)


def total_sum(products):
    """Сумма цен с учётом количества."""
    return sum(p['price'] * p['quantity'] for p in products)
# Hotfix: cart-total

**Дата:** [6-10-2026]
**Автор:** [Коваль Андрей Михайлович]

---

## Что было сломано

Функция `cart_total` в ветке `main` возвращала неверную сумму заказа.
Вместо `price * quantity` она возвращала только `price`.

---

## Как исправлено

Функция `cart_total` приведена к правильному виду:

```python
def cart_total(cart):
    """Сумма позиций корзины."""
    return sum(item['price'] * item['quantity'] for item in cart)
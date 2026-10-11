
---

## Файл 2. `docs/16_Integration_Report.md`

```markdown
# Отчёт об интеграции модулей

**Дата:** [8-10-2026]
**Команда:** [Коваль Андрей Михайлович]

---

## Какие модули были выделены

Проект разбит на модули в папке `src/`:

| Модуль | Назначение |
|--------|------------|
| `src/catalog.py` | Работа с каталогом: поиск, фильтрация, группировка |
| `src/cart.py` | Корзина: добавление, удаление, изменение количества |
| `src/orders.py` | Заказы: создание, печать, выборка по клиенту и периоду |
| `src/analytics.py` | Аналитика: выручка, топ-товар, средняя сумма заказа |
| `src/storage.py` | Работа с JSON: сохранение и загрузка товаров и заказов |
| `src/__init__.py` | Пустой файл для пакета |

**Данные:** `data/products.json` — каталог товаров.

---

## Какие импорты используются

В `main.py`:
```python
from src.storage import load_products, save_orders, load_orders
from src.catalog import get_low_stock, search_by_name, total_quantity
from src.cart import add_to_cart, cart_total, cart_to_string
from src.orders import create_order, print_order
from src.analytics import total_revenue, best_selling_product
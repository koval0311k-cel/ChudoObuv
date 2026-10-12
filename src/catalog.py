"""Работа с каталогом товаров."""


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
    """Список товаров с низким остатком, отсортированный по возрастанию."""
    low = [p for p in products if total_quantity(p) <= threshold]
    return sorted(low, key=lambda p: total_quantity(p))


def search_by_name(products, query):
    """Поиск по подстроке в названии."""
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]


def search_by_brand(products, brand):
    """Поиск по бренду."""
    brand = brand.lower()
    return [p for p in products if p['brand'].lower() == brand]


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """Комбинированный поиск."""
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
    """Названия товаров с низким остатком."""
    return [p['name'] for p in products if total_quantity(p) <= 3]


def count_by_category(products):
    """Словарь {категория: количество товаров}."""
    result = {}
    for p in products:
        result[p['category']] = result.get(p['category'], 0) + 1
    return result


def total_stock_by_brand(products):
    """Словарь {бренд: суммарное количество единиц}."""
    result = {}
    for p in products:
        result[p['brand']] = result.get(p['brand'], 0) + total_quantity(p)
    return result


def avg_rating_by_category(products):
    """Словарь {категория: средний рейтинг}."""
    sums = {}
    counts = {}
    for p in products:
        cat = p['category']
        sums[cat] = sums.get(cat, 0) + p['rating']
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(sums[cat] / counts[cat], 2) for cat in sums}


def top_brand_by_stock(products):
    """Бренд с наибольшим суммарным количеством единиц."""
    stock = total_stock_by_brand(products)
    if not stock:
        return None
    return max(stock, key=stock.get)
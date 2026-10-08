# ============================================================
# РџСЂРѕРµРєС‚ В«РЎРїРѕСЂС‚РўРѕРІР°СЂС‹В». РћС‚СЂР°Р±РѕС‚РєР° Python.
# Р¤Р°Р№Р» shop.py вЂ” Р±РёР·РЅРµСЃ-Р»РѕРіРёРєР° РёРЅС‚РµСЂРЅРµС‚-РјР°РіР°Р·РёРЅР°.
# Р’СЃРµ Р·Р°РґР°РЅРёСЏ 1вЂ“12 РІС‹РїРѕР»РЅРµРЅС‹ РІ РѕРґРЅРѕРј С„Р°Р№Р»Рµ (РєР°Рє С‚СЂРµР±СѓРµС‚ Р·Р°РґР°РЅРёРµ).
# ============================================================

import json
import os
from datetime import datetime


# ============================================================
# Р—РђР”РђРќРР• 1. Р¤РѕСЂРјРёСЂРѕРІР°РЅРёРµ РєР°С‚Р°Р»РѕРіР°
# ============================================================

products = [
    {
        'id': 1,
        'name': 'РљСЂРѕСЃСЃРѕРІРєРё Run',
        'category': 'РћР±СѓРІСЊ',
        'brand': 'Nike',
        'price': 8990.0,
        'sizes': {40: 2, 41: 3, 42: 1},
        'rating': 4.7,
        'created_at': '2024-09-15',
    },
    {
        'id': 2,
        'name': 'РљРµРґС‹ Classic',
        'category': 'РћР±СѓРІСЊ',
        'brand': 'Adidas',
        'price': 7490.0,
        'sizes': {39: 1, 40: 1, 41: 1},
        'rating': 4.5,
        'created_at': '2024-09-20',
    },
    {
        'id': 3,
        'name': 'Р¤СѓС‚Р±РѕР»РєР° Sport',
        'category': 'РћРґРµР¶РґР°',
        'brand': 'Puma',
        'price': 2490.0,
        'sizes': {'S': 5, 'M': 7, 'L': 4},
        'rating': 4.8,
        'created_at': '2024-08-10',
    },
    {
        'id': 4,
        'name': 'РЁРѕСЂС‚С‹ Run',
        'category': 'РћРґРµР¶РґР°',
        'brand': 'Reebok',
        'price': 1990.0,
        'sizes': {'S': 3, 'M': 6, 'L': 2},
        'rating': 4.2,
        'created_at': '2024-09-01',
    },
    {
        'id': 5,
        'name': 'Р СЋРєР·Р°Рє City',
        'category': 'РђРєСЃРµСЃСЃСѓР°СЂС‹',
        'brand': 'Nike',
        'price': 4590.0,
        'sizes': {'OneSize': 8},
        'rating': 4.6,
        'created_at': '2024-09-25',
    },
    {
        'id': 6,
        'name': 'РљРµРїРєР° Sport',
        'category': 'РђРєСЃРµСЃСЃСѓР°СЂС‹',
        'brand': 'Adidas',
        'price': 1590.0,
        'sizes': {'OneSize': 12},
        'rating': 4.1,
        'created_at': '2024-07-15',
    },
    {
        'id': 7,
        'name': 'РљСѓСЂС‚РєР° Wind',
        'category': 'РћРґРµР¶РґР°',
        'brand': 'The North Face',
        'price': 12990.0,
        'sizes': {'M': 2, 'L': 3, 'XL': 1},
        'rating': 4.9,
        'created_at': '2024-09-28',
    },
    {
        'id': 8,
        'name': 'РќРѕСЃРєРё Sport (3 РїР°СЂС‹)',
        'category': 'РђРєСЃРµСЃСЃСѓР°СЂС‹',
        'brand': 'Puma',
        'price': 890.0,
        'sizes': {'OneSize': 20},
        'rating': 4.0,
        'created_at': '2024-08-20',
    },
    {
        'id': 9,
        'name': 'РљСЂРѕСЃСЃРѕРІРєРё Trail',
        'category': 'РћР±СѓРІСЊ',
        'brand': 'Salomon',
        'price': 11990.0,
        'sizes': {41: 2, 42: 2, 43: 1},
        'rating': 4.8,
        'created_at': '2024-09-30',
    },
    {
        'id': 10,
        'name': 'Р‘СѓС‚С‹Р»РєР° РґР»СЏ РІРѕРґС‹',
        'category': 'РђРєСЃРµСЃСЃСѓР°СЂС‹',
        'brand': 'Nike',
        'price': 1290.0,
        'sizes': {'OneSize': 15},
        'rating': 4.3,
        'created_at': '2024-09-05',
    },
]


# ============================================================
# Р—РђР”РђРќРР• 2. Р¤СѓРЅРєС†РёРё-РїРѕРјРѕС‰РЅРёРєРё
# ============================================================

def total_quantity(product):
    """РЎСѓРјРјР°СЂРЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ РµРґРёРЅРёС† С‚РѕРІР°СЂР° РїРѕ РІСЃРµРј СЂР°Р·РјРµСЂР°Рј."""
    return sum(product['sizes'].values())


def avg_price(products):
    """РЎСЂРµРґРЅСЏСЏ С†РµРЅР° РїРѕ РєР°С‚Р°Р»РѕРіСѓ, РѕРєСЂСѓРіР»С‘РЅРЅР°СЏ РґРѕ 2 Р·РЅР°РєРѕРІ."""
    if not products:
        return 0.0
    return round(sum(p['price'] for p in products) / len(products), 2)


def get_categories(products):
    """РњРЅРѕР¶РµСЃС‚РІРѕ СѓРЅРёРєР°Р»СЊРЅС‹С… РєР°С‚РµРіРѕСЂРёР№."""
    return set(p['category'] for p in products)


def get_brands(products):
    """РћС‚СЃРѕСЂС‚РёСЂРѕРІР°РЅРЅС‹Р№ СЃРїРёСЃРѕРє СѓРЅРёРєР°Р»СЊРЅС‹С… Р±СЂРµРЅРґРѕРІ."""
    return sorted(set(p['brand'] for p in products))


def is_low_stock(product, threshold=3):
    """True, РµСЃР»Рё РѕР±С‰РµРµ РєРѕР»РёС‡РµСЃС‚РІРѕ С‚РѕРІР°СЂР° в‰¤ РїРѕСЂРѕРіР°."""
    return total_quantity(product) <= threshold


# ============================================================
# Р—РђР”РђРќРР• 3. РЎРѕСЂС‚РёСЂРѕРІРєР° Рё С‚РѕРїС‹
# ============================================================

def demo_sorting():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ СЃРѕСЂС‚РёСЂРѕРІРѕРє (Р·Р°РґР°РЅРёРµ 3)."""
    # 3.1. РўРѕРї-3 РїРѕ С†РµРЅРµ (СѓР±С‹РІР°РЅРёРµ)
    top_by_price = sorted(products, key=lambda p: p['price'], reverse=True)[:3]
    print("РўРѕРї-3 С‚РѕРІР°СЂР° РїРѕ С†РµРЅРµ:")
    for p in top_by_price:
        print(f"  {p['name']} вЂ” {p['price']} СЂСѓР±.")

    # 3.2. РЎРѕСЂС‚РёСЂРѕРІРєР° РїРѕ СЂРµР№С‚РёРЅРіСѓ (СѓР±С‹РІР°РЅРёРµ), РїСЂРё СЂР°РІРµРЅСЃС‚РІРµ вЂ” РїРѕ С†РµРЅРµ (РІРѕР·СЂР°СЃС‚Р°РЅРёРµ)
    sorted_by_rating = sorted(products, key=lambda p: (-p['rating'], p['price']))
    print("\nРўРѕРІР°СЂС‹ РїРѕ СЂРµР№С‚РёРЅРіСѓ (РїСЂРё СЂР°РІРµРЅСЃС‚РІРµ вЂ” РїРѕ С†РµРЅРµ):")
    for p in sorted_by_rating:
        print(f"  {p['rating']} вЂ” {p['name']} ({p['price']} СЂСѓР±.)")

    # 3.3. РЎРѕСЂС‚РёСЂРѕРІРєР° РїРѕ РґР°С‚Рµ РїРѕСЃС‚СѓРїР»РµРЅРёСЏ: СЃРЅР°С‡Р°Р»Р° РЅРѕРІС‹Рµ
    sorted_by_date = sorted(
        products,
        key=lambda p: datetime.strptime(p['created_at'], '%Y-%m-%d'),
        reverse=True,
    )
    print("\nРўРѕРІР°СЂС‹ РїРѕ РґР°С‚Рµ РїРѕСЃС‚СѓРїР»РµРЅРёСЏ (СЃРЅР°С‡Р°Р»Р° РЅРѕРІС‹Рµ):")
    for p in sorted_by_date:
        print(f"  {p['created_at']} вЂ” {p['name']}")

    # 3.4. РЎРѕСЂС‚РёСЂРѕРІРєР° РїРѕ РЅР°Р·РІР°РЅРёСЋ (Р°Р»С„Р°РІРёС‚)
    sorted_by_name = sorted(products, key=lambda p: p['name'])
    print("\nРўРѕРІР°СЂС‹ РїРѕ Р°Р»С„Р°РІРёС‚Сѓ:")
    for p in sorted_by_name:
        print(f"  {p['name']}")


# ============================================================
# Р—РђР”РђРќРР• 4. Р¤РёР»СЊС‚СЂР°С†РёСЏ
# ============================================================

def demo_filtering():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ С„РёР»СЊС‚СЂР°С†РёРё (Р·Р°РґР°РЅРёРµ 4)."""
    # 4.1. РўРѕРІР°СЂС‹ РґРµС€РµРІР»Рµ 5000 СЂСѓР±. Рё СЃ СЂРµР№С‚РёРЅРіРѕРј в‰Ґ 4.5
    cheap_and_high_rated = [
        p for p in products
        if p['price'] < 5000 and p['rating'] >= 4.5
    ]
    print("\nРўРѕРІР°СЂС‹ РґРµС€РµРІР»Рµ 5000 СЂСѓР±. Рё СЃ СЂРµР№С‚РёРЅРіРѕРј в‰Ґ 4.5:")
    for p in cheap_and_high_rated:
        print(f"  {p['name']} вЂ” {p['price']} СЂСѓР±., СЂРµР№С‚РёРЅРі {p['rating']}")

    # 4.2. РўРѕРІР°СЂС‹ РєР°С‚РµРіРѕСЂРёРё В«РћР±СѓРІСЊВ» РёР»Рё В«РђРєСЃРµСЃСЃСѓР°СЂС‹В»
    shoes_or_accessories = [
        p for p in products
        if p['category'] in ('РћР±СѓРІСЊ', 'РђРєСЃРµСЃСЃСѓР°СЂС‹')
    ]
    print("\nРўРѕРІР°СЂС‹ РєР°С‚РµРіРѕСЂРёР№ В«РћР±СѓРІСЊВ» РёР»Рё В«РђРєСЃРµСЃСЃСѓР°СЂС‹В»:")
    for p in shoes_or_accessories:
        print(f"  {p['name']} ({p['category']})")

    # 4.3. РўРѕРІР°СЂС‹, Сѓ РєРѕС‚РѕСЂС‹С… РµСЃС‚СЊ СЂР°Р·РјРµСЂ 42
    has_size_42 = [p for p in products if 42 in p['sizes']]
    print("\nРўРѕРІР°СЂС‹ СЃ СЂР°Р·РјРµСЂРѕРј 42:")
    for p in has_size_42:
        print(f"  {p['name']} вЂ” СЂР°Р·РјРµСЂС‹: {list(p['sizes'].keys())}")

    # 4.4. РўРѕРІР°СЂС‹, РїРѕСЃС‚СѓРїРёРІС€РёРµ Р·Р° РїРѕСЃР»РµРґРЅРёРµ 30 РґРЅРµР№
    today = datetime.now()
    recent = []
    for p in products:
        date_obj = datetime.strptime(p['created_at'], '%Y-%m-%d')
        days_passed = (today - date_obj).days
        if days_passed <= 30:
            recent.append(p)

    print(f"\nРўРѕРІР°СЂС‹, РїРѕСЃС‚СѓРїРёРІС€РёРµ Р·Р° РїРѕСЃР»РµРґРЅРёРµ 30 РґРЅРµР№ (СЃРµРіРѕРґРЅСЏ {today.strftime('%Y-%m-%d')}):")
    for p in recent:
        date_obj = datetime.strptime(p['created_at'], '%Y-%m-%d')
        days_passed = (today - date_obj).days
        print(f"  {p['name']} вЂ” {p['created_at']} ({days_passed} РґРЅРµР№ РЅР°Р·Р°Рґ)")

    # 4.5. РўРѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј (в‰¤ 3 С€С‚. СЃСѓРјРјР°СЂРЅРѕ)
    low_stock = [p for p in products if total_quantity(p) <= 3]
    print("\nРўРѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј (в‰¤ 3 С€С‚.):")
    for p in low_stock:
        print(f"  {p['name']} вЂ” {total_quantity(p)} С€С‚.")


# ============================================================
# Р—РђР”РђРќРР• 5. РџРѕРёСЃРє
# ============================================================

def search_by_name(products, query):
    """РџРѕРёСЃРє С‚РѕРІР°СЂРѕРІ РїРѕ РїРѕРґСЃС‚СЂРѕРєРµ РІ РЅР°Р·РІР°РЅРёРё."""
    query = query.lower()
    return [p for p in products if query in p['name'].lower()]


def search_by_brand(products, brand):
    """РџРѕРёСЃРє С‚РѕРІР°СЂРѕРІ РїРѕ Р±СЂРµРЅРґСѓ."""
    brand = brand.lower()
    return [p for p in products if p['brand'].lower() == brand]


def search_advanced(products, query, category=None, min_price=None, max_price=None):
    """
    РљРѕРјР±РёРЅРёСЂРѕРІР°РЅРЅС‹Р№ РїРѕРёСЃРє.
    РџР°СЂР°РјРµС‚СЂС‹, СЂР°РІРЅС‹Рµ None, РЅРµ СѓС‡РёС‚С‹РІР°СЋС‚СЃСЏ.
    """
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
    """Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃРїРёСЃРѕРє РЅР°Р·РІР°РЅРёР№ С‚РѕРІР°СЂРѕРІ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј."""
    return [p['name'] for p in products if total_quantity(p) <= 3]


def demo_search():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ РїРѕРёСЃРєР° (Р·Р°РґР°РЅРёРµ 5)."""
    print("\nРџРѕРёСЃРє РїРѕ РЅР°Р·РІР°РЅРёСЋ 'РєСЂРѕСЃСЃ':")
    for p in search_by_name(products, 'РєСЂРѕСЃСЃ'):
        print(f"  {p['name']}")

    print("\nРџРѕРёСЃРє РїРѕ Р±СЂРµРЅРґСѓ 'nike':")
    for p in search_by_brand(products, 'nike'):
        print(f"  {p['name']} ({p['brand']})")

    print("\nРљРѕРјР±РёРЅРёСЂРѕРІР°РЅРЅС‹Р№ РїРѕРёСЃРє: 'РєСЂРѕСЃСЃ', РєР°С‚РµРіРѕСЂРёСЏ 'РћР±СѓРІСЊ', С†РµРЅР° РѕС‚ 8000 РґРѕ 12000:")
    for p in search_advanced(products, 'РєСЂРѕСЃСЃ', category='РћР±СѓРІСЊ', min_price=8000, max_price=12000):
        print(f"  {p['name']} вЂ” {p['price']} СЂСѓР±.")

    print(f"\nРўРѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј (highlight): {highlight(products)}")


# ============================================================
# Р—РђР”РђРќРР• 6. Р“СЂСѓРїРїРёСЂРѕРІРєР° Рё Р°РіСЂРµРіР°С†РёСЏ
# ============================================================

def count_by_category(products):
    """РЎР»РѕРІР°СЂСЊ {РєР°С‚РµРіРѕСЂРёСЏ: РєРѕР»РёС‡РµСЃС‚РІРѕ С‚РѕРІР°СЂРѕРІ}."""
    result = {}
    for p in products:
        result[p['category']] = result.get(p['category'], 0) + 1
    return result


def total_stock_by_brand(products):
    """РЎР»РѕРІР°СЂСЊ {Р±СЂРµРЅРґ: СЃСѓРјРјР°СЂРЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ РµРґРёРЅРёС†}."""
    result = {}
    for p in products:
        result[p['brand']] = result.get(p['brand'], 0) + total_quantity(p)
    return result


def avg_rating_by_category(products):
    """РЎР»РѕРІР°СЂСЊ {РєР°С‚РµРіРѕСЂРёСЏ: СЃСЂРµРґРЅРёР№ СЂРµР№С‚РёРЅРі}."""
    sums = {}
    counts = {}
    for p in products:
        cat = p['category']
        sums[cat] = sums.get(cat, 0) + p['rating']
        counts[cat] = counts.get(cat, 0) + 1
    return {cat: round(sums[cat] / counts[cat], 2) for cat in sums}


def top_brand_by_stock(products):
    """Р‘СЂРµРЅРґ СЃ РЅР°РёР±РѕР»СЊС€РёРј СЃСѓРјРјР°СЂРЅС‹Рј РєРѕР»РёС‡РµСЃС‚РІРѕРј РµРґРёРЅРёС†."""
    stock = total_stock_by_brand(products)
    if not stock:
        return None
    return max(stock, key=stock.get)


def demo_grouping():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ РіСЂСѓРїРїРёСЂРѕРІРєРё Рё Р°РіСЂРµРіР°С†РёРё (Р·Р°РґР°РЅРёРµ 6)."""
    print("\nРљРѕР»РёС‡РµСЃС‚РІРѕ С‚РѕРІР°СЂРѕРІ РїРѕ РєР°С‚РµРіРѕСЂРёСЏРј:")
    for cat, count in count_by_category(products).items():
        print(f"  {cat}: {count}")

    print("\nРЎСѓРјРјР°СЂРЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ РµРґРёРЅРёС† РїРѕ Р±СЂРµРЅРґР°Рј:")
    for brand, qty in total_stock_by_brand(products).items():
        print(f"  {brand}: {qty} С€С‚.")

    print("\nРЎСЂРµРґРЅРёР№ СЂРµР№С‚РёРЅРі РїРѕ РєР°С‚РµРіРѕСЂРёСЏРј:")
    for cat, rating in avg_rating_by_category(products).items():
        print(f"  {cat}: {rating}")

    print(f"\nР‘СЂРµРЅРґ СЃ РЅР°РёР±РѕР»СЊС€РёРј Р·Р°РїР°СЃРѕРј: {top_brand_by_stock(products)}")


# ============================================================
# Р—РђР”РђРќРР• 7. РљРѕСЂР·РёРЅР° СЃ РїСЂРѕРІРµСЂРєРѕР№ РѕСЃС‚Р°С‚РєРѕРІ
# ============================================================

def find_product_by_id(products, product_id):
    """РќР°С…РѕРґРёС‚ С‚РѕРІР°СЂ РїРѕ id. Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃР»РѕРІР°СЂСЊ РёР»Рё None."""
    for p in products:
        if p['id'] == product_id:
            return p
    return None


def add_to_cart(cart, products, product_id, size, quantity):
    """
    Р”РѕР±Р°РІР»СЏРµС‚ С‚РѕРІР°СЂ РІ РєРѕСЂР·РёРЅСѓ СЃ РїСЂРѕРІРµСЂРєР°РјРё.
    Р’РѕР·РІСЂР°С‰Р°РµС‚ (True/False, СЃРѕРѕР±С‰РµРЅРёРµ).
    """
    product = find_product_by_id(products, product_id)
    if product is None:
        return False, f"РўРѕРІР°СЂ СЃ id={product_id} РЅРµ РЅР°Р№РґРµРЅ"

    if size not in product['sizes']:
        return False, f"Р Р°Р·РјРµСЂ {size} РѕС‚СЃСѓС‚СЃС‚РІСѓРµС‚ Сѓ С‚РѕРІР°СЂР° '{product['name']}'"

    available = product['sizes'][size]
    if quantity <= 0:
        return False, "РљРѕР»РёС‡РµСЃС‚РІРѕ РґРѕР»Р¶РЅРѕ Р±С‹С‚СЊ Р±РѕР»СЊС€Рµ 0"

    already_in_cart = 0
    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            already_in_cart = item['quantity']
            break

    if already_in_cart + quantity > available:
        return False, (f"РќРµРґРѕСЃС‚Р°С‚РѕС‡РЅРѕ С‚РѕРІР°СЂР° РЅР° СЃРєР»Р°РґРµ. "
                       f"Р”РѕСЃС‚СѓРїРЅРѕ: {available}, РІ РєРѕСЂР·РёРЅРµ: {already_in_cart}")

    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] += quantity
            return True, f"РљРѕР»РёС‡РµСЃС‚РІРѕ С‚РѕРІР°СЂР° '{product['name']}' СѓРІРµР»РёС‡РµРЅРѕ"

    cart.append({
        'product_id': product_id,
        'name': product['name'],
        'price': product['price'],
        'size': size,
        'quantity': quantity,
    })
    return True, f"РўРѕРІР°СЂ '{product['name']}' РґРѕР±Р°РІР»РµРЅ РІ РєРѕСЂР·РёРЅСѓ"


def remove_from_cart(cart, product_id, size):
    """РЈРґР°Р»СЏРµС‚ РїРѕР·РёС†РёСЋ РёР· РєРѕСЂР·РёРЅС‹."""
    for i, item in enumerate(cart):
        if item['product_id'] == product_id and item['size'] == size:
            cart.pop(i)
            return True, f"РџРѕР·РёС†РёСЏ '{item['name']}' СѓРґР°Р»РµРЅР°"
    return False, "РџРѕР·РёС†РёСЏ РЅРµ РЅР°Р№РґРµРЅР° РІ РєРѕСЂР·РёРЅРµ"


def update_quantity(cart, products, product_id, size, new_qty):
    """РР·РјРµРЅСЏРµС‚ РєРѕР»РёС‡РµСЃС‚РІРѕ СЃ РїСЂРѕРІРµСЂРєРѕР№ РѕСЃС‚Р°С‚РєР°."""
    product = find_product_by_id(products, product_id)
    if product is None:
        return False, "РўРѕРІР°СЂ РЅРµ РЅР°Р№РґРµРЅ"

    if size not in product['sizes']:
        return False, f"Р Р°Р·РјРµСЂ {size} РѕС‚СЃСѓС‚СЃС‚РІСѓРµС‚"

    if new_qty <= 0:
        return remove_from_cart(cart, product_id, size)

    available = product['sizes'][size]
    if new_qty > available:
        return False, f"РќРµРґРѕСЃС‚Р°С‚РѕС‡РЅРѕ С‚РѕРІР°СЂР°. Р”РѕСЃС‚СѓРїРЅРѕ: {available}"

    for item in cart:
        if item['product_id'] == product_id and item['size'] == size:
            item['quantity'] = new_qty
            return True, f"РљРѕР»РёС‡РµСЃС‚РІРѕ РёР·РјРµРЅРµРЅРѕ РЅР° {new_qty}"
    return False, "РџРѕР·РёС†РёСЏ РЅРµ РЅР°Р№РґРµРЅР° РІ РєРѕСЂР·РёРЅРµ"


def cart_total(cart):
    """РЎСѓРјРјР° РїРѕР·РёС†РёР№ РєРѕСЂР·РёРЅС‹."""
    return sum(item['price'] * item['quantity'] for item in cart)


def cart_to_string(cart):
    """РњРЅРѕРіРѕСЃС‚СЂРѕС‡РЅРѕРµ С‚РµРєСЃС‚РѕРІРѕРµ РїСЂРµРґСЃС‚Р°РІР»РµРЅРёРµ РєРѕСЂР·РёРЅС‹."""
    if not cart:
        return "РљРѕСЂР·РёРЅР° РїСѓСЃС‚Р°"
    lines = ["РљРѕСЂР·РёРЅР°:"]
    for item in cart:
        lines.append(
            f"  {item['name']}, СЂР°Р·РјРµСЂ {item['size']}, "
            f"{item['quantity']} С€С‚. Г— {item['price']} = "
            f"{item['quantity'] * item['price']} СЂСѓР±."
        )
    lines.append(f"РС‚РѕРіРѕ: {cart_total(cart)} СЂСѓР±.")
    return "\n".join(lines)


# ============================================================
# Р—РђР”РђРќРР• 8. РћС„РѕСЂРјР»РµРЅРёРµ Р·Р°РєР°Р·Р°
# ============================================================

orders = []
order_counter = [0]


def create_order(cart, client_name, products):
    """
    РџСЂРµРІСЂР°С‰Р°РµС‚ РєРѕСЂР·РёРЅСѓ РІ Р·Р°РєР°Р·.
    РЈРјРµРЅСЊС€Р°РµС‚ РѕСЃС‚Р°С‚РєРё РІ products.
    Р’РѕР·РІСЂР°С‰Р°РµС‚ Р·Р°РєР°Р· РёР»Рё None, РµСЃР»Рё РєРѕСЂР·РёРЅР° РїСѓСЃС‚Р°.
    """
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
    """РџРµС‡Р°С‚Р°РµС‚ Р·Р°РєР°Р·."""
    if order is None:
        print("Р—Р°РєР°Р· РїСѓСЃС‚")
        return
    print(f"Р—Р°РєР°Р· в„–{order['order_id']} РѕС‚ {order['date']}")
    print(f"РљР»РёРµРЅС‚: {order['client']}")
    print("РџРѕР·РёС†РёРё:")
    for item in order['items']:
        print(f"  {item['name']}, СЂР°Р·РјРµСЂ {item['size']}, "
              f"{item['quantity']} С€С‚. Г— {item['price']} = {item['sum']} СЂСѓР±.")
    print(f"РС‚РѕРіРѕ: {order['total']} СЂСѓР±.")


def demo_cart_and_orders():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ РєРѕСЂР·РёРЅС‹ Рё РѕС„РѕСЂРјР»РµРЅРёСЏ Р·Р°РєР°Р·РѕРІ (Р·Р°РґР°РЅРёСЏ 7вЂ“8)."""
    # РџСЂРѕРІРµСЂРєР° РєРѕСЂР·РёРЅС‹
    cart = []
    print("\n--- Р”РѕР±Р°РІР»РµРЅРёРµ С‚РѕРІР°СЂРѕРІ ---")
    print(add_to_cart(cart, products, 1, 40, 2))
    print(add_to_cart(cart, products, 1, 40, 1))
    print(add_to_cart(cart, products, 1, 99, 1))
    print(add_to_cart(cart, products, 3, 'M', 2))
    print(add_to_cart(cart, products, 3, 'M', 10))
    print("\n" + cart_to_string(cart))

    print("\n--- РР·РјРµРЅРµРЅРёРµ РєРѕР»РёС‡РµСЃС‚РІР° ---")
    print(update_quantity(cart, products, 1, 40, 5))
    print(update_quantity(cart, products, 3, 'M', 1))
    print("\n" + cart_to_string(cart))

    print("\n--- РЈРґР°Р»РµРЅРёРµ РїРѕР·РёС†РёРё ---")
    print(remove_from_cart(cart, 1, 40))
    print("\n" + cart_to_string(cart))

    # РћС„РѕСЂРјР»СЏРµРј 3 Р·Р°РєР°Р·Р°
    print("\n--- РћС„РѕСЂРјР»РµРЅРёРµ Р·Р°РєР°Р·РѕРІ ---")
    add_to_cart(cart, products, 1, 41, 2)
    add_to_cart(cart, products, 5, 'OneSize', 1)
    print_order(create_order(cart, 'РРІР°РЅРѕРІ Р.Р.', products))

    add_to_cart(cart, products, 3, 'S', 2)
    add_to_cart(cart, products, 8, 'OneSize', 3)
    print_order(create_order(cart, 'РџРµС‚СЂРѕРІ Рџ.Рџ.', products))

    add_to_cart(cart, products, 9, 42, 1)
    add_to_cart(cart, products, 10, 'OneSize', 2)
    print_order(create_order(cart, 'РЎРёРґРѕСЂРѕРІ РЎ.РЎ.', products))


# ============================================================
# Р—РђР”РђРќРР• 9. РђРЅР°Р»РёС‚РёРєР° РїРѕ Р·Р°РєР°Р·Р°Рј
# ============================================================

def orders_by_client(orders, client_name):
    """РЎРїРёСЃРѕРє Р·Р°РєР°Р·РѕРІ РєР»РёРµРЅС‚Р°."""
    return [o for o in orders if o['client'] == client_name]


def orders_by_period(orders, start_date, end_date):
    """Р—Р°РєР°Р·С‹ Р·Р° РїРµСЂРёРѕРґ (РґР°С‚С‹ РІ С„РѕСЂРјР°С‚Рµ YYYY-MM-DD)."""
    result = []
    for o in orders:
        order_date = o['date'][:10]
        if start_date <= order_date <= end_date:
            result.append(o)
    return result


def total_revenue(orders):
    """РћР±С‰Р°СЏ РІС‹СЂСѓС‡РєР° РїРѕ РІСЃРµРј Р·Р°РєР°Р·Р°Рј."""
    return sum(o['total'] for o in orders)


def best_selling_product(orders):
    """РўРѕРІР°СЂ, РєРѕС‚РѕСЂС‹Р№ С‡Р°С‰Рµ РІСЃРµРіРѕ Р·Р°РєР°Р·С‹РІР°Р»Рё (РїРѕ СЃСѓРјРјРµ РєРѕР»РёС‡РµСЃС‚РІ)."""
    counter = {}
    for order in orders:
        for item in order['items']:
            counter[item['name']] = counter.get(item['name'], 0) + item['quantity']
    if not counter:
        return None
    return max(counter, key=counter.get)


def average_order_total(orders):
    """РЎСЂРµРґРЅСЏСЏ СЃСѓРјРјР° Р·Р°РєР°Р·Р°."""
    if not orders:
        return 0.0
    return round(total_revenue(orders) / len(orders), 2)


def demo_analytics():
    """Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ Р°РЅР°Р»РёС‚РёРєРё (Р·Р°РґР°РЅРёРµ 9)."""
    print(f"\nР’СЃРµРіРѕ Р·Р°РєР°Р·РѕРІ: {len(orders)}")
    print(f"РћР±С‰Р°СЏ РІС‹СЂСѓС‡РєР°: {total_revenue(orders)} СЂСѓР±.")
    print(f"РЎСЂРµРґРЅСЏСЏ СЃСѓРјРјР° Р·Р°РєР°Р·Р°: {average_order_total(orders)} СЂСѓР±.")
    print(f"РЎР°РјС‹Р№ РїСЂРѕРґР°РІР°РµРјС‹Р№ С‚РѕРІР°СЂ: {best_selling_product(orders)}")

    print("\nР—Р°РєР°Р·С‹ РєР»РёРµРЅС‚Р° 'РРІР°РЅРѕРІ Р.Р.':")
    for o in orders_by_client(orders, 'РРІР°РЅРѕРІ Р.Р.'):
        print(f"  Р—Р°РєР°Р· в„–{o['order_id']} РЅР° {o['total']} СЂСѓР±.")

    today_str = datetime.now().strftime('%Y-%m-%d')
    print(f"\nР—Р°РєР°Р·С‹ Р·Р° РїРµСЂРёРѕРґ {today_str} вЂ” {today_str}:")
    for o in orders_by_period(orders, today_str, today_str):
        print(f"  Р—Р°РєР°Р· в„–{o['order_id']} РѕС‚ {o['date']} РЅР° {o['total']} СЂСѓР±.")


# ============================================================
# Р—РђР”РђРќРР• 11. Р Р°Р±РѕС‚Р° СЃ С„Р°Р№Р»Р°РјРё (JSON)
# ============================================================

def save_orders(orders, filename='orders.json'):
    """РЎРѕС…СЂР°РЅСЏРµС‚ СЃРїРёСЃРѕРє Р·Р°РєР°Р·РѕРІ РІ JSON."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(orders, f, ensure_ascii=False, indent=2)
    print(f"Р—Р°РєР°Р·С‹ СЃРѕС…СЂР°РЅРµРЅС‹ РІ {filename}")


def load_orders(filename='orders.json'):
    """Р—Р°РіСЂСѓР¶Р°РµС‚ Р·Р°РєР°Р·С‹ РёР· JSON. Р•СЃР»Рё С„Р°Р№Р»Р° РЅРµС‚ вЂ” РІРѕР·РІСЂР°С‰Р°РµС‚ []."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# ============================================================
# Р—РђР”РђРќРР• 12. Р’Р°Р»РёРґР°С†РёСЏ Рё РѕР±СЂР°Р±РѕС‚РєР° РѕС€РёР±РѕРє
# ============================================================

def safe_int_input(prompt, default=0):
    """Р‘РµР·РѕРїР°СЃРЅС‹Р№ РІРІРѕРґ С†РµР»РѕРіРѕ С‡РёСЃР»Р° СЃ РѕР±СЂР°Р±РѕС‚РєРѕР№ ValueError."""
    try:
        return int(input(prompt))
    except ValueError:
        print("РќРµРєРѕСЂСЂРµРєС‚РЅС‹Р№ РІРІРѕРґ. РСЃРїРѕР»СЊР·СѓСЋ Р·РЅР°С‡РµРЅРёРµ РїРѕ СѓРјРѕР»С‡Р°РЅРёСЋ.")
        return default


# ============================================================
# Р—РђР”РђРќРР• 10. РњРёРЅРё-CLI (РјРµРЅСЋ РІ РєРѕРЅСЃРѕР»Рё)
# ============================================================

def print_menu():
    """РџРµС‡Р°С‚Р°РµС‚ РјРµРЅСЋ."""
    print("\n" + "=" * 40)
    print("РњР•РќР® РњРђР“РђР—РРќРђ В«РЎРџРћР РўРўРћР’РђР Р«В»")
    print("=" * 40)
    print("1 - РџРѕРєР°Р·Р°С‚СЊ РєР°С‚Р°Р»РѕРі")
    print("2 - РћС‚С„РёР»СЊС‚СЂРѕРІР°С‚СЊ РїРѕ РєР°С‚РµРіРѕСЂРёРё")
    print("3 - РџРѕРёСЃРє РїРѕ РЅР°Р·РІР°РЅРёСЋ")
    print("4 - РџРѕРєР°Р·Р°С‚СЊ С‚РѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј")
    print("5 - Р”РѕР±Р°РІРёС‚СЊ РІ РєРѕСЂР·РёРЅСѓ")
    print("6 - РџРѕРєР°Р·Р°С‚СЊ РєРѕСЂР·РёРЅСѓ")
    print("7 - РћС„РѕСЂРјРёС‚СЊ Р·Р°РєР°Р·")
    print("8 - РџРѕРєР°Р·Р°С‚СЊ РІСЃРµ Р·Р°РєР°Р·С‹")
    print("9 - РђРЅР°Р»РёС‚РёРєР°")
    print("0 - Р’С‹С…РѕРґ")
    print("=" * 40)


def show_catalog():
    """РџРµС‡Р°С‚Р°РµС‚ РєР°С‚Р°Р»РѕРі."""
    print("\n--- РљРђРўРђР›РћР“ ---")
    for p in products:
        print(f"  [{p['id']}] {p['name']} ({p['category']}, {p['brand']}) вЂ” "
              f"{p['price']} СЂСѓР±., СЂРµР№С‚РёРЅРі {p['rating']}, "
              f"РІСЃРµРіРѕ {total_quantity(p)} С€С‚.")


def filter_by_category_cli():
    """РџСѓРЅРєС‚ 2: С„РёР»СЊС‚СЂ РїРѕ РєР°С‚РµРіРѕСЂРёРё."""
    cat = input("Р’РІРµРґРёС‚Рµ РєР°С‚РµРіРѕСЂРёСЋ (РћР±СѓРІСЊ/РћРґРµР¶РґР°/РђРєСЃРµСЃСЃСѓР°СЂС‹): ").strip()
    filtered = [p for p in products if p['category'].lower() == cat.lower()]
    if not filtered:
        print("РўРѕРІР°СЂРѕРІ РІ СЌС‚РѕР№ РєР°С‚РµРіРѕСЂРёРё РЅРµ РЅР°Р№РґРµРЅРѕ.")
        return
    print(f"\nРўРѕРІР°СЂС‹ РєР°С‚РµРіРѕСЂРёРё '{cat}':")
    for p in filtered:
        print(f"  {p['name']} вЂ” {p['price']} СЂСѓР±.")


def search_cli():
    """РџСѓРЅРєС‚ 3: РїРѕРёСЃРє РїРѕ РЅР°Р·РІР°РЅРёСЋ."""
    query = input("Р’РІРµРґРёС‚Рµ С‡Р°СЃС‚СЊ РЅР°Р·РІР°РЅРёСЏ: ").strip()
    found = search_by_name(products, query)
    if not found:
        print("РќРёС‡РµРіРѕ РЅРµ РЅР°Р№РґРµРЅРѕ.")
        return
    print("\nР РµР·СѓР»СЊС‚Р°С‚С‹ РїРѕРёСЃРєР°:")
    for p in found:
        print(f"  [{p['id']}] {p['name']} вЂ” {p['price']} СЂСѓР±.")


def low_stock_cli():
    """РџСѓРЅРєС‚ 4: С‚РѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј."""
    low = [p for p in products if total_quantity(p) <= 3]
    if not low:
        print("РќРµС‚ С‚РѕРІР°СЂРѕРІ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј.")
        return
    print("\nРўРѕРІР°СЂС‹ СЃ РЅРёР·РєРёРј РѕСЃС‚Р°С‚РєРѕРј:")
    for p in low:
        print(f"  {p['name']} вЂ” {total_quantity(p)} С€С‚.")


def add_to_cart_cli(cart):
    """РџСѓРЅРєС‚ 5: РґРѕР±Р°РІРёС‚СЊ С‚РѕРІР°СЂ РІ РєРѕСЂР·РёРЅСѓ."""
    show_catalog()
    pid = safe_int_input("Р’РІРµРґРёС‚Рµ id С‚РѕРІР°СЂР°: ")
    product = find_product_by_id(products, pid)
    if product is None:
        print("РўРѕРІР°СЂ РЅРµ РЅР°Р№РґРµРЅ.")
        return

    print(f"Р”РѕСЃС‚СѓРїРЅС‹Рµ СЂР°Р·РјРµСЂС‹: {list(product['sizes'].keys())}")
    size_raw = input("Р’РІРµРґРёС‚Рµ СЂР°Р·РјРµСЂ: ").strip()

    try:
        size = int(size_raw)
    except ValueError:
        size = size_raw

    qty = safe_int_input("Р’РІРµРґРёС‚Рµ РєРѕР»РёС‡РµСЃС‚РІРѕ: ", default=1)
    result, message = add_to_cart(cart, products, pid, size, qty)
    print(message)


def show_cart_cli(cart):
    """РџСѓРЅРєС‚ 6: РїРѕРєР°Р·Р°С‚СЊ РєРѕСЂР·РёРЅСѓ."""
    print("\n" + cart_to_string(cart))


def create_order_cli(cart):
    """РџСѓРЅРєС‚ 7: РѕС„РѕСЂРјРёС‚СЊ Р·Р°РєР°Р·."""
    if not cart:
        print("РљРѕСЂР·РёРЅР° РїСѓСЃС‚Р°. РќРµС‡РµРіРѕ РѕС„РѕСЂРјР»СЏС‚СЊ.")
        return
    print("\n" + cart_to_string(cart))
    client = input("Р’РІРµРґРёС‚Рµ РёРјСЏ РєР»РёРµРЅС‚Р°: ").strip()
    if not client:
        client = "Р‘РµР· РёРјРµРЅРё"
    order = create_order(cart, client, products)
    print("\nР—Р°РєР°Р· РѕС„РѕСЂРјР»РµРЅ:")
    print_order(order)


def show_orders_cli():
    """РџСѓРЅРєС‚ 8: РїРѕРєР°Р·Р°С‚СЊ РІСЃРµ Р·Р°РєР°Р·С‹."""
    if not orders:
        print("Р—Р°РєР°Р·РѕРІ РїРѕРєР° РЅРµС‚.")
        return
    print("\n--- Р’РЎР• Р—РђРљРђР—Р« ---")
    for o in orders:
        print_order(o)
        print()


def analytics_cli():
    """РџСѓРЅРєС‚ 9: Р°РЅР°Р»РёС‚РёРєР°."""
    if not orders:
        print("Р—Р°РєР°Р·РѕРІ РїРѕРєР° РЅРµС‚. РђРЅР°Р»РёС‚РёРєР° РЅРµРґРѕСЃС‚СѓРїРЅР°.")
        return
    print("\n--- РђРќРђР›РРўРРљРђ ---")
    print(f"Р’СЃРµРіРѕ Р·Р°РєР°Р·РѕРІ: {len(orders)}")
    print(f"РћР±С‰Р°СЏ РІС‹СЂСѓС‡РєР°: {total_revenue(orders)} СЂСѓР±.")
    print(f"РЎСЂРµРґРЅСЏСЏ СЃСѓРјРјР° Р·Р°РєР°Р·Р°: {average_order_total(orders)} СЂСѓР±.")
    print(f"РЎР°РјС‹Р№ РїСЂРѕРґР°РІР°РµРјС‹Р№ С‚РѕРІР°СЂ: {best_selling_product(orders)}")


def main():
    """Р“Р»Р°РІРЅС‹Р№ С†РёРєР» CLI (Р·Р°РґР°РЅРёРµ 10)."""
    print("Р”РѕР±СЂРѕ РїРѕР¶Р°Р»РѕРІР°С‚СЊ РІ РјР°РіР°Р·РёРЅ В«РЎРїРѕСЂС‚РўРѕРІР°СЂС‹В»!")

    cart = []  # РєРѕСЂР·РёРЅР° CLI

    while True:
        print_menu()
        choice = safe_int_input("Р’Р°С€ РІС‹Р±РѕСЂ: ", default=-1)

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
            print("Р”Рѕ СЃРІРёРґР°РЅРёСЏ!")
            break
        else:
            print("РќРµРІРµСЂРЅС‹Р№ РїСѓРЅРєС‚ РјРµРЅСЋ. РџРѕРїСЂРѕР±СѓР№С‚Рµ СЃРЅРѕРІР°.")


# ============================================================
# Р—РђРџРЈРЎРљ
# ============================================================
# РџРѕ Р·Р°РґР°РЅРёСЋ: РґРµРјРѕРЅСЃС‚СЂР°С†РёРё Р·Р°РґР°РЅРёР№ 3вЂ“9 РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ РїРѕРєР°Р·Р°РЅС‹.
# Р•СЃР»Рё СЂР°СЃРєРѕРјРјРµРЅС‚РёСЂРѕРІР°С‚СЊ СЃС‚СЂРѕРєРё РЅРёР¶Рµ вЂ” СѓРІРёРґРёС€СЊ РІРµСЃСЊ РІС‹РІРѕРґ Р·Р°РґР°РЅРёР№.
# Р•СЃР»Рё РѕСЃС‚Р°РІРёС‚СЊ РєР°Рє РµСЃС‚СЊ вЂ” СЃСЂР°Р·Сѓ Р·Р°РїСѓСЃС‚РёС‚СЃСЏ CLI (Р·Р°РґР°РЅРёРµ 10).
#
# Р’РќРРњРђРќРР•: РґРµРјРѕРЅСЃС‚СЂР°С†РёСЏ Р·Р°РґР°РЅРёР№ 7вЂ“8 РѕС„РѕСЂРјР»СЏРµС‚ Р·Р°РєР°Р·С‹ Рё СѓРјРµРЅСЊС€Р°РµС‚ РѕСЃС‚Р°С‚РєРё.
# РџРѕСЌС‚РѕРјСѓ Р·Р°РїСѓСЃРєР°С‚СЊ РµС‘ Р»СѓС‡С€Рµ РѕС‚РґРµР»СЊРЅРѕ, Р° РЅРµ РїРµСЂРµРґ CLI.

if __name__ == '__main__':
    # --- Р”РµРјРѕРЅСЃС‚СЂР°С†РёСЏ Р·Р°РґР°РЅРёР№ 3вЂ“9 (СЂР°СЃРєРѕРјРјРµРЅС‚РёСЂСѓР№ РїСЂРё РЅРµРѕР±С…РѕРґРёРјРѕСЃС‚Рё) ---
    # demo_sorting()
    # demo_filtering()
    # demo_search()
    # demo_grouping()
    # demo_cart_and_orders()
    # demo_analytics()
    # save_orders(orders)
    # print(f"Р—Р°РіСЂСѓР¶РµРЅРѕ Р·Р°РєР°Р·РѕРІ: {len(load_orders())}")

    # --- Р—Р°РїСѓСЃРє CLI (Р·Р°РґР°РЅРёРµ 10) ---
    main()


def total_sum(products):
    """Версия 1: сумма цен без учёта количества."""
    return sum(p['price'] for p in products)

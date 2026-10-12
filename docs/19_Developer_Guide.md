Руководство разработчика — «СпортТовары»
Дата: [9-10-2026]
Автор: [Коваль Андрей Михайлович]

1. Введение
Документ предназначен для разработчиков, которые будут поддерживать или расширять проект «СпортТовары». Описывает структуру проекта, правила работы с Git, порядок добавления новых функций и запуск тестов.

2. Структура проекта
text
ChudoObuv/
├── src/                    # Исходный код (модули)
│   ├── __init__.py
│   ├── catalog.py          # Работа с каталогом
│   ├── cart.py             # Корзина
│   ├── orders.py           # Заказы
│   ├── analytics.py        # Аналитика
│   └── storage.py          # Работа с JSON
├── tests/                  # Тесты
│   ├── __init__.py
│   ├── test_shop.py        # Модульные тесты
│   └── test_integration.py # Интеграционные тесты
├── docs/                   # Документация
├── data/                   # Данные
│   └── products.json       # Каталог товаров
├── main.py                 # Точка входа (CLI)
├── build.py                # Скрипт сборки
├── shop.py                 # Монолитный файл (задания 1–12)
└── README.md
3. Установка окружения разработчика
3.1. Клонирование репозитория
git clone https://github.com/koval0311k-cel/ChudoObuv.git
cd ChudoObuv
3.2. Виртуальное окружение (опционально)
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate    # Linux/macOS
3.3. Проверка версии Python
python --version
Должно быть 3.10 или выше.

3.4. Установка зависимостей
Проект использует только стандартную библиотеку Python. Установка дополнительных пакетов не требуется.

4. Работа с Git
4.1. Основные ветки
main — стабильная версия продукта. Сюда попадают только проверенные релизы.

develop — основная рабочая ветка. Все изменения делаются здесь.

4.2. Правила
Никогда не коммитить напрямую в main.

Рабочие изменения — только в develop.

Перед началом работы — переключиться в develop:

git checkout develop
git pull
После работы — коммит и push:

git add .
git commit -m "Краткое описание"
git push origin develop
4.3. Формат сообщений коммитов
Рекомендуется использовать префиксы:

Day N: ... — коммиты по практическим занятиям.

Fix: ... — исправления.

Docs: ... — документация.

Test: ... — тесты.

Примеры:

Day 10: добавлен docs/19_Developer_Guide.md
Fix: исправлена total_sum
Docs: обновлён README.md
5. Как добавить новую функцию
Шаг 1. Определить, в какой модуль добавить
Работа с каталогом → src/catalog.py

Корзина → src/cart.py

Заказы → src/orders.py

Аналитика → src/analytics.py

Сохранение/загрузка → src/storage.py

Шаг 2. Написать функцию с docstring
Пример:

python
def my_new_function(products, threshold=5):
    """
    Краткое описание функции.

    :param products: список товаров
    :type products: list[dict]
    :param threshold: порог (по умолчанию 5)
    :type threshold: int
    :return: отфильтрованный список
    :rtype: list[dict]
    """
    return [p for p in products if p['price'] < threshold]
Шаг 3. Подключить функцию к main.py
Импортировать:

python
from src.catalog import my_new_function
И добавить пункт меню:

python
elif choice == 10:
    result = my_new_function(products)
    print(result)
Шаг 4. Написать тест
В tests/test_shop.py:

python
class TestMyNewFunction(unittest.TestCase):
    def test_basic(self):
        products = [{'price': 100}, {'price': 5000}]
        result = my_new_function(products, threshold=1000)
        self.assertEqual(len(result), 1)
Шаг 5. Запустить тесты
python -m unittest discover -s tests
Шаг 6. Коммит
git add .
git commit -m "Добавлена функция my_new_function"
git push origin develop
6. Тестирование
6.1. Модульные тесты
python -m unittest discover -s tests
6.2. Конкретный файл тестов
python -m unittest tests.test_shop
python -m unittest tests.test_integration
6.3. Запуск одного теста
python -m unittest tests.test_shop.TestGetLowStock.test_empty_list
7. Сборка
Скрипт сборки проверяет:

Версию Python (3.10+).

Наличие data/products.json.

Запускает все тесты.

python build.py
Ожидаемый результат:

Python 3.14 — OK
Файл данных — OK
Все тесты пройдены — OK
Сборка успешна!
8. Стиль кода
Python 3.10+.

Отступы: 4 пробела.

Длина строки: не более 100 символов.

Имена функций: snake_case.

Имена классов: PascalCase.

Docstrings для всех публичных функций.

Пример оформления функции:
python
def calculate_discount(price, discount_percent):
    """
    Вычисляет цену со скидкой.

    :param price: исходная цена
    :type price: float
    :param discount_percent: процент скидки (0–100)
    :type discount_percent: float
    :return: цена со скидкой
    :rtype: float
    """
    return round(price * (1 - discount_percent / 100), 2)
9. Отладка
9.1. Точки останова
Открой файл в VS Code.

Кликни слева от номера строки — появится красная точка.

Нажми F5 — отладка начнётся.

Программа остановится на точке останова.

9.2. Панель отладки
F5 — продолжить.

F10 — Step Over.

F11 — Step Into.

Shift+F11 — Step Out.

9.3. Панель Variables
Показывает значения всех переменных в текущем контексте.

10. Полезные команды Git

git branch                  # список веток
git checkout develop        # переключиться в develop
git checkout -b feature/x   # создать ветку
git merge feature/x         # слить ветку
git log --oneline --graph   # история с графом
git status                  # состояние
git diff                    # изменения
git push origin develop     # пуш
11. Контакты
Разработчик: Коваль Андрей Михайлович.
Репозиторий: https://github.com/koval0311k-cel/ChudoObuv
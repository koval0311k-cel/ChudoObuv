# История Git проекта «СпортТовары»

**Дата:** [6-10-2026]
**Команда:** [Коваль Андрей Михайлович]

---

## Вывод команды `git log --oneline --graph --all`

* 43668e8 (HEAD -> develop) Merge branch 'hotfix/cart-total' into develop
* e1fe51f US-2: реализована функция search_advanced (PR-описание)
* 9692af0 Day 7: сохранена история Git в docs/12_Git_History.md
* 0b30560 Исправлена total_sum: удалена пустая функция после конфликта
* 84d2188 Day 7: разрешён конфликт в total_sum (документация)
*   ac52cb0 Разрешён конфликт в total_sum
|\  
| * 871463f feature/total-v2: добавлена функция total_sum (с количеством)
* | 402b945 feature/total-v1: добавлена функция total_sum (без количества)
|/  
* 2f5647e Подготовка к заданию 3: очистка total_sum
* 35e805d Day 7: добавлена схема Git Flow
| * e8e8b40 (main, hotfix/cart-total) hotfix: исправлена cart_total + описание hotfix
|/  
* 12b0b51 Initial commit: project structure


---

## Анализ истории

### Сколько веток было создано?

В ходе работы над проектом были созданы следующие ветки:

- `main` — стабильная версия продукта.
- `develop` — основная рабочая ветка.
- `feature/low-stock` — функция `get_low_stock`.
- `feature/total-v1` — версия 1 функции `total_sum`.
- `feature/total-v2` — версия 2 функции `total_sum`.
- `feature/search-advanced` — функция `search_advanced`.
- `hotfix/cart-total` — срочное исправление `cart_total`.

**Итого:** 7 веток.

### Какие слияния произошли?

1. `feature/low-stock` → `develop`
2. `feature/total-v1` → `develop`
3. `feature/total-v2` → `develop` (с конфликтом)
4. `feature/search-advanced` → `develop`
5. `hotfix/cart-total` → `main`
6. `hotfix/cart-total` → `develop`

### Был ли конфликт и как он разрешён?

**Да**, конфликт возник при слиянии `feature/total-v2` в `develop`,
потому что обе ветки (`total-v1` и `total-v2`) изменили одну и ту же функцию `total_sum`.

**Разрешение:** оставлена версия 2 (с учётом количества), маркеры конфликта удалены,
слияние завершено коммитом «Разрешён конфликт в total_sum».
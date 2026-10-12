"""Скрипт локальной сборки проекта «СпортТовары»."""

import subprocess
import sys
import os


def check_python_version():
    """Проверяет, что Python версии 3.10+."""
    if sys.version_info < (3, 10):
        print("Требуется Python 3.10+")
        sys.exit(1)
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} — OK")


def check_data():
    """Проверяет наличие файла данных."""
    if not os.path.exists('data/products.json'):
        print("Файл data/products.json не найден!")
        sys.exit(1)
    print("Файл данных — OK")


def run_tests():
    """Запускает все тесты."""
    print("\nЗапуск тестов...")
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("Тесты не прошли!")
        print(result.stderr)
        sys.exit(1)
    print("Все тесты пройдены — OK")


def run_app():
    """Запускает приложение."""
    print("\nЗапуск приложения...")
    subprocess.run([sys.executable, "main.py"])


if __name__ == '__main__':
    print("=" * 40)
    print("СБОРКА ПРОЕКТА «СПОРТТОВАРЫ»")
    print("=" * 40)
    check_python_version()
    check_data()
    run_tests()
    print("\nСборка успешна!")
    print("=" * 40)
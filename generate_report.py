#!/usr/bin/env python3
"""
Скрипт для генерации HTML отчетов pytest (кросс-платформенный)
Использование: python generate_report.py [уровень]
"""

import sys
import subprocess
import os
from pathlib import Path

def run_command(cmd):
    """Запуск команды pytest"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Ошибка выполнения: {e}")
        return False

def main():
    print("🚀 Генерация HTML отчета pytest...")
    
    # Создаем папку reports если её нет
    Path("reports").mkdir(exist_ok=True)
    
    # Определяем уровень тестирования
    level = sys.argv[1] if len(sys.argv) > 1 else ""
    
    if level == "":
        print("📊 Запуск всех тестов...")
        cmd = "pytest --html=reports/report.html --self-contained-html"
    elif level == "level0":
        print("🟦 Запуск Level 0 (Основы Python)...")
        cmd = "pytest -m level0 --html=reports/report_level0.html --self-contained-html"
    elif level == "level1":
        print("🟢 Запуск Level 1 (Примеры)...")
        cmd = "pytest -m level1 --html=reports/report_level1.html --self-contained-html"
    elif level == "level2":
        print("🟡 Запуск Level 2 (Простые TODO)...")
        cmd = "pytest -m level2 --html=reports/report_level2.html --self-contained-html"
    elif level == "level3":
        print("🟠 Запуск Level 3 (Средние TODO)...")
        cmd = "pytest -m level3 --html=reports/report_level3.html --self-contained-html"
    elif level == "level4":
        print("🔴 Запуск Level 4 (Сложные TODO)...")
        cmd = "pytest -m level4 --html=reports/report_level4.html --self-contained-html"
    else:
        print(f"❌ Неизвестный уровень: {level}")
        print("Доступные уровни: level0, level1, level2, level3, level4")
        sys.exit(1)
    
    # Запускаем pytest
    success = run_command(cmd)
    
    if success:
        print("✅ Отчет готов! Откройте файл reports/report*.html в браузере")
        
        # Показываем путь к отчету
        report_files = list(Path("reports").glob("*.html"))
        if report_files:
            latest_report = max(report_files, key=os.path.getmtime)
            print(f"📂 Последний отчет: {latest_report}")
    else:
        print("❌ Произошла ошибка при генерации отчета")
        sys.exit(1)

if __name__ == "__main__":
    main() 
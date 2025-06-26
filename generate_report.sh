#!/bin/bash

# Скрипт для генерации HTML отчетов pytest
# Использование: ./generate_report.sh [уровень]
# Примеры:
#   ./generate_report.sh        # Все тесты
#   ./generate_report.sh level1 # Только Level 1
#   ./generate_report.sh level2 # Только Level 2

echo "🚀 Генерация HTML отчета pytest..."

# Создаем папку reports если её нет
mkdir -p reports

# Определяем какие тесты запускать
if [ "$1" = "" ]; then
    echo "📊 Запуск всех тестов..."
    pytest --html=reports/report.html --self-contained-html
elif [ "$1" = "level0" ]; then
    echo "🟦 Запуск Level 0 (Основы Python)..."
    pytest -m level0 --html=reports/report_level0.html --self-contained-html
elif [ "$1" = "level1" ]; then
    echo "🟢 Запуск Level 1 (Примеры)..."
    pytest -m level1 --html=reports/report_level1.html --self-contained-html
elif [ "$1" = "level2" ]; then
    echo "🟡 Запуск Level 2 (Простые TODO)..."
    pytest -m level2 --html=reports/report_level2.html --self-contained-html
elif [ "$1" = "level3" ]; then
    echo "🟠 Запуск Level 3 (Средние TODO)..."
    pytest -m level3 --html=reports/report_level3.html --self-contained-html
elif [ "$1" = "level4" ]; then
    echo "🔴 Запуск Level 4 (Сложные TODO)..."
    pytest -m level4 --html=reports/report_level4.html --self-contained-html
else
    echo "❌ Неизвестный уровень: $1"
    echo "Доступные уровни: level0, level1, level2, level3, level4"
    exit 1
fi

echo "✅ Отчет готов! Откройте файл reports/report*.html в браузере"
echo "📂 Или выполните: open reports/report.html (на macOS)" 
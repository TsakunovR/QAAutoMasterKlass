# ⚡ Быстрый старт - Шпаргалка

## 🚀 Установка за 2 минуты

```bash
# 1. Клонировать проект
git clone <URL_РЕПОЗИТОРИЯ>
cd QAAutoMasterKlass

# 2. Установить зависимости  
pip install -r requirements.txt
# Или если не работает pip:
pip3 install -r requirements.txt

# 3. Проверить систему (рекомендуется)
python3 check_system.py

# 4. Запустить примеры
pytest tests/test_level1_examples.py -v
```

## 📝 Основные команды

```bash
# Запуск всех тестов
pytest -v

# Запуск по уровням
pytest -m level0 -v    # Основы Python
pytest -m level1 -v    # Примеры
pytest -m level2 -v    # Простые TODO  
pytest -m level3 -v    # Средние TODO
pytest -m level4 -v    # Сложные TODO

# HTML отчет (кросс-платформенный)
python3 generate_report.py        # Все тесты
python3 generate_report.py level1 # Только Level 1
```

## 🎯 План изучения

### Шаг 0: Основы Python (15 мин) 
```bash
# Изучите основы Python
python3 src/pet.py

# Запустите unit-тесты
pytest tests/test_level0_python_basics.py -v
```

### Шаг 1: Изучите примеры (15 мин)
```bash
# Запустите готовые тесты
pytest tests/test_level1_examples.py -v

# Откройте файл и изучите код
# tests/test_level1_examples.py
```

### Шаг 2: Простые TODO (30 мин)
```bash
# Откройте файл
# tests/test_level2_simple_todos.py

# Раскомментируйте код в местах TODO
# Удалите строки pass
# Запустите тесты
pytest tests/test_level2_simple_todos.py -v
```

### Шаг 3: Средние TODO (45 мин)
```bash
# Откройте файл  
# tests/test_level3_medium_todos.py

# Дописывайте код по подсказкам
pytest tests/test_level3_medium_todos.py -v
```

### Шаг 4: Сложные TODO (60 мин)
```bash
# Откройте файл
# tests/test_level4_advanced_todos.py

# Изучите фикстуры и параметризацию
pytest tests/test_level4_advanced_todos.py -v
```

## 🔧 API Эндпоинты для тестов

```python
# GET запросы
"/store/inventory"           # Инвентарь магазина
"/pet/findByStatus"          # Питомцы по статусу  
"/pet/{petId}"              # Питомец по ID
"/user/{username}"          # Пользователь по имени
"/user/login"               # Авторизация

# POST запросы  
"/pet"                      # Создать питомца
"/user"                     # Создать пользователя
"/store/order"              # Создать заказ

# PUT запросы
"/pet"                      # Обновить питомца
"/user/{username}"          # Обновить пользователя

# DELETE запросы
"/pet/{petId}"              # Удалить питомца
"/user/{username}"          # Удалить пользователя
```

## 💡 Шаблон TODO выполнения

**Было:**
```python
def test_example(self):
    # TODO: Отправить GET запрос
    # response = self.client.get("/endpoint")
    # assert response.status_code == 200
    pass  # Удалите эту строку
```

**Стало:**
```python
def test_example(self):
    # TODO: Отправить GET запрос
    response = self.client.get("/endpoint")
    assert response.status_code == 200
```

## 🐛 Быстрое решение проблем

### Проверка системы в первую очередь
```bash
# Запустите диагностику
python3 check_system.py

# Исправьте все ❌ проблемы перед началом работы
```

### Ошибка импорта
```bash
# Проверить что находитесь в корне проекта
pwd
ls -la  # Должны видеть requirements.txt

# Переустановить зависимости
pip install -r requirements.txt
# Или если не работает pip:
pip3 install -r requirements.txt
```

### API недоступно
```bash
# Проверить доступность API
curl https://swagger.rv-school.ru/api/v3/store/inventory
```

### Синтаксическая ошибка
```bash
# Проверить синтаксис файла
python -m py_compile tests/test_level2_simple_todos.py
```

## 📊 Прогресс изучения

- [ ] ✅ Установил проект и зависимости
- [ ] 🟦 Изучил Level 0 (основы Python)
- [ ] 🟢 Запустил Level 1 (примеры)
- [ ] 🟡 Решил Level 2 (простые TODO)
- [ ] 🟠 Решил Level 3 (средние TODO)  
- [ ] 🔴 Решил Level 4 (сложные TODO)
- [ ] 🎯 Создал свой собственный тест

**Время на изучение: ~2-3 часа**

---

## 🎓 Продолжите обучение
После освоения мастер-класса изучите **полноценное обучение** автотестированию:  
🌐 [rvschool.ru](https://rvschool.ru) | 💬 Отзывы: [t.me/rvtsakunovreview](https://t.me/rvtsakunovreview)

📖 **Подробная документация:** [README.md](README.md)  
🌐 **API документация:** https://swagger.rv-school.ru 
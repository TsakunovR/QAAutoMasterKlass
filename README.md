# 🚀 QA AutoMaster Класс - API Тестирование

Добро пожаловать на мастер-класс по написанию автотестов на Python! 

Этот проект создан для изучения API тестирования с использованием **pytest** и **requests**. Мы будем тестировать классический Petstore API.

## 🎯 Цель мастер-класса

Научиться писать автотесты для REST API, начиная с простых GET запросов и заканчивая сложными сценариями.

## 📋 Что нужно установить

### Python 3.8+
Убедитесь что у вас установлен Python версии 3.8 или выше:
```bash
python --version
```

### Зависимости проекта
```bash
pip install -r requirements.txt
```

## 🏗 Структура проекта

```
QAAutoMasterKlass/
├── README.md                    # Этот файл
├── requirements.txt             # Зависимости Python
├── pytest.ini                  # Настройки pytest
├── src/
│   ├── __init__.py
│   └── pet.py                  # 🟦 Класс для изучения основ Python
├── config/
│   ├── __init__.py
│   └── settings.py             # Настройки API (URL, данные)
├── utils/
│   ├── __init__.py
│   └── api_client.py           # HTTP клиент для API
├── tests/
│   ├── __init__.py
│   ├── test_level0_python_basics.py # 🟦 Основы Python
│   ├── test_level1_examples.py      # 🟢 Готовые примеры
│   ├── test_level2_simple_todos.py  # 🟡 Простые TODO
│   ├── test_level3_medium_todos.py  # 🟠 Средние TODO
│   └── test_level4_advanced_todos.py # 🔴 Сложные TODO
├── data/                       # Тестовые данные (если нужны)
├── reports/                    # HTML отчеты pytest
└── generate_report.sh          # Скрипт для создания HTML отчетов
```

## 🎓 Система обучения по уровням

### 🟦 **Level 0: Основы Python**
Файл: `src/pet.py` и `tests/test_level0_python_basics.py`

**Что изучаем:**
- Что такое переменные (строки, числа, списки)
- Что такое функции (методы)
- Базовые операции и условная логика
- Unit-тестирование обычного Python кода

**Запуск:**
```bash
# Демонстрация класса Pet
python3 src/pet.py

# Unit-тесты
pytest tests/test_level0_python_basics.py -v
```

### 🟢 **Level 1: Готовые примеры**
Файл: `tests/test_level1_examples.py`

**Что изучаем:**
- Базовые GET запросы
- Проверка статус кодов
- Работа с JSON ответами
- Простые assertions

**Запуск:**
```bash
pytest tests/test_level1_examples.py -v
```

### 🟡 **Level 2: Простые TODO**
Файл: `tests/test_level2_simple_todos.py`

**Что изучаем:**
- GET запросы с параметрами
- Обработка разных статус кодов
- Проверка структуры данных

**Задания:**
- Получение питомца по ID
- Поиск питомцев по статусу
- Получение пользователя по имени

**Запуск:**
```bash
pytest tests/test_level2_simple_todos.py -v
```

### 🟠 **Level 3: Средние TODO**
Файл: `tests/test_level3_medium_todos.py`

**Что изучаем:**
- POST/PUT запросы
- Создание и обновление данных
- Очистка тестовых данных
- Валидация ответов

**Задания:**
- Создание нового питомца
- Обновление существующего питомца
- Создание пользователя
- Размещение заказа

**Запуск:**
```bash
pytest tests/test_level3_medium_todos.py -v
```

### 🔴 **Level 4: Сложные TODO**
Файл: `tests/test_level4_advanced_todos.py`

**Что изучаем:**
- Фикстуры pytest
- Параметризация тестов
- Комплексные сценарии
- Обработка ошибок

**Задания:**
- Полный жизненный цикл питомца
- Параметризованные тесты
- Тестирование ошибок
- Интеграционные сценарии

**Запуск:**
```bash
pytest tests/test_level4_advanced_todos.py -v
```

## 🚀 Быстрый старт

### 1. Клонируйте проект
!!!Пропустите если уже скачали проект из GitHub!!!
```bash
git clone <URL_РЕПОЗИТОРИЯ>
cd QAAutoMasterKlass
```

### 2. Установите зависимости
```bash
pip install -r requirements.txt
# Или если не работает pip:
pip3 install -r requirements.txt
```

### 3. Проверьте готовность системы (рекомендуется)
```bash
python3 check_system.py
```

### 4. Запустите готовые примеры
```bash
pytest tests/test_level1_examples.py -v
```

### 5. Изучите код примеров
Откройте файл `tests/test_level1_examples.py` и посмотрите как написаны тесты.

### 6. Начните решать TODO задания
Откройте `tests/test_level2_simple_todos.py` и начните дописывать код в местах с комментариями `# TODO`.

## 📚 Полезные команды

### Запуск всех тестов
```bash
pytest -v
```

### Запуск тестов определенного уровня
```bash
pytest -m level0 -v    # Основы Python
pytest -m level1 -v    # Только готовые примеры
pytest -m level2 -v    # Только простые TODO
pytest -m level3 -v    # Только средние TODO
pytest -m level4 -v    # Только сложные TODO
```

### Запуск с HTML отчетом
```bash
# Вручную
pytest --html=reports/report.html --self-contained-html

# Автоматический скрипт (кросс-платформенный)
python3 generate_report.py        # Все тесты
python3 generate_report.py level1 # Только Level 1
python3 generate_report.py level2 # Только Level 2

# Bash версия (только Linux/macOS)
./generate_report.sh level1
```

### Запуск конкретного теста
```bash
pytest tests/test_level1_examples.py::TestLevel1Examples::test_get_store_inventory_example -v
```

## 🔧 API Documentation

Мы тестируем Petstore API, документация доступна по адресу:
**https://swagger.rv-school.ru**

### Основные эндпоинты:

**Питомцы (Pet):**
- `GET /pet/findByStatus` - поиск по статусу
- `GET /pet/{petId}` - получение по ID  
- `POST /pet` - создание питомца
- `PUT /pet` - обновление питомца
- `DELETE /pet/{petId}` - удаление питомца

**Пользователи (User):**
- `GET /user/{username}` - получение пользователя
- `POST /user` - создание пользователя
- `PUT /user/{username}` - обновление пользователя
- `GET /user/login` - авторизация
- `GET /user/logout` - выход

**Магазин (Store):**
- `GET /store/inventory` - инвентарь
- `POST /store/order` - создание заказа
- `GET /store/order/{orderId}` - получение заказа

## 💡 Подсказки для выполнения TODO

### Как раскомментировать код
В файлах с TODO вы увидите закомментированный код:
```python
# TODO: Отправить GET запрос
# response = self.client.get("/endpoint")
```

Для выполнения задания нужно:
1. Убрать символы `# ` в начале строк
2. Удалить строку `pass` в конце метода

### Пример выполнения TODO
**До:**
```python
def test_example(self):
    # TODO: Отправить GET запрос
    # response = self.client.get("/store/inventory")
    # assert response.status_code == 200
    pass  # Удалите эту строку
```

**После:**
```python
def test_example(self):
    # TODO: Отправить GET запрос
    response = self.client.get("/store/inventory")
    assert response.status_code == 200
```

## 🐛 Что делать если тесты не проходят

### 1. Проверьте доступность API
```bash
curl https://swagger.rv-school.ru/api/v3/store/inventory
```

### 2. Проверьте установленные зависимости
```bash
pip list | grep -E "(pytest|requests)"
# Или:
pip3 list | grep -E "(pytest|requests)"
```

### 3. Запустите тесты с подробным выводом
```bash
pytest tests/test_level1_examples.py -v -s
```

### 4. Проверьте синтаксис Python
```bash
python -m py_compile tests/test_level2_simple_todos.py
```

## 🎯 Задания для самостоятельной работы

После прохождения всех уровней попробуйте:

1. **Добавить новые тесты** в `test_level2_simple_todos.py`
2. **Создать свои фикстуры** для повторяющихся операций
3. **Добавить параметризацию** в существующие тесты
4. **Протестировать больше эндпоинтов** из Swagger документации
5. **Добавить логирование** в тесты
6. **Создать отдельный класс** для работы с каждой сущностью (Pet, User, Store)

## 🎉 Поздравления!

Если вы дошли до конца - вы освоили основы API тестирования! 

Теперь вы умеете:
- ✅ Писать GET/POST/PUT/DELETE тесты
- ✅ Работать с JSON данными  
- ✅ Использовать фикстуры и параметризацию
- ✅ Обрабатывать ошибки API
- ✅ Создавать комплексные сценарии

**Следующие шаги:**
- Изучите более продвинутые возможности pytest
- Попробуйте другие инструменты: Postman, Newman, RestAssured
- Изучите тестирование GraphQL API
- Освойте нагрузочное тестирование с помощью Locust или JMeter

---

## 🤝 Контакты

Если у вас есть вопросы или предложения - создайте Issue в репозитории!

## 🎓 Хотите изучить больше?

Этот мастер-класс - только начало! Если вы хотите **профессионально освоить автоматизацию тестирования API и WEB**, рекомендуем полноценное обучение:

### 📚 **Комплексное обучение автотестированию**
🌐 **Сайт:** [rvschool.ru](https://rvschool.ru)

**Что вас ждет в полном курсе:**
- 🔧 **API тестирование** - от базовых запросов до сложных интеграций
- 🌐 **WEB автотестирование** - Selenium, Page Object, фреймворки
- 🏗️ **Архитектура тестов** - правильная организация проектов
- 📊 **CI/CD интеграция** - автоматический запуск тестов
- 💼 **Реальные проекты** - портфолио для трудоустройства

### 💬 **Отзывы учеников**
📱 Читайте честные отзывы наших выпускников: [t.me/rvtsakunovreview](https://t.me/rvtsakunovreview)

---

**Удачи в изучении автотестирования! 🚀** 
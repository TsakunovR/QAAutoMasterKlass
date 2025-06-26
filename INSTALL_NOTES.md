# 🛠️ Заметки по установке

## ✅ Что должно работать "из коробки"

После выполнения простых шагов:
1. `git clone` проекта  
2. `pip install -r requirements.txt`
3. `python3 check_system.py`

**Все должно работать без дополнительных настроек!**

## 🔧 Требования

- **Python 3.8+** (обязательно)
- **pip** (обычно идет с Python)
- **Интернет соединение** (для доступа к API)

## 📱 Поддерживаемые ОС

- ✅ **macOS** - полностью протестировано
- ✅ **Linux Ubuntu/Debian** - должно работать
- ✅ **Windows 10/11** - должно работать
- ⚠️ **Старые версии Windows** - не тестировалось

## 🐍 Команды Python по ОС

### macOS / Linux
```bash
python3 check_system.py
python3 generate_report.py
```

### Windows  
```cmd
python check_system.py
python generate_report.py
```

## 🚨 Возможные проблемы и решения

### 1. `python3: command not found` (Windows)
**Проблема:** В Windows может не работать команда `python3`
**Решение:** Используйте `python` вместо `python3`

### 2. Ошибки SSL/сертификатов
**Проблема:** API недоступно из-за корпоративного файрвола
**Решение:** Попробуйте с личного интернета или мобильного интернета

### 3. Медленная установка пакетов
**Проблема:** `pip install` долго работает
**Решение:** 
```bash
pip install -r requirements.txt --upgrade
```

### 4. Permission denied на bash скриптах
**Проблема:** `./generate_report.sh: Permission denied`
**Решение:** Используйте Python версию:
```bash
python3 generate_report.py level1
```

### 5. Конфликты версий Python
**Проблема:** Несовместимые версии пакетов
**Решение:** 
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🏆 Контрольный список готовности

Выполните эти шаги чтобы убедиться что все работает:

- [ ] Python 3.8+ установлен (`python3 --version`)
- [ ] Зависимости установлены (`pip install -r requirements.txt`)
- [ ] Диагностика пройдена (`python3 check_system.py`)
- [ ] Примеры работают (`pytest tests/test_level1_examples.py -v`)
- [ ] Отчеты создаются (`python3 generate_report.py level1`)

**Если все пункты ✅ - вы готовы к мастер-классу!**

## 💡 Альтернативные способы запуска

### Если не работает `python3`
```bash
python check_system.py
python generate_report.py
```

### Если не работают скрипты
```bash
# Вместо ./generate_report.sh
python3 generate_report.py

# Прямые команды pytest
pytest --html=reports/report.html --self-contained-html
```

### Если проблемы с правами
```bash
# Сделать скрипт исполняемым
chmod +x generate_report.sh

# Или запускать через bash
bash generate_report.sh level1
```

## 🌐 Тестирование доступности API

Если есть сомнения в доступности API:

```bash
# Linux/macOS
curl https://swagger.rv-school.ru/api/v3/store/inventory

# Windows (PowerShell)
Invoke-WebRequest https://swagger.rv-school.ru/api/v3/store/inventory
```

Должен вернуться код 200 и JSON с данными.

---
**💬 Помощь:** Если что-то не работает - запустите `python3 check_system.py` для диагностики! 
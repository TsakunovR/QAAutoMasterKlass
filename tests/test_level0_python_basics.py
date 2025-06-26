"""
🟦 LEVEL 0: Основы Python и Unit-тестирование

Этот файл демонстрирует:
- Как тестировать обычный Python код (не API)
- Что такое unit-тесты
- Основы pytest на простых примерах

Запуск: pytest tests/test_level0_python_basics.py -v
"""
import pytest
from src.pet import Pet


class TestPythonBasics:
    """Базовые тесты для демонстрации unit-тестирования"""
    
    def setup_method(self):
        """Подготовка перед каждым тестом"""
        # Сбрасываем счетчик питомцев
        Pet.total_pets = 0
    
    @pytest.mark.level0
    def test_pet_creation_example(self):
        """
        Пример 1: Тестирование создания питомца
        
        Демонстрирует:
        - Создание объекта
        - Проверка переменных экземпляра
        - Базовые assertions
        """
        # Создаем питомца
        dog = Pet("Бобик", "собака", 3)
        
        # Проверяем что все переменные установлены правильно
        assert dog.name == "Бобик"
        assert dog.animal_type == "собака"
        assert dog.age == 3
        assert dog.is_hungry == True  # Новый питомец всегда голоден
        assert dog.friends == []      # У нового питомца нет друзей
        
        print(f"✅ Питомец {dog.name} создан корректно!")
    
    @pytest.mark.level0
    def test_pet_methods_example(self):
        """
        Пример 2: Тестирование методов (функций) класса
        
        Демонстрирует:
        - Вызов методов
        - Проверка возвращаемых значений
        - Проверка изменения состояния
        """
        cat = Pet("Мурка", "кошка", 2)
        
        # Тестируем метод introduce()
        introduction = cat.introduce()
        expected_text = "Привет! Меня зовут Мурка, я кошка, мне 2 лет"
        assert introduction == expected_text
        
        # Тестируем метод feed()
        assert cat.is_hungry == True  # Сначала голодная
        
        result = cat.feed()
        assert "покушал и теперь доволен" in result
        assert cat.is_hungry == False  # После кормления не голодная
        
        # Попробуем покормить еще раз
        result2 = cat.feed()
        assert "уже сыт" in result2
        assert cat.is_hungry == False  # Состояние не изменилось
        
        print("✅ Все методы работают корректно!")
    
    @pytest.mark.level0
    def test_friends_functionality_example(self):
        """
        Пример 3: Тестирование работы со списками
        
        Демонстрирует:
        - Добавление элементов в список
        - Проверка длины списка
        - Работа с методами возвращающими числа
        """
        dog = Pet("Рекс", "собака", 4)
        
        # В начале друзей нет
        assert dog.get_friends_count() == 0
        assert len(dog.friends) == 0
        
        # Добавляем первого друга
        result1 = dog.add_friend("Мурка")
        assert "Мурка теперь друг Рекс" in result1
        assert dog.get_friends_count() == 1
        assert "Мурка" in dog.friends
        
        # Добавляем второго друга
        dog.add_friend("Шарик")
        assert dog.get_friends_count() == 2
        assert len(dog.friends) == 2
        assert "Шарик" in dog.friends
        
        print(f"✅ У {dog.name} теперь {dog.get_friends_count()} друзей!")
    
    @pytest.mark.level0
    def test_birthday_math_example(self):
        """
        Пример 4: Тестирование математических операций
        
        Демонстрирует:
        - Изменение числовых переменных
        - Математические операции
        - Проверка состояния до и после
        """
        pet = Pet("Тузик", "собака", 1)
        
        # Проверяем начальный возраст
        assert pet.age == 1
        
        # День рождения!
        result = pet.have_birthday()
        
        # Проверяем что возраст увеличился
        assert pet.age == 2
        assert "Было 1 лет, стало 2 лет" in result
        
        # Еще один день рождения
        pet.have_birthday()
        assert pet.age == 3
        
        print(f"✅ {pet.name} правильно стареет!")
    
    @pytest.mark.level0
    def test_class_variable_example(self):
        """
        Пример 5: Тестирование переменных класса
        
        Демонстрирует:
        - Общие переменные для всех объектов
        - Статические методы
        - Счетчики и глобальное состояние
        """
        # В начале питомцев нет
        assert Pet.get_total_pets() == 0
        
        # Создаем первого питомца
        pet1 = Pet("Барсик", "кот", 3)
        assert Pet.get_total_pets() == 1
        
        # Создаем второго питомца
        pet2 = Pet("Дружок", "собака", 2)
        assert Pet.get_total_pets() == 2
        
        # Проверяем что счетчик общий для всех
        assert pet1.total_pets == 2
        assert pet2.total_pets == 2
        
        print(f"✅ Счетчик питомцев работает: {Pet.get_total_pets()}")


class TestPythonDataTypes:
    """Демонстрация основных типов данных Python"""
    
    @pytest.mark.level0
    def test_data_types_example(self):
        """
        Пример 6: Основные типы данных в Python
        
        Демонстрирует:
        - Строки (str)
        - Числа (int, float)
        - Булевы значения (bool)
        - Списки (list)
        """
        pet = Pet("Мухтар", "собака", 5)
        
        # Строки (str)
        assert isinstance(pet.name, str)
        assert isinstance(pet.animal_type, str)
        
        # Числа (int)
        assert isinstance(pet.age, int)
        
        # Булевы значения (bool)
        assert isinstance(pet.is_hungry, bool)
        assert pet.is_hungry in [True, False]
        
        # Списки (list)
        assert isinstance(pet.friends, list)
        
        # Можем добавлять в список
        pet.friends.append("Новый друг")
        assert len(pet.friends) == 1
        
        print("✅ Все типы данных работают корректно!")


class TestPythonConditions:
    """Демонстрация условной логики"""
    
    @pytest.mark.level0  
    def test_if_else_logic_example(self):
        """
        Пример 7: Условная логика (if/else)
        
        Демонстрирует:
        - Условные операторы
        - Логические проверки
        - Разное поведение в зависимости от условий
        """
        hungry_pet = Pet("Голодный", "кот", 1)
        
        # Тестируем условие "если голоден"
        assert hungry_pet.is_hungry == True
        result = hungry_pet.feed()
        assert "покушал и теперь доволен" in result
        
        # Тестируем условие "если не голоден"
        assert hungry_pet.is_hungry == False
        result = hungry_pet.feed()
        assert "уже сыт" in result
        
        print("✅ Условная логика работает!")


# 🎯 ДЕМОНСТРАЦИОННЫЕ ФУНКЦИИ (для показа на видео)

def demo_variables():
    """Демонстрация переменных для видео"""
    print("\n" + "="*50)
    print("📚 ДЕМОНСТРАЦИЯ ПЕРЕМЕННЫХ")
    print("="*50)
    
    # Разные типы переменных
    name = "Шарик"          # строка
    age = 3                 # число
    weight = 15.5           # дробное число
    is_happy = True         # True/False
    toys = ["мяч", "кость"] # список
    
    print(f"name = '{name}'")
    print(f"age = {age}")
    print(f"weight = {weight}")
    print(f"is_happy = {is_happy}")
    print(f"toys = {toys}")
    
    # Использование переменных
    print(f"\n{name} весит {weight} кг и ему {age} лет")
    if is_happy:
        print(f"{name} счастлив! 😊")


def demo_functions():
    """Демонстрация функций для видео"""
    print("\n" + "="*50)
    print("🔧 ДЕМОНСТРАЦИЯ ФУНКЦИЙ")
    print("="*50)
    
    def greet_pet(pet_name, pet_type):
        """Простая функция приветствия"""
        greeting = f"Привет, {pet_name}! Ты отличный {pet_type}!"
        return greeting
    
    # Используем функцию
    message = greet_pet("Бобик", "пес")
    print(message)
    
    def calculate_pet_age_in_months(years):
        """Функция с вычислениями"""
        months = years * 12
        return months
    
    pet_years = 2
    pet_months = calculate_pet_age_in_months(pet_years)
    print(f"\n{pet_years} лет = {pet_months} месяцев")


if __name__ == "__main__":
    """
    Демонстрация для запуска напрямую:
    python tests/test_level0_python_basics.py
    """
    demo_variables()
    demo_functions()
    
    print("\n" + "="*50)
    print("🐕 СОЗДАНИЕ ПИТОМЦА")
    print("="*50)
    
    # Создаем питомца и показываем его возможности
    my_pet = Pet("Демо-пес", "собака", 2)
    print(my_pet.introduce())
    print(my_pet.feed())
    print(my_pet.add_friend("Демо-кот"))
    print(my_pet.have_birthday())
    print(my_pet.get_info()) 
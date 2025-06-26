"""
🐕 Простой класс Pet для изучения основ Python

Этот файл создан для объяснения базовых концепций:
- Что такое переменные
- Что такое функции (методы)
- Основные типы данных
- Простая логика в Python
"""


class Pet:
    """
    Класс для представления домашнего питомца
    
    Демонстрирует основные концепции Python:
    - Переменные класса и экземпляра
    - Методы (функции)
    - Типы данных: строки, числа, списки, булевы
    """
    
    # 📌 ПЕРЕМЕННАЯ КЛАССА - общая для всех питомцев
    total_pets = 0  # Счетчик всех созданных питомцев
    
    def __init__(self, name, animal_type, age):
        """
        🏗 Конструктор - специальная функция для создания питомца
        
        Параметры (это тоже переменные!):
        - name: имя питомца (строка/string)
        - animal_type: тип животного (строка/string) 
        - age: возраст (число/integer)
        """
        # 📌 ПЕРЕМЕННЫЕ ЭКЗЕМПЛЯРА - уникальные для каждого питомца
        self.name = name                    # строка (str)
        self.animal_type = animal_type      # строка (str)
        self.age = age                      # число (int)
        self.is_hungry = True               # булево значение (bool)
        self.friends = []                   # список (list)
        
        # Увеличиваем общий счетчик питомцев
        Pet.total_pets += 1
        
        print(f"🐾 Питомец {self.name} создан! Всего питомцев: {Pet.total_pets}")
    
    def introduce(self):
        """
        📢 ФУНКЦИЯ (МЕТОД) - блок кода, который можно вызывать
        
        Эта функция представляет питомца
        Возвращает строку с информацией
        """
        # 📌 ПЕРЕМЕННАЯ ВНУТРИ ФУНКЦИИ
        introduction = f"Привет! Меня зовут {self.name}, я {self.animal_type}, мне {self.age} лет"
        
        return introduction  # Возвращаем результат
    
    def feed(self):
        """
        🍖 Функция кормления питомца
        
        Демонстрирует:
        - Изменение состояния (переменной)
        - Условную логику (if/else)
        """
        if self.is_hungry:  # 📌 УСЛОВИЕ - проверяем переменную
            self.is_hungry = False  # 📌 ИЗМЕНЯЕМ ПЕРЕМЕННУЮ
            return f"{self.name} покушал и теперь доволен! 😊"
        else:
            return f"{self.name} уже сыт! 😴"
    
    def add_friend(self, friend_name):
        """
        👫 Добавить друга питомцу
        
        Параметр:
        - friend_name: имя друга (строка)
        
        Демонстрирует работу со списками
        """
        # 📌 РАБОТА СО СПИСКОМ - добавляем элемент
        self.friends.append(friend_name)
        return f"{friend_name} теперь друг {self.name}! 🎉"
    
    def get_friends_count(self):
        """
        📊 Получить количество друзей
        
        Демонстрирует:
        - Функцию len() - длина списка
        - Возврат числового значения
        """
        friends_count = len(self.friends)  # 📌 ПЕРЕМЕННАЯ с результатом функции
        return friends_count
    
    def have_birthday(self):
        """
        🎂 День рождения питомца
        
        Демонстрирует математические операции
        """
        old_age = self.age          # 📌 СОХРАНЯЕМ старое значение
        self.age = self.age + 1     # 📌 МАТЕМАТИЧЕСКАЯ ОПЕРАЦИЯ (можно писать self.age += 1)
        
        return f"У {self.name} день рождения! Было {old_age} лет, стало {self.age} лет! 🎉"
    
    def get_info(self):
        """
        📋 Полная информация о питомце
        
        Демонстрирует:
        - Работу с несколькими переменными
        - Форматирование строк
        - Условную логику
        """
        # 📌 НЕСКОЛЬКО ПЕРЕМЕННЫХ
        hunger_status = "голоден" if self.is_hungry else "сыт"
        friends_info = f"{len(self.friends)} друзей" if self.friends else "пока нет друзей"
        
        # 📌 МНОГОСТРОЧНАЯ ПЕРЕМЕННАЯ
        info = f"""
🐾 Информация о питомце:
   Имя: {self.name}
   Тип: {self.animal_type}
   Возраст: {self.age} лет
   Статус: {hunger_status}
   Друзья: {friends_info}
        """
        
        return info.strip()  # strip() убирает лишние пробелы
    
    @staticmethod
    def get_total_pets():
        """
        📊 Статический метод - можно вызывать без создания питомца
        
        Возвращает общее количество созданных питомцев
        """
        return Pet.total_pets


# 🎯 ДЕМОНСТРАЦИОННЫЕ ФУНКЦИИ (не методы класса)

def create_demo_pets():
    """
    🎪 Демонстрационная функция - создает примеры питомцев
    
    Показывает как использовать класс Pet
    """
    print("=" * 50)
    print("🎪 ДЕМОНСТРАЦИЯ КЛАССА PET")
    print("=" * 50)
    
    # 📌 СОЗДАНИЕ ОБЪЕКТОВ (переменные, которые содержат питомцев)
    dog = Pet("Бобик", "собака", 3)
    cat = Pet("Мурка", "кошка", 2)
    
    print("\n📢 ПРЕДСТАВЛЕНИЕ ПИТОМЦЕВ:")
    print(dog.introduce())
    print(cat.introduce())
    
    print("\n🍖 КОРМЛЕНИЕ:")
    print(dog.feed())  # Покормим собаку
    print(dog.feed())  # Попробуем покормить еще раз
    
    print("\n👫 ДОБАВЛЕНИЕ ДРУЗЕЙ:")
    print(dog.add_friend("Мурка"))
    print(cat.add_friend("Бобик"))
    print(dog.add_friend("Рекс"))
    
    print("\n🎂 ДЕНЬ РОЖДЕНИЯ:")
    print(cat.have_birthday())
    
    print("\n📋 ПОЛНАЯ ИНФОРМАЦИЯ:")
    print(dog.get_info())
    print(cat.get_info())
    
    print(f"\n📊 ВСЕГО ПИТОМЦЕВ СОЗДАНО: {Pet.get_total_pets()}")


def explain_variables():
    """
    📚 Функция для объяснения переменных
    """
    print("\n" + "=" * 50)
    print("📚 ЧТО ТАКОЕ ПЕРЕМЕННЫЕ?")
    print("=" * 50)
    
    # 📌 РАЗНЫЕ ТИПЫ ПЕРЕМЕННЫХ
    pet_name = "Шарик"              # строка (str)
    pet_age = 5                     # число (int)
    pet_weight = 15.5               # дробное число (float)
    is_vaccinated = True            # булево значение (bool)
    pet_toys = ["мячик", "кость"]   # список (list)
    
    print("Переменная - это 'коробочка' для хранения данных:")
    print(f"pet_name = '{pet_name}'        # строка")
    print(f"pet_age = {pet_age}                     # число")
    print(f"pet_weight = {pet_weight}               # дробное число")
    print(f"is_vaccinated = {is_vaccinated}         # True/False")
    print(f"pet_toys = {pet_toys}      # список")
    
    print(f"\nМожем использовать переменные:")
    print(f"Питомец {pet_name} весит {pet_weight} кг и ему {pet_age} лет")


def explain_functions():
    """
    🔧 Функция для объяснения функций
    """
    print("\n" + "=" * 50)
    print("🔧 ЧТО ТАКОЕ ФУНКЦИИ?")
    print("=" * 50)
    
    print("Функция - это 'рецепт' для выполнения действий:")
    print("1. Получает данные (параметры)")
    print("2. Что-то делает с ними") 
    print("3. Возвращает результат")
    
    def calculate_dog_years(human_age):
        """Простая функция - переводит человеческие годы в собачьи"""
        dog_age = human_age * 7
        return dog_age
    
    # Используем функцию
    human_years = 3
    dog_years = calculate_dog_years(human_years)
    print(f"\nПример: {human_years} человеческих лет = {dog_years} собачьих лет")


# 🚀 ГЛАВНАЯ ФУНКЦИЯ
if __name__ == "__main__":
    """
    Эта часть выполнится только если запустить файл напрямую:
    python src/pet.py
    """
    explain_variables()
    explain_functions()
    create_demo_pets() 
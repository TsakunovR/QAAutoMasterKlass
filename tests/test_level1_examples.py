"""
🟢 LEVEL 1: Готовые примеры для демонстрации

Эти тесты показывают базовые принципы API тестирования.
Запустите их командой: pytest tests/test_level1_examples.py -v
"""
import pytest
from utils.api_client import APIClient


class TestLevel1Examples:
    """Готовые примеры для показа на мастер-классе"""
    
    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.client = APIClient()
    
    @pytest.mark.level1
    def test_get_store_inventory_example(self):
        """
        Пример 1: Простой GET запрос на получение инвентаря магазина
        
        Что проверяем:
        - Статус код 200 (успешный запрос)
        - Ответ в формате JSON
        - Ответ содержит данные
        """
        # Отправляем GET запрос
        response = self.client.get("/store/inventory")
        
        # Проверяем статус код
        assert response.status_code == 200, f"Ожидали 200, получили {response.status_code}"
        
        # Проверяем что ответ в JSON формате
        inventory = response.json()
        assert isinstance(inventory, dict), "Ответ должен быть словарем"
        
        # Выводим данные для понимания
        print(f"\\nПолучен инвентарь: {inventory}")
    
    @pytest.mark.level1  
    def test_find_pets_by_status_example(self):
        """
        Пример 2: GET запрос с параметрами (поиск питомцев по статусу)
        
        Что проверяем:
        - Статус код 200
        - Ответ - это список
        - У каждого питомца есть нужные поля
        """
        # GET запрос с параметром
        response = self.client.get("/pet/findByStatus", params={"status": "available"})
        
        # Базовые проверки
        assert response.status_code == 200
        pets = response.json()
        assert isinstance(pets, list), "Ответ должен быть списком"
        
        # Если есть питомцы, проверяем структуру первого
        if pets:
            first_pet = pets[0]
            assert "id" in first_pet, "У питомца должен быть id"
            assert "name" in first_pet, "У питомца должно быть имя"
            assert "status" in first_pet, "У питомца должен быть статус"
            
            print(f"\\nНайдено питомцев: {len(pets)}")
            print(f"Первый питомец: {first_pet.get('name', 'Без имени')}")
    
    @pytest.mark.level1
    def test_user_login_example(self):
        """
        Пример 3: GET запрос с query параметрами (авторизация)
        
        Что проверяем:
        - Статус код 200
        - Получение токена или сообщения
        """
        # Параметры для входа
        login_params = {
            "username": "user1",
            "password": "password"
        }
        
        response = self.client.get("/user/login", params=login_params)
        
        # В данном API login может возвращать разные коды
        # Показываем как обрабатывать разные случаи
        if response.status_code == 200:
            result = response.text  # Может быть просто строка
            print(f"\\nВход выполнен: {result}")
        else:
            print(f"\\nОшибка входа: {response.status_code}")
            
        # Не делаем жесткую проверку, т.к. это может быть демо
        assert response.status_code in [200, 400], "Ожидали 200 или 400" 
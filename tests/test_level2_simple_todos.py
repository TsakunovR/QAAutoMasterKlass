"""
🟡 LEVEL 2: Простые TODO задания

Дополните недостающий код в местах с комментариями TODO.
Используйте готовые примеры из Level 1 как образец.

Запуск: pytest tests/test_level2_simple_todos.py -v
"""
import pytest
from utils.api_client import APIClient


class TestLevel2SimpleTodos:
    """Простые задания для самостоятельного выполнения"""
    
    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.client = APIClient()
    
    @pytest.mark.level2
    def test_get_pet_by_id(self):
        """
        TODO: Получить информацию о питомце по ID
        
        Подсказки:
        - Эндпоинт: /pet/{petId}
        - Используйте pet_id = 1 для тестирования
        - Проверьте статус код и основные поля
        """
        pet_id = 1
        
        # TODO: Отправить GET запрос на /pet/{pet_id}
        # response = self.client.get(f"/pet/{pet_id}")
        
        # TODO: Проверить что статус код 200 или 404
        # assert response.status_code in [200, 404]
        
        # TODO: Если статус 200, проверить что ответ содержит поля id и name
        # if response.status_code == 200:
        #     pet = response.json()
        #     assert "id" in pet
        #     assert "name" in pet
        #     print(f"\\nПитомец найден: {pet.get('name')}")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level2
    def test_find_pets_by_different_status(self):
        """
        TODO: Найти питомцев со статусом "pending"
        
        Подсказки:
        - Эндпоинт: /pet/findByStatus
        - Параметр: status="pending"
        - Проверьте что все найденные питомцы имеют статус "pending"
        """
        
        # TODO: Отправить GET запрос с параметром status="pending"
        # response = self.client.get("/pet/findByStatus", params={"status": "pending"})
        
        # TODO: Проверить статус код 200
        # assert response.status_code == 200
        
        # TODO: Получить список питомцев из JSON ответа
        # pets = response.json()
        
        # TODO: Проверить что ответ - это список
        # assert isinstance(pets, list)
        
        # TODO: Если есть питомцы, проверить что у всех статус "pending"
        # for pet in pets:
        #     assert pet.get("status") == "pending", f"Питомец {pet.get('name')} имеет статус {pet.get('status')}"
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level2  
    def test_get_user_by_username(self):
        """
        TODO: Получить информацию о пользователе по имени
        
        Подсказки:
        - Эндпоинт: /user/{username}
        - Используйте username = "user1" для теста
        - Обработайте случаи когда пользователь найден и не найден
        """
        username = "user1"
        
        # TODO: Отправить GET запрос на /user/{username}
        # response = self.client.get(f"/user/{username}")
        
        # TODO: Проверить что статус код 200 (найден) или 404 (не найден)
        # assert response.status_code in [200, 404]
        
        # TODO: Если пользователь найден (статус 200), проверить основные поля
        # if response.status_code == 200:
        #     user = response.json()
        #     assert "username" in user
        #     assert "email" in user
        #     print(f"\\nПользователь найден: {user.get('username')}")
        # else:
        #     print(f"\\nПользователь {username} не найден")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level2
    def test_find_pets_by_tags(self):
        """
        TODO: Найти питомцев по тегам
        
        Подсказки:
        - Эндпоинт: /pet/findByTags  
        - Параметр: tags=["tag1", "tag2"]
        - Проверьте базовую структуру ответа
        """
        
        # TODO: Отправить GET запрос с параметром tags
        # Для множественных значений используйте список
        # response = self.client.get("/pet/findByTags", params={"tags": ["tag1", "tag2"]})
        
        # TODO: Проверить статус код (200 или 400)
        # assert response.status_code in [200, 400]
        
        # TODO: Если статус 200, проверить что ответ - это список
        # if response.status_code == 200:
        #     pets = response.json()
        #     assert isinstance(pets, list)
        #     print(f"\\nНайдено питомцев по тегам: {len(pets)}")
        
        pass  # Удалите эту строку когда напишете код


# BONUS TODO: Создайте свой собственный тест
class TestLevel2Bonus:
    """Бонусное задание: создайте свой тест"""
    
    def setup_method(self):
        self.client = APIClient()
    
    @pytest.mark.level2
    def test_your_own_test(self):
        """
        TODO: Придумайте и реализуйте свой собственный тест
        
        Идеи:
        - Проверить что эндпоинт /user/logout работает
        - Протестировать получение заказа по ID (/store/order/{orderId})
        - Любой другой GET эндпоинт из документации
        """
        pass  # Напишите свой код здесь 
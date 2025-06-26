"""
🟠 LEVEL 3: Средние TODO задания

Работа с POST/PUT запросами и валидацией данных.
Требует понимания HTTP методов и JSON структур.

Запуск: pytest tests/test_level3_medium_todos.py -v
"""
import pytest
from utils.api_client import APIClient
from config.settings import TEST_PET_DATA, TEST_USER_DATA


class TestLevel3MediumTodos:
    """Средние задания с созданием и обновлением данных"""
    
    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.client = APIClient()
        self.created_pet_ids = []  # Для очистки после тестов
        self.created_usernames = []  # Для очистки после тестов
    
    def teardown_method(self):
        """Очистка после каждого теста"""
        # Удаляем созданных питомцев
        for pet_id in self.created_pet_ids:
            try:
                self.client.delete(f"/pet/{pet_id}")
            except:
                pass  # Игнорируем ошибки при очистке
        
        # Удаляем созданных пользователей
        for username in self.created_usernames:
            try:
                self.client.delete(f"/user/{username}")
            except:
                pass  # Игнорируем ошибки при очистке
    
    @pytest.mark.level3
    def test_create_new_pet(self):
        """
        TODO: Создать нового питомца через POST запрос
        
        Подсказки:
        - Эндпоинт: /pet
        - HTTP метод: POST
        - Используйте TEST_PET_DATA из настроек
        - Добавьте уникальности в имя питомца
        """
        
        # TODO: Подготовить данные для нового питомца
        # Используйте TEST_PET_DATA как основу и добавьте уникальность
        # import time
        # unique_name = f"TestPet_{int(time.time())}"
        # pet_data = TEST_PET_DATA.copy()
        # pet_data["name"] = unique_name
        
        # TODO: Отправить POST запрос для создания питомца
        # response = self.client.post("/pet", data=pet_data)
        
        # TODO: Проверить что питомец создан (статус 200)
        # assert response.status_code == 200
        
        # TODO: Получить данные созданного питомца
        # created_pet = response.json()
        
        # TODO: Проверить что питомец имеет ID и правильное имя
        # assert "id" in created_pet
        # assert created_pet["name"] == unique_name
        
        # TODO: Сохранить ID для очистки в teardown_method
        # pet_id = created_pet["id"]
        # self.created_pet_ids.append(pet_id)
        
        # print(f"\\nСоздан питомец: {created_pet['name']} с ID: {pet_id}")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level3
    def test_update_existing_pet(self):
        """
        TODO: Обновить существующего питомца через PUT запрос
        
        Подсказки:
        - Сначала создайте питомца (POST /pet)
        - Затем обновите его (PUT /pet)
        - Проверьте что изменения применились
        """
        
        # TODO: Шаг 1 - Создать питомца
        # import time
        # original_name = f"OriginalPet_{int(time.time())}"
        # pet_data = TEST_PET_DATA.copy()
        # pet_data["name"] = original_name
        
        # create_response = self.client.post("/pet", data=pet_data)
        # assert create_response.status_code == 200
        # created_pet = create_response.json()
        # pet_id = created_pet["id"]
        # self.created_pet_ids.append(pet_id)
        
        # TODO: Шаг 2 - Обновить питомца
        # updated_name = f"UpdatedPet_{int(time.time())}"
        # updated_pet_data = created_pet.copy()
        # updated_pet_data["name"] = updated_name
        # updated_pet_data["status"] = "sold"  # Изменим статус
        
        # update_response = self.client.put("/pet", data=updated_pet_data)
        # assert update_response.status_code == 200
        
        # TODO: Шаг 3 - Проверить что изменения применились
        # get_response = self.client.get(f"/pet/{pet_id}")
        # if get_response.status_code == 200:
        #     updated_pet = get_response.json()
        #     assert updated_pet["name"] == updated_name
        #     assert updated_pet["status"] == "sold"
        #     print(f"\\nПитомец обновлен: {original_name} -> {updated_name}")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level3
    def test_create_user(self):
        """
        TODO: Создать нового пользователя
        
        Подсказки:
        - Эндпоинт: /user
        - HTTP метод: POST
        - Используйте TEST_USER_DATA из настроек
        - Сделайте уникальное имя пользователя
        """
        
        # TODO: Подготовить уникальные данные пользователя
        # import time
        # unique_username = f"testuser_{int(time.time())}"
        # user_data = TEST_USER_DATA.copy()
        # user_data["username"] = unique_username
        # user_data["email"] = f"{unique_username}@example.com"
        
        # TODO: Создать пользователя
        # response = self.client.post("/user", data=user_data)
        
        # TODO: Проверить успешное создание
        # В этом API POST /user может возвращать разные статусы
        # assert response.status_code in [200, 201]
        
        # TODO: Сохранить username для очистки
        # self.created_usernames.append(unique_username)
        
        # TODO: Проверить что пользователь действительно создан
        # get_response = self.client.get(f"/user/{unique_username}")
        # if get_response.status_code == 200:
        #     user = get_response.json()
        #     assert user["username"] == unique_username
        #     print(f"\\nПользователь создан: {unique_username}")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level3
    def test_place_order(self):
        """
        TODO: Создать заказ в магазине
        
        Подсказки:
        - Эндпоинт: /store/order
        - HTTP метод: POST
        - Подготовьте данные заказа согласно схеме Order
        """
        
        # TODO: Подготовить данные заказа
        # import time
        # from datetime import datetime
        # 
        # order_data = {
        #     "petId": 1,  # ID питомца
        #     "quantity": 1,
        #     "shipDate": datetime.now().isoformat(),
        #     "status": "placed",
        #     "complete": False
        # }
        
        # TODO: Отправить POST запрос для создания заказа
        # response = self.client.post("/store/order", data=order_data)
        
        # TODO: Проверить создание заказа
        # assert response.status_code in [200, 201]
        
        # TODO: Если заказ создан, проверить его структуру
        # if response.status_code in [200, 201]:
        #     order = response.json()
        #     assert "id" in order
        #     assert order["petId"] == 1
        #     assert order["status"] == "placed"
        #     print(f"\\nЗаказ создан с ID: {order.get('id')}")
        
        pass  # Удалите эту строку когда напишете код
    
    @pytest.mark.level3
    def test_update_user(self):
        """
        TODO: Обновить данные пользователя
        
        Подсказки:
        - Сначала создайте пользователя
        - Затем обновите его через PUT /user/{username}
        - Проверьте что изменения сохранились
        """
        
        # TODO: Создать пользователя (код аналогичен test_create_user)
        
        # TODO: Обновить данные пользователя
        # updated_data = user_data.copy()
        # updated_data["firstName"] = "UpdatedName"
        # updated_data["email"] = f"updated_{unique_username}@example.com"
        
        # update_response = self.client.put(f"/user/{unique_username}", data=updated_data)
        
        # TODO: Проверить обновление
        # TODO: Получить пользователя и сравнить данные
        
        pass  # Удалите эту строку когда напишете код


class TestLevel3Validation:
    """Дополнительные задания на валидацию"""
    
    def setup_method(self):
        self.client = APIClient()
    
    @pytest.mark.level3
    def test_create_pet_validation(self):
        """
        TODO: Протестировать валидацию при создании питомца
        
        Подсказки:
        - Попробуйте создать питомца без обязательных полей
        - Проверьте что API возвращает ошибку валидации
        """
        
        # TODO: Отправить POST запрос с невалидными данными
        # invalid_data = {"name": ""}  # Пустое имя
        # response = self.client.post("/pet", data=invalid_data)
        
        # TODO: Проверить что получена ошибка (4xx статус)
        # assert 400 <= response.status_code < 500
        
        pass  # Удалите эту строку когда напишете код 
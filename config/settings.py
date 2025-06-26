"""
Конфигурация для тестирования Petstore API
"""

# Базовый URL для всех запросов
BASE_URL = "https://swagger.rv-school.ru/api/v3"

# Таймауты для запросов
REQUEST_TIMEOUT = 10

# Заголовки по умолчанию
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Тестовые данные для создания питомцев
TEST_PET_DATA = {
    "name": "TestPet",
    "photoUrls": ["https://example.com/photo.jpg"],
    "status": "available"
}

# Тестовые данные для пользователей
TEST_USER_DATA = {
    "username": "testuser",
    "firstName": "Test",
    "lastName": "User", 
    "email": "test@example.com",
    "password": "password123",
    "phone": "123456789",
    "userStatus": 1
} 
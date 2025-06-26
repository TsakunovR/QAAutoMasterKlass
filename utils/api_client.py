"""
Простой HTTP клиент для работы с API
"""
import requests
from config.settings import BASE_URL, DEFAULT_HEADERS, REQUEST_TIMEOUT


class APIClient:
    """Базовый клиент для работы с API"""
    
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = DEFAULT_HEADERS.copy()
        self.timeout = REQUEST_TIMEOUT
    
    def get(self, endpoint, params=None):
        """GET запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
        return response
    
    def post(self, endpoint, data=None):
        """POST запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data, headers=self.headers, timeout=self.timeout)
        return response
    
    def put(self, endpoint, data=None):
        """PUT запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data, headers=self.headers, timeout=self.timeout)
        return response
    
    def delete(self, endpoint):
        """DELETE запрос"""
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers, timeout=self.timeout)
        return response 
#!/usr/bin/env python3
"""
Скрипт для проверки готовности системы к работе
Проверяет все критические зависимости и настройки
"""

import sys
import subprocess
import importlib
import platform
import requests

def check_python_version():
    """Проверка версии Python"""
    print("🐍 Проверка версии Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor} - требуется Python 3.8+")
        return False

def check_package(package_name):
    """Проверка установленного пакета"""
    try:
        importlib.import_module(package_name)
        return True
    except ImportError:
        return False

def check_dependencies():
    """Проверка всех зависимостей"""
    print("📦 Проверка зависимостей...")
    packages = {
        'pytest': 'pytest',
        'requests': 'requests', 
        'jsonschema': 'jsonschema',
        'pytest_html': 'pytest-html'
    }
    
    all_ok = True
    for import_name, package_name in packages.items():
        if check_package(import_name):
            print(f"   ✅ {package_name} - установлен")
        else:
            print(f"   ❌ {package_name} - НЕ установлен")
            all_ok = False
    
    return all_ok

def check_api_access():
    """Проверка доступности API"""
    print("🌐 Проверка доступности API...")
    try:
        response = requests.get(
            "https://swagger.rv-school.ru/api/v3/store/inventory", 
            timeout=10
        )
        if response.status_code == 200:
            print("   ✅ API доступно")
            return True
        else:
            print(f"   ⚠️  API отвечает с кодом {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ API недоступно: {e}")
        return False

def check_pytest_markers():
    """Проверка работы pytest маркеров"""
    print("🔍 Проверка pytest маркеров...")
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "--collect-only", "-q"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("   ✅ pytest конфигурация - OK")
            return True
        else:
            print("   ❌ Проблемы с pytest конфигурацией")
            print(f"      {result.stderr[:200]}...")
            return False
    except Exception as e:
        print(f"   ❌ Ошибка проверки pytest: {e}")
        return False

def main():
    print("🚀 Проверка готовности системы для QA мастер-класса")
    print("=" * 50)
    
    checks = [
        check_python_version(),
        check_dependencies(),
        check_api_access(),
        check_pytest_markers()
    ]
    
    print("\n" + "=" * 50)
    
    if all(checks):
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ! Система готова к работе.")
        print("\n📋 Что дальше:")
        print("   1. Запустите: pytest tests/test_level1_examples.py -v")
        print("   2. Или используйте: python generate_report.py level1")
        print("   3. Изучите готовые примеры в tests/test_level1_examples.py")
        return True
    else:
        print("❌ ЕСТЬ ПРОБЛЕМЫ! Необходимо исправить ошибки выше.")
        print("\n🔧 Возможные решения:")
        print("   1. Установите зависимости: pip install -r requirements.txt (или pip3)")
        print("   2. Обновите Python до версии 3.8+")
        print("   3. Проверьте интернет соединение")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 
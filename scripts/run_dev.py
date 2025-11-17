import subprocess
import os
import time
from threading import Thread
import requests

def is_backend_ready():
    """Проверяет, готов ли бэкенд"""
    try:
        response = requests.get('http://localhost:5010/api/health', timeout=2)
        print(f"Backend is ready! Status: {response.status_code}")
        return True
    except requests.exceptions.ConnectionError:
        print("Backend not ready yet...")
        return False
    except Exception as e:
        print(f"Backend check error: {e}")
        return False

def run_backend():
    """Запускает бэкенд через Poetry"""
    backend_dir = os.path.join(os.path.dirname(__file__), '..', 'backend')
    os.chdir(backend_dir)
    
    print("Starting backend server on http://localhost:5010")
    
    # Запускаем через poetry run
    subprocess.run(["poetry", "run", "python", "api.py"])

def run_frontend():
    """Запускает фронтенд Vite"""
    frontend_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend')
    os.chdir(frontend_dir)
    print("Starting frontend server on http://localhost:3000")
    
    subprocess.run(["npm", "run", "dev"])

def main():
    print("Starting Computer Algebra System...")
    
    # Запускаем бэкенд в отдельном потоке
    backend_thread = Thread(target=run_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Ждем пока бэкенд запустится
    print("Waiting for backend to start...")
    max_wait = 20
    waited = 0
    
    while not is_backend_ready() and waited < max_wait:
        time.sleep(1)
        waited += 1
        if waited % 5 == 0:
            print(f"Still waiting... {waited}s")
    
    if waited >= max_wait:
        print("Backend failed to start in time.")
    else:
        print("Backend is ready!")
    
    # Запускаем фронтенд
    print("Starting frontend...")
    frontend_thread = Thread(target=run_frontend)
    frontend_thread.daemon = True
    frontend_thread.start()
    
    # Даем время фронтенду на запуск
    time.sleep(5)
    
    print("\nDevelopment servers are running!")
    print("Backend:  http://localhost:5010")
    print("Frontend: http://localhost:3000")
    print("Press Ctrl+C to stop servers")
    
    try:
        # Держим скрипт активным
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")

if __name__ == "__main__":
    main()
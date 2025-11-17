import subprocess
import os
import time
from threading import Thread
import requests
from pathlib import Path
import shutil

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
    frontend_dir = Path(__file__).parent.parent / "frontend"

    npm_exe = shutil.which("npm") or shutil.which("npm.cmd") or shutil.which("npx")
    if not npm_exe:
        print("Error: npm (или npm.cmd / npx) не найден в PATH. Установите Node.js и перезапустите терминал.")
        sys.exit(1)

    # Запускаем в каталоге фронтенда, чтобы npm правильно нашёл package.json
    try:
        subprocess.run([npm_exe, "run", "dev"], cwd=str(frontend_dir), check=True)
    except subprocess.CalledProcessError as e:
        print("npm завершился с ошибкой:", e)
        sys.exit(e.returncode)


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
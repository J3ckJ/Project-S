import pyautogui
import pygetwindow
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Ожидаем вставки флешки
flash_drive_path = "/Volumes/ESD-USB/"
while not os.path.exists(os.path.join(flash_drive_path, "public_key.pem")):
    pass

# Загружаем публичный ключ с флешки
with open(os.path.join(flash_drive_path, "public_key.pem"), "rb") as public_file:
    public_key = public_file.read()

key = RSA.import_key(public_key)

# Блокируем компьютер
pyautogui.hotkey('win', 'l')

# Ожидаем вставку правильного токена
while True:
    # Проверяем, вставлен ли флеш-токен
    if os.path.exists(os.path.join(flash_drive_path, "token.txt")):
        # Файл с токеном на флешке обнаружен
        # Расшифруем токен с использованием публичного ключа
        with open(os.path.join(flash_drive_path, "token.txt"), "rb") as token_file:
            token_data = token_file.read()
        try:
            cipher = PKCS1_OAEP.new(key)
            token = cipher.decrypt(token_data)
            token = token.decode('utf-8')  # Преобразуем токен в строку

            print(token)
        except Exception as e:
            print("Ошибка при расшифровке токена:", str(e))
    
    # Если токен не валиден или его нет, продолжаем ожидание
from Crypto.PublicKey import RSA
import os

# Генерируем ключи
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Укажите путь к флешке
flash_drive_path = "/Volumes/ESD-USB/"

# Сохраняем ключи на флешке
with open(os.path.join(flash_drive_path, "private_key.pem"), "wb") as private_file:
    private_file.write(private_key)

with open(os.path.join(flash_drive_path, "public_key.pem"), "wb") as public_file:
    public_file.write(public_key)
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Hello SCANOSS"
encrypted = cipher.encrypt(message)

print(encrypted)

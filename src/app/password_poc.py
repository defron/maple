import hashlib
import secrets
import time

salt = secrets.token_bytes(32)
password = input("enter password: ")
password_bytes = password.encode("utf-8")

start = time.time()
hashed_password = hashlib.scrypt(password_bytes, salt=salt, n=32768, r=8, p=3, maxmem=34078720)
end = time.time()

print(f"password hashed: {hashed_password.hex()}")
print(f"salt: {salt.hex()}")

print(f"time taken: {end - start}")

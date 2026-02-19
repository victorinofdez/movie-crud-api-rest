from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password = "jose"
hashed = pwd_context.hash(password)
print("Password original:", password)
print("Hash generado:", hashed)
import random
import string

def generate_password(length):
  chars = string.ascii_letters + string.digits
  return ''.join(random.choice(chars) for _ in range(length))

N = int(input("Введите количество паролей: "))
K = int(input("Введите длину паролей: "))

passwords = set()

while len(passwords) < N:
  password = generate_password(K)
  passwords.add(password)

for password in passwords:
  print(password)
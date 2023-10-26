import random

RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'

def generate_password(length):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*?!"
    password = "".join(random.sample(s, length))
    return password

passlen = int(input(f"Enter the {BOLD}{GREEN}length{END} of password: "))
password = generate_password(passlen)

print(f"\n{BOLD}Your New Password{END}: {RED}{password}{END}\n")
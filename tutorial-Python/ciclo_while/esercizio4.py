import random

num = random.randint(1, 10)
guess = int(input("Indovina un numero compreso tra 1 e 10: "))

while guess != num:
    guess = int(input("Sbagliato. Prova ancora: "))

print("Indovinato!")
lst = []
n = int(input("Quanti numeri vuoi inserire? "))
i = 0

while i < n:
    num = int(input("Inserisci un numero: "))
    lst.append(num)
    i += 1

sum = 0
i = 0

while i < len(lst):
    sum += lst[i]
    i += 1

print("La somma di tuttu i numeri è", sum)
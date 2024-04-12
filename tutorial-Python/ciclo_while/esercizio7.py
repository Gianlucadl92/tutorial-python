n = int(input("Inserisci un valore n: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1
print("Il fattoriale di", n, "é", fact)
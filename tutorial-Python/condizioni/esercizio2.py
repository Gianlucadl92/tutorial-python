numero1 = int(input("Scrivi il primo numero "))
numero2 = int(input("Scrivi il secondo numero "))

if numero1 > numero2:
    print(f"Il numero {numero1} è maggiore del numero {numero2}")
elif numero1 < numero2:
    print(f"Il numero {numero2} è maggiore del numero {numero1}")
else:
    print("sono uguali")
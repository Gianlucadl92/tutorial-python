carettere = str(input("Inserisci un carattere: "))

if carettere in "aeiouAEIOU":
    print("è una vocale")
elif carettere.isalpha():
    print("è una consonante")
else:
    print("non è una lettera")

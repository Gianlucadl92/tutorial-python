import csv

valori = []

while True:
    valore = input("Inserisci un valore digitale (digita 'fine' per terminare): ")
    if valore == 'fine':
        break
    valori.append(valore)

with open("nome_file_csv", "w") as file:
    scrittore_csv = csv.writer(file)
    scrittore_csv.writerow(valori)
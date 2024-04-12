import csv

#apriamo il file in lettura
with open('nome_file.csv', 'r') as file:
    #utilizzo modulo csv per leggere il file
    lettore_csv = csv.reader(file)

    for riga in lettore_csv:
        print("|".join(riga))
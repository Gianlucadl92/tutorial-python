# chiediamo all'utente di inserire una stringa
stringa = input("Inserisci una stringa: ")

# apriamo il file in scrittura
with open('nome_file.txt', 'w') as file:
  # scriviamo la stringa nel file
  file.write(stringa)
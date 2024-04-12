# apriamo il file di origine in lettura
with open('nome_file_origine.txt', 'r') as file_origine:
  # leggiamo il contenuto del file e lo assegnamo alla variabile `contenuto`
  contenuto = file_origine.read()

# apriamo il file di destinazione in scrittura
with open('nome_file_destinazione.txt', 'w') as file_destinazione:
  # scriviamo il contenuto del file di origine nel file di destinazione
  file_destinazione.write(contenuto)

  print(contenuto)
  print(file_destinazione)
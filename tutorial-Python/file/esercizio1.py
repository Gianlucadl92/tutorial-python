# apriamo il file in lettura
with open('nome_file.txt', 'r') as file:
  # leggiamo il contenuto del file e lo assegnamo alla variabile `contenuto`
  contenuto = file.read()

# stampiamo il contenuto del file a schermo
print(contenuto)
# apriamo il file di origine in lettura
with open('nome_file_origine.txt', 'r') as file_origine:
  # leggiamo il contenuto del file riga per riga e lo assegnamo alla lista `righe`
  righe = []
  for riga in file_origine:
    righe.append(riga)

# apriamo il file di destinazione in scrittura
with open('nome_file_destinazione.txt', 'w') as file_destinazione:
  # scriviamo le righe del file di origine nel file di destinazione invertendo l'ordine
  for riga in reversed(righe):
    file_destinazione.write(riga)

print(righe)
print(riga)

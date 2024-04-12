import datetime

data = input("Inserisci una data (gg/mm/aaaa): ")
data = datetime.datetime.strptime(data, "%d/%m/%Y")

nome_mese = data.strftime("%B")
print("Il nome del mese corrispondente è:", nome_mese)
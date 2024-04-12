import datetime

data = input("Inserisci una data (gg/mm/aaaa): ")
num_giorni = int(input("Inserisci il numero di giorni: "))

data = datetime.datetime.strptime(data, "%d/%m/%Y")
nuova_data = data + datetime.timedelta(days=num_giorni)

print("La nuova data è:", nuova_data.strftime("%d/%m/%Y"))
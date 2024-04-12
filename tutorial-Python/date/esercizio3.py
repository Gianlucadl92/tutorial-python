import datetime

data1 = input("Inserisci la prima data (gg/mm/aaaa): ")
data2 = input("Inserisci la seconda data (gg/mm/aaaa): ")

data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")

diff = abs(data2 - data1).days
print("La differenza ingiorni tra le due date è:", diff)
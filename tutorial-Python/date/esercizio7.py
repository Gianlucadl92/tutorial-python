import datetime

data1 = input("Inserisci la prima data (gg/mm/aaaa): ")
data2 = input("Inserisci la seconda data (gg/mm/aaaa): ")

data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")

delta = datetime.timedelta(days=1)

while data1 <= data2:
    print(data1.strftime("%Y-%m-%d"))
    data1 += delta
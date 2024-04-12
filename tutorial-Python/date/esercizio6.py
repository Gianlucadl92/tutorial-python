import datetime, calendar

data = input("Inserisci una data (gg/mm/aaaa): ")
data = datetime.datetime.strptime(data, "%d/%m/%Y")

if calendar.isleap(data.year):
    print("L'anno è bisestile.")
else:
    print("L'anno non è bisestile.")
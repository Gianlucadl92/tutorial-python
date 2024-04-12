from datetime import datetime

def giorni_trascorsi(date1, date2):
    diff = date2 - date1
    return diff.days

data1 = datetime(2022, 5, 1)
data2 = datetime(2022, 5, 10)
print(giorni_trascorsi(data1, data2))
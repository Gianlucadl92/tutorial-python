from datetime import datetime

def giorno_settimana(data):
    giorni_settimana = ['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
    giorno = giorni_settimana[data.weekday()]
    return giorno

data = datetime(2022, 5, 1)
print(giorno_settimana(data))
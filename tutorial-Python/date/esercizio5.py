import calendar

anno = int(input("Inserisci l'anno: "))
mese = int(input("Inserisci il mese (1-12): "))

cal = calendar.monthcalendar(anno, mese)
for settimana in cal:
    for giorno in settimana:
        if giorno != 0:
            print(giorno)
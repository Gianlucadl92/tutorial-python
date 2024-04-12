nome = "Mario"
cognome = "Rossi"
stringa = "Il mio nome è {nome} ed il cognome è {cognome}".format(nome=nome.upper(), cognome=cognome.replace("s", "K"))
print(stringa)
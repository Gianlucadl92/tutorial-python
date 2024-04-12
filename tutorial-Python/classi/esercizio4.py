class Impiegato:
    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self):
        self.stipendio *= 1.1

    def stampa_dettagli(self):
        print(f"Impiegato: {self.nome} {self.cognome}, matricola {self.matricola}, stipendio {self.stipendio:.2f} Euro")

i = Impiegato("Marco", "Rossi", 12345, 3000)
i.aumenta_stipendio()
i.stampa_dettagli()
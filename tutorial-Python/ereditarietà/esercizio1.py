class Persona: 
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f"Ciao sono {self.nome } {self.cognome}" )

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia

    def saluta(self):
        print(f"Buongiorno sono {self.nome } {self.cognome}" )

    def voto(self):
        print("Bravo! un bel 9")

persona1 = Persona("Marco", "Verdi")
persona1.saluta()

insegnante1 = Insegnante("Paolo", "Bianco", "Matematica")
insegnante1.saluta()
insegnante1.voto()
class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def emetti_suono(self):
        if self.specie == "gatto":
            print("miao")
        elif self.specie == "cane":
            print("bau")
        else:
            print("Suono sconosciuto")

a = Animale("Fuffi", "gatto")
a.emetti_suono()

b = Animale("Buddy", "cane")
b.emetti_suono()
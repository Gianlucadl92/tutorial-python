class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def accelera(self):
        print(f"{self.marca} {self.modello} {self.anno} sta accelerando")

    def frena(self):
        print(f"{self.marca} {self.modello} {self.anno} sta frenando")


class Auto(Veicolo):
    def __init__(self,marca, modello, anno, colore):
        super(Auto, self).__init__(marca, modello, anno)
        self.colore = colore

    def cambia_colore(self):
        print(f"{self.marca} {self.modello} {self.anno} {self.colore}")

veicolo1 = Veicolo("Audi", "A3", 2021)
veicolo1.accelera()
veicolo1.frena()

auto1 = Auto("Audi", "A3", 2021, "Bianca")
auto1.cambia_colore()

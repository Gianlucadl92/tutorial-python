class Persona:
    def __init__(self, nome, età, sesso):
        self.nome = nome
        self.età = età
        self.sesso = sesso

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.età} anni")

p = Persona("Marco", 32, "maschio")
p.presentati()
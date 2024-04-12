class Automobile:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi(self):
        print(f"Questa è una {self.marca} {self.modello} del {self.anno}")

auto = Automobile("Toyota", "Coralla", 2017)
auto.descrivi()
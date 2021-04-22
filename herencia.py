class Animales:
    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal de tipo", type(self).__name__)

class Perro(Animales):
    def hablar(self):
        print("guau!")
    def moverse(self):
        print("Camino en 4 patas")

class Pato(Animales):
    def hablar(self):
        print("cuac cuac")
    def moverse(self):
        print("Camino en 2 patas")

class Abeja(Animales):
    def hablar(self):
        print("bzzz")

    def picar(self):
        print("Te pico")


mi_perro = Perro(10, "mamifero")
mi_pato = Pato(3, "mamifero")
mi_abeja = Abeja(45, "insecto")
mi_perro.hablar()
mi_perro.describeme()
mi_pato.moverse()
mi_abeja.picar()
import math


class Punto:

    def __init__(self, x=0, y=0):  # creo atributos de Punto
        self.x = x
        self.y = y

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print(f"El punto {self} se encuentra sobre el cuadrante I")
        elif self.x < 0 < self.y:
            print(f"El punto {self} se encuentra sobre el cuadrante II")
        elif self.x < 0 and self.y < 0:
            print(f"El punto {self} se encuentra sobre el cuadrante III")
        elif self.x > 0 > self.y:
            print(f"El punto {self} se encuentra sobre el cuadrante IV")
        elif self.x == 0 and self.y != 0:
            print(f"El punto {self} se encuentra sobre el eje y")
        elif self.x != 0 and self.y == 0:
            print(f"El punto {self} se sitúa sobre el eje x")
        else:
            print(f"El punto {self} se sitúa sobre el origen")

    def vector(self, q):
        print(f"El vector entre {self} y {q} es {q.x - self.x}, {q.y - self.y}")

    def distancia(self, q):
        # pow(a, b) b es la potencia
        ex = pow(q.x - self.x, 2)
        ey = pow(q.y - self.y, 2)
        print(f"La distancia entre {self} y {q} es {math.sqrt(ex + ey)}")


class Rectangulo:

    def __init__(self, inicial=Punto(), final=Punto()):
        self.inicial = inicial
        self.final = final
        self.base = self.final.x - self.inicial.x
        self.altura = self.final.y - self.inicial.y
        self.area = self.base * self.altura

    def base_met(self):
        print(f"La base del rectangulo es {self.base}")

    def altura_met(self):
        print(f"La altura del rectangulo es {self.altura}")

    def area_met(self):
        print(f"El área del rectangulo es {self.area}")


A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)
print(A, B, C, D)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

mi_rectangulo = Rectangulo(A, B)
mi_rectangulo.base_met()
mi_rectangulo.altura_met()
mi_rectangulo.area_met()

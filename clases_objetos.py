class Perro:
    # Atributo de clase
    especie = "mamífero"

    # el método __init__ es llamado al crear el objeto (es el constructor)
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")


mi_perro = Perro("Toby", "bulldog")
mi_perro.ladra()
mi_perro.camina(10)

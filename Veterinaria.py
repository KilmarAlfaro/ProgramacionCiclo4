print("------EJERCICIO 1.--------")


class Perro:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.estado = "NO ATENDIDO"
        self.categoria = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def registrar(self):
        self.estado = "ATENDIDO"

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Estado: {self.estado}")
        print(f"Categoría: {self.categoria}")


perro1 = Perro("Boby", "Rotwailer", 5, 12)
perro1.mostrar_info()
perro1.registrar()
perro1.mostrar_info()
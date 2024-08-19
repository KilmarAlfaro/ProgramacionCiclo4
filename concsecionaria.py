
print("------EJERCICIO 3--------")

class Auto:
    def __init__(self, marca, modelo, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.4
        self.caracteristicas = []

    def agregar_caracteristica(self, caracteristica):
        if len(self.caracteristicas) < 10:
            self.caracteristicas.append(caracteristica)
        else:
            print("Ya se han agregado las 10 características principales.")

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Precio de compra: {self.precio_compra}")
        print(f"Precio de venta: {self.precio_venta}")
        print("Características:")
        for c in self.caracteristicas:
            print(f"- {c}")


# DATOS
auto1 = Auto("Toyota", "Corolla", 20000)
auto1.agregar_caracteristica("4 ruedas")
auto1.agregar_caracteristica("Capacidad para 5 pasajeros")
auto1.mostrar_info()


print("------EJERCICIO 4--------")

class Dispositivo:
    def __init__(self, tipo, marca, precio_compra):
        self.tipo = tipo
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7
        self.caracteristicas = []

    def agregar_caracteristica(self, caracteristica):
        if len(self.caracteristicas) < 6:
            self.caracteristicas.append(caracteristica)
        else:
            print("Ya se han agregado las 6 características principales.")

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Precio de compra: {self.precio_compra}")
        print(f"Precio de venta: {self.precio_venta}")
        print("Características:")
        for c in self.caracteristicas:
            print(f"- {c}")


# DATOS
dispositivo1 = Dispositivo("Celular", "Samsung", 300)
dispositivo1.agregar_caracteristica("Pantalla AMOLED")
dispositivo1.agregar_caracteristica("Batería 4000mAh")
dispositivo1.mostrar_info()
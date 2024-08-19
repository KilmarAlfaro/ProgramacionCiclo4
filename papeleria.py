print("------EJERCICIO 2--------")

class Articulo:
    def __init__(self, tipo, marca, precio_compra, hojas_o_grafito=None):
        self.tipo = tipo
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30
        self.hojas_o_grafito = hojas_o_grafito

    def mostrar_info(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Precio de compra: {self.precio_compra}")
        print(f"Precio de venta: {self.precio_venta}")
        if self.tipo == "Cuaderno":
            print(f"Hojas: {self.hojas_o_grafito}")
        elif self.tipo == "Lápiz":
            print(f"Tipo de grafito: {self.hojas_o_grafito}")


# DATOS
cuaderno1 = Articulo("Cuaderno", "VIVO", 10, 100)
lapiz1 = Articulo("Lápiz", "RAYAS", 2, "Grafito")

cuaderno1.mostrar_info()
lapiz1.mostrar_info()

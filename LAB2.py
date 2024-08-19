

print("-------------------------")
# El siguiente codigo es basado en un banco donde el usuario podra crear una cuenta y depositar/retirar fondos de la misma, teniendo un par de restrinciones en caso que el usuario 
# no ingrese los datos correctamente


# Aqui se define lo que sera el numero de cuenta, su nombre y el saldo inicial
class CuentaBancaria:
    def __init__(self, numero_cuenta, nombre_titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.saldo = saldo_inicial
# Si el usuario elige la opcion 3 podra depositar dinero al numero de cuenta solamente si ese numero de cuenta existe, esta bien escrito y debe ingresar un valor positivo
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito realizado. Nuevo saldo: ${self.saldo}\n")
        else:
            print("El monto a depositar debe ser positivo.\n")
# Si el usuario elige la opcion 4 podra retirar dinero de su cuenta pero para que sea posible debera tener fondos en su cuenta, de lo contrario saltara el mensaje de fondos insufientes
# y no podra colocar valores negativos
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro realizado. Nuevo saldo: ${self.saldo}\n")
        elif monto > self.saldo:
            print("Fondos insuficientes para realizar el retiro.\n")
        else:
            print("El monto a retirar debe ser positivo.\n")
# Consulta el saldo actual de la cuenta
    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo}\n")

# Esto permite que los numeros de cuenta no se repitan
class Banco:
    def __init__(self):
        self.cuentas = {}

    def abrir_cuenta(self, numero_cuenta, nombre_titular, saldo_inicial=0):
        if numero_cuenta not in self.cuentas:
            nueva_cuenta = CuentaBancaria(numero_cuenta, nombre_titular, saldo_inicial)
            self.cuentas[numero_cuenta] = nueva_cuenta
            print(f"Cuenta '{numero_cuenta}' abierta para {nombre_titular}.\n")
        else:
            print("El número de cuenta ya existe.\n")
# en caso que el programa solicite el numero de cuenta y el usuario ingrese una cuenta inexistente
    def obtener_cuenta(self, numero_cuenta):
        cuenta = self.cuentas.get(numero_cuenta)
        if cuenta:
            return cuenta
        else:
            print("Cuenta no encontrada.\n")
            return None


# menu principal
def main():
    banco = Banco()

    while True:
        print("Gestión de Cuentas Bancarias")
        print("1. Abrir cuenta")
        print("2. Consultar saldo")
        print("3. Depositar dinero")
        print("4. Retirar dinero")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            numero_cuenta = input("Número de cuenta: ")
            nombre_titular = input("Nombre del titular: ")
            saldo_inicial = float(input("Saldo inicial: "))
            banco.abrir_cuenta(numero_cuenta, nombre_titular, saldo_inicial)

        elif opcion == '2':
            numero_cuenta = input("Número de cuenta: ")
            cuenta = banco.obtener_cuenta(numero_cuenta)
            if cuenta:
                cuenta.consultar_saldo()

        elif opcion == '3':
            numero_cuenta = input("Número de cuenta: ")
            cuenta = banco.obtener_cuenta(numero_cuenta)
            if cuenta:
                monto = float(input("Monto a depositar: "))
                cuenta.depositar(monto)

        elif opcion == '4':
            numero_cuenta = input("Número de cuenta: ")
            cuenta = banco.obtener_cuenta(numero_cuenta)
            if cuenta:
                monto = float(input("Monto a retirar: "))
                cuenta.retirar(monto)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, inténtalo de nuevo.\n")


if __name__ == "__main__":
    main()

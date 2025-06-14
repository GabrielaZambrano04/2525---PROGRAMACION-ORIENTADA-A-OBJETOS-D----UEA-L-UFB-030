
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        print(f"Coche: {self.marca} {self.modelo}, Puertas: {self.puertas}")

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Moto: {self.marca} {self.modelo}, Tipo: {self.tipo}")

def crear_vehiculos():
    vehiculos = []
    vehiculos.append(Coche("Toyota", "Corolla", 4))
    vehiculos.append(Moto("Yamaha", "MT-03", "Deportiva"))
    vehiculos.append(Coche("Kia", "Rio", 5))
    return vehiculos

def mostrar_vehiculos(lista):
    print("LISTA DE VEHÍCULOS:")
    for v in lista:
        v.mostrar_info()

if __name__ == "__main__":
    lista = crear_vehiculos()
    mostrar_vehiculos(lista)
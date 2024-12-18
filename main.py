# Parte 1: Clases

class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas
        
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas')
    
# creacion de la clase hija Automovil

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad = velocidad
        self.cilindraje = cilindraje
            
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas, velocidad: {self.velocidad} km/h, {self.cilindraje} cc')
    
# prueba

a1 = Automovil('Toyoda', 'Tarcel', 5, 100, 8000)
print(a1)

# Funcion registro de automoviles

def registro_automovil():
    
    attributes = list(range(5))
    n = int(input("¿Cuántos vehiculos desea insertar? "))
    registers_data = list(range(n))
    registers = list(range(n))
    for i in range(n):
        attributes[0] = str(input(f'Inserte la marca del automovil {i+1}: '))
        attributes[1] = str(input('Inserte el modelo: '))
        attributes[2] = int(input('Inserte el número de ruedas: '))
        attributes[3] = int(input('Inserte la velocidad en km/h: '))
        attributes[4] = int(input('Inserte el cilidraje en cc: '))
        registers_data[i] = attributes
        print(f'Datos del automovil {i+1}: ')
        registers[i] = Automovil(*registers_data[i])
        print(Automovil(*registers_data[i]))
    
    return(registers)


# creacion clase automovil particular

class AutomovilParticular(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, numero_de_puesto):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje,)
        self.numero_de_puesto = numero_de_puesto
            
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas, velocidad: {self.velocidad} km/h, {self.cilindraje} cc, {self.numero_de_puesto} puestos')
    
# prueba clase automovil particular

print(AutomovilParticular('Nissu','Skybird GTI',4,300,5000,4))

# creacion clase automvil de carga

class AutomovilCarga(Automovil):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindraje, peso_carga):
        super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindraje,)
        self.peso_carga = peso_carga
            
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas, velocidad: {self.velocidad} km/h, {self.cilindraje} cc, {self.peso_carga} kg')

# creacion de la clase hija bicicleta

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo = tipo
            
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas, tipo {self.tipo}')

# creacion de la clase hija motocicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
            
    def __str__(self):
        return (f'Marca: {self.marca}, Modelo: {self.modelo}, {self.numero_de_ruedas} ruedas, tipo {self.tipo}, {self.nro_radios} radios, cuadro {self.cuadro}, motor {self.motor}T')

# relaciones ente clases

print(f'Motocicleta es instancia con relacion a Vehiculo: {issubclass(Motocicleta,Vehiculo)}\
\nMotocicleta es instancia con relacion a Automovil: {issubclass(Motocicleta,Automovil)}\
\nMotocicleta es instancia con relacion a Vehiculo Particular: {issubclass(Motocicleta,AutomovilParticular)}\
\nMotocicleta es instancia con relacion a Vehiculo de Carga: {issubclass(Motocicleta,AutomovilCarga)}\
\nMotocicleta es instancia con relacion a Bicicleta: {issubclass(Motocicleta,Bicicleta)}\
\nMotocicleta es instancia con relacion a Motocicleta: {issubclass(Motocicleta,Motocicleta)}')

# generacion csv

# datos de prueba

sample_vehiculos = [['Toyota','Yaris', 4],['Fiat','Palio',4],['Ford','Fiesta',4]]
sample_automoviles = [['Toyota','Yaris', 4, 120, 800],['Fiat','Palio',4 ,95 ,1200],['Ford','Fiesta',4 ,125 ,1500]]
sample_particular = [['Ford','Fiesta',4, 180, 500, 5]]
sample_carga = [['Daft Trucks', 'G 38', 10, 120, '1000', '20000']]
sample_bicicleta = [['Shimano', 'MT Ranger', 2, 'Carrera']]
sample_motocicleta = [['BMW', 'F800s',2,'Deportiva','2T','Doble Viga', 21]]


# registros en csv a partir de datos de pprueba

import csv

reg = 'registro_vehiculos.csv'
with open(reg, mode='w', newline='') as csvfile:
    for i in range(len(sample_vehiculos)):
        writer = csv.writer(csvfile)
        fila = [(type(Vehiculo(*sample_vehiculos[i])).__name__, Vehiculo(*sample_vehiculos[i]).__dict__)]
        writer.writerow(fila)
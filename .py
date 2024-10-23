Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True
    def arrancar(self):
        self.arrancado = True
        self.parado = False
    def parar(self):
        self.parado = True
        self.arrancado = False
    def resume(self):
        print("Marca:", self.marca, "\n", "Modelo.", self.modelo, "\nª, "Color:, self.color, "\n", "Estña arrancado:", self.arrancado,"\n", "Está parado:", self.parado)
        
SyntaxError: invalid syntax. Perhaps you forgot a comma?
miCoche = Vehiculo("Renault", "Megane")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    miCoche = Vehiculo("Renault", "Megane")
NameError: name 'Vehiculo' is not defined
miCoche.arrancar()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    miCoche.arrancar()
NameError: name 'miCoche' is not defined

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

        
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

        
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo

    
class Vehiculo('Rojo', 4)
SyntaxError: expected ':'
class Vehiculo('Rojo', 4):
    print(vehiculo)

    
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    class Vehiculo('Rojo', 4):
TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
class Vehiculo:
    def __init__(self, rojo, 4):
        self.color = color
        self.ruedas = ruedas

        
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

        
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return 'Color: ' + self.color + ', Ruedas: ' + str(self.ruedas)

    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ', Velocidad (km/hr): ' + str(self.velocidad)

    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ', Tipo: ' + self.tipo
    
SyntaxError: invalid syntax
vehiculo = Vehiculo('Rojo', 4)
print(vehiculo)
Color: Rojo, Ruedas: 4
coche = Coche('Azul', 150)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    coche = Coche('Azul', 150)
TypeError: Coche.__init__() missing 1 required positional argument: 'velocidad'
coche = Coche('Azul', 4, 150)
print(coche)
Color: Azul, Ruedas: 4, Velocidad (km/hr): 150
bicicleta = Bicicleta('Blanca', 2, 'Urbano')
print(bicicleta)
Color: Blanca, Ruedas: 2, Tipo: Urbano


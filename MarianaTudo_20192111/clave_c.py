import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1, num2):
    multiplicacion = num1 * num2
    return multiplicacion


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco(num1, num2):
    result = 0
    for x in range(num1, num2):
        if x % 3 == 0 and x % 5 == 0:
            result += x
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""

# start-->


def definicionCono(altura, radio):
    return {
        "generatriz": obtenerGeneratriz(altura, radio),
        "area": obtenerArea(altura, radio),
        "volumen": obtenerVolumen(altura, radio),
    }


def obtenerGeneratriz(altura, radio):
    generatriz = math.sqrt(altura ** 2 + radio ** 2)
    return generatriz


def obtenerArea(altura, radio):
    generatriz = obtenerGeneratriz(altura, radio)
    area = math.pi * radio * (radio + generatriz)
    return area


def obtenerVolumen(altura, radio):
    volumen = (1 / 3) * math.pi * (radio ** 2) * altura
    return volumen


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""

# start-->

class Cono:

    def __init__(self, altura, radio):
        self.altura = altura
        self.radio = radio

    def definicionCono(self):
        generatriz = math.sqrt(self.altura ** 2 + self.radio ** 2)
        area = math.pi * self.radio * (self.radio + generatriz)
        volumen = (1 / 3) * math.pi * (self.radio ** 2) * self.altura
        return {
            "generatriz": generatriz,
            "area": area,
            "volumen": volumen,
        }


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico:

    def __init__(self):
        return

    def registrar(self):
        Paciente.show_Paciente()

    def totalCostoSanSalvador(self):
        return 0

    def totalCostoConDescuento(self):
        return 0


class Paciente:
    def __init__(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        self.__nombre = nombre
        self.__lugar = lugar
        self.__descripcion = descripcion
        self.__costo = costo
        self.__conDescuento = conDescuento
        self.__descuento = descuento

    def get_nombre(self):
        return self.__nombre

    def get_lugar(self):
        return self.__lugar

    def get_descripcion(self):
        return self.__descripcion

    def get_costo(self):
        return self.__costo

    def get_conDescuento(self):
        return self.__conDescuento

    def get_descuento(self):
        return self.__descuento

    def show_Paciente(self):
        print(
            f"{self.get_nombre()}|{self.get_lugar()}|{self.get_descripcion()}|{self.get_costo()}|{self.get_conDescuento()}|{self.get_descuento()}"
        )


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""

# github url-->
def getGithubUrl():
    return "https://github.com/marianatudo/MarianaTudo_20192111.git"

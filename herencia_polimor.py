#EJERCICIO #1-JERARQUIA PERSONA ->PASAJERO/EMPLEADO
#Modela una empresa aérea con Persona como clase base y Pasajero y Empleado como hijas. Cada hija añade su propio atributo y método.

# 1) ENTENDER EL PROBLEMA

# Entrada - que me dan
# los datos de una persona mas los especificos

# Proceso - que hago con eso
# clase base con lo comun, hijas con lo especifico

# Salida - que debo mostrar
# presentacion adaptada a cada tipo
# Ejemplo de entrada:
# Pasajero Ana con reserva AB1
# Salida esperada:
# Pasajero Ana [reserva: AB1] · 500 millas


# 2) BOSQUEJO A MANO

# MOLDE (clase base Persona):
# nombre, cedula

# CLASE HIJA (Pasajero):
# Hereda nombre y cedula de Persona.
# Agrega codigo_reserva.
# Metodo sumar_millas().

# CLASE HIJA (Empleado):
# Hereda nombre y cedula de Persona.
# Agrega codigo_emp y salario.
# Metodo aumentar_salario().


# 3) DESCUBRIR EL PATRON

# Este es el ejemplo canonico. Veras la misma estructura
# en el proyecto de aerolinea del final.

# Fijate que __str__ se sobrescribe en cada hija:
# mismo nombre, comportamiento distinto.
# Eso es polimorfismo.


# 4) ESCRIBIR EL CODIGO

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cédula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)         # inicializa lo del padre
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"


p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)

p.sumar_millas(500)
e.aumentar_salario(10)

p.presentarse()                                   
e.presentarse()                                   


print(p)                                           
print(e)                                         

# Ahora tú
#Añade una clase Tripulante(Empleado) con rol (piloto, copiloto, azafata) y método horas_vuelo.

class Persona:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def presentarse(self):
        print(f"Soy {self.nombre}, cedula {self.cedula}")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


class Pasajero(Persona):
    def __init__(self, nombre, cedula, codigo_reserva):
        super().__init__(nombre, cedula)
        self.codigo_reserva = codigo_reserva
        self.millas = 0

    def sumar_millas(self, m):
        self.millas += m

    def __str__(self):
        return f"Pasajero {self.nombre} [reserva: {self.codigo_reserva}] · {self.millas} millas"


class Empleado(Persona):
    def __init__(self, nombre, cedula, codigo_emp, salario):
        super().__init__(nombre, cedula)
        self.codigo_emp = codigo_emp
        self.salario = salario

    def aumentar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"Empleado {self.nombre} [{self.codigo_emp}] · ${self.salario:.2f}"


class Tripulante(Empleado):
    def __init__(self, nombre, cedula, codigo_emp, salario, rol):
        super().__init__(nombre, cedula, codigo_emp, salario)
        self.rol = rol
        self.horas_vuelo = 0

    def registrar_horas_vuelo(self, horas):
        self.horas_vuelo += horas

    def __str__(self):
        return f"Tripulante {self.nombre} [{self.rol}] · {self.horas_vuelo} horas de vuelo · ${self.salario:.2f}"



p = Pasajero("Ana", "0912345678", "AB-1234")
e = Empleado("Luis", "0987654321", "EMP-01", 1200)
t = Tripulante("Carlos", "0923456789", "EMP-02", 1800, "piloto")

p.sumar_millas(500)
e.aumentar_salario(10)
t.aumentar_salario(10)
t.registrar_horas_vuelo(25)

# Todos heredan presentarse()
p.presentarse()
e.presentarse()
t.presentarse()

print(p)
print(e)
print(t)

#EJERCICIO #2)
#POLIMORFISMO CON FIGURAS GEOMÉTRICAS
#Clase base Figura con método area(). Clases hijas Rectangulo, Circulo, Triangulo que la implementan.

# 1) ENTENDER EL PROBLEMA

# Entrada - que me dan
# figuras de distinta forma

# Proceso - que hago con eso
# una lista mixta de figuras

# Salida - que debo mostrar
# las areas de todas, con un mismo bucle
# Ejemplo de entrada:
# 3 figuras distintas
# Salida esperada:
# Areas: 15, 78.54, 6


# 2) BOSQUEJO A MANO

# figuras = [Rectangulo(5,3), Circulo(5), Triangulo(4,3)]

# for f in figuras:
#     print(f.area())

# Resultado:
# 15, 78.54, 6
# Cada figura calcula su area de manera diferente.


# 3) DESCUBRIR EL PATRON

# El polimorfismo permite utilizar un mismo metodo
# en diferentes clases, aunque cada una lo ejecute
# de manera distinta.
#
# Todas las figuras tienen el metodo area(),
# pero cada figura utiliza su propia formula.


# 4) IMPLEMENTACION DEL CODIGO

import math

class Figura:
    def area(self):
        raise NotImplementedError("Cada figura debe implementar area()")

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

# --- Uso polimórfico ---
figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3)
]

for f in figuras:
    print(f"{type(f).__name__}: {f.area():.2f}")

# Rectangulo: 15.00
# Circulo: 78.54
# Triangulo: 6.00

# Y podemos sumar todas
total = sum(f.area() for f in figuras)
print(f"Área total: {total:.2f}")


#Ahora tú
#Añade el método perimetro() a las tres.
#Añade una nueva figura: Cuadrado (que hereda de Rectángulo).

import math


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio


class Triangulo:
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2


# CREAR LA LISTA DE FIGURAS

figuras = [
    Rectangulo(5, 3),
    Circulo(5),
    Triangulo(4, 3, 2, 3),
    Cuadrado(4)
]


# MOSTRAR AREAS Y PERIMETROS

for f in figuras:
    print(f"Area: {f.area():.2f}")
    print(f"Perimetro: {f.perimetro():.2f}")



#EJERCICIO #3)
#VEHICULO->AUTO/MOTO

# 1) ENTENDER EL PROBLEMA

# Entrada - que me dan
# Los datos de un vehiculo y sus caracteristicas especificas.

# Proceso - que hago con eso
# Crear una clase base Vehiculo con marca y modelo.
# Crear clases hijas Auto y Moto con sus atributos propios.

# Salida - que debo mostrar
# La informacion de cada vehiculo segun su tipo.
# Ejemplo de entrada:
# Auto Toyota Corolla con 4 puertas.
# Salida esperada:
# Toyota Corolla — 4 puertas


# 2) BOSQUEJO A MANO

# MOLDE (clase base Vehiculo):
# marca, modelo

# CLASE HIJA (Auto):
# Hereda marca y modelo de Vehiculo.
# Agrega puertas.
# Metodo __str__().

# CLASE HIJA (Moto):
# Hereda marca y modelo de Vehiculo.
# Agrega cilindraje.
# Metodo __str__().


# 3) DESCUBRIR EL PATRON

# La clase Vehiculo contiene los atributos comunes.
# Auto y Moto heredan esos atributos y agregan los suyos.
# Cada clase hija tiene su propia version de __str__().
# Esto es polimorfismo: cada objeto muestra su informacion
# de manera diferente.


# 4) IMPLEMENTACION DEL CODIGO

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def __str__(self):
        return f"{self.marca} {self.modelo} — {self.cilindraje}cc"

# --- Uso ---
auto = Auto("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR", 600)
for v in [auto, moto]:
    print(v)


#EJERCICIO #4)
# ANIMAL->PERRO/GATO/AVE

# 1) ENTENDER EL PROBLEMA

# Entrada - que me dan
# Los nombres de diferentes animales.

# Proceso - que hago con eso
# Crear una clase base Animal con el metodo hablar().
# Crear clases hijas que sobrescriban el metodo hablar()
# con el sonido propio de cada animal.

# Salida - que debo mostrar
# El nombre de cada animal junto con su sonido.
# Ejemplo de entrada:
# 3 animales: Rex, Felix y Piolin.
# Salida esperada:
# Rex: Guau, Felix: Miau, Piolin: Pio

# 2) BOSQUEJO A MANO

# MOLDE (clase base Animal):
# nombre
# Metodo hablar() que muestra "(sonido)".

# CLASE HIJA (Perro):
# Hereda nombre de Animal.
# Metodo hablar(): Guau.

# CLASE HIJA (Gato):
# Hereda nombre de Animal.
# Metodo hablar(): Miau.

# CLASE HIJA (Canario):
# Hereda nombre de Animal.
# Metodo hablar(): Pio.


# 3) DESCUBRIR EL PATRON

# La clase Animal tiene un metodo hablar() general.
# Cada clase hija sobrescribe ese metodo con su propio sonido.
# Esto es polimorfismo: un mismo metodo tiene diferentes
# comportamientos segun el objeto.


# 4) IMPLEMENTACION DEL CODIGO

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre}: (sonido)")

class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre}: ¡Guau!")

class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre}: Miau")

class Ave(Animal):
    def hablar(self):
        print(f"{self.nombre}: Pío pío")

# Uso polimórfico
animales = [Perro("Rex"), Gato("Felix"), Ave("Piolín")]
for a in animales:
    a.hablar()


# EJERCICIO #4)
#EMPLEADO-> POR HORAS/FIJO

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# Los datos de empleados con diferentes formas de pago.

# Proceso - que hago con eso
# Crear una clase base abstracta Empleado con el metodo
# sueldo_mensual().
# Crear clases hijas que calculen el sueldo de manera diferente.

# Salida - que debo mostrar
# El sueldo mensual de cada empleado.
# Ejemplo de entrada:
# Empleado por horas: 160 horas trabajadas × 8.
# Empleado fijo: sueldo de 1500.
# Salida esperada:
# 1280.00, 1500.00


# 2) BOSQUEJO A MANO
# MOLDE (clase base Empleado):
# nombre
# Metodo abstracto sueldo_mensual().

# CLASE HIJA (EmpleadoPorHoras):
# Hereda nombre de Empleado.
# Agrega horas_trabajadas y tarifa.
# Metodo sueldo_mensual() = horas_trabajadas * tarifa.

# CLASE HIJA (EmpleadoFijo):
# Hereda nombre de Empleado.
# Agrega sueldo_fijo.
# Metodo sueldo_mensual() = sueldo_fijo.

# 3) DESCUBRIR EL PATRON
# La clase Empleado define un metodo abstracto que obliga
# a las clases hijas a implementar su propio calculo.
# Cada empleado calcula su sueldo de manera diferente.


# 4) IMPLEMENTACION DEL CODIGO

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def sueldo_mensual(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nombre}: ${self.sueldo_mensual():.2f}"


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def sueldo_mensual(self):
        return self.horas * self.tarifa


class EmpleadoFijo(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)
        self.sueldo = sueldo

    def sueldo_mensual(self):
        return self.sueldo


# Nómina polimórfica
empleados = [
    EmpleadoPorHoras("Ana", 160, 8),
    EmpleadoFijo("Luis", 1500)
]

nomina = 0
for e in empleados:
    print(e)
    nomina += e.sueldo_mensual()

print(f"Total nómina: ${nomina:.2f}")
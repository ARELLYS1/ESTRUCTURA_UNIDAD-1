#EJERCICIO #1)
#CRUD DE PASAJEROS CON CLASE PASAJERO+LIST
#Sistema completo: agregar, listar, buscar por cédula, modificar y eliminar pasajeros. Usa clase Pasajero y una list como contenedor.

#1 "ENTENDER EL PROBLEMA:"
#--Entrada — qué me dan
# opción del menú y datos

#Proceso — qué hago con eso
#operaciones sobre la lista con validaciones

#Salida — qué debo mostrar
#resultado de cada acción

#2 "BOSQUEJO A MANO:"
#class Pasajero(nombre, cedula)

# lista = []
# menú:
#   1. Agregar    → lista.append(Pasajero(...))
#   2. Listar     → for p in lista: print(p)
#   3. Buscar     → next((p for p in lista if p.cedula==ced), None)
#   4. Modificar  → buscar + p.nombre = nuevo
#   5. Eliminar   → lista[:] = [p for p in lista if p.cedula != ced]
#   6. Salir      → break

#3 "DESCUBRIR EL PATRÓN:"
#El truco elegante para buscar es next((p for p in lista if p.cedula == ced), None):
# recorre la lista hasta encontrar el primero que cumple, o retorna None si no existe.

#Para eliminar hay dos formas: (a) lista.remove(p) con el objeto encontrado, o (b) reconstruir la lista sin él con list comprehension.
#  La segunda es más «pythonica».

#4 "ESCRIBIR EL CÓDIGO:"
class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        break

    # Ahora tú
#Añade una opción «Ordenar por nombre» que use lista.sort(key=lambda p: p.nombre).

class Pasajero:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"


def buscar_por_cedula(lista, ced):
    """Retorna el objeto o None."""
    return next((p for p in lista if p.cedula == ced), None)


# --- Programa principal ---
lista = []

while True:
    print("\n--- MENÚ ---")
    print("1.Agregar 2.Listar 3.Buscar 4.Modificar 5.Eliminar 6.Ordenar por nombre 7.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        ced = input("Cédula: ")
        if buscar_por_cedula(lista, ced):
            print("Ya existe un pasajero con esa cédula")
        else:
            lista.append(Pasajero(nom, ced))
            print("Agregado ✓")

    elif op == "2":
        if not lista:
            print("No hay pasajeros")
        for i, p in enumerate(lista):
            print(f"[{i}] {p}")

    elif op == "3":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        print(p if p else "No existe")

    elif op == "4":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            p.nombre = input("Nuevo nombre: ")
            print("Modificado ✓")
        else:
            print("No existe")

    elif op == "5":
        ced = input("Cédula: ")
        p = buscar_por_cedula(lista, ced)
        if p:
            lista.remove(p)
            print("Eliminado ✓")
        else:
            print("No existe")

    elif op == "6":
        if not lista:
            print("No hay pasajeros para ordenar")
        else:
            lista.sort(key=lambda p: p.nombre)
            print("Lista ordenada por nombre ✓")

    elif op == "7":
        break



# EJERCICIO #2)

#ESTADISTICA DE UNA LISTA DE NOTAS
#Dada una lista de N notas, calcular:
#  promedio, máxima, mínima, cantidad de aprobados y el nombre del mejor estudiante (paralelo con nombres).


#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# N, lista de nombres y lista de notas

# Proceso — qué hago con eso
# recorridos en paralelo para calcular estadísticas

# Salida — qué debo mostrar
# todas las métricas

#2 "BSOQUEJO A MANO:"
# nombres = ["Ana", "Luis", "Diana"]
# notas   = [ 8,     6,      10 ]

# promedio = (8+6+10) / 3 = 8.0
# máxima   = 10 (índice 2 → Diana)
# aprobados = 2 (8>=7, 10>=7)

#3 "DESCUBRIR EL PATRON:"
# Este ejercicio junta 4 patrones en uno: acumulador (suma), campeón (máximo), contador (aprobados) y búsqueda (nombre del máximo).

# Fíjate en el uso de listas paralelas: nombres[i] y notas[i] se refieren a la misma persona. 
# En el módulo siguiente verás cómo un dict o una clase mejora esto.

#4 "ESCRIBIR EL CODIGO:"
nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas   = [ 8,     6,      10,      7,      5]

# Python trae todo esto:
print(f"Promedio: {sum(notas) / len(notas):.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")

# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

print(f"\nManual → prom: {suma/len(notas):.2f}, máx: {maxima}, aprob: {aprob_manual}")



# Ahora tú
# Añade la desviación estándar. Fórmula: sqrt(sum((n - prom)² for n in notas) / len(notas)).
import math

nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
notas = [8, 6, 10, 7, 5]

# --- Versión Python (con funciones integradas y math) ---
prom = sum(notas) / len(notas)
desviacion = math.sqrt(sum((n - prom) ** 2 for n in notas) / len(notas))

print(f"Promedio: {prom:.2f}")
print(f"Máxima: {max(notas)}")
print(f"Mínima: {min(notas)}")
print(f"Desviación estándar: {desviacion:.2f}")

# Aprobados: filtro + len
aprobados = [n for n in notas if n >= 7]
print(f"Aprobados: {len(aprobados)} de {len(notas)}")

# Mejor estudiante: índice del máximo
idx_max = notas.index(max(notas))
print(f"Mejor: {nombres[idx_max]} con {notas[idx_max]}")


# --- Versión manual (para entender qué hace por dentro) ---
suma = 0
maxima = notas[0]
minima = notas[0]
idx_max_manual = 0
aprob_manual = 0

for i in range(len(notas)):
    suma += notas[i]
    if notas[i] > maxima:
        maxima = notas[i]
        idx_max_manual = i
    if notas[i] < minima:
        minima = notas[i]
    if notas[i] >= 7:
        aprob_manual += 1

prom_manual = suma / len(notas)

# Cálculo manual de la desviación estándar usando la fórmula
suma_cuadrados = 0
for n in notas:
    suma_cuadrados += (n - prom_manual) ** 2

desv_manual = (suma_cuadrados / len(notas)) ** 0.5

print(
    f"\nManual → prom: {prom_manual:.2f}, máx: {maxima}, "
    f"aprob: {aprob_manual}, desv: {desv_manual:.2f}"
)



#EJERCICIO #3)
#ORDENAR UNA LISTA (BUBBLE SORT)
#Implementar el algoritmo de ordenamiento burbuja sobre una lista. Luego comparar con list.sort().

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# una lista de números desordenada

# Proceso — qué hago con eso
# recorrer varias veces intercambiando pares consecutivos

# Salida — qué debo mostrar
# la lista ordenada

#2 "BSOQUEJO A MANO:"
#[5, 2, 8, 1, 9]

# Vuelta 1:
#   5>2 → swap → [2, 5, 8, 1, 9]
#   5<8 → nada
#   8>1 → swap → [2, 5, 1, 8, 9]
#   8<9 → nada
# Vuelta 2:
#   2<5 → nada
#   5>1 → swap → [2, 1, 5, 8, 9]
#   5<8, 8<9 → nada
# Vuelta 3:
#   2>1 → swap → [1, 2, 5, 8, 9]


#3 "DESCUBRIR EL PATRON:"
#El bubble sort funciona comparando parejas consecutivas y las intercambia si están 
# desordenadas. Después de cada vuelta, el más grande queda al final (por eso «burbuja»).

#Es lento (O(n²)) — solo se enseña por su claridad conceptual.
#  En la vida real siempre usa lista.sort().


#4 "ESCRIBIR EL CODIGO:"
def bubble_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for vuelta in range(n - 1):
        # Bandera para optimizar: si en una vuelta no hubo swaps, ya está ordenado
        hubo_swap = False
        for i in range(n - 1 - vuelta):
            if arr[i] > arr[i + 1]:
                # Intercambio en una línea
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hubo_swap = True
        if not hubo_swap:
            break
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión
ordenada = bubble_sort(notas)
print(ordenada)                            # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]                           # copia para no romper el original
copia.sort()
print(copia)                               # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)                               # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)                            # ['a', 'el', 'python', 'código']


#Ahora tú
#Implementa selection sort: en cada vuelta busca el mínimo del resto y lo coloca al inicio.
def selection_sort(lista):
    n = len(lista)
    # Copia para no modificar el original
    arr = lista[:]
    for i in range(n - 1):
        # Suponemos que el mínimo está en la posición actual
        min_idx = i
        # Buscamos el mínimo en el resto de la lista (desde i + 1 hasta el final)
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el mínimo encontrado con el elemento de la posición actual
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# --- Uso ---
notas = [5, 2, 8, 1, 9, 3, 7]

# Nuestra versión con Selection Sort
ordenada = selection_sort(notas)
print(ordenada)  # [1, 2, 3, 5, 7, 8, 9]

# La versión de Python (usa Timsort, mucho más rápido)
copia = notas[:]  # copia para no romper el original
copia.sort()
print(copia)  # [1, 2, 3, 5, 7, 8, 9]

# Descendente
copia.sort(reverse=True)
print(copia)  # [9, 8, 7, 5, 3, 2, 1]

# Ordenar por criterio (ej. por longitud del string)
palabras = ["python", "a", "código", "el"]
palabras.sort(key=len)
print(palabras)  # ['a', 'el', 'python', 'código']



# EJERCICIO #4
#CONTAR APARICIONES DE UN VALOR
#Dada una lista de números y un valor, contar cuántas veces aparece.

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números y un valor a buscar (v)

# Proceso — qué hago con eso
# Recorrer la lista elemento por elemento comparando si cada número es igual a v, 
# o usar el método nativo de Python para contar ocurrencias.

# Salida — qué debo mostrar
# El número total de veces que aparece el valor en la lista.


#2 "BOSQUEJO A MANO:"
# lista = [1, 3, 2, 3, 4, 3, 5], v = 3
# count = 0

# x = 1 → 1 == 3 (Falso)  → count = 0
# x = 3 → 3 == 3 (Verdadero) → count = 1
# x = 2 → 2 == 3 (Falso)  → count = 1
# x = 3 → 3 == 3 (Verdadero) → count = 2
# x = 4 → 4 == 3 (Falso)  → count = 2
# x = 3 → 3 == 3 (Verdadero) → count = 3
# x = 5 → 5 == 3 (Falso)  → count = 3

# Resultado final: 3 aparece 3 veces.


#3 "DESCUBRIR EL PATRON:"
# El conteo manual recorre linealmente la estructura acumulando coincidencias en una variable de control.
# Python encapsula esta lógica repetitiva de manera ultra eficiente en el método incorporado `lista.count(v)`, 
# el cual está escrito y optimizado en C por debajo.


#4 "ESCRIBIR EL CODIGO:"
lista = [1, 3, 2, 3, 4, 3, 5]
v = 3

# Manual
count = 0
for x in lista:
    if x == v:
        count += 1
print(f"{v} aparece {count} veces")

# Pythonic
print(f"{v} aparece {lista.count(v)} veces")



#EJERCICIO #5)
#INVERTIR UNA LISTA
#Invertir el orden de una lista sin usar lista.reverse().

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de elementos.

# Proceso — qué hago con eso
# Invertir el orden de sus elementos recorriendo índices hacia atrás o usando funciones nativas.

# Salida — qué debo mostrar
# Una nueva lista con los elementos en orden inverso.


#2 "BOSQUEJO A MANO:"
# lista = [1, 2, 3, 4, 5]
# Bucle con range(4, -1, -1) (índices: 4, 3, 2, 1, 0)
# i = 4 → 5
# i = 3 → 4
# i = 2 → 3
# i = 1 → 2
# i = 0 → 1
# Resultado: [5, 4, 3, 2, 1]


#3 "DESCUBRIR EL PATRON:"
# Recorrer la lista de atrás hacia adelante muestra cómo funcionan los índices inversos,
# pero Python lo resuelve de forma directa con slicing ([::-1]) o con la función `reversed()`.


#4 "ESCRIBIR EL CODIGO:""
lista = [1, 2, 3, 4, 5]

# Con bucle
invertida = []
for i in range(len(lista) - 1, -1, -1):
    invertida.append(lista[i])
print(invertida)

# Con slicing (pythonic)
print(lista[::-1])

# Con reversed
print(list(reversed(lista)))



# EJERCICIO #6)
#NUMEROS UNICOS
#Dada una lista con posibles duplicados, retornar una lista sin duplicados manteniendo el orden.

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números con elementos duplicados.

# Proceso — qué hago con eso
# Filtrar los duplicados ya sea de forma manual comprobando existencia, 
# convirtiendo a un conjunto (set) o usando un diccionario (dict.fromkeys).

# Salida — qué debo mostrar
# Una lista limpia únicamente con los elementos únicos.


#2 "BOSQUEJO A MANO:"
# nums = [1, 3, 2, 3, 4, 1, 5, 2]
# unicos = []

# x = 1 → no está → unicos = [1]
# x = 3 → no está → unicos = [1, 3]
# x = 2 → no está → unicos = [1, 3, 2]
# x = 3 → ya está → se omite
# x = 4 → no está → unicos = [1, 3, 2, 4]
# x = 1 → ya está → se omite
# x = 5 → no está → unicos = [1, 3, 2, 4, 5]
# x = 2 → ya está → se omite

# Resultado final: [1, 3, 2, 4, 5]


#3 "DESCUBRIR EL PATRON:"
# Filtrar manualmente preserva el orden iterando y validando duplicados. 
# Usar `set()` es muy rápido pero desordena los elementos. 
# `dict.fromkeys()` es la solución ideal en Python para eliminar duplicados de forma rápida y manteniendo el orden original.


#4 "ESCRIBIR EL CODIGO:"
nums = [1, 3, 2, 3, 4, 1, 5, 2]

# Manual (mantiene orden)
unicos = []
for x in nums:
    if x not in unicos:
        unicos.append(x)
print(unicos)                       # [1, 3, 2, 4, 5]

# Rápido (NO mantiene orden)
print(list(set(nums)))

# Rápido MANTENIENDO orden (Python 3.7+)
print(list(dict.fromkeys(nums)))    # [1, 3, 2, 4, 5]



# EJERCICIO #7)
#SEGUNDO MAYOR
#Encontrar el segundo número más grande de una lista (sin ordenar toda la lista).

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Una lista de números desordenada.

# Proceso — qué hago con eso
# Recorrer la lista una sola vez manteniendo dos variables de control (el mayor y el segundo mayor), 
# actualizándolas conforme encontramos números más grandes.

# Salida — qué debo mostrar
# El número mayor y el segundo mayor valor de la lista.


#2 "BOSQUEJO A MANO:"
# nums = [5, 2, 9, 7, 9, 3, 8]
# Inicial: mayor = -inf, segundo = -inf

# n = 5 → 5 > mayor (-inf) → segundo = -inf, mayor = 5
# n = 2 → 2 > 5 (no), 2 > -inf y 2 < 5 → segundo = 2 (mayor = 5)
# n = 9 → 9 > 5 (sí) → segundo = 5, mayor = 9
# n = 7 → 7 > 9 (no), 7 > 5 y 7 < 9 → segundo = 7 (mayor = 9)
# n = 9 → 9 > 9 (no), 9 > 7 y 9 < 9 (falso) → sin cambios
# n = 3 → 3 > 9 (no), 3 > 7 (falso) → sin cambios
# n = 8 → 8 > 9 (no), 8 > 7 y 8 < 9 → segundo = 8 (mayor = 9)

# Resultado final: Mayor: 9, Segundo: 8.


#3 "DESCUBRIR EL PATRON:"
# Rastrear los dos valores más altos en una sola pasada ($O(n)$) evita ordenar la lista completa, 
# actualizando de forma inteligente al campeón actual y desplazando al anterior al puesto de segundo.


#4 "ESCRIBIR EL CODIGO:"
nums = [5, 2, 9, 7, 9, 3, 8]

# Dos campeones: mayor y segundo
mayor = float("-inf")
segundo = float("-inf")

for n in nums:
    if n > mayor:
        segundo = mayor         # el que era mayor pasa a segundo
        mayor = n
    elif n > segundo and n < mayor:
        segundo = n

print(f"Mayor: {mayor}")
print(f"Segundo: {segundo}")



#EJERCICIO #8)
#FUSIONAR DOS LISTAS ORDENADAS
#Dadas dos listas ordenadas, fusionarlas en una tercera también ordenada, sin usar sort()

#1 "ENTENDER EL PROBLEMA:"
# Entrada — qué me dan
# Dos listas ordenadas de números (a y b).

# Proceso — qué hago con eso
# Recorrer ambas listas simultáneamente usando dos punteros (i, j), 
# comparando los elementos actuales y añadiendo el menor a una lista de resultados, 
# para finalmente anexar los elementos restantes de la lista que no haya terminado.

# Salida — qué debo mostrar
# Una única lista fusionada que mantiene el orden ascendente.


#2 "BOSQUEJO A MANO:"
# a = [1, 3, 5, 7], b = [2, 4, 6, 8, 10]
# i = 0 (1), j = 0 (2), resultado = []

# i=0, j=0: 1 <= 2 → resultado = [1], i = 1
# i=1, j=0: 3 <= 2 (Falso) → resultado = [1, 2], j = 1
# i=1, j=1: 3 <= 4 → resultado = [1, 2, 3], i = 2
# i=2, j=1: 5 <= 4 (Falso) → resultado = [1, 2, 3, 4], j = 2
# i=2, j=2: 5 <= 6 → resultado = [1, 2, 3, 4, 5], i = 3
# i=3, j=2: 7 <= 6 (Falso) → resultado = [1, 2, 3, 4, 5, 6], j = 3
# i=3, j=3: 7 <= 8 → resultado = [1, 2, 3, 4, 5, 6, 7], i = 4 (Fin de 'a')
# Fin del while. Añadimos restos: resultado.extend(b[3:]) → añade [8, 10]

# Resultado final: [1, 2, 3, 4, 5, 6, 7, 8, 10]


#3 "DESCUBRIR EL PATRON:"
# Fusionar listas con dos punteros permite combinar secuencias ordenadas de forma muy eficiente ($O(n + m)$), 
# seleccionando siempre el valor menor y vaciando los elementos sobrantes al final.


#4 "ESCRIBIR EL CODIGO:"
a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 10]

resultado = []
i = j = 0

# Recorremos las dos listas a la par
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        resultado.append(a[i])
        i += 1
    else:
        resultado.append(b[j])
        j += 1

# Añadimos lo que quede de la más larga
resultado.extend(a[i:])
resultado.extend(b[j:])

print(resultado)                    # [1, 2, 3, 4, 5, 6, 7, 8, 10]
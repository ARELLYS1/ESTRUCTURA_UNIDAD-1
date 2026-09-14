#FUNCIONES:
#Fragmentar el programa en piezas reutilizables. 

#EJERCICIO1:FUNCIÓN PARA CALCULAR EL IVA:
#Escribir una función calcular_iva(precio) que reciba un precio y retorne el IVA (15%).

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #precio(input)

    #2:"PROCESO"--QUE HAGO CON ESO
    #multiplicar por 0.15 dentro de la función

    #3:"SALIDA"--QUE DEBO MOSTRAR
    #el IVA calculado

#2->BOSQUEJO A MANO
    #def calcular_iva(precio):
   # return precio * 0.15

   #iva = calcular_iva(80)
   #imprimo iva

#3->DESCUBRIR EL PATRÓN
    #a función se puede reusar en 100 sitios distintos
    #cada uno decide si mostrar, sumar, guardar o comparar el resultado.

#4->ESCRIBIR EL CÓDIGO
def calcular_iva(precio):
    return precio * 0.15

precio = float(input("Ingrese el precio: "))
iva = calcular_iva(precio)
print(f"IVA DE : {precio} : {iva:.2f}")

#AHORA TÚ:Amplíala: define calcular_total(precio) que retorne precio + IVA usando la función anterior.

def calcular_iva(precio):
    return precio * 0.15

def calcular_total(precio):
     return precio + calcular_iva(precio)

precio = float(input("Ingrese el precio: "))
iva = calcular_iva(precio)
total = calcular_total(precio)

print(f"IVA DE : {precio} : {iva:.2f}")
print(f"EL TOTAL A PAGAR ES: {total:.2f}")
#_______________________________________________________________________________________________________________________


#EJERCICIO_2:Funcion es_primo(n):
#Escribir una función que reciba un número y retorne True si es primo, False si no.

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #numero(input)

    #2:"PROCESO"--QUE HAGO CON ESO
    #el algoritmo del módulo 3 dentro de la función

    #3:"SALIDA"--QUE DEBO MOSTRAR
    #True o False

#2->BOSQUEJO A MANO
# es_primo(7) → devuelve True
# es_primo(10) → devuelve False
# es_primo(1) → devuelve False

# Uso: if es_primo(numero): ...

#3->DESCUBRIR EL PATRON
    #realizar un bucle que compruebe si el numero ingresado es primo o no.

#4->ESCRIBIR EL CÓDIGO

def es_primo(n):
     if n < 2:
         return False
     for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
             return False           
     return True                   

num = int(input("Número: "))
if es_primo(num):
     print(f"{num} es primo")
else:
     print(f"{num} NO es primo")


#AHORA TU:
#Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.

def es_primo(n):
     if n < 2:
        return False
     for i in range(2, int(n ** 0.5) + 1):
         if n % i == 0:
             return False
     return True

def contar_primos(a, b):
     contador = 0
     for num in range(a, b + 1):
         if es_primo(num):
             contador += 1
     return contador

# # Prueba
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
print(f"Cantidad de primos entre {a} y {b}: {contar_primos(a, b)}")
#_________________________________________________________________________________________________________

#EJERCICIO_3:SUMA DE DÍGITOS CON FUNCION RECURSIVA
#Escribir una función suma_digitos(n) que retorne la suma de los dígitos de un número.

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #numero(input)

    #2:"PROCESO"--QUE HAGO CON ESO
    #extraer dígitos con % y //, acumular

    #3:"SALIDA"--QUE DEBO MOSTRAR
    #la suma de los dígitos

#2->BOSQUEJO A MANO
# suma_digitos(4783):
#   suma = 0
#   4783 % 10 = 3   → suma = 3,  n = 478
#    478 % 10 = 8   → suma = 11, n = 47
#     47 % 10 = 7   → suma = 18, n = 4
#      4 % 10 = 4   → suma = 22, n = 0
#   fin → return 22

#3->DESCUBRIR EL PATRON
    #Debemos usar un acumulador para ir sumando +1 cada vez que haya numeros primos

#4->ESCRIBIR EL CÓDIGO

def suma_digitos(n):
     n = abs(n)                     
     suma = 0
     while n > 0:
         suma += n % 10            
n = n // 10                
return suma

num = int(input("Número: "))
print(f"Suma: {suma_digitos(num)}")


#AHORA TU:
#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos elevados al número de dígitos.
# Ej.: 153 = 1³+5³+3³.

def es_narcisista(n):
    digitos = str(n)
    num_digitos = len(digitos)
suma = 0
for d in digitos:
         suma += int(d) ** num_digitos
return suma == n

n = int(input("Ingrese un número: "))
if es_narcisista(n):
     print(f"{n} es narcisista")
else:
     print(f"{n} no es narcisista")
#____________________________________________________________________________________________________________________________


#EJERCICIO_4:MENÚ MODULAR CON FUNCIONES:
#Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #opciones del menú

    #2:"PROCESO"--QUE HAGO CON ESO
    #función por opción, menú principal que las llama

    #3:"SALIDA"--QUE DEBO MOSTRAR
    #el resultado de cada opción

#2->BOSQUEJO A MANO
    # saludar()   → pide nombre, muestra saludo
    # despedir()  → pide nombre, muestra despedida
    # menu()      → muestra opciones y llama a la función correcta

#3->DESCUBRIR EL PATRON
    #Dividir el programa en funciones lo vuelve mantenible: cada función hace UNA cosa; el bucle principal solo despacha.
    #Además cada función se puede probar por separado.

#4->ESCRIBIR EL CÓDIGO

def saludar():
     nombre = input("Nombre: ")
     print(f"¡Hola, {nombre}!")

def despedir():
     nombre = input("Nombre: ")
     print(f"¡Adiós, {nombre}!")

def mostrar_menu():
     print("\n--- MENÚ ---")
     print("1. Saludar")
     print("2. Despedir")
     print("3. Salir")

# # Programa principal

while True:
     mostrar_menu()
     opcion = input("Opción: ")
     if opcion == "1":
         saludar()
     elif opcion == "2":
         despedir()
     elif opcion == "3":
        print("Adiós")
break
      else
        print("Opción inválida")

    
#AHORA TU:
#Añade una función calcular() que pida dos números y muestre suma, resta, multiplicación y división. Nueva opción del menú.
# def saludar():
#     nombre = input("Nombre: ")
#     print(f"¡Hola, {nombre}!")

# def despedir():
#     nombre = input("Nombre: ")
#     print(f"¡Adiós, {nombre}!")

# def calcular():
#     n1 = float(input("Ingrese el primer número: "))
#     n2 = float(input("Ingrese el segundo número: "))
#     suma = n1 + n2
#     resta = n1 - n2
#     mult = n1 * n2
#     print(f"Suma: {suma}")
#     print(f"Resta: {resta}")
#     print(f"Multiplicación: {mult}")
#     if n2 != 0:
#         div = n1 / n2
#         print(f"División: {div:.2f}")
#     else:
#         print("División: No se puede dividir entre 0")

# def mostrar_menu():
#     print("\n--- MENÚ ---")
#     print("1. Saludar")
#     print("2. Despedir")
#     print("3. Calcular")
#     print("4. Salir")

# # Programa principal
# while True:
#     mostrar_menu()
#     opcion = input("Opción: ")
#     if opcion == "1":
#         saludar()
#     elif opcion == "2":
#         despedir()
#     elif opcion == "3":
#         calcular()
#     elif opcion == "4":
#         print("Adiós")
#         break
#     else:
#         print("Opción inválida")
#_____________________________________________________________________________________________


#EJERCICIO_5:FUNCIÓN AREA DE RECTÁNDULO:
#Función area_rectangulo(base, altura) que retorne el área.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #base y altura (parámetros de la función)

    #"PROCESO"--QUE HAGO CON ESO
    #multiplicar base * altura

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL ÁREA DEL RECTÁNGULO

#2->BOSQUEJO A MANO
    #base=5, altura=3
    #area = 5 * 3 = 15

    #base=4.5, altura=2
    #area = 4.5 * 2 = 9.0

#3->DESCUBRIR EL PATRÓN
    #Función simple que aplica una fórmula matemática directa,
    #sin condicionales ni bucles. El tipo de dato de salida
    #depende del tipo de los parámetros (int*int=int, float*int=float).

#4->ESCRIBIR EL CODIGO
# def area_rectangulo(base, altura):
#     return base * altura

# area = area_rectangulo(3, 5)
# print(area)
#__________________________________________________________________________________________________

#EJERCICIO_6:FUNCION MAXIMO DE TRES
#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #a, b, c (tres números, parámetros de la función)

    #"PROCESO"--QUE HAGO CON ESO
    #comparar los tres valores para encontrar el mayor
    #(usando max() o comparaciones manuales con if)

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL VALOR MÁS GRANDE DE LOS TRES

#2->BOSQUEJO A MANO
    #a=5, b=9, c=3
    #maximo(): max(5,9,3) -> compara los 3 de una vez -> 9

    #maximo_manual():
    #mayor = a = 5
    #b > mayor? 9 > 5 -> SÍ -> mayor = 9
    #c > mayor? 3 > 9 -> NO -> mayor sigue siendo 9
    #retorna 9

#3->DESCUBRIR EL PATRÓN
    #maximo_manual() usa el patrón de "mejor hasta ahora": guarda un
    #valor inicial (a) y lo va reemplazando solo si encuentra algo
    #mayor. Este mismo patrón sirve para encontrar el mínimo (cambiando
    #> por <) o el mayor/menor de una lista completa con un bucle.

#4->ESCRIBIR EL CODIGO
# def maximo(a, b, c):
#     return max(a, b, c)        

# # O manualmente:
# def maximo_manual(a, b, c):
#     mayor = a
#     if b > mayor: mayor = b
#     if c > mayor: mayor = c
#     return mayor

# print(maximo(5, 9, 3))          
# print(maximo_manual(5, 9, 3))  
#______________________________________________________________________________________________

#EJERCICIO_7: funcion es_bisiesto(año)

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #anio (parámetro de la función)

    #"PROCESO"--QUE HAGO CON ESO
    #verificar reglas de años bisiestos con % (divisible entre 400,
    #100 y 4), en ese orden específico

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #TRUE SI ES BISIESTO, FALSE SI NO LO ES

#2->BOSQUEJO A MANO
    #anio=2025
    #2025 % 400 == 0? 2025/400=5.06... NO
    #2025 % 100 == 0? 2025/100=20.25... NO
    #2025 % 4   == 0? 2025/4=506.25... NO
    #no cumplió ninguna condición -> return False

#3->DESCUBRIR EL PATRÓN
    #Cadena de if independientes (no elif) que retorna apenas se
    #cumple una condición, cortando la ejecución con return.
    #El orden importa: primero se descartan las excepciones (400, 100)
    #antes de aplicar la regla general (4), porque no todo múltiplo
    #de 4 es bisiesto (ej. 1900 es múltiplo de 4 y 100, pero no de 400).

#4->ESCRIBIR EL CODIGO
# def es_bisiesto(anio):
#     if anio % 400 == 0:
#         return True
#     if anio % 100 == 0:
#         return False
#     if anio % 4 == 0:
#         return True
#     return False

# siono = es_bisiesto(2025)
# print(siono)
#___________________________________________________________________________________________


#EJERCICIO_8:FUNCION FACTORIAL Y COMBINATORIA
#Función factorial(n) y luego combinatoria(n, k) = n! / (k! · (n-k)!).

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #n (para factorial) / n, k (para combinatoria)

    #"PROCESO"--QUE HAGO CON ESO
    #factorial: multiplicar sucesivamente de 2 hasta n
    #combinatoria: usar factorial() para aplicar la fórmula
    #n! / (k! * (n-k)!)

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL FACTORIAL DE N / EL NÚMERO DE COMBINACIONES POSIBLES

#2->BOSQUEJO A MANO
    #factorial(5):
    #fact=1
    #i=2: fact=1*2=2
    #i=3: fact=2*3=6
    #i=4: fact=6*4=24
    #i=5: fact=24*5=120
    #retorna 120

    #combinatoria(5,2):
    #factorial(5)=120, factorial(2)=2, factorial(5-2)=factorial(3)=6
    #resultado = 120 // (2 * 6) = 120 // 12 = 10

#3->DESCUBRIR EL PATRÓN
    #factorial() acumula un producto con un bucle (patrón "acumulador",
    #similar a sumar pero con *= en vez de +=, empezando en 1 y no en 0).
    #combinatoria() reutiliza factorial() tres veces en vez de reescribir
    #la lógica del producto, igual que calcular_total() reutilizaba
    #calcular_iva().

#4->ESCRIBIR EL CODIGO
# def factorial(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact *= i
#     return fact

# def combinatoria(n, k):
#     return factorial(n) // (factorial(k) * factorial(n - k))

# # Uso
# print(factorial(5))            # 120
# print(combinatoria(5, 2))      # 10 = 5!/(2!·3!) = 120/12
#______________________________________________________________________________________________________________

#EJERCICIO-9: CALCULADORA MODULAR:
#Programa que use funciones separadas para cada operación (sumar, restar, multiplicar, dividir) y un menú que llame a la correcta.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #op (opción del menú), a y b (números), todo por input

    #"PROCESO"--QUE HAGO CON ESO
    #según "op", llamar a la función correspondiente (sumar, restar,
    #multiplicar o dividir) y validar división entre 0 con None

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL RESULTADO DE LA OPERACIÓN ELEGIDA (o mensaje de error si aplica)

#2->BOSQUEJO A MANO
    #op="1", a=8, b=3
    #op == "5"? NO -> continúa
    #op == "1"? SÍ -> r = sumar(8, 3) = 8 + 3 = 11
    #(no entra a los elif de "2","3","4")
    #print -> "Resultado: 11.0"  (float porque a y b son float)

#3->DESCUBRIR EL PATRÓN
    #Es el patrón de "menú con funciones" (como saludar/despedir),
    #combinado con el patrón de "valor centinela" (None) para señalar
    #un caso inválido sin usar excepciones, y "continue" para saltar
    #el print final cuando hubo un error.

#4->ESCRIBIR EL CODIGO
# def sumar(a, b): return a + b
# def restar(a, b): return a - b
# def multiplicar(a, b): return a * b
# def dividir(a, b):
#     if b == 0:
#         return None          
#     return a / b

# while True:
#     print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
#     op = input("Opción: ")
#     if op == "5":
#         break
#     a = float(input("a: "))
#     b = float(input("b: "))
#     if op == "1": r = sumar(a, b)
#     elif op == "2": r = restar(a, b)
#     elif op == "3": r = multiplicar(a, b)
#     elif op == "4":
#         r = dividir(a, b)
#         if r is None:
#             print("No se puede dividir entre 0")
#             continue
#     else:
#         print("Opción inválida"); continue
#     print(f"Resultado: {r}")
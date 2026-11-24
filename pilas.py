#EJERCICIO #1)
#INVERTIR UNA CADENA CON PILA
#Usar una pila para invertir una cadena de texto.

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# una cadena

# Proceso - que hago con eso
# empujar cada letra a la pila, luego desapilar hasta vaciarla

# Salida - que debo mostrar
# la cadena al reves
# Ejemplo de entrada:
# s = "Python"
# Salida esperada:
# nohtyP

# 2) BOSQUEJO A MANO

# s = "Python"

# Push cada letra:
# push('P') -> [P]
# push('y') -> [P, y]
# ...
# push('n') -> [P, y, t, h, o, n]
# (tope = n)

# Pop y concatenar:
# pop() = n -> "n"
# pop() = o -> "no"
# ...
# resultado: "nohtyP"


# 3) DESCUBRIR EL PATRON

# Este es el ejemplo clasico. Muestra el corazon del LIFO:
# lo primero que entro (P) sale al final,
# lo ultimo que entro (n) sale primero.
#
# Nota que Python tiene s[::-1] que hace lo mismo
# en una linea, pero el ejercicio busca entender la pila.


# 4) ESCRIBIR EL CODIGO

from collections import deque


def invertir_con_pila(s):
    pila = deque()

    # Fase 1: apilar todas las letras
    for letra in s:
        pila.append(letra)

    # Fase 2: desapilar formando la salida
    resultado = ""
    while pila:
        resultado += pila.pop()

    return resultado


print(invertir_con_pila("Python"))    # nohtyP
print(invertir_con_pila("Hola"))      # aloH


# Comparacion con la version pythonic
print("Python"[::-1])                 # nohtyP


#Ahora tú
#Adaptarlo para invertir solo palabras (no caracteres): 
#"Hola Mundo" → "Mundo Hola". Pista: split(" ").

from collections import deque


def invertir_con_pila(s):
    pila = deque()

    # Fase 1: apilar todas las palabras
    for palabra in s.split(" "):
        pila.append(palabra)

    # Fase 2: desapilar formando la salida
    resultado = []
    while pila:
        resultado.append(pila.pop())

    return " ".join(resultado)


print(invertir_con_pila("Hola Mundo"))    # Mundo Hola
print(invertir_con_pila("Python es genial"))  # genial es Python


#EJERCICIO #2)
#VERIFICAR PARENTESIS BALANCEADOS
#Dada una expresión con paréntesis, corchetes y llaves, verificar que estén correctamente balanceados y anidados.

# 1) ENTENDER EL PROBLEMA

# Entrada - que me dan
# una cadena con simbolos

# Proceso - que hago con eso
# usar una pila: apilar aperturas, al cerrar comprobar match

# Salida - que debo mostrar
# True si esta balanceado, False si no

# Ejemplo de entrada
# s = "({[]})"

# Salida esperada
# True


# 2) BOSQUEJO A MANO

# "({[]})"

# ( -> push  -> pila: [(]
# { -> push  -> pila: [(, {]
# [ -> push  -> pila: [(, {, []
# ] -> pop [ -> match -> pila: [(, {]
# } -> pop { -> match -> pila: [(]
# ) -> pop ( -> match -> pila: []

# Pila vacia al final -> balanceado

# Ejemplo malo:
# "({[)]}"
# [ -> push
# ) -> pop [ -> NO match
# Resultado: False


# 3) DESCUBRIR EL PATRON

# Este es el uso clasico de la pila.
# Cada vez que veo una apertura, la apilo.
# Cada vez que veo un cierre, el tope de la pila
# debe ser su pareja.
#
# Al final la pila debe quedar vacia.
# Si sobra algo, hay una apertura sin cerrar.


# 4) ESCRIBIR EL CODIGO

from collections import deque


def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}  # cierre -> apertura

    for ch in s:
        if ch in "([{":
            # Es apertura, la apilo
            pila.append(ch)

        elif ch in ")]}":
            # Es cierre, el tope debe ser su pareja
            if not pila or pila.pop() != parejas[ch]:
                return False

    # Al final: si sobra algo en la pila, hay aperturas sin cerrar
    return len(pila) == 0


# Pruebas

tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]

for t in tests:
    print(f"{t!r:15} -> {paren_balanceado(t)}")


# Ahora tú
#Amplíalo para reportar la posición del error cuando no está balanceado.

from collections import deque


def paren_balanceado(s):
    pila = deque()
    parejas = {")": "(", "]": "[", "}": "{"}  # cierre -> apertura

    for i, ch in enumerate(s):
        if ch in "([{":
            # Es apertura, la apilo
            pila.append((ch, i))

        elif ch in ")]}":
            # Es cierre, tope debe ser su pareja
            if not pila:
                return f"Error en posicion {i}: cierre sin apertura"

            apertura, posicion = pila.pop()

            if apertura != parejas[ch]:
                return f"Error en posicion {i}: se esperaba cerrar {apertura}"

    # Comprobar si quedaron aperturas sin cerrar
    if pila:
        apertura, posicion = pila[-1]
        return f"Error en posicion {posicion}: apertura sin cerrar"

    return "Balanceado"


# Pruebas

tests = ["()", "({[]})", "()[]{}", "(]", "({[)]}", "((("]

for t in tests:
    print(f"{t!r:15} -> {paren_balanceado(t)}")


# EJERCICIO #3)
# DECIMAL A BINARIO CON PILA
#Convertir un número decimal a binario usando el algoritmo de divisiones sucesivas por 2.
# Los residuos se apilan y al final se leen al revés (desapilando).

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# un entero positivo

# Proceso - que hago con eso
# dividir sucesivamente entre 2, apilar residuos, luego desapilar

# Salida - que debo mostrar
# el numero en binario
# Ejemplo de entrada
# n = 13
# Salida esperada
# 1101

# 2) BOSQUEJO A MANO

# 13 / 2 = 6, sobra 1 -> push 1 -> pila: [1]
# 6 / 2 = 3, sobra 0 -> push 0 -> pila: [1, 0]
# 3 / 2 = 1, sobra 1 -> push 1 -> pila: [1, 0, 1]
# 1 / 2 = 0, sobra 1 -> push 1 -> pila: [1, 0, 1, 1]

# Ahora desapilo: 1, 1, 0, 1 -> "1101"


# 3) DESCUBRIR EL PATRON

# Los residuos se generan del bit menos significativo
# al mas significativo, pero el binario se lee al reves.
# Por eso la pila permite obtener el orden correcto.
# Podriamos usar bin(13) -> '0b1101',
# pero el ejercicio es entender el mecanismo.


# 4) ESCRIBIR EL CODIGO

from collections import deque


def decimal_a_binario(n):
    if n == 0:
        return "0"

    pila = deque()

    while n > 0:
        residuo = n % 2
        pila.append(residuo)
        n = n // 2

    # Desapilar y armar el resultado
    binario = ""

    while pila:
        binario += str(pila.pop())

    return binario


# Pruebas

for n in [0, 1, 5, 13, 100, 255]:
    print(f"{n:4d} -> {decimal_a_binario(n)}")


# Verificar con la nativa
print(bin(13))          # 0b1101


# EJERCICIO #4)
# CTRL + Z DE ACCIONES 
#Programa que use una pila para historial: opciones «Hacer acción», «Deshacer», «Ver historial».

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# acciones que realiza el usuario

# Proceso - que hago con eso
# guardar las acciones en una pila y eliminar la ultima cuando se deshace

# Salida - que debo mostrar
# mostrar las acciones realizadas y el historial actualizado
# Ejemplo de entrada
# hacer A, hacer B, deshacer
# Salida esperada
# Historial: [A]

# 2) BOSQUEJO A MANO
# Hacer accion A -> push A -> Pila: [A]
# Hacer accion B -> push B -> Pila: [A, B]
# Deshacer -> pop B -> Pila: [A]


# 3) DESCUBRIR EL PATRON
# Una pila trabaja con el principio LIFO:
# el ultimo elemento en entrar es el primero en salir.
# append() permite agregar una accion a la pila.
# pop() permite eliminar la ultima accion agregada.
# Por eso, al deshacer, se elimina la accion mas reciente.


# 4) ESCRIBIR EL CODIGO

from collections import deque

historial = deque()

while True:
    print("\n1. Hacer accion")
    print("2. Deshacer")
    print("3. Ver historial")
    print("4. Salir")

    op = input("Opcion: ")

    if op == "1":
        accion = input("Descripcion: ")
        historial.append(accion)
        print(f"Hecho: {accion}")

    elif op == "2":
        if not historial:
            print("Nada que deshacer")
        else:
            deshecha = historial.pop()
            print(f"Deshecho: {deshecha}")

    elif op == "3":
        if not historial:
            print("(vacio)")
        else:
            print("Historial:", list(historial))

    elif op == "4":
        print("Saliendo...")
        break

    else:
        print("Opcion no valida")



# EJERCICIO #5)
#INVERTIR ORDEN DE PALABRAS EN UNA FRASE
#Usar una pila para invertir el ORDEN de las palabras (no las letras).

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# una frase con varias palabras

# Proceso - que hago con eso
# separar las palabras, guardarlas en una pila y desapilarlas

# Salida - que debo mostrar
# la frase con las palabras en orden inverso
# Ejemplo de entrada
# s = "Hola Mundo desde Python"
# Salida esperada
# Python desde Mundo Hola

# 2) BOSQUEJO A MANO
# Frase: Hola Mundo desde Python
# Separar las palabras:
# Hola -> push
# Mundo -> push
# desde -> push
# Python -> push
# Pila: [Hola, Mundo, desde, Python]

# Desapilar:
# Python -> pop
# desde -> pop
# Mundo -> pop
# Hola -> pop
# Resultado: Python desde Mundo Hola

# 3) DESCUBRIR EL PATRON
# La pila trabaja con el principio LIFO:
# el ultimo elemento en entrar es el primero en salir.
# split() separa la frase en palabras.
# append() agrega cada palabra a la pila.
# pop() extrae las palabras en orden inverso.
# join() une las palabras para formar la frase final.


# 4) ESCRIBIR EL CODIGO
from collections import deque


def invertir_palabras(frase):
    pila = deque()

    for palabra in frase.split():
        pila.append(palabra)

    resultado = []

    while pila:
        resultado.append(pila.pop())

    return " ".join(resultado)


# Prueba

print(invertir_palabras("Hola Mundo desde Python"))

# Salida: Python desde Mundo Hola



#EJERCICIO #6)
# ES PALINDROMO?
#Verificar si una palabra es palíndromo (se lee igual al derecho y al revés): «reconocer», «ana».

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# una palabra o frase

# Proceso - que hago con eso
# convertir a minusculas, eliminar espacios,
# apilar la mitad izquierda y comparar con la mitad derecha

# Salida - que debo mostrar
# indicar si es palindromo o no
# Ejemplo de entrada:
# s = "reconocer"
# Salida esperada:
# Si, es palindromo


# 2) BOSQUEJO A MANO
# Palabra: reconocer
# Mitad izquierda:
# r -> push
# e -> push
# c -> push
# o -> push
# Pila: [r, e, c, o]

# Saltar la letra central: n
# Comparar la mitad derecha:
# o -> pop y comparar
# c -> pop y comparar
# e -> pop y comparar
# r -> pop y comparar
# Todas las letras coinciden.
# Resultado: Si, es palindromo

# 3) DESCUBRIR EL PATRON
# Una pila trabaja con el principio LIFO:
# el ultimo elemento en entrar es el primero en salir.
# Se guarda la mitad izquierda de la palabra.
# Luego se compara con la mitad derecha.
# Si todas las letras coinciden, es un palindromo.
# Si la palabra tiene una cantidad impar de letras,
# se ignora la letra central.


# 4) ESCRIBIR EL CODIGO
from collections import deque

def es_palindromo(s):
    s = s.lower().replace(" ", "")
    pila = deque()

    # Apilar la mitad izquierda
    mitad = len(s) // 2

    for i in range(mitad):
        pila.append(s[i])

    # Saltar la letra central si la longitud es impar
    inicio_der = mitad + (1 if len(s) % 2 == 1 else 0)

    # Comparar con la mitad derecha
    for i in range(inicio_der, len(s)):
        if pila.pop() != s[i]:
            return False

    return True
# Pruebas
for p in ["ana", "reconocer", "python", "anita lava la tina"]:
    if es_palindromo(p):
        print(f"{p!r}: Si, es palindromo")
    else:
        print(f"{p!r}: No es palindromo")



# EJERCICIO #7)
# EVALUAR EXPRESION POSTFIJA
#En notación postfija («polaca inversa»), los operadores van después: 3 4 + = 7. Evalúa una expresión como 3 4 + 5 * = 35.

# 1) ENTENDER EL PROBLEMA
# Entrada - que me dan
# una expresion matematica en notacion postfija

# Proceso - que hago con eso
# guardar los numeros en una pila y realizar las operaciones
# cuando aparece un operador

# Salida - que debo mostrar
# el resultado de la expresion
# Ejemplo de entrada
# "3 4 + 5 *"
# Salida esperada
# 35

# 2) BOSQUEJO A MANO
# Expresion: 3 4 + 5 *
# 3 -> push = Pila: [3]
# 4 -> push =  Pila: [3, 4]

# + -> pop 4 y pop 3
# 3 + 4 = 7 -> push
# Pila: [7]

# 5 -> push
# Pila: [7, 5]

# * -> pop 5 y pop 7
# 7 * 5 = 35 -> push
# Resultado: 35

# 3) DESCUBRIR EL PATRON
# Los numeros se guardan en la pila.
# Cuando aparece un operador, se extraen dos numeros,
# se realiza la operacion y se guarda el resultado.
# Al final, queda el resultado de la expresion.


# 4) ESCRIBIR EL CODIGO
from collections import deque

def evaluar_postfija(expr):
    pila = deque()

    for token in expr.split():
        if token in "+-*/":
            b = pila.pop()
            a = pila.pop()

            if token == "+":
                pila.append(a + b)
            elif token == "-":
                pila.append(a - b)
            elif token == "*":
                pila.append(a * b)
            elif token == "/":
                pila.append(a / b)
        else:
            pila.append(int(token))

    return pila.pop()

# Pruebas
print(evaluar_postfija("3 4 +"))             # 7
print(evaluar_postfija("3 4 + 5 *"))         # 35
print(evaluar_postfija("5 1 2 + 4 * + 3 -")) # 14
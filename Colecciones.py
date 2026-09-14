#COLECCIONES:
#Cadenas, listas, tuplas, conjuntos y diccionarios: cómo se crean, cómo se recorren y cuándo usar cada una.

#EJERCICIO_1:CONTAR VOCALES EN UNA CADENA
#Pide una frase al usuario y cuenta cuántas vocales (a, e, i, o, u) tiene. Ignora mayúsculas/minúsculas.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #frase (texto ingresado por input, convertido a minúsculas)

    #"PROCESO"--QUE HAGO CON ESO
    #recorrer cada carácter de la frase y verificar si está en el
    #conjunto de vocales, sumando 1 al contador si es así

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #LA CANTIDAD TOTAL DE VOCALES EN LA FRASE

#2->BOSQUEJO A MANO
    #frase = "Hola Mundo" -> .lower() -> "hola mundo"
    #vocales = {"a","e","i","o","u"}
    #resultado: "4 vocales"

#3->DESCUBRIR EL PATRÓN
    #Patrón de "recorrer y contar": se recorre cada elemento (carácter)
    #con un for, se pregunta una condición (in vocales) y se acumula
    #con total += 1. Usar un set ({}) en vez de una lista hace la
    #búsqueda "in" más eficiente.

#4->ESCRIBIR EL CODIGO

frase = input("Frase: ").lower()
vocales = {"a", "e", "i", "o", "u"}
total = 0
for ch in frase:
    if ch in vocales:
         total += 1
print(f"{total} vocales")
#__________________________________________________________________________________________


#EJERCICIO_2:PROMEDIO YT MAX DE UNA LISTA DE NOTAS
#Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5], calcula el promedio, la nota máxima y la mínima.
#Imprime los tres valores con 2 decimales.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #notas (lista de números ya definida en el código)

    #"PROCESO"--QUE HAGO CON ESO
    #calcular promedio con sum()/len(), y obtener max() y min()

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL PROMEDIO, EL MÁXIMO Y EL MÍNIMO DE LAS NOTAS

#2->BOSQUEJO A MANO
    #notas = [7, 8.5, 6, 9, 10, 5.5]
    #sum(notas) = 7+8.5+6+9+10+5.5 = 46
    #len(notas) = 6
    #promedio = 46 / 6 = 7.666... -> 7.67
    #max(notas) = 10 -> "10.00"
    #min(notas) = 5.5 -> "5.50"

#3->DESCUBRIR EL PATRÓN
    #Uso de funciones integradas de Python (sum, len, max, min) que
    #operan directamente sobre listas, evitando escribir bucles
    #manuales para sumar o comparar elemento por elemento.

#4->ESCRIBIR EL CODIGO

notas = [7, 8.5, 6, 9, 10, 5.5]
promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Máximo:   {max(notas):.2f}")
print(f"Mínimo:   {min(notas):.2f}")
#________________________________________________________________________________________


#EJERCICIO_3: ELIMINAR DUPLICADOS MANTENIENDO EL ORDEN
#Dada la lista ["a", "b", "a", "c", "b", "d"], retorna una nueva lista sin duplicados respetando el orden de la primera aparición.
# (Con set se pierde el orden — hay que combinar set + list.)

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #datos (lista con elementos posiblemente repetidos)

    #"PROCESO"--QUE HAGO CON ESO
    #convertir la lista a set() para eliminar duplicados,
    #luego volverla a convertir en list()

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #LA LISTA SIN ELEMENTOS DUPLICADOS

#2->BOSQUEJO A MANO
    #datos = ["a","b","a","c","b","d"]
    #set(datos) -> {"a","b","c","d"}  (elimina los repetidos "a" y "b")
    #list({...}) -> ["a","b","c","d"] (orden no garantizado)

#3->DESCUBRIR EL PATRÓN
    #set() es la forma más directa de eliminar duplicados en Python,
    #porque por definición no admite valores repetidos. El "costo" es
    #que se pierde el orden original de la lista.

#4->ESCRIBIR EL CODIGO

datos = ["a", "b", "a", "c", "b", "d"]
resultado = list(set(datos))
print(resultado)
__________________________________________________________________________________________


#EJERCICIO_4:CONTAR FRECUENCIA DE PALABRAS
#Dado un texto, retorna un diccionario con la frecuencia de cada palabra (ignora mayúsculas). 
#Al final, imprime la palabra que más se repite.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #texto (cadena ya definida en el código)

    #"PROCESO"--QUE HAGO CON ESO
    #separar el texto en palabras (.lower().split()), contar cuántas
    #veces aparece cada una en un diccionario, y encontrar la de
    #mayor conteo con max(..., key=...)

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL DICCIONARIO DE CONTEOS Y LA PALABRA MÁS REPETIDA

#2->BOSQUEJO A MANO
    #texto="El perro y el gato y el perro" -> .lower() ->
    #"el perro y el gato y el perro"
    #.split() -> ["el","perro","y","el","gato","y","el","perro"]
    #salida: "Más repetida: 'el' (3 veces)"

#3->DESCUBRIR EL PATRÓN
    #Patrón de "conteo con diccionario": conteo.get(palabra, 0) evita
    #un KeyError cuando la palabra aún no existe (le da un valor por
    #defecto de 0). Luego max(dict, key=dict.get) recorre las claves
    #del diccionario pero compara usando sus valores.

#4->ESCRIBIR EL CODIGO

texto = "El perro y el gato y el perro"
conteo = {}
for palabra in texto.lower().split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)

mas = max(conteo, key=conteo.get)
print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")
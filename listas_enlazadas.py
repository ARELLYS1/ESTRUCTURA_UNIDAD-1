#====================================================
# EJERCICIO_1 INSERTAR MANTENIEDNDO EL ORDEN 
#===================================================
# Añadir a ListaEnlazada el método insertar_ordenado(data):
# si la lista está ordenada de menor a mayor, el nuevo dato 
# debe quedar en su lugar correcto para que la lista siga ordenada.

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # una lista ordenada y un dato
  # nsertar_ordenado(25) en 10 → 20 → 30 → 40
  #2) Proceso -  Qué hago con eso
  # encontrar el ANTERIOR al lugar correcto y reenganchar
  
  # 3) Salida — Qué debo mostrar
  # la misma lista, aún ordenada, con un nodo más
  # 10 → 20 → 25 → 30 → 40
  
#2) BOSQUEJO A MANO 

  # Lista: 10 → 20 → 30 → 40      dato: 25

  # ¿25 va antes de la cabeza (25 < 10)? No.

  # Me paro en 10 y miro adelante: 20 ≤ 25 → avanzo a 20
  # Me paro en 20 y miro adelante: 30 ≤ 25? NO → aquí es

  # El 25 va entre 20 y 30:
  # 25.next = 30        (primero agarra el resto)
  # 20.next = 25        (después 20 apunta al nuevo)

  # ¿Y si el dato fuera 5?  5 < 10 → va al INICIO
  # ¿Y si fuera 50?  camino hasta 40, 40.next es None → va al FINAL
  
# 3) DESCUBRIR EL PATRON 

  # Es la misma idea que eliminar_por_valor: el dedo 
  # se queda en el anterior y mira un vagón adelante. 
  # Solo cambia la condición para seguir caminando:
  # «mientras el siguiente sea menor o igual que el dato».
  #Y el reenganche es el mismo de insertar_en: 
  # primero agarra, después suelta. Hay un caso especial 
  # (va antes de la cabeza) que se resuelve igual que insertar_inicio.
  
  
# 4) ESCRIBIR CODIGO 

    # Método nuevo para la clase ListaEnlazada

# 1) CLASE NODO
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2) CLASE LISTA ENLAZADA
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

   
    def insertar_ordenado(self, data):
        nuevo = Nodo(data)

        # Caso A: lista vacía o nuevo menor que cabeza
        if self.head is None or data < self.head.data:
            nuevo.next = self.head
            self.head = nuevo

        else:
            # Caso B: buscar el nodo anterior
            anterior = self.head

            while anterior.next is not None and anterior.next.data <= data:
                anterior = anterior.next

            # Paso 1: el nuevo nodo apunta al resto
            nuevo.next = anterior.next

            # Paso 2: el anterior apunta al nuevo
            anterior.next = nuevo

        self.cantidad += 1

    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")


notas = ListaEnlazada()

for n in [30, 10, 40, 20]:
    notas.insertar_ordenado(n)

notas.listar()

notas.insertar_ordenado(25)
notas.insertar_ordenado(5)
notas.insertar_ordenado(50)

notas.listar()

# Haz insertar_ordenado_desc(data) para listas ordenadas de mayor a menor. 
# ¿Qué dos comparaciones cambian?

def insertar_ordenado_desc(self, data):
    nuevo = Nodo(data)

    # Caso A: lista vacía o nuevo mayor que cabeza
    if self.head is None or data > self.head.data:
        nuevo.next = self.head
        self.head = nuevo

    else:
        # Caso B: buscar el anterior
        anterior = self.head

        while anterior.next is not None and anterior.next.data >= data:
            anterior = anterior.next

        nuevo.next = anterior.next
        anterior.next = nuevo

    self.cantidad += 1



#========================================================
# EJERCICIO_2 ELIMINAR TODAS LAS APARICIONES DE UN VALOR 
#========================================================
# Añadir el método eliminar_todos(data) que quite todos los 
# nodos con ese dato (no solo el primero) y retorne cuántos borró.
# Debe funcionar aunque los repetidos estén seguidos o en la cabeza.

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # una lista y un dato
  # eliminar_todos(3) en 3 → 3 → 7 → 3 → 3 → 5 → 3
  
  #2) Proceso -  Qué hago con eso
  # saltarme cada nodo con ese dato, contándolos
  
  # 3) Salida — Qué debo mostrar
  # la lista sin ese dato y cuántos se borraron
  # 7 → 5 y retorna 5
  
  
#2) BOSQUEJO A MANO 

  # 3 → 3 → 7 → 3 → 3 → 5 → 3

  #FASE 1 — la cabeza tiene un 3: la muevo
  # head = 3 (el segundo)   → otra vez 3: la muevo
  # head = 7                → ya no es 3, paro

  # FASE 2 — me paro en 7 y miro adelante
  #  7 mira: 3 → me lo salto (7 → 3 → 5 → 3). ¡NO avanzo!
  # mira: 3 → me lo salto (7 → 5 → 3).     ¡NO avanzo!
  # 7 mira: 5 → no es 3 → ahora sí avanzo a 5
  # 5 mira: 3 → me lo salto (5 → None)
  # 5 mira: None → terminé
  # Resultado: 7 → 5     borrados = 2 + 3 = 5
  
# 3) DESCUBRIR EL PATRON 

  # El problema se divide en dos fases: la cabeza (que no tiene anterior) 
  # y el resto (que se resuelve mirando un vagón adelante).

  # La clave está en una sola decisión: después de saltarme un nodo, 
  # NO avanzo, porque el nuevo siguiente también podría ser un 3. 
  # Solo avanzo cuando el siguiente NO es el dato. Es el patrón 🔵 contador con borrados.
  

# 4) ESCRIBIR CODIGO 

# 1) CLASE NODO
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2) CLASE LISTA ENLAZADA
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

   
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1


    def eliminar_todos(self, data):
        borrados = 0

        # Fase 1: mientras la cabeza tenga el dato, la quito
        while self.head is not None and self.head.data == data:
            self.head = self.head.next
            borrados = borrados + 1

        # Fase 2: reviso el resto mirando un nodo adelante
        anterior = self.head

        while anterior is not None and anterior.next is not None:
            if anterior.next.data == data:
                anterior.next = anterior.next.next
                borrados = borrados + 1
            else:
                anterior = anterior.next

        # Actualizar cantidad de elementos
        self.cantidad = self.cantidad - borrados

        return borrados

    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")

    
    def longitud(self):
        return self.cantidad



l = ListaEnlazada()

for x in [3, 3, 7, 3, 3, 5, 3]:
    l.insertar_final(x)

# Mostrar lista original
l.listar()

# Eliminar todos los elementos que sean 3
print("Elementos borrados:", l.eliminar_todos(3))

# Mostrar lista resultante
l.listar()

# Mostrar cantidad de elementos
print("Longitud:", l.longitud())


# Escribe quitar_duplicados() para una lista ordenada:
# 1 → 1 → 2 → 3 → 3 → 3 debe quedar 1 → 2 → 3. Pista: 
# compara cada nodo con su siguiente y usa la misma regla
# de «no avanzar después de borrar».

#====================================================
# LISTA ENLAZADA - QUITAR DUPLICADOS
#====================================================

# 1) CLASE NODO
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# 2) CLASE LISTA ENLAZADA
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    def quitar_duplicados(self):
        borrados = 0
        actual = self.head

        while actual is not None and actual.next is not None:

            if actual.data == actual.next.data:
                actual.next = actual.next.next
                borrados += 1
                # No avanzo porque puede haber otro duplicado
            else:
                actual = actual.next

        self.cantidad = self.cantidad - borrados

        return borrados

    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")


    def longitud(self):
        return self.cantidad


l = ListaEnlazada()

for x in [1, 1, 2, 3, 3, 3]:
    l.insertar_final(x)

l.listar()

print("Duplicados eliminados:", l.quitar_duplicados())

l.listar()

print("Longitud:", l.longitud())


#====================================================
# EJERCICIO 3: CONTAR NODOS CAMINANDO
#====================================================
# Método contar() que retorne cuántos nodos hay,
# recorriéndolos uno a uno sin usar self.cantidad.

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una lista enlazada con varios nodos.
    # 2) Proceso - Qué hago con eso
    # Recorrer los nodos uno a uno.
    # Incrementar un contador por cada nodo.
    # 3) Salida - Qué debo mostrar
    # La cantidad total de nodos.

# 2) BOSQUEJO A MANO
    # A -> B -> C -> D -> None
    # A = 1
    # B = 2
    # C = 3
    # D = 4
    # Resultado = 4

# 3) DESCUBRIR EL PATRON
    # Contador inicializado en 0.
    # Recorrer la lista usando while.
    # Sumar 1 por cada nodo.
    # Avanzar al siguiente nodo.
    # Retornar el contador.

# 4) ESCRIBIR CODIGO

# --- Clase Nodo ---
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# --- Clase ListaEnlazada ---
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    # --- Contar nodos caminando ---
    def contar(self):
        contador = 0
        actual = self.head

        while actual is not None:
            contador += 1
            actual = actual.next

        return contador

    # --- Listar elementos ---
    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")


# --- Uso ---
l = ListaEnlazada()

for x in ["A", "B", "C", "D"]:
    l.insertar_final(x)

l.listar()
print("Cantidad de nodos:", l.contar())



#====================================================
# EJERCICIO 4: EL MAYOR DE LA LISTA
#====================================================
# Método mayor() que retorne el dato más grande
# de la lista o None si está vacía.

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una lista enlazada con varios números.
    # 2) Proceso - Qué hago con eso
    # Recorrer los nodos y comparar sus valores.
    # El primer nodo será el campeón provisional.
    # Si encuentro uno mayor, será el nuevo campeón.
    # 3) Salida - Qué debo mostrar
    # El número más grande de la lista.
    # Si está vacía, retornar None.

# 2) BOSQUEJO A MANO
    # Lista: 4 -> 9 -> 2 -> 7
    # Campeón inicial = 4
    # Comparo 9 con 4: gana 9.
    # Comparo 2 con 9: gana 9.
    # Comparo 7 con 9: gana 9.
    # Resultado = 9

# 3) DESCUBRIR EL PATRON
    # Campeón: guarda el mayor valor encontrado.
    # Recorrido: comienza desde el segundo nodo.
    # Comparación: si encuentro uno mayor, actualizo.
    # Retorno: devolver el campeón al terminar.

# 4) ESCRIBIR CODIGO


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    def mayor(self):
        if self.head is None:
            return None

        campeon = self.head.data
        actual = self.head.next

        while actual is not None:
            if actual.data > campeon:
                campeon = actual.data

            actual = actual.next

        return campeon

    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")


l = ListaEnlazada()

for x in [4, 9, 2, 7]:
    l.insertar_final(x)

l.listar()

print("El mayor de la lista es:", l.mayor())



#====================================================
# EJERCICIO 5: ELIMINAR EL ULTIMO NODO
#====================================================
# Método eliminar_final() que quite el último nodo
# y retorne su dato.

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una lista enlazada con varios nodos.
    # 2) Proceso - Qué hago con eso
    # Buscar el penúltimo nodo.
    # Guardar el dato del último nodo.
    # Desconectar el último nodo.
    # Contemplar lista vacía y un solo nodo.
    # 3) Salida - Qué debo mostrar
    # Retornar el dato eliminado.
    # Mostrar la lista sin el último nodo.

# 2) BOSQUEJO A MANO
    # Lista: 4 -> 9 -> 2 -> 7 -> None
    # Penúltimo = 2
    # Último = 7
    # Eliminar 7.
    # Resultado: 4 -> 9 -> 2 -> None
    # Dato retornado = 7

# 3) DESCUBRIR EL PATRON
    # Caso 1: lista vacía, retornar None.
    # Caso 2: un solo nodo, eliminar la cabeza.
    # Caso 3: varios nodos, buscar el penúltimo.
    # Guardar el dato del último nodo.
    # Desconectar el último nodo.
    # Actualizar la cantidad.

# 4) ESCRIBIR CODIGO


class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# --- Clase ListaEnlazada ---
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    # --- Eliminar el último nodo ---
    def eliminar_final(self):

        # Caso 1: lista vacía
        if self.head is None:
            print("Lista vacía")
            return None

        # Caso 2: solamente un nodo
        if self.head.next is None:
            dato = self.head.data
            self.head = None
            self.cantidad -= 1
            return dato

        # Caso 3: buscar el penúltimo nodo
        penultimo = self.head

        while penultimo.next.next is not None:
            penultimo = penultimo.next

        # Guardar el dato del último nodo
        dato = penultimo.next.data

        # Desconectar el último nodo
        penultimo.next = None

  
        self.cantidad -= 1

        return dato

    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")

    # --- Mostrar longitud ---
    def longitud(self):
        return self.cantidad


l = ListaEnlazada()

for x in [4, 9, 2, 7]:
    l.insertar_final(x)

print("Lista original:")
l.listar()

print("Dato eliminado:", l.eliminar_final())

print("Lista resultante:")
l.listar()

print("Cantidad de nodos:", l.longitud())


#====================================================
# EJERCICIO 6: INSERTAR DESPUES DE UN VALOR
#====================================================
# Método insertar_despues(referencia, data) que busque
# un nodo y coloque uno nuevo justo después.

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una referencia y un nuevo dato.
    # 2) Proceso - Qué hago con eso
    # Buscar el primer nodo que tenga la referencia.
    # Crear un nodo nuevo.
    # Insertarlo después del nodo encontrado.
    # Si no existe la referencia, mostrar un mensaje.
    # 3) Salida - Qué debo mostrar
    # La lista con el nuevo nodo insertado.

# 2) BOSQUEJO A MANO
    # Lista: 4 -> 9 -> 2 -> None
    # Referencia = 9
    # Nuevo dato = 5
    # El nodo 9 apunta al nuevo nodo 5.
    # El nodo 5 apunta al nodo 2.
    # Resultado: 4 -> 9 -> 5 -> 2 -> None

# 3) DESCUBRIR EL PATRON
    # Recorrido para encontrar la referencia.
    # Si no existe, mostrar un mensaje.
    # Crear un nodo nuevo.
    # Paso 1: el nuevo nodo agarra el resto.
    # Paso 2: el nodo encontrado apunta al nuevo.
    # Actualizar la cantidad.

# 4) ESCRIBIR CODIGO

# --- Clase Nodo ---
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# --- Clase ListaEnlazada ---
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    # --- Insertar después de un valor ---
    def insertar_despues(self, referencia, data):
        actual = self.head

        # Buscar el primer nodo con la referencia
        while actual is not None and actual.data != referencia:
            actual = actual.next

        # Si la referencia no existe
        if actual is None:
            print(referencia, "no existe")
            return

        # Crear el nuevo nodo
        nuevo = Nodo(data)

        # Paso 1: el nuevo nodo agarra el resto
        nuevo.next = actual.next

        # Paso 2: el nodo encontrado apunta al nuevo
        actual.next = nuevo

        # Actualizar cantidad
        self.cantidad += 1

    # --- Listar elementos ---
    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")

    # --- Mostrar longitud ---
    def longitud(self):
        return self.cantidad


l = ListaEnlazada()

for x in [4, 9, 2]:
    l.insertar_final(x)

print("Lista original:")
l.listar()

# Insertar 5 después del valor 9
l.insertar_despues(9, 5)

print("Lista después de insertar:")
l.listar()

print("Cantidad de nodos:", l.longitud())

# Probar una referencia que no existe
l.insertar_despues(15, 8)



#====================================================
# EJERCICIO 7: EL K-ESIMO DESDE EL FINAL
#====================================================
# Método desde_final(k) que retorne el dato del nodo
# k-ésimo contando desde el final, sin usar cantidad.

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una lista enlazada y un número k.
    # 2) Proceso - Qué hago con eso
    # Utilizar dos punteros separados por k posiciones.
    # Avanzar ambos hasta que el primero llegue a None.
    # 3) Salida - Qué debo mostrar
    # Retornar el dato del nodo k-ésimo desde el final.
    # Si k no es válido, retornar None.

# 2) BOSQUEJO A MANO
    # Lista: A -> B -> C -> D -> E
    # k = 2
    # Adelantado avanza dos posiciones.
    # Detrás comienza desde A.
    # Ambos avanzan hasta que adelantado llegue a None.
    # Detrás queda en D.
    # Resultado = D

# 3) DESCUBRIR EL PATRON
    # Dos punteros: adelantado y detrás.
    # Adelantado avanza k posiciones.
    # Detrás comienza desde la cabeza.
    # Ambos avanzan al mismo tiempo.
    # Cuando adelantado llega a None, detrás
    # está en el nodo buscado.
    # No utilizamos self.cantidad.

# 4) ESCRIBIR CODIGO

# --- Clase Nodo ---
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# --- Clase ListaEnlazada ---
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    # --- K-ésimo desde el final ---
    def desde_final(self, k):

        # Validar que k sea positivo
        if k <= 0:
            return None

        # Primer puntero
        adelantado = self.head

        # Adelantar k posiciones
        for _ in range(k):
            if adelantado is None:
                return None

            adelantado = adelantado.next

        # Segundo puntero
        detras = self.head

        # Avanzar ambos punteros
        while adelantado is not None:
            adelantado = adelantado.next
            detras = detras.next

        return detras.data

    # --- Listar elementos ---
    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")

l = ListaEnlazada()

for x in ["A", "B", "C", "D", "E"]:
    l.insertar_final(x)

print("Lista original:")
l.listar()

k = 2

print("K:", k)
print("Dato desde el final:", l.desde_final(k))




#====================================================
# EJERCICIO 8: DETECTAR UN CICLO EN LA LISTA
#====================================================
# Método tiene_ciclo() que retorne True si algún nodo
# apunta a uno anterior, formando un ciclo.
# Utilizar el algoritmo de Floyd (liebre y tortuga).

# 1) ENTENDER EL PROBLEMA
    # 1) Entrada - Qué me dan
    # Una lista enlazada que puede tener un ciclo.
    # 2) Proceso - Qué hago con eso
    # Utilizar dos punteros:
    # La tortuga avanza un nodo.
    # La liebre avanza dos nodos.
    # Si se encuentran, existe un ciclo.
    # 3) Salida - Qué debo mostrar
    # True si existe un ciclo.
    # False si no existe un ciclo.

# 2) BOSQUEJO A MANO
    # Lista: A -> B -> C -> D
    #                    ^    |
    #                    |____|
    # D vuelve a B.
    # La liebre y la tortuga terminan encontrándose.
    # Resultado = True

# 3) DESCUBRIR EL PATRON
    # Algoritmo de Floyd.
    # Tortuga: avanza un nodo.
    # Liebre: avanza dos nodos.
    # Comparar si ambos están en el mismo nodo.
    # Si se encuentran, retornar True.
    # Si la liebre llega a None, retornar False.

# 4) ESCRIBIR CODIGO

# --- Clase Nodo ---
class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None


# --- Clase ListaEnlazada ---
class ListaEnlazada:
    def __init__(self):
        self.head = None
        self.cantidad = 0

    # --- Insertar al final ---
    def insertar_final(self, data):
        nuevo = Nodo(data)

        if self.head is None:
            self.head = nuevo
        else:
            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

        self.cantidad += 1

    # --- Detectar un ciclo ---
    def tiene_ciclo(self):
        tortuga = self.head
        liebre = self.head

        # La liebre avanza dos nodos y la tortuga uno
        while liebre is not None and liebre.next is not None:

            tortuga = tortuga.next
            liebre = liebre.next.next

            # Si se encuentran, existe un ciclo
            if tortuga is liebre:
                return True

        # Si la liebre llega a None, no hay ciclo
        return False

    # --- Listar elementos ---
    def listar(self):
        actual = self.head

        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.next

        print("None")


lista = ListaEnlazada()

for x in ["A", "B", "C", "D"]:
    lista.insertar_final(x)

print("¿Tiene ciclo inicialmente?")
print(lista.tiene_ciclo())


d = lista.head.next.next.next
d.next = lista.head.next

print("¿Tiene ciclo después de conectar D con B?")
print(lista.tiene_ciclo())
#====================================================
# EJERCICIO 1: FILA DE ATENCIÓN EN UN BANCO 
#===================================================
# Simular una fila de banco: los clientes llegan 
# (encolar) y el cajero los atiende en orden
# (desencolar).

# 1) ENTENDER EL PROBLEMA

  #1) Entrada -  Qué me dan
  # opción del menú y datos
  # llegan 3, atender 1
  
  #2) Proceso -  Qué hago con eso
  # menú con encolar/desencolar/frente
  
  # 3) Salida — Qué debo mostrar
  # estado de la fila y siguiente en atención
  # atendido: Ana. Quedan: Beto, Carlos
  
#2) BOSQUEJO A MANO 

  # cola = []

  # Ana llega  → encolar("Ana")  → [Ana]
  # Beto llega → encolar("Beto") → [Ana, Beto]
  # Carlos llega → encolar("Carlos") → [Ana, Beto, Carlos]

  # atender → desencolar() → "Ana"  → [Beto, Carlos]
  # frente → "Beto"


# 3) DESCUBRIR EL PATRON 

  # Ejercicio directo: FIFO puro.
  # El orden de llegada es el orden de atención.
  # Usamos deque por eficiencia — aunque
  # para 5 clientes daría igual, es buena costumbre.
  
# 4) ESCRIBIR CODIGO 

from collections import deque

cola = deque()

while True:
    print("\n1.Llega cliente 2.Atender 3.Ver frente 4.Ver toda la cola 5.Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        cola.append(nom)
        print(f"{nom} entró a la fila. {len(cola)} clientes en espera.")

    elif op == "2":
        if not cola:
            print("No hay clientes")
        else:
            atendido = cola.popleft()
            print(f"Atendiendo a: {atendido}. Quedan {len(cola)}.")

    elif op == "3":
        if not cola:
            print("Fila vacía")
        else:
            print(f"Siguiente: {cola[0]}")

    elif op == "4":
        if not cola:
            print("(vacía)")
        else:
            for i, c in enumerate(cola):
                marca = " ← siguiente" if i == 0 else ""
                print(f"  {i+1}. {c}{marca}")

    elif op == "5":
        break
    
# Añade prioridad:
# los clientes VIP entran al frente con cola.appendleft(nom).


from collections import deque

# Crear la cola de atención
cola = deque()

while True:

    print("\n====================================")
    print("       BANCO - FILA DE ATENCION")
    print("====================================")
    print("1. Llega cliente normal")
    print("2. Llega cliente VIP")
    print("3. Atender cliente")
    print("4. Ver frente de la fila")
    print("5. Ver toda la fila")
    print("6. Salir")

    op = input("Opcion: ")


    if op == "1":
        nom = input("Nombre del cliente: ")

        cola.append(nom)

        print(f"{nom} entro al final de la fila.")
        print(f"Clientes en espera: {len(cola)}")

  
    elif op == "2":
        nom = input("Nombre del cliente VIP: ")

        cola.appendleft(nom)

        print(f"{nom} ingreso al frente de la fila.")
        print(f"Clientes en espera: {len(cola)}")

    elif op == "3":

        if not cola:
            print("No hay clientes para atender.")

        else:
            atendido = cola.popleft()

            print(f"Atendiendo a: {atendido}")
            print(f"Clientes restantes: {len(cola)}")


    elif op == "4":

        if not cola:
            print("Fila vacia.")

        else:
            print(f"Siguiente cliente: {cola[0]}")

  
    elif op == "5":

        if not cola:
            print("La fila esta vacia.")

        else:
            print("\nCLIENTES EN ESPERA:")

            for i, c in enumerate(cola):
                marca = " <- SIGUIENTE" if i == 0 else ""
                print(f"{i+1}. {c}{marca}")


    elif op == "6":
        print("Saliendo del sistema del banco...")
        break

    else:
        print("Opcion incorrecta. Intente nuevamente.")
        
        
        

#====================================================
# EJERCICIO 2: SIMULADOR DE IMPRESORA 
#====================================================

# ENTENDER EL PROBLEMA
# ENTRADA:
# Documentos con nombre y cantidad de páginas.
#
# PROCESO:
# Crear una cola y procesar los documentos
# en el mismo orden en que llegaron.
#
# SALIDA:
# Mostrar el documento, su tiempo de impresión
# y el tiempo total acumulado.

#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Cola:
# A(5 páginas), B(2 páginas), C(10 páginas)
#
# A -> 5 * 2 = 10 segundos
# B -> 2 * 2 = 4 segundos
# C -> 10 * 2 = 20 segundos
#
# Total = 10 + 4 + 20 = 34 segundos

#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# Utilizamos una cola FIFO:
# El primero en entrar es el primero en salir.
#
# append() agrega un documento.
# popleft() procesa el primer documento.
# tiempo_total acumula los segundos.

#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

from collections import deque

def procesar_impresora(trabajos):

    # Creamos la cola con los documentos recibidos
    cola = deque(trabajos)

    # Variable para acumular el tiempo
    tiempo_total = 0

    # Procesamos mientras existan documentos
    while cola:

        # Sacamos el primer documento de la cola
        nombre, paginas = cola.popleft()

        # Calculamos el tiempo de impresión
        tiempo = paginas * 2

        # Sumamos el tiempo al acumulado
        tiempo_total += tiempo

        # Mostramos el estado de impresión
        print(f"Imprimiendo {nombre}: {paginas} páginas")
        print(f"Tiempo: {tiempo} segundos")
        print(f"Tiempo acumulado: {tiempo_total} segundos")
        print("-----------------------------------")

    # Devolvemos el tiempo total
    return tiempo_total


trabajos = [
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10)
]

total = procesar_impresora(trabajos)

print(f"\nTiempo total de impresión: {total} segundos")


# Añade opción «cancelar trabajo por nombre» — busca en la 
# deque y usa cola.remove((nombre, ...)).

def cancelar_trabajo(cola, nombre):

    # Buscamos el documento por su nombre
    for trabajo in cola:

        if trabajo[0].lower() == nombre.lower():

            # Eliminamos la tupla encontrada
            cola.remove(trabajo)

            print(f"Trabajo {nombre} cancelado correctamente.")
            return True

    # Si no encontramos el documento
    print(f"No existe el trabajo: {nombre}")
    return False


def procesar_impresora(cola):

    tiempo_total = 0

    # Procesamos mientras existan documentos
    while cola:

        # Extraemos el primer documento
        nombre, paginas = cola.popleft()

        # Calculamos el tiempo de impresión
        tiempo = paginas * 2

        # Acumulamos el tiempo
        tiempo_total += tiempo

        print(f"\nImprimiendo: {nombre}")
        print(f"Páginas: {paginas}")
        print(f"Tiempo: {tiempo} segundos")
        print(f"Tiempo acumulado: {tiempo_total} segundos")

    return tiempo_total


cola = deque([
    ("Contrato.pdf", 5),
    ("Recibo.pdf", 2),
    ("Manual.pdf", 10)
])

while True:

    print("\n===== SIMULADOR DE IMPRESORA =====")
    print("1. Agregar trabajo")
    print("2. Cancelar trabajo por nombre")
    print("3. Ver trabajos pendientes")
    print("4. Procesar impresora")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre del documento: ")
        paginas = int(input("Cantidad de páginas: "))

        if paginas > 0:
            cola.append((nombre, paginas))
            print("Trabajo agregado correctamente.")
        else:
            print("La cantidad de páginas debe ser mayor que cero.")

    elif opcion == "2":

        nombre = input("Nombre del trabajo que desea cancelar: ")

        cancelar_trabajo(cola, nombre)

    elif opcion == "3":

        print("\n===== TRABAJOS PENDIENTES =====")

        if cola:
            for trabajo in cola:
                print(f"Documento: {trabajo[0]} - Páginas: {trabajo[1]}")
        else:
            print("No hay trabajos pendientes.")

    elif opcion == "4":

        if cola:
            total = procesar_impresora(cola)
            print(f"\nTiempo total: {total} segundos")
        else:
            print("No hay trabajos para imprimir.")

    elif opcion == "5":

        print("Saliendo del simulador...")
        break

    else:
        print("Opción no válida.")
        
        

#====================================================
# EJERCICIO 3: COLA DE PRIORIDAD SIMPLE 
#====================================================

# ENTENDER EL PROBLEMA
# ENTRADA:
# Elementos con nombre y nivel de prioridad.
#
# PROCESO:
# Crear una cola (deque) para cada prioridad.
# Atender primero la prioridad más alta.
# Entre prioridades iguales, respetar llegada.
#
# SALIDA:
# Mostrar el orden de atención.

#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Ana(1), Luis(3), Diana(1), Beto(2)
#
# Prioridad 3: Luis
# Prioridad 2: Beto
# Prioridad 1: Ana, Diana
#
# Orden: Luis, Beto, Ana, Diana

#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# deque() crea una cola por prioridad.
# append() agrega un elemento al final.
# popleft() extrae el primero de la cola.
# Recorremos las prioridades de mayor a menor.

#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

from collections import deque

class ColaPrioridad:

    def __init__(self, niveles=3):

        # Cantidad de niveles de prioridad
        self.niveles = niveles

        # Creamos una cola para cada prioridad
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, nombre, prioridad):

        # Validamos que la prioridad sea correcta
        if not 1 <= prioridad <= self.niveles:
            print("Prioridad no válida.")
            return

        # Agregamos el elemento a su cola
        self.colas[prioridad].append(nombre)

        print(f"{nombre} agregado con prioridad {prioridad}.")

    def desencolar(self):

        # Buscamos desde la prioridad más alta
        for i in range(self.niveles, 0, -1):

            # Comprobamos si hay elementos
            if self.colas[i]:

                # Atendemos al primero que llegó
                nombre = self.colas[i].popleft()

                return nombre, i

        # Si todas las colas están vacías
        return None

    def mostrar(self):

        print("\n===== COLAS POR PRIORIDAD =====")

        # Mostramos desde la prioridad más alta
        for i in range(self.niveles, 0, -1):

            print(f"Prioridad {i}: {list(self.colas[i])}")

    def vacia(self):

        # Verificamos si todas las colas están vacías
        for cola in self.colas:
            if cola:
                return False

        return True


cp = ColaPrioridad(3)

while True:

    print("\n===== COLA DE PRIORIDAD =====")
    print("1. Agregar elemento")
    print("2. Atender elemento")
    print("3. Mostrar colas")
    print("4. Atender todos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        prioridad = int(input("Prioridad (1 a 3): "))

        cp.encolar(nombre, prioridad)

    elif opcion == "2":

        resultado = cp.desencolar()

        if resultado is not None:
            nombre, prioridad = resultado

            print(f"Atendiendo: {nombre}")
            print(f"Prioridad: {prioridad}")
        else:
            print("La cola está vacía.")

    elif opcion == "3":

        cp.mostrar()

    elif opcion == "4":

        if cp.vacia():
            print("No hay elementos para atender.")
        else:
            print("\n===== ORDEN DE ATENCIÓN =====")

            while not cp.vacia():

                nombre, prioridad = cp.desencolar()

                print(f"Atendiendo: {nombre} (Prioridad {prioridad})")

    elif opcion == "5":

        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")

        
# Añade una opción para cambiar la prioridad de un elemento
# ya encolado (buscarlo, moverlo).

from collections import deque

class ColaPrioridad:

    def __init__(self, niveles=3):

        # Cantidad de niveles de prioridad
        self.niveles = niveles

        # Creamos una cola para cada prioridad
        self.colas = [deque() for _ in range(niveles + 1)]

    def encolar(self, nombre, prioridad):

        # Validamos la prioridad
        if not 1 <= prioridad <= self.niveles:
            print("Prioridad no válida.")
            return

        # Evitamos nombres duplicados
        for cola in self.colas:
            if nombre in cola:
                print("El elemento ya está encolado.")
                return

        # Agregamos el elemento
        self.colas[prioridad].append(nombre)

        print(f"{nombre} agregado con prioridad {prioridad}.")

    def desencolar(self):

        # Buscamos desde la prioridad más alta
        for i in range(self.niveles, 0, -1):

            if self.colas[i]:

                # Extraemos el primero de la cola
                nombre = self.colas[i].popleft()

                return nombre, i

        return None

    def cambiar_prioridad(self, nombre, nueva_prioridad):

        # Validamos la nueva prioridad
        if not 1 <= nueva_prioridad <= self.niveles:
            print("Nueva prioridad no válida.")
            return False

        # Buscamos el elemento en todas las colas
        for prioridad, cola in enumerate(self.colas):

            if nombre in cola:

                # Si ya tiene esa prioridad, no hacemos cambios
                if prioridad == nueva_prioridad:
                    print("El elemento ya tiene esa prioridad.")
                    return False

                # Eliminamos el elemento de su cola anterior
                cola.remove(nombre)

                # Lo agregamos a la nueva cola
                self.colas[nueva_prioridad].append(nombre)

                print(f"\nPrioridad de {nombre} cambiada correctamente.")
                print(f"Prioridad anterior: {prioridad}")
                print(f"Nueva prioridad: {nueva_prioridad}")

                return True

        # Si no encontramos el elemento
        print(f"El elemento {nombre} no existe en la cola.")
        return False

    def mostrar(self):

        print("\n===== COLAS POR PRIORIDAD =====")

        for i in range(self.niveles, 0, -1):

            print(f"Prioridad {i}: {list(self.colas[i])}")

    def vacia(self):

        # Comprobamos si todas las colas están vacías
        for cola in self.colas:
            if cola:
                return False

        return True

cp = ColaPrioridad(3)

# Datos iniciales
cp.encolar("Ana", 1)
cp.encolar("Luis", 3)
cp.encolar("Diana", 1)
cp.encolar("Beto", 2)

while True:

    print("\n===== COLA DE PRIORIDAD =====")
    print("1. Agregar elemento")
    print("2. Atender elemento")
    print("3. Mostrar colas")
    print("4. Atender todos")
    print("5. Cambiar prioridad")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Nombre: ")
        prioridad = int(input("Prioridad (1 a 3): "))

        cp.encolar(nombre, prioridad)

    elif opcion == "2":

        resultado = cp.desencolar()

        if resultado is not None:
            nombre, prioridad = resultado
            print(f"Atendiendo: {nombre} (Prioridad {prioridad})")
        else:
            print("La cola está vacía.")

    elif opcion == "3":

        cp.mostrar()

    elif opcion == "4":

        if cp.vacia():
            print("No hay elementos para atender.")
        else:
            print("\n===== ORDEN DE ATENCIÓN =====")

            while not cp.vacia():

                nombre, prioridad = cp.desencolar()
                print(f"Atendiendo: {nombre} (Prioridad {prioridad})")

    elif opcion == "5":

        nombre = input("Nombre del elemento: ")
        nueva_prioridad = int(input("Nueva prioridad (1 a 3): "))

        cp.cambiar_prioridad(nombre, nueva_prioridad)

    elif opcion == "6":

        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida.")
        
        
#====================================================
# EJERCICIO 4: FILA CON TICKETS NUMERADOS 
#====================================================

# ENTENDER EL PROBLEMA
# ENTRADA:
# Nombre del elemento y su nueva prioridad.
#
# PROCESO:
# Buscar el elemento en todas las colas.
# Eliminarlo de su prioridad anterior.
# Agregarlo a la nueva prioridad.
#
# SALIDA:
# Mostrar el resultado del cambio de prioridad.

#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Colas iniciales:
# Prioridad 3: Luis
# Prioridad 2: Beto
# Prioridad 1: Ana, Diana
#
# Cambiar Ana de prioridad 1 a prioridad 3:
#
# Prioridad 3: Luis, Ana
# Prioridad 2: Beto
# Prioridad 1: Diana

#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# enumerate() permite recorrer las colas.
# remove() elimina el elemento de su cola anterior.
# append() lo agrega al final de la nueva cola.
# Así mantenemos el orden de llegada entre iguales.

#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

from collections import deque

cola = deque()
proximo = 1

while True:
    print("\n1.Llega 2.Atender 3.Ver cola 4.Salir")
    op = input("Opción: ")

    if op == "1":
        cola.append(proximo)
        print(f"Ticket {proximo} asignado. {len(cola)} en espera.")
        proximo += 1
    elif op == "2":
        if not cola:
            print("Sin clientes")
        else:
            print(f"Turno {cola.popleft()}")
    elif op == "3":
        print(list(cola))
    elif op == "4":
        break
    
    
#====================================================
# EJERCICIO 5: ROUND-ROBIN (TURNO ROTATIVO)
#====================================================

#ENTENDER EL PROBLEMA
# ENTRADA:
# Tres jugadores: Ana, Beto y Carlos.
# Cantidad de turnos: 10.
#
# PROCESO:
# Crear una cola con los jugadores.
# Sacar al primer jugador para realizar su turno.
# Colocarlo nuevamente al final de la cola.
# Repetir el proceso 10 veces.
#
# SALIDA:
# Mostrar el número de turno y el jugador
# que participa en cada turno.


#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Cola inicial:
# [Ana, Beto, Carlos]
#
# Turno 1: Ana    -> [Beto, Carlos, Ana]
# Turno 2: Beto   -> [Carlos, Ana, Beto]
# Turno 3: Carlos -> [Ana, Beto, Carlos]
# Turno 4: Ana    -> [Beto, Carlos, Ana]
# Turno 5: Beto   -> [Carlos, Ana, Beto]
# Turno 6: Carlos -> [Ana, Beto, Carlos]
# Turno 7: Ana    -> [Beto, Carlos, Ana]
# Turno 8: Beto   -> [Carlos, Ana, Beto]
# Turno 9: Carlos -> [Ana, Beto, Carlos]
# Turno 10: Ana   -> [Beto, Carlos, Ana]
#
# Resultado:
# Ana, Beto, Carlos, Ana, Beto,
# Carlos, Ana, Beto, Carlos, Ana


#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# deque() crea la cola de jugadores.
# popleft() saca al primer jugador.
# append() coloca al jugador al final.
# for repite el proceso 10 veces.
#
# PATRÓN:
# El primer jugador sale, realiza su turno
# y regresa al final de la cola.
# Así todos participan de manera rotativa.
# Este método se conoce como ROUND-ROBIN.

#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

from collections import deque

jugadores = deque(["Ana", "Beto", "Carlos"])

for turno in range(10):
    actual = jugadores.popleft()      # sale del frente
    print(f"Turno {turno+1}: {actual}")
    jugadores.append(actual)          # vuelve al final
    
    
#====================================================
# EJERCICIO 6: COLA CON MÁXIMO (HISTORICO)
#====================================================

# ENTENDER EL PROBLEMA
# ENTRADA:
# Una serie de números: 5, 3, 8, 2.
#
# PROCESO:
# Crear una cola para almacenar los números.
# Agregar cada número al final de la cola.
# Comparar cada número para identificar el máximo.
# Extraer los números en orden de llegada.
#
# SALIDA:
# Mostrar los números que salen de la cola.
# Mostrar el número máximo que se ha ingresado.


#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Números de entrada:
# [5, 3, 8, 2]
#
# Cola después de ingresar los números:
# [5, 3, 8, 2]
#
# Comparación del máximo:
# 5 > -infinito -> máximo = 5
# 3 < 5         -> máximo = 5
# 8 > 5         -> máximo = 8
# 2 < 8         -> máximo = 8
#
# Extracción de la cola:
# Sale 5 -> [3, 8, 2]
# Sale 3 -> [8, 2]
# Sale 8 -> [2]
# Sale 2 -> []
#
# Resultado:
# Números: 5, 3, 8, 2
# Máximo visto: 8


#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# deque() crea una cola.
# append() agrega un número al final.
# popleft() extrae el primer número ingresado.
# float("-inf") representa un valor menor que
# cualquier número real.
# if permite comparar cada número con el máximo.
#
# PATRÓN:
# Cada vez que ingresa un número, se compara
# con el máximo registrado.
# Si es mayor, se actualiza el máximo.
# La cola conserva el orden de llegada (FIFO).
# Así podemos conocer el máximo visto mientras
# los números se procesan.

#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

from collections import deque

class ColaConMax:
    def __init__(self):
        self._datos = deque()
        self._max_visto = float("-inf")

    def encolar(self, v):
        self._datos.append(v)
        if v > self._max_visto:
            self._max_visto = v

    def desencolar(self):
        if not self._datos:
            raise IndexError("vacía")
        return self._datos.popleft()

    def maximo_visto(self):
        return self._max_visto


c = ColaConMax()
for x in [5, 3, 8, 2]:
    c.encolar(x)
while c._datos:
    print(c.desencolar())
print("Máximo visto:", c.maximo_visto())


#====================================================
# EJERCICIO 7: SIMULADOR DE CAFÉ: DOS CAJAS 
#====================================================

# ENTENDER EL PROBLEMA
# ENTRADA:
# 10 clientes que llegan a una fila.
# 2 cajas disponibles para atender.
# Cada cliente tiene un tiempo de atención aleatorio
# entre 30 y 90 segundos.
#
# PROCESO:
# Crear una cola con los 10 clientes.
# Cada caja libre toma al primer cliente de la cola.
# Cada caja ocupada atiende durante 1 segundo.
# Cuando termina de atender, la caja queda libre
# y puede recibir al siguiente cliente.
# El tiempo avanza segundo por segundo hasta
# que todos los clientes hayan sido atendidos.
#
# SALIDA:
# Mostrar cuándo cada caja comienza a atender.
# Mostrar cuándo termina de atender a cada cliente.
# Mostrar el tiempo total de atención.


#====================================================
# 2. BOSQUEJO A MANO
#====================================================
# Clientes iniciales:
# [Cliente-1, Cliente-2, Cliente-3, ..., Cliente-10]
#
# Cajas:
# Caja 1: Libre
# Caja 2: Libre
#
# Segundo 0:
# Caja 1 toma Cliente-1.
# Caja 2 toma Cliente-2.
#
# Mientras trabajan:
# Cada segundo se reduce en 1 el tiempo restante
# de atención de cada cliente.
#
# Cuando una caja termina:
# Queda libre y toma al siguiente cliente de la cola.
#
# El proceso continúa hasta que:
# La cola esté vacía y las dos cajas estén libres.
#
# Resultado:
# Se muestra el tiempo de inicio y finalización
# de cada atención y el tiempo total.


#====================================================
# 3. DESCUBRIR EL PATRÓN
#====================================================
# deque() crea la cola de clientes.
# popleft() entrega el primer cliente a una caja.
# random.randint(30, 90) genera el tiempo de atención.
# cajas = [None, None] representa las dos cajas.
# None significa que la caja está libre.
# any(cajas) comprueba si alguna caja está ocupada.
# El ciclo while continúa mientras haya clientes
# esperando o alguna caja esté atendiendo.
# -= 1 reduce el tiempo restante cada segundo.
#
# PATRÓN:
# Se utiliza una cola FIFO para atender a los clientes
# por orden de llegada y dos cajas que trabajan
# simultáneamente.
# Cuando una caja termina, recibe al siguiente cliente.
# Esto representa un sistema de atención con
# múltiples servidores.


#====================================================
# 4. ESCRIBIR EL CÓDIGO
#====================================================

import random
from collections import deque

random.seed(42)                     # para reproducibilidad
cola = deque([f"Cliente-{i+1}" for i in range(10)])

# Dos cajas: cada una guarda (cliente, tiempo_restante) o None si libre
cajas = [None, None]

segundo = 0

while cola or any(cajas):
    # Cada caja libre agarra al primero
    for i in range(2):
        if cajas[i] is None and cola:
            cliente = cola.popleft()
            tiempo = random.randint(30, 90)
            cajas[i] = [cliente, tiempo]
            print(f"[{segundo}s] Caja {i+1}: atendiendo a {cliente} ({tiempo}s)")

    # Cada caja ocupada trabaja 1 segundo
    for i in range(2):
        if cajas[i]:
            cajas[i][1] -= 1
            if cajas[i][1] == 0:
                print(f"[{segundo+1}s] Caja {i+1}: terminó con {cajas[i][0]}")
                cajas[i] = None

    segundo += 1

print(f"\nTiempo total: {segundo}s")
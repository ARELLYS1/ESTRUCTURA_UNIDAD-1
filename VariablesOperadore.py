#VARIABLES, TIPOS Y OPERADORES
#EJERCICIO_1:CALCULAR IVA(15%) Y PRECIO FINAL->Leer el precio de un producto sin IVA y mostrar el IVA y el precio final. El IVA en Ecuador es 15%.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA#--QUE ME DAN
    #precio(input)

    #"PROCESO"--QUE HAGO CON ESO
    #iva= precio * 0,15; total=precio + iva

    #"SALIDA"--QUE DEBO MOSTRAR
    #EL IVA Y EL TOTAL

#2->BOSQUEJO A MANO
    #precio = 80
    #iva= 80 * 0.15 = 12
    #total= 80 + 12 = 92

#3->DESCUBRIR EL PATRÓN 
    #Dos cálculos separados que usan el mismo dato de entrada. 
    #El 0.15 es una constante del problema — puedes definirla arriba con IVA = 0.15 para dejarla clara.
    #El formato :.2f muestra exactamente dos decimales, que es lo que se espera para dinero.

#4->ESCRIBIR EL CÓDIGO
IVA = 0.15
precio = float(input("Ingrese el precio:"))
iva = precio * IVA
total= precio + iva

print(f"IVA: ${iva:.2f}")
print(f"TOTAL: 4{total:.2f}")

#AHORA TÚ:
#Añadir un descuento del 10% que se aplique antes del IVA. 
#Muestra los tres valores: descuento, IVA, total.

precio = float(input("Ingresa el precio del producto: "))
des= precio * 0.10
dest = precio - des
calculo = dest * 0.15# total = dest + calculo
print(f"DESCUENTO: {des}")
print(f"IVA: {calculo}")
print(f"TOTAL A PAGAR: {total: .2f}")

#__________________________________________________________________________________________________________________

#EJERCICIO_2:PAR O IMPAR->Leer un número entero y determinar si es par o impar.

#1->ENTENDER EL PROBLEMA

    #"ENTRADA"--QUE ME DAN
    #num(input)

    #"PROCESO"--QUE HAGO CON ESO
    #VERIFICAR SI num % 2 == 0

    #"SALIDA"--QUE DEBO MOSTRAR
    #"PAR" O "IMPAR"

#2->BOSQUEJO A MANO
   # num = 7
   #7 % 2 = 1->IMPAR
   #4 % 2 = 0->PAR
   #0 % 2 = 0->PAR

#3->ENCUENTRA EL PATRÓN
    #LA OPERACIÓN QUE SE EJECUTA ES DIVIDIR EL NUMERO PARA 2
    #SI EL RESIDUO DA 0 ES PAR Y SINO ES IMPAR

#4->ESCRIBIR EL CÓDIGO

num = int(input("INGRESE UN NÚMERO:"))
esultado= "PAR" if num % 2 == 0 else "IMPAR"
print(f"{num} es {resultado}.")

#AHORA TÚ:
#Modifícalo para que además diga si es múltiplo de 3, de 5, o de ambos.

num = int(input("INGRESE UN NÚMERO:"))
resultado = "PAR" if num % 2 == 0 else "IMPAR"

if num % 3 == 0 and num % 5 == 0:
     multiplo = "múltiplo de 3 y de 5"
elif num % 3 == 0:
     multiplo = "múltiplo de 3"
elif num % 5 == 0:
    multiplo = "múltiplo de 5"
else:
     multiplo = "no es múltiplo de 3 ni de 5"

print(f"{num} es {multiplo} y es {resultado}.")

#______________________________________________________________________________

#JERCICIO_3:CONVERTIR TIEMPO:SEGUNDOS A hh:mm:ss

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #seg(input)

    #"PROCESO"--QUE HAGO CON ESO
    #dividir sucesivamente para 3600 y 60 usando // y %

    #"SALIDA"--QUE DEBO MOSTRAR
    #LOS SEGUNDOS EN hh:mm:ss

#2->BOSQUEJO A MANO
    #seg=3725
    #horas = 3725 // 3600 = 1  sobran 125
    #minutos = 125 // 60 = 2   sobran 5
    #segundos = 5

#3->DESCUBRIR EL PATRÓN
    #Este ejercicio muestra la potencia de combinar // y %. 
    #La división entera te dice cuántas unidades grandes caben (horas); 
    #el residuo, lo que sobra para las unidades más pequeñas.

#4->ESCRIBIR EL CODIGO

seg = int(input("INGRESE LOS SEGUNDOS TOTALES:"))
horas = seg // 3600
resto = seg % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

#AHORA TÚ:
#Al revés: leer hh:mm:ss y convertir a segundos totales. Tendrás que usar split(":").

tiempo = input("INGRESE LA HORA (hh:mm:ss): ")
partes = tiempo.split(":")
horas = int(partes[0])
minutos = int(partes[1])
segundos = int(partes[2])
total_segundos = horas * 3600 + minutos * 60 + segundos

print(f"Segundos totales: {total_segundos}")

#___________________________________________________________________________________________________-

#EJERCICIO_4:CAMBIO DE BILLETES->Un cajero solo tiene billetes de $20, $10, $5 y $1. 
#Dado un monto, mostrar cuántos billetes de cada uno se necesitan (usando la mínima cantidad).

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #monto(input)

    #"PROCESO"--QUE HAGO CON ESO
    #dividir sucesivamente por 20, 10, 5, 1 con // y %

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #CANTIDAD DE BILLETES DE CADA TIPO

#2->BOSQUEJO A MANO
    #monto=87
    #$20: 87 // 20 = 4, sobra 7
    #$10:  7 // 10 = 0, sobra 7
    #$5 :  7 //  5 = 1, sobra 2
    #$1 :  2 //  1 = 2, sobra 0

#3->DESCUBRIR EL PATRÓN
    #Es el mismo patrón que segundos→horas, pero con billetes
    # en cada paso agarras la mayor denominación que quepa.
    #Trabajamos siempre con el resto, no con el monto original.

#4->ESCRIBIR EL CODIGO

monto = int(input("Monto: $"))
resto = monto

b20 = resto // 20; resto = resto % 20
b10 = resto // 10; resto = resto % 10
b5  = resto // 5;  resto = resto % 5
b1  = resto // 1;  resto = resto % 1

print(f"$20 * {b20}")
print(f"$10 * {b10}")
print(f"$5  * {b5}")
print(f"$1  * {b1}")

#AHORA TÚ:
#Añadir billete de $50 al inicio.
#Después probar con monedas de $0.25, $0.10, $0.05 y $0.01 (necesitas trabajar con centavos).

monto = float(input("Monto: $"))
centavos = round(monto * 100)
resto = centavos

b50 = resto // 5000; resto = resto % 5000
b20 = resto // 2000; resto = resto % 2000
b10 = resto // 1000; resto = resto % 1000
b5  = resto // 500;  resto = resto % 500
b1  = resto // 100;  resto = resto % 100

m25 = resto // 25; resto = resto % 25
m10 = resto // 10; resto = resto % 10
m5  = resto // 5;  resto = resto % 5
m1  = resto // 1;  resto = resto % 1

print(f"$50 * {b50}")
print(f"$20 * {b20}")
print(f"$10 * {b10}")
print(f"$5  * {b5}")
print(f"$1  * {b1}")
print(f"$0.25 * {m25}")
print(f"$0.10 * {m10}")
print(f"$0.05 * {m5}")
print(f"$0.01 * {m1}")
#______________________________________________________________________________________________________

#EJERCICIO_5:SUMAS DÍGITOS DE UN NÚMERO DE 3 CIFRAS:
#Lee un número de 3 cifras y muestra la suma de sus dígitos. Ejemplo: 435 → 4+3+5 = 12.

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #num(input)

    #"PROCESO"--QUE HAGO CON ESO
    #extraer cada cifra (centenas, decenas, unidades) usando // y %
    #sumar las tres cifras extraídas

        #"SALIDA"->QUÉ DEBO MOSTRAR
    #LA SUMA DE LAS CIFRAS DEL NÚMERO

#2->BOSQUEJO A MANO
    #num= 358
    #centenas: 358 // 100 = 3        (la cifra de las centenas)
    #decenas :(358 // 10) % 10 = 5   (35 // 10... no, 358//10=35, 35%10=5)
    #unidades: 358 % 10 = 8          (el resto de dividir entre 10)
    #suma = 3 + 5 + 8 = 16

#3->DESCUBRIR EL PATRÓN
    #Cada cifra se extrae directo de "num" (no de un resto acumulado):
    #  // 100 -> centenas | // 10 % 10 -> decenas | % 10 -> unidades
    #Es el patrón clásico de "separar dígitos" de un número.

#4->ESCRIBIR EL CÓDIGO

num = int(input("Número de 3 cifras: "))

centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10

suma = centenas + decenas + unidades
print(f"Suma: {suma}")
#_______________________________________________________________________________________________________________

#EJERCICIO_6:CONVERTIR MINUTOS A HORAS Y MINUTOS
#Lee una cantidad de minutos y muéstrala como «X horas Y minutos». 
#Ejemplo: 135 → «2 horas 15 minutos».

#1->ENTENDER EL PROBLEMA:
    #"ENTRADA"--QUE ME DAN
    #minutos(input)

     #"PROCESO"--QUE HAGO CON ESO
    #dividir total entre 60 con // y % para separar horas y minutos

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #LA CANTIDAD DE HORAS Y MINUTOS

#2->BOSQUEJO A MANO
    #total=125
    #horas: 125 // 60 = 2   (sobran 5 minutos)
    #mins :125 % 60 = 5

#3->DESCUBRIR EL PATRÓN
    #Misma lógica que billetes/cifras: // para la parte entera,
    #% para lo que sobra. Aquí solo hay un nivel (60), no una cadena.

#4->ESCRIBIR EL CODIGO

total = int(input("Minutos totales: "))

horas = total // 60
mins = total % 60

print(f"{horas} horas {mins} minutos")
#______________________________________________________________________________________________________________

#EJERCICIO_7:INDICE DE MASA CORPORAL:
#Lee peso (kg) y estatura (m) y calcula el IMC. Fórmula: IMC = peso / estatura². Muestra el IMC con 2 decimales.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #peso (kg) y estatura (m), por input

    #"PROCESO"--QUE HAGO CON ESO
    #calcular imc = peso / (estatura ** 2)

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL VALOR DEL IMC, CON 2 DECIMALES

#2->BOSQUEJO A MANO
    #peso=70, estatura=1.75
    #estatura ** 2 = 1.75 * 1.75 = 3.0625
    #imc = 70 / 3.0625 = 22.857142...
    #imc formateado: 22.86

#3->DESCUBRIR EL PATRÓN
    #No hay // ni % aquí; es una fórmula matemática directa.
    #El patrón clave es usar (estatura ** 2) para elevar al cuadrado
    #y el formato :.2f para redondear la salida a 2 decimales.

#4->ESCRIBIR EL CODIGO

peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")
#___________________________________________________________________________________________________

#EJERCICIO_8:REDONDEO POR CIFRA DECIMAL:Lee un número decimal y una cantidad de decimales, y muéstralo redondeado.
# Ejemplo: 3.14159 con 2 decimales → 3.14.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #num (el número a redondear) y dec (cantidad de decimales), por input

    #"PROCESO"--QUE HAGO CON ESO
    #usar round(num, dec) para redondear num a "dec" decimales

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #EL NÚMERO YA REDONDEADO

#2->BOSQUEJO A MANO
    #num=3.14159, dec=2
    #round(3.14159, 2) -> mira el 3er decimal (1) para decidir
    #como es menor a 5, no sube -> resultado = 3.14

#3->DESCUBRIR EL PATRÓN
    #round(valor, n) redondea "valor" dejando "n" decimales,
    #a diferencia de :.2f (que solo formatea el texto de salida),
    #round() cambia el valor numérico real.

#4->ESCRIBIR EL CODIGO

num = float(input("Número: "))
dec = int(input("Decimales: "))

resultado = round(num, dec)
print(resultado)
#_______________________________________________________________________________________________

#EJERCICIO_9:DSCTO POR CANTIDAD:Un producto vale $12.
# Si compras 10 o más te dan 15% de descuento.
#si compras entre 5 y 9 te dan 5%. Calcula el total.

#1->ENTENDER EL PROBLEMA
    #"ENTRADA"--QUE ME DAN
    #cant (cantidad de unidades a comprar), por input
    #PRECIO (constante = 12, precio unitario fijo)

    #"PROCESO"--QUE HAGO CON ESO
    #decidir el % de descuento según rangos de "cant" (if/elif/else)
    #calcular subtotal = PRECIO * cant
    #calcular total aplicando el descuento

    #"SALIDA"->QUÉ DEBO MOSTRAR
    #PRECIO UNITARIO, PORCENTAJE DE DESCUENTO Y TOTAL A PAGAR

#2->BOSQUEJO A MANO
    #cant=12
    #cant >= 10? SÍ -> descuento = 0.15 (no evalúa los demás elif/else)
    #subtotal = 12 * 12 = 144
    #total = 144 * (1 - 0.15) = 144 * 0.85 = 122.4
    #salida: Precio unitario: $12 | Descuento: 15% | Total: $122.40

#3->DESCUBRIR EL PATRÓN
    #Es una cadena de condiciones (if/elif/else) evaluada de arriba
    #hacia abajo: apenas una se cumple, se detiene. Por eso el orden
    #debe ir de mayor a menor exigencia (>=10 antes que >=5).

#4->ESCRIBIR EL CODIGO

PRECIO = 12
cant = int(input("Cantidad: "))

# Determinar el descuento

if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
   descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")
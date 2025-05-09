# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(f"Numero: {i}")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = input("Ingrese un numero")
total_digitos = 0
for digito in numero:
    total_digitos += 1
print(f"Total digitos: {total_digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el primer numero"))     
num2 = int(input("Ingrese el segundo numero"))

if num1 > num2:
    aux = num1
    num1 = num2
    num2 = aux
suma = 0
for i in range(num1 + 1,num2):
    suma += i

print(f"La suma total entre los 2 valores es: {suma}")

# 4) Sumar números ingresados por el usuario hasta que ingrese 0, luego mostrar el total acumulado.

numero = int(input("Ingrese un numero"))
suma = 0

while numero != 0:
    suma = suma + numero
    numero = int(input("Ingrese un numero"))

print(f"La suma total es {suma}")

# 5) Juego de adivinar un número aleatorio entre 0 y 9, mostrando la cantidad de intentos al acertar.

import random
numero_random=random.randint(0,9)
intentos = 0

numero_user=int(input("Intente adivinar el numero aleatorio del 0 al 9. Ingrese un numero"))

while numero_user != numero_random:
    intentos += 1
    numero_user=int(input("Numero incorrecto ingrese uno nuevamente"))

print(f"Excelente adivinaste el numero en {intentos} intentos")

# 6) Imprimir todos los números pares entre 0 y 100 en orden decreciente.

for i in range(100,0,-2):
    print(f"Numero {i}")

# 7) Calcular la suma de todos los números entre 0 y un número positivo ingresado por el usuario.

numero = int(input("Ingrese un numero positivo"))
suma=0
for i in range(0,numero,+1):
    suma = suma + i
print(f"La suma total es{suma}")

# 8) Ingresar 100 números enteros y contar cuántos son pares, impares, negativos y positivos.

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(1, 101): 
    numero = int(input(f"Ingrese el número {i}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9) Ingresar 100 números enteros y calcular la media de esos valores.

suma = 0
cantidad = 100 

for i in range(1, cantidad + 1):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero

media = suma / cantidad
print(f"La media de los {cantidad} números ingresados es: {media}")

# 10) Invertir los dígitos de un número ingresado por el usuario (ejemplo: 547 → 745).

num = input("Ingrese un numero para invertir sus digitos")
longitud = len(num)
reverso=""
for i in range(longitud -1,-1,-1):
    reverso = reverso + num[i]
print(f"El numero revertido es {reverso}")
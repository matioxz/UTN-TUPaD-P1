import math

# 1. Imprimir Hola Mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludar usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    # 1
    imprimir_hola_mundo()
    
    # 2
    nombre = input("Ingresa tu nombre: ")
    print(saludar_usuario(nombre))
    
    # 3
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    # 4
    radio = float(input("Ingresa el radio de un círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")
    
    # 5
    segundos = int(input("Ingresa una cantidad de segundos: "))
    print(f"Equivale a {segundos_a_horas(segundos):.2f} horas")
    
    # 6
    numero_tabla = int(input("Número para tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)
    
    # 7
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {mult}, División: {div}")
    
    # 8
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es {imc:.2f}")
    
    # 9
    celsius = float(input("Temperatura en Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}")
    
    # 10
    n1 = float(input("Primer número: "))
    n2 = float(input("Segundo número: "))
    n3 = float(input("Tercer número: "))
    promedio = calcular_promedio(n1, n2, n3)
    print(f"El promedio es: {promedio:.2f}")

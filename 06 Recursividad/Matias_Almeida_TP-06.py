# Ejercicio 1: Factorial recursivo
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    return [factorial(i) for i in range(1, hasta + 1)]

# Ejercicio 2: Fibonacci recursivo
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)

def mostrar_serie_fibonacci(hasta):
    return [fibonacci(i) for i in range(hasta + 1)]

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejercicio 4: Convertir a binario
def a_binario(n):
    if n == 0:
        return ""
    return a_binario(n // 2) + str(n % 2)

def binario(n):
    return a_binario(n) or "0"

# Ejercicio 5: Verificar palindromo sin usar [::-1] ni reverse()
def es_palindromo(palabra):
    def limpiar(cadena):
        return ''.join(c for c in cadena if c != ' ')
    
    palabra = limpiar(palabra)
    
    def verificar(i, j):
        if i >= j:
            return True
        if palabra[i] != palabra[j]:
            return False
        return verificar(i + 1, j - 1)

    return verificar(0, len(palabra) - 1)

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejercicio 7: Contar bloques de pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejercicio 8: Contar apariciones de un dígito en un número
def contar_digito(numero, digito):
    digito = str(digito)
    def contar(n):
        if n == 0:
            return 0
        return (1 if str(n % 10) == digito else 0) + contar(n // 10)
    return contar(numero)

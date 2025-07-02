# Práctica 7: Estructuras de datos complejas
# Punto 1: Crear el diccionario e incorporar nuevas frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

# Punto 2: Actualizar precios
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})

# Punto 3: Obtener listas de frutas y precios
lista_frutas = list(precios_frutas.keys())
lista_precios = list(precios_frutas.values())
print("Frutas:", lista_frutas)
print("Precios:", lista_precios)

# Punto 4: Agenda de contactos
contactos = {
    "Juan": "123456",
    "Ana": "987654",
    "Luis": "555555",
    "Sofía": "444444",
    "Pedro": "333333"
}
# Consultar contacto
nombre = "Juan"
print(f"Número de {nombre}: {contactos.get(nombre, 'No existe')}")

# Punto 5: Procesar frase
frase = "hola mundo hola"
palabras = frase.split()
unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Palabras únicas:", unicas)
print("Recuento:", recuento)

# Punto 6: Alumnos con tuplas de notas
alumnos = {
    "Sofía": (10, 9, 8),
    "Luis": (6, 7, 7),
    "María": (9, 9, 10)
}
promedios = {alumno: sum(notas)/3 for alumno, notas in alumnos.items()}
print("Promedios:", promedios)

# Punto 7: Operaciones con sets
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
alguno = parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Solo uno:", solo_uno)
print("Alguno de los dos:", alguno)

# Punto 8: Diccionario con stock
stock = {"manzana": 10, "banana": 20}

def consultar_stock(producto):
    return stock.get(producto, "No existe")

def agregar_stock(producto, cantidad):
    if producto in stock:
        stock[producto] += cantidad
    else:
        stock[producto] = cantidad

print("Stock de banana:", consultar_stock("banana"))
agregar_stock("banana", 5)
agregar_stock("naranja", 12)
print("Stock actualizado:", stock)

# Punto 9: Agenda con claves como tuplas
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}
print("Actividad del martes 15:00:", agenda.get(("martes", "15:00"), "No hay actividad"))

# Punto 10: Invertir diccionario
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {capital: pais for pais, capital in original.items()}
print("Diccionario invertido:", invertido)

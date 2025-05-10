
# 1) Múltiplos de 4 del 1 al 100
multiplos_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4:", multiplos_de_4)

# 2) Mostrar el penúltimo elemento
favoritos = ["pizza", "gato", "café", "sol", "libros"]
print("2) Penúltimo favorito:", favoritos[-2])

# 3) Lista vacía + append
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("python")
print("3) Lista con palabras:", lista_vacia)

# 4) Reemplazo en lista animales
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Animales modificados:", animales)

# 5) Explicación del programa
  # El programa crea una lista de números, elimina el número más grande usando max y remove, y muestra la lista resultante sin ese número.

# 6) Lista del 10 al 30 con saltos de 5 y mostrar dos primeros
lista_saltos = list(range(10, 31, 5))
print("6) Dos primeros de la lista:", lista_saltos[:2])

# 7) Reemplazo en lista autos
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]
print("7) Autos modificados:", autos)

# 8) Lista dobles con append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista de dobles:", dobles)

# 9) Modificaciones en lista compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")                # a)
compras[1][1] = "tallarines"            # b)
compras[0].remove("pan")                # c)
print("9) Compras modificadas:", compras)  # d)

# 10) Lista anidada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10) Lista anidada:", lista_anidada)

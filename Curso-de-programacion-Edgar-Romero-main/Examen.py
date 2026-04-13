# Ejercicio 1

oracion = input("Introduce una frase para saber cuantas vocales y consonantes tiene: ").lower()

vocales = 0
consonante = 0

for l in oracion:
    if l in "aeiou": 
        vocales += 1
    elif l in "bcdfghjklmnñpqrstvwxyz":
        consonante += 1
    
print(f"La frase tiene un total de {vocales} vocales y {consonante} consonantes")


# Ejercicio 2

import random
num = random.randint(1, 100)
conteo = 0

while conteo != num:
    conteo = int(input("Adivina el numero del 1 al 100: "))
    if conteo < num:
        print("Vuelvelo a intentar. El numero es mayor")
    elif conteo > num:
        print("Vuelvelo a intentar. El numero es menor")
print("Has acertado el numero. ¡Felicidades!")

# Ejercicio 3

listanum = []

while True:
    numeros = input("Ingresa los numeros que quieras y pon fin para terminar: ")
    if numeros.lower() == "fin":
        numeros.append(float(numeros))
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio total de los numeros es de: {promedio}")

# Ejercicio 4

def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

las_palabras = input("Introduce la frase o palabra que quieras: ")

if polindromo(las_palabras):
        print("Es un palindromo. True")
else:
        print("No es un palindromo. False")

# Ejercicio 5

parrafos = input("Ingresa un párrafo para saber las palabras repetidas y el numero de veces: ")
termino = parrafos.split()
veces = {} 

for p in termino:
    if p in veces:
        veces[p] += 1 
    else:
        veces[p] = 1 


# Ejercicio 6 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = 0

for n in numeros:
    if n % 2 == 0: 
     pares += n

print(f"Al sumar los numeros pares el resultado es: {pares}")

# Ejercicio 7

agenda = {}

while True:
    print("1. Agregar, 2. Buscar, 3. Listar, 4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        nombre = input("Ingresa el nombre: ")
        telefono = input("Ingresa el teléfono: ")
        agenda[nombre] = telefono
    elif opcion == "2":
        nombre = input("Ingresa el nombre que quieres buscar: ")
        if nombre in agenda:
            print(f"El teléfono de {nombre} es {agenda[nombre]}")
        else:
            print("Contacto no encontrado.")
    
    elif opcion == "3": 
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    elif opcion == "4":
        print("Saliendo de la agenda.")
        break

# Ejercicio 8

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = []

for e in lista1:
    if e in lista2 and e not in comunes:
        comunes.append(e)
print(f"Los elementos comunes entre las dos listas son: {comunes}")

# Ejercicio 9

tupla = [("nombre", "Edgar"), ("edad", 17), ("ciudad", "Maracaibo")]
diccionario = {}

for c, v in tupla:
    diccionario[c] = v

print(f"El diccionario creado a partir de la tupla es: {diccionario}")

# Ejercicio 10

n = int(input("Ingresa la altura deseada del triangulo: "))

for a in range(1, n + 1):
    print("*" * a)

while True:
    numeros = input("Ingresa los numeros que quieras y pon fin para terminar: ")
    if numeros.lower() == "fin":
        numeros.append(float(numeros))
    if len(numeros) > 0:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio total de los numeros es de: {promedio}")
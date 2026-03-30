# Ejercicio 1

oracion = input("Introduce una frase para saber cuantas vocales y consonantes tiene: ")

vocales = 0
consonante = 0

for l in oracion:
    if l in "aeiou": 
        vocales += 1
    elif l in "bcdfghjklmnñpqrstvwxyz":
        consonante += 1
    
print(f"La frase tiene un total de {vocales} vocales y {consonante} consonantes")

for l in oracion:
    if len(l):
        print("")


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
        print("Es un polindromo. True")
else:
        print("No es un polindromo. False")

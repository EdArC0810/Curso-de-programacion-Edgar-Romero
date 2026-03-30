# Ejercicio 1

print("Calculo del total del precio con el 21% De IVA")

monto = float(input("Introduce el monto de su compra: "))

precio_final = (monto * 1.21)

print(f"El precio final con un 21% de impuestos será de: {precio_final}")

# Ejercicio #2

print("Descubre: ¿cuantos dias tienes desde que naciste?.")

años = int(input("Ingresa tu edad: "))

cal_dias = años * 365

print(f"Tienes un total de: {cal_dias} dias")

# Ejercicio #3

print("Calcula el Borde de un Circulo acá.")
medida = int(input("Ingresa el diametro del Circulo: "))
calculo = medida * 3.1416

print(f"El borde del circulo es de {calculo}cm")

# Ejercicio 4

print("Confirma si eres mayor de edad.")

edad = int(input("Ingresa tu edad actual: "))

mayor = edad >= 18

print(f"¿Es mayor de 18 años?: {mayor}")

# Ejercicio 5

print("¿Cuántos kilómetros recorre por cada litro?")

km = int(input("Introduce la cantidad de kilometros recorridos: "))

litros = int(input("\nAhora la cantidad de litros usados: "))

cal = km / litros

print(f"Se consumen un total de {cal}km/l")

# Ejercicio 6

numero = int(input("Introduce un número para verificar si se encuentra entre 10 y 20: "))

comparacion = 10 <= numero <= 20 and 20 >= numero >= 10

print(f"¿Está entre el rango 10-20?: {comparacion}")

# Ejercicio 7

calculodias = int(input("Introduce el numero de dias para saber sus segundos en total: "))

cal = calculodias * 24 * 60 * 60 

print(f"En total {calculodias} dias son {cal} segundos")

# Ejercicios 8

A = float(input("Elige un numero para la letra a: "))

B = float(input("Elige un numero para la letra a: "))

X = -B / A

print(f"Al despejar x queda: x = {X}")

# Ejercicio 9

Peso = float(input("Ingresa tu peso corporal: "))
Altura = float(input("Ingresa tu altura: "))

masa_corporal = Peso / Altura * 2

print(f"Tu masa corporal es de {masa_corporal}")

# Ejercicio 10

palabra1 = input("Introduce la primera palabra: ")
palabra2 = input("Introduce la segunda palabra: ")

mas_larga = (len(palabra1) > len(palabra2) and palabra1) or palabra2

print(f"La palabra mas larga es: {mas_larga}")
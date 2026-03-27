# Ejercicio 5

print("Es año bisiesto?")

año = int(input("Ingresa un año: "))

si_366 = (año % 4 == 0 and año % 100 != 0)

if si_366:
    print(f"{año} es un año bisiesto")

else:
    print(f"{año} no es un año bisiesto")


# Ejercicio 6

print("Hola, Bienvenido a la Calculadora Aritmetica")

numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))

print("Escoje la operacion: ")
print("+ | suma")
print("* | multiplicacion")
print("- | resta")
print("/ | division")

operacion = input("Introduce el tipo de operacion a realizar: ").lower()

if operacion in ["+", "suma"]:
    resultado = numero1 + numero2
    print(f"Resultado de la suma: {resultado}")
elif operacion in ["*", "multiplicacion"]:
    resultado= numero1 * numero2
    print(f"Resultado de la multiplicacion: {resultado}")
elif operacion in ["-", "resta"]:
    resultado = numero1 - numero2
    print(f"Resultado de la resta: {resultado}")
elif operacion in ["/", "division"]:
    if numero2 == 0:
        print("ERROR: No se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
        print(f"Resultado de la Division: {resultado}")


# Ejercicio 7


long1 = int(input("Digita la longitud del primer lado del Triangulo: "))
long2 = int(input("Digita la longitud del segundo lado del Triangulo: "))
long3 = int(input("Digita la longitud del tercer lado del Triangulo: "))

if (long1 + long2 > long3) and (long1 + long3 > long2) and (long2 + long3 > long1):
    if long1 == long2 == long3:
        print("El Triangulo es: Equilatero")
elif long1 == long2 != long3 or long3 == long2 != long1 or long2 != long3 == long1:
    print("El Triangulo es: Isósceles")
elif long1 != long2 != long3:
    print("El Triangulo es: Isósceles")
else:
    print("Error: Medidas inválidas para formar un triángulo.")


# Ejercicio 8

nota = int(input("Ingresa tu puntaje y obtén tu nota alfabética: "))

if 90 <= nota <= 100:
    print(f"Su {nota} es equivalente a una A")
elif 80 <= nota <= 89:
    print(f"Su {nota} es equivalente a una B")
elif 70 <= nota <= 79:
    print(f"Su {nota} es equivalente a una C")
elif 60 <= nota <= 69:
    print(f"Su {nota} es equivalente a una D")
elif 0 <= nota <= 59:
    print(f"Su {nota} es equivalente a una F")

else:
    print("ERROR: Has introducido un puntaje fuera del rango")

# Ejercicio 9

print("Bienvenido jugadores, este es el juego del Piedra, Papel o Tijera")

jugador1 = print(input("Jugador 1, ¿Que  vas a sacar?: "))
jugador2 = print(input("Jugador 2, ¿Que  vas a sacar?: ")),


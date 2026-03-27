# Ejercicio 1
print("Bienvenido al programa donde compruebas si el numero es Par o Impar")

numero = int(input("Introduce el numero a comprobar: "))

if numero % 2 == 0:
    print("El número es par")

else: 
    print("El número es impar")


# Ejercicio 2

print("Descubrelo si el numero es mayor o igual al otro")

num1 = int(input("Introduce el 1er numero a comparar: "))
num2 = int(input("Introduce el 2do numero a comparar: "))

if num1 == num2:
    print(f"{num1} es igual a {num2}.")
elif num1 > num2:
    print(f"{num1} es mayor que {num2}.")


# Ejercicio 3

edad = int(input("¿Cuantos años tienes?: "))

if edad == 18:
    print("Tienes la mayoría de edad")

elif edad >= 19:
    print("Eres Mayor de edad")

elif edad < 18:
    print("Eres Menor de edad")

# Ejercicio 4

print("Calcula si el monto de la compra tiene un descuento")

monto = float(input("Introduce el monto total de su compra: "))

cal_descuento = monto * 0.15
precio_final = monto - cal_descuento

if monto > 999:
    print("Tu compra tiene un descuento de 15%")
    print(f"El precio final será de: {precio_final}")
else:
    print("Tu compra no tiene un descuento de 15%")
    print(f"El precio final será de: {monto}")


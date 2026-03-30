# Ejercicio 2
prohibidos = ("admin", "root", "system", "fuck", "python", "madrid", "edgararc") 
rechazados = [] usuario = input("Introduce un nombre de usuario: ") 

while usuario in prohibidos: rechazados.append(usuario) print("ERROR: Nombre de usuario no encontrado") 
usuario = input("Intenta nuevamente: ")
print(f"Bienvenido al Mundo Futbolero {usuario}")
print(f"Intentos fallados de nombres: {rechazados}") 

#Ejercicio 5

print("Bienvenido a crea tu contraseña segura")

validas = []
limites = (8, 18)

contraseñas = input("Escribe tus opciones de contraseñas para evaluarlas (separadas por coma): ")

lista = contraseñas.split(",")

for c in  lista:
    c = c.strip()
    if len(c) >= limites[0] and len(c) <= limites[1]:
        if "@" in c or "#" in c or "$" or "*" or "+" in c:
            validas.append(c)
print("\nResultados: Contraseñas válidas y ultra seguras:", validas)





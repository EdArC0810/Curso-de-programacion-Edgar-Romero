# Ejercicio 2
prohibidos = ("admin", "root", "system", "fuck", "python", "madrid", "edgararc") 
rechazados = []
usuario = input("Introduce un nombre de usuario: ") 
while usuario in prohibidos:
    rechazados.append(usuario)
    print("ERROR: Nombre de usuario no encontrado")
    usuario = input("Intenta nuevamente: ")
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

# Ejercicio 6
print("Bienvenido al juego de combate!")

hp = [200, 200]
daño = [30, 50]

print("¡Inicia el combate!")

while hp[0] > 0 and hp[1] > 0:
    ataque = input("Elige tu ataque: GOLPE o PATADA: ").lower()
    if ataque == "golpe":
        hp[1] -= daño[0]
        print(f"Gran golpe el enemigo pierde {daño[0]} puntos de vida. HP restante: {hp[1]}")
    elif ataque == "patada":
        hp[1] -= daño[1]
        print(f"¡Increíble patada! El enemigo pierde {daño[1]} puntos de vida. HP restante: {hp[1]}")
    else:
        print("El Ataque no existe, intenta nuevamente.")

    if hp[1] > 0:
        hp[0] -= daño[0]
        print(f"El enemigo contraataca y te quita {daño[1]} puntos de vida. HP restante: {hp[0]}")
        
    print(f"Vidas Finales. Jugador: {hp[0]}, Enemigo: {hp[1]}")

if hp[0] > 0:
    print("Victoria! Has derrotado al enemigo.")
else:
    print("Derrota... El enemigo ha ganado el combate.")
    



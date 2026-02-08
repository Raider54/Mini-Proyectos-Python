import random

print("juego de piedra, papel o tijera!".upper())

while True: 

    print("-" * 30)

    opciones = ["piedra", "papel", "tijera"]

    jugador = input("Por favor elige: Piedra🪨, Papel📃, Tijera✂️ : ").lower()

    if jugador not in opciones:
        print("Opcion no valida ❌")
        continue

    computadora = random.choice(opciones)

    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("Empatados")

    elif jugador == "piedra" and computadora == "tijera":
        print("Has ganado!")

    elif jugador == "tijera" and computadora == "piedra":
        print("Has perdido!")

    elif jugador == "papel" and computadora == "piedra":
        print("Has ganado!")

    elif jugador == "piedra" and computadora == "papel":
        print("Has perdido!")

    elif jugador == "tijera" and computadora == "papel":
        print("Has ganado!")
    
    elif jugador == "papel" and computadora == "tijera":
        print("Has perdido!")

    print("-" * 30)

    salir = input("Deseas continuar jugando? (s/n): ")

    if salir == "s":
        print("A seguir jugando!")

    else:
        print("Saliendo del juego...")
        break
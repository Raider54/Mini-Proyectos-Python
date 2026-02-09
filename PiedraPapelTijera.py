import random

print("juego de piedra, papel o tijera!".upper())

opciones = ["piedra", "papel", "tijera"]

while True: 

    print("-" * 30)

    jugador = input("Por favor elige: Piedra🪨, Papel📃, Tijera✂️ : ").lower()

    if jugador not in opciones:
        print("Opcion no valida ❌")
        continue

    computadora = random.choice(opciones)

    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("Empatados")

    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("Has ganado! 🙌")

    else:
        print("Has perdido... 🤖")

    print("-" * 30)

    salir = input("Deseas continuar jugando? (s/n): ").lower()

    if salir == "s":
        print("A seguir jugando!")

    else:
        print("Saliendo del juego...")
        break
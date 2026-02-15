print("😎Comprobación de edad😎".upper())

while True:

    try:

        edad = int(input("Dame tu edad: "))

    except ValueError:
        print("Edad no valida...!")
        continue

    if edad >= 18:
            print("Eres mayor de edad!")

    elif edad >= 15 and edad <= 17:
            print("Todavía estas adolescente!")

    else:
            print("Eres menor de edad!")

    while True:

        salir = input("Deseas salir? (si/no): ").lower()

        if salir == "si":
            print("Saliendo del programa...!")
            exit()

        elif salir == "no":
            print("Continuemos...!")
            break
        
        else:
            print("Escribe Si o No para salir...!")
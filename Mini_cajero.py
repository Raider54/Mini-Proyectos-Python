saldo = 1000

while True:

    print("\nopciones disponibles".upper())
    print("1. Consulta de saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    try:
        opcion = int(input("\nElige una opcion: "))
    except ValueError:
        print("Solo numeros.")
        continue

    if opcion == 1:
        print(f"Saldo disponible: {saldo}")

    elif opcion == 2:
        agregar = float(input("Cantidad a depositar: "))
        saldo += agregar
        print(f"Se agrego: {agregar}$")

    elif opcion == 3:
        retirar = float(input("Cantidad a retirar: "))
        if retirar < saldo:
            saldo -= retirar
            print(f"Cantidad retirada: {retirar}")

        else:
            print("Fondo insuficiente ❌")

    elif opcion == 4:
        salir = input("Salir? (s/n): ").lower()

        if salir == "s":
            print("Consulta terminada")
            break
        else:
            print("Continuado")
    
    else:
        print("Numero incorrecto, revisa las opciones")
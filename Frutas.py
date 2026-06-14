frutas = ["pera", "manzana", "uvas"]

while True:

    print(f"Esta es la lista disponible: {frutas}")

    print("\n===Opciones disponibles===")
    print("1. Para agregar una fruta de tu preferencia")
    print("2. Para remover una fruta")
    print("3. Salir")


    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        agregar = input("Agrega una fruta de tu preferencia: ")
        if agregar not in frutas:
            frutas.append(agregar)
            print(f"Tu fruta {agregar} se agrego correctamente!")
        else:
            print("La fruta ya existe")
    elif opcion == "2":
        remover = input("Coloca una fruta para remover: ")
        if remover in frutas:
            frutas.remove(remover)
            print(f"Se elimino {remover} correctamente!")
        else:
            print(f"La fruta {remover} no esta en la lista")

    elif opcion == "4":
        print("Saliendo")
        break

    else:
        print("❌ Opcion no valida. Por favor, elige 1, 2 o 3.")
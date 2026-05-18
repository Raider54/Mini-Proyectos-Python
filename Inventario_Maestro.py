inventario = []
categorias_validas = ("Arma", "Pocion", "Tesoro")

while True:
    print("\n---OPCIONES DISPONIBLES---")
    print("1. Agregar")
    print("2. Ver todo")
    print("3. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        cat = input("Categoria del arma (Arma, Pocion, Teroso): ").capitalize()
        if cat not in categorias_validas:
            print(f"Cat {cat} no es una categoria valida.")
            continue

        agregar = input(f"Nombre del {cat}?: ").lower()
        if agregar in inventario:
            print("El objeto ya existe en tu inventario")
            continue
        else:
            inventario.append(agregar)
            print("Se agrego el nuevo objeto!")
    
    elif opcion == "2":
        for objeto in inventario:
            print(f"Objeto del inventario: {objeto}")
        if inventario == []:
            print("Inventario vario...")

    elif opcion == "3":
        cerrar = input("Realmente quieres salir? (s/n): ").lower()
        if cerrar == "s":
            print("Cerrando!")
            break
        else:
            print("Continuando!")
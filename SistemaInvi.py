import json
print("----bienvenido al sistema de control de inventario----".upper()) #Bienvenida

inventario = [] #Inventario general 

while True:

    print("\nmenu de opciones".upper()) #Menu de opciones
    print("1. Registrar Producto")
    print("2. Visualizar inventario")
    print("3. Eliminar Producto")
    print("4. Salir")

    opcion = input("Elige una opcion: ") #Le pedimos al usuario que ingres una opcion valida

    if opcion == "1": #Empezamos con las condiciones junto con Try y Except para evitar posibles errores
        nombre_producto = input("Ingresa el nombre del producto: ")
        try: #Usamos Try para evitar errores de letras.
            cantidad = int(input("Cantidad a Ingresar: "))
            precio_unitario = float(input("Precio Unitario: ")) 
        except ValueError:
            print("Solo numeros...")
            continue

        datos_compra = { #Guardamos toda la information dentro del dict
        "nombre_producto" : nombre_producto,
        "cantidad" : cantidad,
        "precio_unitario" : precio_unitario,
        "total" : cantidad * precio_unitario
    }
        inventario.append(datos_compra)
        print("Producto registrado con éxito!")

    elif opcion == "2":
        if inventario == []: #Si inventario vacio no mostramos nada, solo el print
            print("Inventario vacio...")
        else:
            for elemento in inventario: #Con for mostraremos los productos ingresados en el dict
                 print("-" * 30)
                 print(f"Nombre del producto: {elemento['nombre_producto']}".title().strip())
                 print(f"Cantidad ingresada: {elemento['cantidad']}")
                 print(f"Precio unitario: {elemento['precio_unitario']:.2f}$")
                 print(f"Precio total: {elemento['total']:.2f}$")
                 print("-" * 30)
                 print(json.dumps(inventario, indent=3, ensure_ascii=False))

    elif opcion == "3":
        if inventario == []:
            print("Inventario vacio...")
            continue
        else: #Al tener un producto a eliminar saltamos a este else
            print("Productos disponibles: ")
            for elemento in inventario:
                print(f"Producto: {elemento['nombre_producto']}")
            eliminar = input("Ingresa el nombre del producto a eliminar: ").lower()
        
            if eliminar == "":
                print("No se ingreso un producto...")
                continue
            encontrado = False
            for elemento in inventario:
                if elemento['nombre_producto'].lower() == eliminar:
                    inventario.remove(elemento)
                    print(f"Producto '{eliminar}' eliminado con exito!")
                    encontrado = True
                    break

            if not encontrado:
                print("Producto no encontrado en el inventario...")
            
    elif opcion == "4":
        salir = input("Salir? (s/n): ").lower()

        if salir == "s":
            print("Cerrando el sistema....")
            break
        else:
            print("Continuando...")

    else:
        print("opcion no valida...❌")
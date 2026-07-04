print("----bienvenido al sistema de control de inventario----".upper()) #Bienvenida

inventario_productos = {}

while True:

    print("====Menu de Opciones====")
    print("1. Registrar Producto")
    print("2. Eliminar Producto")
    print("3. Visualizar Inventario")
    print("4. Salir")

    opcion = input("Que desea consultar?: ")

    if opcion == "1":

        nombre_producto = input("Nombre del producto: ").lower().strip()
        try:
            cantidad = int(input("Cantidad: "))
            precio_unitario = float(input("Precio Unitario: "))
        except ValueError:
            print("Solo numeros.")
            continue
        precio_total = cantidad * precio_unitario

        inventario_productos[nombre_producto] = {
            "cantidad" : cantidad,
            "precio_unitario" : precio_unitario,
            "precio_total" : precio_total
        }

    elif opcion == "2":
        if inventario_productos == {}:
            print("El inventario está vacío. No hay productos para eliminar. 🚫")
        else:
            eliminar_producto = input("Que producto desea eliminar?: ").lower().strip()
            if eliminar_producto in inventario_productos:
                del inventario_productos[eliminar_producto]
                print("Producto eliminado con éxito.")
            else:
                print("El producto no se encuentra en el inventario. ❌")
                
    elif opcion == "3":
        if inventario_productos == {}:
            print("El inventario está vacío. No hay productos para mostrar. 🚫")
        for nombre, detalles in inventario_productos.items():
            print(f"Nombre Del Producto: {nombre}")
            print(f"Cantidad: {detalles['cantidad']}")
            print(f"Precio Unitario: {detalles['precio_unitario']}")
            print(f"Total: ${detalles['precio_total']} 📈")

    elif opcion == "4":
        salir = input("Desea salir? (s/n): ").lower()
        if salir == "s":
            print("Saliendo del programa")
            break
        else:
            print("Continuando")

    else:
        print("Opcion no valida, intente nuevamente.")
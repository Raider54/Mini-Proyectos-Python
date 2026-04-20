print("💻sistema de producto💻".upper())

while True:

    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Precio del Producto: "))

    while True: 
        try:
            stock = int(input("Stock: "))
            break
        except ValueError:
            print("Por favor ingrese solo numeros.")

    datos_producto = {
        "nombre producto" : nombre_producto,
        "precio producto" : precio_producto,
        "stock" : stock
    }

    print("-" * 30)

    print("resumen de operación".upper())

    print(f"➡️ Producto: {datos_producto['nombre producto'].upper()}")

    if datos_producto["precio producto"] < 0:
        print("Precio invalido")

    else: 
        print(f"➡️ Precio del Producto: {datos_producto['precio producto']:.2f}$")

    if datos_producto["stock"] > 0:
        print("➡️ Disponible en Stock!")

    elif datos_producto["stock"] == 0:
        print("Stock Agotado ❌")

    elif datos_producto["stock"] < 0:
        print("Stock Invalido ⚠️")

    else:
        print("Error ⚠️")

    print("-" * 30)
    
    cerrar = input("Salir del programa? Escribe (si/no): ").lower()

    if cerrar == "si":
        print("Saliendo...")
        break

    else:
        print("Continuar Consultando.")
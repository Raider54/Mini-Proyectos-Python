carrito = []

while True:
    producto = input("Agregar producto o escriba 'Finalizar' para salir: ").lower()

    if producto == "finalizar":
        print("Programa terminado")
        break

    else:
        carrito.append(producto)
        print("Producto agregado!")

        continuar = input("Continuar agregando? (s/n): ").lower()

        if continuar == "s":
            print("Continuando")
            continue

        else:
            print("Programa finalizado!")
            break

print("---RECIBO---")
for producto in carrito:
    print(f"Producto: {producto.capitalize()}")

print(f"Total productos agregados: {len(carrito)}")
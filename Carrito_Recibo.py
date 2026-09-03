inventario = {
    "manzana" : 1.5,
    "pan": 2.0,
    "leche" : 1.2
}

print("---LISTA DE PRODUCTOS DISPONIBLES---")
for producto in inventario:
        print(producto)

producto = input("Escribe un producto: ").lower()

if producto in inventario:
        cantidad = int(input("Cuantas unidades desea?: "))
        precio = float(input("Por favor ingrese el precio: "))
        total = precio * cantidad
else:
        print("Lo siento el producto no existe")

print("---RESUMEN DE COMPRA---")
print(f"Producto: {producto}")
print(f"Cantidad adquirida: {cantidad}")
print(f"Precio: {precio}")
print(f"Total a pagar: {total}")
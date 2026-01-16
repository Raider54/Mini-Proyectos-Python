#Trabajando con una pequeña lista
frutas = ["manzanas", "peras", "uva", "naranja"]
frutas.append("kiwi")
frutas.insert(0,"cerezas")

print("La cantidad de frutas:", len(frutas))

frutas.sort(reverse=True)
print(f"Lista ordenada: {frutas}")

eliminado = frutas.pop(2)
print(f"Se elimino: {eliminado}")
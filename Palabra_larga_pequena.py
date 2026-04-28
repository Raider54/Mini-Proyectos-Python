# 🎯 Enunciado

# El usuario escribe una frase:

# Debes hacer TODO en un solo for:

# Mostrar cada palabra
# Decir si es larga (>5 letras)
# Contar cuántas son largas

frase = input("Frase: ")
palabras = frase.split()
contador = 0
largas = []

for palabra in palabras:
    if len(palabra) > 5:
        print(f"\nTu palabra es larga: {palabra}")
        largas.append(palabra)
        contador += 1
    else:
        print(f"\nPalabra pequeña: {palabras}")

print(f"Cantidad: {contador}")

if largas:
    print(f"Palabras mas larga: {max(largas, key=len)}")
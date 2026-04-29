# El usuario escribe una frase y tú:

# Muestras todas
# Separas largas y cortas
# Cuentas cada grupo
# Muestras la más larga

frase = input("Frase: ")
palabras = frase.replace(",", "").split()
largas = []
cortas = []
contador_largas = 0
contador_cortas = 0

for palabra in palabras:
    print(f"\nPalabra: {palabra}")

    if len(palabra) > 5:
        print(f"Palabra larga: {palabra}")
        largas.append(palabra)
        contador_largas += 1

    else:
        print(f"Palabra corta: {palabra}")
        cortas.append(palabra)
        contador_cortas += 1
        
print("\n--- RESULTADOS ---")

print(f"Cantidad largas: {contador_largas}")
print(f"Cantidad cortas: {contador_cortas}")

if largas:
    print(f"Palabra mas larga: {max(largas, key=len)}")

else:
    print("No hay palabras largas")
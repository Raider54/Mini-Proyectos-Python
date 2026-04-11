pedir_palabra = input("Escribe una palabra: ")
letra = input("Escribe una letra: ").lower()

if letra in pedir_palabra:

    posicion = pedir_palabra.find(letra)

    print(f"La letra {letra} se encuentra en la posicion {posicion}")

else:
    print(f"La letra '{letra}' no se encuentra en tu palabra")
   

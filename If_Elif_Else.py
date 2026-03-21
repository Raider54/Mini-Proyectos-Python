
print("ejercicio de condiciones IF/ELIF/ELSE\n".upper())

while True:
        
    usuario = input("Usuario: ")

    try:
        password = int(input("Password: "))

    except ValueError:
        print("Solo numeros...")
        continue

    if usuario == "admin" and password == 1234:
        print("Acceso permitido")
    elif usuario == "admin":
        print("Password incorrecto")
    elif password == 1234:
        print("Usuario no encontrado")
    else:
        print("Credenciales incorrectas!\n")

    while True:

        salir = input("Deseas salir? (si/no): ").lower()

        if salir == "si":
            print("Saliendo del programa...")
            break #En vez de Exit es mejor Break en programas reales, para practicar esta bien

        elif salir == "no":
            print()
            break

        else:
            print("Escribe correctamente Si o No para salir del programa.")
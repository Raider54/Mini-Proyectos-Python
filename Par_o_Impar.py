#! Haz un programa que pida: un numero, diga si es par o mayor que 10, es par y menor o igual a 10, es impar y mayor a 10, luego es impar y menor o igual a 10

print("Par o Impar, Mayor o Igual a X numero!\n")

while True:

    try:

        num = int(input("Pon un numero: "))

    except ValueError:
        print("Solo numeros!")
        continue

    if num % 2 == 0 and num > 10:
        print("Par y mayor a 10")

    elif num % 2 == 0 and num <= 10:
        print("Par y menor o igual a 10")

    elif num % 2 != 0 and num > 10:
        print("Impar y mayor a 10")

    elif num % 2 != 0 and num <= 10:
        print("Impar y menor o igual a 10")

    while True:

        salir = input("Salir del programa? (s/n): ").lower()

        if salir == "s":
            print("Saliendo del programa!")
            exit()
            
        elif salir == "n":
            print("Continuemos")
            break

        else:
            print("Solo coloca S o N...")
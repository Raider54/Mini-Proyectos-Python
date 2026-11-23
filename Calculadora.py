#Calculadora 

print("🧮=====calculadora=====🧮".upper())

while True:

    try:

        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))

        print("-" * 50)

        #Operaciones aritméticos disponibles

        print("operaciones disponibles👇".title())
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Modulo")

        print("-" * 50)

        #Pidiendo al usuario que escoja una de las 4 opciones

        opcion = input("Seleccione una opcion del 1-5: ")

        if opcion == "1":
            print(f"El resultado de la suma es: {a + b}")

        elif opcion == "2":
            print(f"El resultado de la resta es: {a - b}")

        elif opcion == "3":
            print(f"El resultado de la multiplicación es: {a * b:.2f}")

        elif opcion == "4":
            if b != 0:
                print(f"El resultado de la division es: {a / b:.2f}")
            else:
                print("No se puede dividir por 0")

        elif opcion == "5":
            print(f"El resultado del modulo es: {a % b}")

        else:
            print("Error operación incorrecta ❌")

    except ValueError:
        print("Error, solo numeros...!")
        continue

        #Saliendo del programa

    while True:

        salir = input("Deseas salir del programa (si/no): ").lower()

        if salir == "si":
            print("🧮 Gracias por usar la calculadora 🧮".title())
            

        elif salir == "no":
            print("Continuemos...!")
            break

        else:
            print("Por favor escribe, Si o No...!")
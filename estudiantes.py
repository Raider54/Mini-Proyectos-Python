estudiantes = {}

print("===opciones===".upper())
print("1.Agregar")
print("2.Ver Alumnos")
print("3.Salir")

while True:

    opciones = input("Escoge una opcion: ")

    if opciones == "1":
        nombre_alumno = input("Nombre del estudiante: ")
        try:
            nota_alumno = int(input("Nota del estudiante: "))
        except ValueError:
            print("Solo numeros.")
            continue
        estudiantes[nombre_alumno] = nota_alumno
        print("Estudiante agregado correctamente!")
    
    elif opciones == "2":
        if estudiantes == {}:
            print("Dict vacio.")
            continue
        for nombre, nota in estudiantes.items():
            if nota >= 5:
                print(f"{nombre} Aprobado, nota {nota}")
            else:
                print(f"{nombre} Desaprobado, nota {nota}")
    
    elif opciones == "3":
        salir = input("Salir? (s/n): ").lower()

        if salir == "s":
            print("Cerrando programa")
            break
        
        else:
            print("Continuar")
    
    else:
        print("Opcion no valida, intente nuevamente.")
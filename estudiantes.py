estudiantes = {}

def mostrar_menu():

    print("===opciones===".upper())
    print("1.Agregar")
    print("2.Ver Alumnos")
    print("3.Salir")

def evaluar_nota(nota):
    if nota > 18:
        return "Sobresaliente"
    elif nota >= 10:
        return "Aprobado"
    else:
        return "Reprobado"

while True:

    mostrar_menu()
    opciones = input("Escoge una opcion: ")

    if opciones == "1":
        nombre_alumno = input("Nombre del estudiante: ")
        try:
            nota = int(input("Nota del estudiante: "))
        except ValueError:
            print("Solo numeros.")
            continue
        estudiantes[nombre_alumno] = nota
        print("Estudiante agregado correctamente!")
    
    elif opciones == "2":
        if not estudiantes:
            print("Dict vacio.")
            continue
        print("\n=== LISTA DE ESTUDIANTES ===")
        for nombre, nota in estudiantes.items():
            estado = evaluar_nota(nota)
            print(f"Estudiante: {nombre.title()} | Nota: {nota} | Estado: {estado}")
            print("=" * 28)
    elif opciones == "3":
        salir = input("Salir? (s/n): ").lower()

        if salir == "s":
            print("Cerrando programa")
            break
        
        else:
            print("Continuar")
    
    else:
        print("Opcion no valida, intente nuevamente.")
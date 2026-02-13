from datetime import datetime

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

ano_actual = datetime.now().year
edad_en_2050 = edad + (2050 - ano_actual)

print("Saludos", nombre + " Usted tiene", edad, "años")
print("En el ano 2050 usted tendra:", edad_en_2050, "años")

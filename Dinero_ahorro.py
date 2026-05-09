meta = 50
ahorro_total = 0

while ahorro_total < meta:

    dinero = float(input("Dinero a guardar: "))

    ahorro_total += dinero #Al contenedor de la izquierda en cualquier ejercicio, se le suma lo que esta a su derecha

    print(f"LLevas ahorrado: {ahorro_total}")

print("\nresumen de operacion".upper())
print(f"Meta {meta}$")
print(f"Meta alcanzada: {ahorro_total}$")
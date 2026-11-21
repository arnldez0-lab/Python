edad = int(input("¿Cuántos años tienes? "))
# Evalúa la condición principal; la sangría indica qué pertenece al bloque
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 0:  # Solo se revisa si la condición anterior fue falsa
    print("Eres menor de edad.")
else:
    print("Edad no válida.")

# Escribe un programa que pregunte el nombre, apellido, estado civil,
# que pregunte numero de hijos y edad del usuario en la consola y despues
# muestre por pantalla con todas las letras mayusculas, en la edad solo acepte
# numeros de 2 digitos y en los hijos 1 dijito.

nombre = input("Nombre: ")
apellido = input("Apellido: ")
estadoCivil = input("Estado civil: ")

while True:
    edad = input("Edad (2 digitos): ")
    if len(edad) == 2:
        try:
            int(edad)
            break
        except:
            print("Error: solo numeros")
    else:
        print("Error: solo 2 digitos")

while True:
    hijos = input("Numero de hijos (1 digito): ")
    if len(hijos) == 1:
        try:
            int(hijos)
            break
        except:
            print("Error: solo numeros")
    else:
        print("Error: solo 1 digito")

print("\n--- DATOS DEL USUARIO ---")
print("Nombre:", nombre.upper())
print("Apellido:", apellido.upper())
print("Estado civil:", estadoCivil.upper())
print("Edad:", edad)
print("Hijos:", hijos)
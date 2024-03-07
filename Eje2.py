#Crea un programa que solicite al usuario ingresar un número entero positivo (N). El programa debe mostrar la tabla demultiplicar del número, teniendo en cuenta que se debe generar la tabla con los primeros 10 valores de dicha tabla. 
 
def tabla_de_multiplicar():
    while True:
        try:
            numeroInt = int(input("Ingresa un número entero - > : "))
            if numeroInt > 0:
                print(f"Tabla de multiplicar del {numeroInt}:")
                for i in range(1, 11):
                    print(f"{numeroInt} x {i} = {numeroInt * i}")
                break
            else:
                print("Por favor, ingresa un número entero - > :")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

tabla_de_multiplicar()
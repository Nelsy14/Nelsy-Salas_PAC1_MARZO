
#Escribe un programa que permita al usuario convertir una temperatura en grados centígrados a Fahrenheit o viceversa. El programa debesolicitar al usuario ingresar la temperatura y la unidad de medida (C para Celsius, F para Fahrenheit) y luego realizar la conversióncorrespondiente, el programa debe manejar un menú de opciones y solo detenerse cuando se presione la opción finalizar.

def celsius_a_fahrenheit(celsiusInt):
    return (celsiusInt * 9/5) + 32

def fahrenheit_a_celsius(fahrenheitInt):
    return (fahrenheitInt + 5/9) - 32


def main():
    while True:
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Finalizar")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            celsiusInt = float(input("Ingresa la temperatura en grados Celsius: "))
            print(f"{celsiusInt}°C = {celsius_a_fahrenheit(celsiusInt)}°F")
        elif opcion == "2":
            fahrenheitInt = float(input("Ingresa la temperatura en grados Fahrenheit: "))
            print(f"{fahrenheitInt}°F = {fahrenheit_a_celsius(fahrenheitInt)}°C")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige una opción del menú.")

if __name__ == "__main__":
    main()
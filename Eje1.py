#Crea un programa que solicite al usuario ingresar valores y este debe verificar cuando se ingresa una vocal, el programa debe contar y mostrar la cantidad de vocales (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar.

def contar_vocales(valores):
    vocalesSrt = 'aeiou'
    contadorInt = {}.fromkeys(vocalesSrt, 0)
    letraSrt = valores.lower()

    for letra in valores:
        if letraSrt.lower() in vocalesSrt:
            contadorInt[letraSrt.lower()] += 1

    return contadorInt

def main():
    while True:
        valor = input("Ingresa una letra o escribe 'finalizar' para terminar: ")

        if valor.lower() == 'finalizar':
            break
        elif len(valor) == 1 and valor.isalpha():
            resultadoInt = contar_vocales(valor)
            print("Cantidad de vocales ingresadas:")
            for vocal, cantidad in resultadoInt.items():
                print(f"{vocal}: {cantidad}")
        else:
            print("Ingresa solo una letra válida o 'finalizar'.")

if __name__ == "__main__":
    main()


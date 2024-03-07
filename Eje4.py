def calcular_descuento(categoria, precio):
    descuentos = {
        "Ferretería": 0.10,
        "Aseo": 0.05,
        "Seguridad": 0.15,
        "Alimentos": 0.08,
        "Electrodomésticos": 0.12
    }

    if categoria in descuentos:
        descuento = descuentos[categoria]
        precio_final = precio - (precio * descuento)
        return precio_final
    else:
        return precio

def main():
    categorias = {
        "Ferretería": 0,
        "Aseo": 0,
        "Seguridad": 0,
        "Alimentos": 0,
        "Electrodomésticos": 0
    }
    total_recaudado = 0

    while True:
        categoria = input("Ingresa la categoría del producto (Ferretería, Aseo, Seguridad, Alimentos, Electrodomésticos) o 'TERMINAR' para finalizar: ")
        
        if categoria == "TERMINAR":
            break
        
        if categoria not in categorias:
            print("Categoría no válida.")
            continue

        try:
            precio = float(input("Ingresa el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
        except ValueError:
            print("Precio inválido.")
            continue

        categorias[categoria] += 1
        total_recaudado += calcular_descuento(categoria, precio)

    print("\nResumen de compras:")
    for categoria, cantidad in categorias.items():
        print(f"{categoria}: {cantidad} productos")
    
    print(f"\nTotal recaudado: ${total_recaudado}")

if __name__ == "__main__":
    main()
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")
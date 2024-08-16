def generar_pseudoaleatorios(m, a, c, s, cantidad):
    # Inicializamos la lista de números pseudoaleatorios con el valor de la semilla
    numeros = [s]

    for _ in range(1, cantidad):
        # Generamos el siguiente número en la secuencia
        nuevo_numero = (a * numeros[-1] + c) % m
        numeros.append(nuevo_numero)

    return numeros

def solicitar_valor_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Error: El valor debe ser un entero positivo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

def solicitar_valor_no_negativo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Error: El valor debe ser un entero no negativo. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

def solicitar_semilla(mensaje, m):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0 or valor >= m:
                print(f"Error: El valor de la semilla debe ser un entero no negativo y menor que {m}. Intente nuevamente.")
            else:
                return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

def main():
    try:
        # Solicitar el valor de m
        m = solicitar_valor_positivo("Ingrese el valor de m (modulo): ")

        # Solicitar el valor de a
        a = solicitar_valor_positivo("Ingrese el valor de a (multiplicador): ")

        # Solicitar el valor de c
        c = solicitar_valor_no_negativo("Ingrese el valor de c (incremento): ")

        # Solicitar el valor de s (semilla)
        s = solicitar_semilla("Ingrese el valor de s (semilla): ", m)

        # Solicitar la cantidad de números a generar
        cantidad = solicitar_valor_positivo("Ingrese la cantidad de números a generar: ")

        # Generar la secuencia de números pseudoaleatorios
        secuencia = generar_pseudoaleatorios(m, a, c, s, cantidad)
        print(f"Secuencia de números pseudoaleatorios generada: {secuencia}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

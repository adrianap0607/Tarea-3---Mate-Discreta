def hash_insert(array, num_cells):
    # Verificar que el número de celdas sea un entero positivo
    if not isinstance(num_cells, int) or num_cells <= 0:
        raise ValueError("El número de celdas debe ser un entero positivo.")

    # Verificar que el array no tenga más elementos que el número de celdas
    if len(array) > num_cells:
        raise ValueError("El número de elementos en el array no puede exceder el número de celdas.")

    # Inicializamos las celdas de memoria como una lista con None para representar celdas vacías
    memory_cells = [None] * num_cells

    def hash_function(n):
        # Función de dispersión H(n) = n % num_cells
        return n % num_cells

    for number in array:
        # Calculamos la posición inicial usando la función de dispersión
        position = hash_function(number)
        
        # Si la celda está ocupada, buscamos la siguiente disponible
        while memory_cells[position] is not None:
            position = (position + 1) % num_cells  # Avanzamos a la siguiente celda, ciclando si es necesario
        
        # Almacenamos el número en la celda disponible
        memory_cells[position] = number

    return memory_cells

# Función interactiva para pedir datos al usuario
def main():
    try:
        # Solicitar el número de celdas
        num_cells = int(input("Ingrese el número de celdas de la tabla hash: "))
        
        while True:
            # Solicitar el array de números separados por comas
            array_input = input("Ingrese los números a almacenar en el array, separados por comas: ")
            
            # Verificar si el array está correctamente formateado
            array_items = array_input.split(',')
            if len(array_items) < 2:  # Validación para asegurarse de que haya comas
                print("Error: Debe ingresar al menos dos números separados por comas. Intente nuevamente.")
                continue
            
            # Validar que todos los elementos sean enteros
            try:
                array = [int(item.strip()) for item in array_items]
            except ValueError:
                print("Error: Todos los elementos deben ser números enteros válidos. Intente nuevamente.")
                continue

            # Verificar que el número de elementos no exceda el número de celdas
            if len(array) > num_cells:
                print(f"Error: El número de elementos ({len(array)}) no puede exceder el número de celdas ({num_cells}).")
            else:
                break
        
        # Insertar los números en las celdas de la tabla hash
        stored_data = hash_insert(array, num_cells)
        print(f"Estado final de las celdas de memoria: {stored_data}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

def bubble_sort(arr):
    """
    Implementación de Bubble Sort.
    Complejidad: O(n²) en tiempo, O(1) en espacio
    """
    n = len(arr)
    # Recorremos la lista n veces
    for i in range(n):
        # Flag para optimizar: si no hay intercambios, la lista ya está ordenada
        swapped = False
        
        # En cada iteración, el elemento más grande flota hasta su posición final
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, intercambiarlos
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Si no hubo intercambios en esta pasada, la lista ya está ordenada
        if not swapped:
            break
    
    return arr

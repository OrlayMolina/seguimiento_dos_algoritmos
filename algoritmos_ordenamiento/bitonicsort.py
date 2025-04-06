def bitonic_sort(arr):
    """
    Implementación de Bitonic Sort.
    Requiere que la longitud del array sea una potencia de 2.
    Complejidad: O(n log²(n)) en tiempo, O(1) en espacio (in-place)
    """
    # Verificar que la longitud sea una potencia de 2
    n = len(arr)
    if n & (n-1) != 0:
        raise ValueError("La longitud del array debe ser una potencia de 2")
    
    def bitonic_merge(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                comp_and_swap(arr, i, i + k, direction)
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            # Ordenar la primera mitad en dirección ascendente
            bitonic_sort_recursive(arr, low, k, 1)
            # Ordenar la segunda mitad en dirección descendente
            bitonic_sort_recursive(arr, low + k, k, 0)
            # Mezclar toda la secuencia en la dirección especificada
            bitonic_merge(arr, low, cnt, direction)
    
    def comp_and_swap(arr, i, j, direction):
        # Si direction=1, significa orden ascendente
        if (direction == 1 and arr[i] > arr[j]) or (direction == 0 and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    # Comenzar la ordenación
    bitonic_sort_recursive(arr, 0, n, 1)
    return arr

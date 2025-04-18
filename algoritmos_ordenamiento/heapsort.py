def heapsort(data, comparator=None):
    result = data.copy()

    def compare(a, b):
        if comparator:
            return comparator(a, b)
        else:
            # Verifica si los elementos son tuplas/listas con al menos 2 elementos
            if isinstance(a, (list, tuple)) and len(a) > 1 and isinstance(b, (list, tuple)) and len(b) > 1:
                if a[1] > b[1]:
                    return -1
                elif a[1] < b[1]:
                    return 1
                else:
                    if isinstance(a[0], str) and isinstance(b[0], str):
                        return -1 if a[0].lower() < b[0].lower() else 1
                    return -1 if a[0] < b[0] else 1
            else:
                # Para tipos simples (números, strings, etc.)
                if a > b:
                    return -1
                elif a < b:
                    return 1
                else:
                    return 0
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and compare(arr[left], arr[largest]) < 0:
            largest = left

        if right < n and compare(arr[right], arr[largest]) < 0:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(result)

    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(result, i, 0)
    
    return result
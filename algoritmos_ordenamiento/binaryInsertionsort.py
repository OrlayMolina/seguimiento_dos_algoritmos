def binaryInsertionsort(data):
    def binary_search(arr, val, start, end):
        # Verificar si estamos trabajando con tuplas/listas
        trabajando_con_tuplas = (isinstance(val, (list, tuple)) and len(val) > 1)
        
        if start == end:
            if trabajando_con_tuplas:
                if arr[start][1] < val[1]:
                    return start
                elif arr[start][1] > val[1]:
                    return start + 1
                else:
                    if isinstance(arr[start][0], str) and isinstance(val[0], str):
                        if arr[start][0].lower() > val[0].lower():
                            return start
                    else:
                        if arr[start][0] > val[0]:
                            return start
                    return start + 1
            else:
                # Para tipos simples
                if arr[start] < val:
                    return start
                else:
                    return start + 1
        
        if start > end:
            return start

        mid = (start + end) // 2
        
        if trabajando_con_tuplas:
            if arr[mid][1] < val[1]:
                return binary_search(arr, val, start, mid - 1)
            elif arr[mid][1] > val[1]:
                return binary_search(arr, val, mid + 1, end)
            else:
                if isinstance(arr[mid][0], str) and isinstance(val[0], str):
                    if arr[mid][0].lower() > val[0].lower():
                        return binary_search(arr, val, start, mid - 1)
                else:
                    if arr[mid][0] > val[0]:
                        return binary_search(arr, val, start, mid - 1)
                return binary_search(arr, val, mid + 1, end)
        else:
            # Para tipos simples
            if arr[mid] < val:
                return binary_search(arr, val, start, mid - 1)
            else:
                return binary_search(arr, val, mid + 1, end)
    
    result = data.copy()
    
    for i in range(1, len(result)):
        val = result[i]
        j = binary_search(result, val, 0, i - 1)
        result.insert(j, result.pop(i))
    
    return result
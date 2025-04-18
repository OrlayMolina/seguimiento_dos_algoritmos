def insertionsort(data, key=None):
    result = data.copy()
    n = len(result)
    
    def get_key(item):
        if key is not None:
            return key(item)
        elif isinstance(item, (list, tuple)) and len(item) > 1:
            return item[1]
        return item

    def get_term(item):
        if isinstance(item, (list, tuple)) and len(item) > 0:
            return str(item[0]).lower()
        return str(item).lower()
    
    for i in range(1, n):
        current = result[i]
        current_key = get_key(current)
        current_term = get_term(current)
        j = i - 1
        
        while j >= 0:
            j_key = get_key(result[j])
            
            # Comparar por clave primero
            if j_key < current_key:
                break
            elif j_key > current_key:
                result[j + 1] = result[j]
                j -= 1
            else:
                # Si las claves son iguales, comparar por término
                j_term = get_term(result[j])
                if j_term <= current_term:
                    break
                result[j + 1] = result[j]
                j -= 1
        
        result[j + 1] = current
    
    return result

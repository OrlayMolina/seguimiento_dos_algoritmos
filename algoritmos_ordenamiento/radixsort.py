def radixsort(data, key=None):
    result = data.copy()
    
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

    # Verificar si estamos trabajando con tuplas/listas con segundo elemento numérico
    if all(isinstance(item, (list, tuple)) and len(item) > 1 and 
           isinstance(get_key(item), (int, float)) for item in result):
        
        max_freq = max(get_key(item) for item in result)
        
        exp = 1
        while max_freq // exp > 0:
            count = [[] for _ in range(10)]
            
            for item in result:
                digit = (get_key(item) // exp) % 10
                count[digit].append(item)
    
            result.clear()
            # Recorremos en orden inverso para tener orden descendente
            for i in range(9, -1, -1):
                if key is not None:
                    count[i].sort(key=lambda x: get_term(x))
                else:
                    count[i].sort(key=lambda x: get_term(x))
                result.extend(count[i])
            
            exp *= 10
    # Si son solo números (sin tuplas)
    elif all(isinstance(item, (int, float)) for item in result):
        max_num = max(result)
        
        exp = 1
        while max_num // exp > 0:
            count = [[] for _ in range(10)]
            
            for item in result:
                digit = (item // exp) % 10
                count[digit].append(item)
    
            result.clear()
            for i in range(10):
                result.extend(count[i])
            
            exp *= 10
    else:
        # Para otros tipos (como cadenas)
        if key is not None:
            result.sort(key=key)
        else:
            result.sort(reverse=True)
    
    return result
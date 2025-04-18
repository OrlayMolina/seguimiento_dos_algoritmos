def selectionsort(data, key=None):
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
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if key is not None:
                # Usar el comparador personalizado
                if key(result[j], result[max_idx]) < 0:
                    max_idx = j
            else:
                # Usar comparación predeterminada
                key_j = get_key(result[j])
                key_max = get_key(result[max_idx])
                
                if key_j > key_max:
                    max_idx = j
                elif key_j == key_max:
                    term_j = get_term(result[j])
                    term_max = get_term(result[max_idx])
                    
                    if term_j < term_max:
                        max_idx = j
        
        result[i], result[max_idx] = result[max_idx], result[i]
    
    return result
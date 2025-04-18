def shellsort(data, key=None):
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

    # Secuencia de gaps recomendada por Knuth
    gap = 1
    while gap < n // 3:
        gap = gap * 3 + 1
    
    while gap > 0:
        for i in range(gap, n):
            temp = result[i]
            j = i
            
            # Comparación basada en la función key o en la lógica predeterminada
            while j >= gap:
                key_j_gap = get_key(result[j - gap])
                key_temp = get_key(temp)
                
                if key_j_gap < key_temp:
                    result[j] = result[j - gap]
                    j -= gap
                elif key_j_gap == key_temp:
                    term_j_gap = get_term(result[j - gap])
                    term_temp = get_term(temp)
                    
                    if term_j_gap > term_temp:
                        result[j] = result[j - gap]
                        j -= gap
                    else:
                        break
                else:
                    break
            
            result[j] = temp
        
        # Reducir el gap según la secuencia de Knuth
        gap //= 3
    
    return result

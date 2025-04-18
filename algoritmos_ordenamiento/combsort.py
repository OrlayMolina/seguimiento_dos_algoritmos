def combsort(data, key=None):
    result = data.copy()
    n = len(result)
    gap = n
    shrink = 1.3
    sorted_flag = False
    
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

    def compare_items(a, b):
        key_a = get_key(a)
        key_b = get_key(b)

        if key_a != key_b:
            return key_a > key_b
        else:
            term_a = get_term(a)
            term_b = get_term(b)
            return term_a < term_b
    
    while not sorted_flag:
        gap = max(1, int(gap / shrink))
        
        if gap == 1:
            sorted_flag = True
        
        for i in range(0, n - gap):
            j = i + gap
            
            if key is not None:
                # Usar la función de comparación personalizada
                if key(result[i], result[j]) > 0:
                    result[i], result[j] = result[j], result[i]
                    sorted_flag = False
            else:
                # Usar la comparación predeterminada
                if compare_items(result[i], result[j]):
                    result[i], result[j] = result[j], result[i]
                    sorted_flag = False
                
    return result
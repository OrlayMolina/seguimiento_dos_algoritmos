def directionbubblesort(data, key=None):
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
    
    if n <= 1:
        return result
    
    left = 0
    right = n - 1
    last_swap = 0
    direction = True  # True para moverse de izquierda a derecha, False para derecha a izquierda
    
    while left < right:
        if direction:  # De izquierda a derecha
            for i in range(left, right):
                key_i = get_key(result[i])
                key_i_plus_1 = get_key(result[i + 1])
                
                if key_i < key_i_plus_1:
                    result[i], result[i + 1] = result[i + 1], result[i]
                    last_swap = i
                elif key_i == key_i_plus_1:
                    term_i = get_term(result[i])
                    term_i_plus_1 = get_term(result[i + 1])
                    
                    if term_i > term_i_plus_1:
                        result[i], result[i + 1] = result[i + 1], result[i]
                        last_swap = i
            
            right = last_swap
        else:  # De derecha a izquierda
            for i in range(right, left, -1):
                key_i = get_key(result[i])
                key_i_minus_1 = get_key(result[i - 1])
                
                if key_i_minus_1 < key_i:
                    result[i], result[i - 1] = result[i - 1], result[i]
                    last_swap = i
                elif key_i_minus_1 == key_i:
                    term_i = get_term(result[i])
                    term_i_minus_1 = get_term(result[i - 1])
                    
                    if term_i_minus_1 > term_i:
                        result[i], result[i - 1] = result[i - 1], result[i]
                        last_swap = i
            
            left = last_swap
        
        direction = not direction
    
    return result

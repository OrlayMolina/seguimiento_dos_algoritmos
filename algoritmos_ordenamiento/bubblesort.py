def bubblesort(data, key=None):
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
        swapped = False
        
        for j in range(0, n - i - 1):
            key_j = get_key(result[j])
            key_j_plus_1 = get_key(result[j + 1])

            if key_j < key_j_plus_1:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
            elif key_j == key_j_plus_1:
                term_j = get_term(result[j])
                term_j_plus_1 = get_term(result[j + 1])
                
                if term_j > term_j_plus_1:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True

        if not swapped:
            break
    
    return result
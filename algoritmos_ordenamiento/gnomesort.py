def gnomesort(data, key=None):
    result = data.copy()
    n = len(result)
    index = 0

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

    def compare_elements(a, b):
        if key is not None:
            # Usar la función comparadora personalizada
            return key(a, b) <= 0
        else:
            # Usar la comparación predeterminada
            key_a = get_key(a)
            key_b = get_key(b)
            
            if key_a > key_b:
                return True
            elif key_a == key_b:
                term_a = get_term(a)
                term_b = get_term(b)
                return term_a < term_b
            return False
    
    while index < n:
        if index == 0:
            index += 1
            continue

        if compare_elements(result[index], result[index - 1]):
            result[index], result[index - 1] = result[index - 1], result[index]
            index -= 1
        else:
            index += 1
    
    return result
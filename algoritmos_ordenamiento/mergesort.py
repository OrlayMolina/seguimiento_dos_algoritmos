def mergesort(data, key=None):
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
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            key_left = get_key(left[i])
            key_right = get_key(right[j])
            
            if key_left > key_right:
                result.append(left[i])
                i += 1
            elif key_left < key_right:
                result.append(right[j])
                j += 1
            else:
                # Si las claves son iguales, comparar por término
                term_left = get_term(left[i])
                term_right = get_term(right[j])
                
                if term_left < term_right:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
        
        # Añadir los elementos restantes
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def _mergesort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = _mergesort(arr[:mid])
        right = _mergesort(arr[mid:])
        
        return merge(left, right)
    
    if not data:
        return []
    
    return _mergesort(data.copy())

def bitonicsort(data, key=None):
    def extract_key(item):
        if key is not None:
            return key(item)
        elif isinstance(item, tuple) and len(item) > 1:
            return item[1]
        else:
            return item
    
    def get_first(item):
        if isinstance(item, tuple) and len(item) > 0:
            return str(item[0]).lower()
        return ""
    
    def compare_items(a, b, ascending):
        key_a = extract_key(a)
        key_b = extract_key(b)

        if isinstance(key_a, (int, float)) and isinstance(key_b, (int, float)):
            if key_a != key_b:
                return key_a < key_b if ascending else key_a > key_b
        elif isinstance(key_a, str) and isinstance(key_b, str):
            if key_a != key_b:
                return key_a < key_b if ascending else key_a > key_b
        else:
            str_a = str(key_a)
            str_b = str(key_b)
            if str_a != str_b:
                return str_a < str_b if ascending else str_a > str_b

        first_a = get_first(a)
        first_b = get_first(b)
        return first_a < first_b if ascending else first_a > first_b
    
    def bitonic_merge(arr, low, cnt, ascending):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                if compare_items(arr[i], arr[i + k], ascending):
                    arr[i], arr[i + k] = arr[i + k], arr[i]
            bitonic_merge(arr, low, k, ascending)
            bitonic_merge(arr, low + k, k, ascending)
    
    def bitonic_sort(arr, low, cnt, ascending):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort(arr, low, k, True)
            bitonic_sort(arr, low + k, k, False)
            bitonic_merge(arr, low, cnt, ascending)
    
    result = list(data)
    n = len(result)

    if n == 0:
        return result

    next_pow2 = 1
    while next_pow2 < n:
        next_pow2 *= 2

    padding = [None] * (next_pow2 - n)
    result.extend(padding)

    original_compare = compare_items
    
    def safe_compare(a, b, ascending):
        if a is None and b is None:
            return False
        if a is None:
            return not ascending
        if b is None:
            return ascending
        return original_compare(a, b, ascending)

    compare_items = safe_compare

    bitonic_sort(result, 0, next_pow2, False)

    result = [item for item in result if item is not None]
    
    return result
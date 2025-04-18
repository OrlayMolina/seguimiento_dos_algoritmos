def quicksort(data, key=None):
    if not data:
        return []

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

        if isinstance(key_a, (int, float)) and isinstance(key_b, (int, float)):
            if key_a != key_b:
                return -1 if key_a > key_b else 1
        elif isinstance(key_a, str) and isinstance(key_b, str):
            if key_a != key_b:
                return -1 if key_a > key_b else 1
        else:

            str_a = str(key_a)
            str_b = str(key_b)
            if str_a != str_b:
                return -1 if str_a > str_b else 1

        term_a = get_term(a)
        term_b = get_term(b)
        return -1 if term_a < term_b else 1 if term_a > term_b else 0

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if compare_items(arr[j], pivot) <= 0:
                i += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def _quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)

            _quicksort(arr, low, pi - 1)
            _quicksort(arr, pi + 1, high)
        
        return arr

    result = data.copy()

    if len(result) <= 1:
        return result

    return _quicksort(result, 0, len(result) - 1)
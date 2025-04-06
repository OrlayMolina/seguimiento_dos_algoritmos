def radixsort(arr):
    if not arr:
        return []
    # Encontrar la longitud máxima de las cadenas
    max_len = max(len(s) for s in arr)
    # Procesar desde el último carácter hasta el primero
    for pos in range(max_len - 1, -1, -1):
        buckets = {}
        for s in arr:
            # Si la cadena es muy corta, usamos "" (que se ordena antes)
            key = s[pos] if pos < len(s) else ""
            buckets.setdefault(key, []).append(s)
        sorted_keys = sorted(buckets.keys())
        arr = []
        for key in sorted_keys:
            arr.extend(buckets[key])
    return arr

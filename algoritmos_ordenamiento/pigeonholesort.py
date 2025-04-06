def pigeonholesort(arr):
    if not arr:
        return []
    
    # Para strings, usar hash simplificado
    min_val = 0
    max_val = 0
    
    str_to_num = {}
    for i, s in enumerate(arr):
        if s == "":
            val = -1  # Manejar cadenas vacías
        else:
            val = hash(s) % 1000000  # Limitar el rango
        str_to_num[s] = val
        
        if i == 0 or val < min_val:
            min_val = val
        if i == 0 or val > max_val:
            max_val = val
    
    size = max_val - min_val + 1
    holes = [[] for _ in range(size)]
    
    for s in arr:
        val = str_to_num[s]
        holes[val - min_val].append(s)
    
    result = []
    for hole in holes:
        result.extend(sorted(hole))
    
    return result

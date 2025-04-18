def pigeonholesort(data, key=None):
    def get_freq(item):
        if key is not None:
            return key(item)
        elif isinstance(item, (list, tuple)) and len(item) > 1:
            try:
                return int(item[1])
            except (ValueError, TypeError):
                return 0
        else:
            return 0

    def get_term(item):
        if isinstance(item, (list, tuple)) and len(item) > 0:
            return str(item[0]).lower()
        return str(item).lower()

    if not data:
        return []
    
    min_freq = min(get_freq(item) for item in data)
    max_freq = max(get_freq(item) for item in data)
    
    range_size = max_freq - min_freq + 1
    pigeonholes = {i: [] for i in range(min_freq, max_freq + 1)}

    for item in data:
        pigeonholes[get_freq(item)].append(item)

    for freq in pigeonholes:
        if key is not None:
            # Ordenar usando el comparador personalizado para los items con la misma frecuencia
            pigeonholes[freq].sort(key=lambda x: get_term(x))
        else:
            # Ordenamiento predeterminado
            pigeonholes[freq].sort(key=lambda x: get_term(x))
    
    result = []
    for freq in range(max_freq, min_freq - 1, -1):
        result.extend(pigeonholes[freq])
    
    return result
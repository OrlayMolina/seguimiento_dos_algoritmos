def bucketsort(data, key=None):
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

    # Encontrar frecuencias min y max
    min_freq = min(get_freq(item) for item in data)
    max_freq = max(get_freq(item) for item in data)

    bucket_count = max_freq - min_freq + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir los elementos en buckets basados en la frecuencia
    for item in data:
        freq = get_freq(item)
        buckets[freq - min_freq].append(item)

    # Ordenar cada bucket
    for i in range(bucket_count):
        if key is not None:
            # Usar el comparador personalizado para ordenar dentro de los buckets
            sub_items = buckets[i]
            sub_items.sort(key=lambda x: get_term(x))
        else:
            # Ordenamiento predeterminado
            buckets[i].sort(key=lambda x: get_term(x))
    
    # Concatenar todos los buckets en el resultado final (en orden inverso)
    result = []
    for i in range(bucket_count - 1, -1, -1):
        if buckets[i]:
            result.extend(buckets[i])
    
    return result
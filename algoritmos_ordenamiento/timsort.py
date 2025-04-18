from functools import cmp_to_key

def timsort(data, comparator=None):
    if comparator:
        return sorted(data, key=cmp_to_key(comparator))
    else:
        if data and isinstance(data, list) and len(data) > 0 and isinstance(data[0], tuple) and len(data[0]) >= 2:
            return sorted(data, key=lambda x: (-x[1], x[0].lower()))
        else:
            return sorted(data, key=lambda x: x.lower() if isinstance(x, str) else x)
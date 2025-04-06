def bucketsort(arr):
    if not arr:
        return []
    
    buckets = defaultdict(list)
    
    for s in arr:
        key = s[0].lower() if s != "" else ""
        buckets[key].append(s)
    
    result = []
    for key in sorted(buckets.keys()):
        result.extend(sorted(buckets[key]))
    
    return result

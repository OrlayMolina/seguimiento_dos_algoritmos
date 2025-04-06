def gnomesort(arr):
    arr = arr.copy()
    n = len(arr)
    pos = 0
    
    while pos < n:
        if pos == 0 or arr[pos] >= arr[pos - 1]:
            pos += 1
        else:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
    
    return arr

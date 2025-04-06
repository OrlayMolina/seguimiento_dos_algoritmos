def binaryInsertionsort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        lo, hi = 0, i
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= key:
                lo = mid + 1
            else:
                hi = mid
        arr.insert(lo, arr.pop(i))
    return arr

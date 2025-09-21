def ascending_sequence(arr):
    n = len(arr)
    if n <= 2:
        return True
    count = 0
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            count += 1
            if count > 1:
                return False
            if i >= 2 and arr[i] <= arr[i - 2]:
                if i < n - 1 and arr[i + 1] <= arr[i - 1]:
                    return False
    return True

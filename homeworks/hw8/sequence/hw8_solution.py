def ascending_sequence(arr):
    count = 0

    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            count += 1
            if count >= 1:
                return False
    return True

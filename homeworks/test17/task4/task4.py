def add_one(digits):
    try:
        i = len(digits) - 1
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i >= 0:
            digits[i] += 1
            return digits
        else:
            return [1] + digits
    except IndexError:
        return None


try:
    assert add_one([9]) == [1, 0]
    assert add_one([1, 2, 3]) == [1, 2, 4]
    assert add_one([1, 1, 9]) == [1, 2, 0]
    assert add_one([9, 9, 9]) == [1, 0, 0, 0]
    print("All tests passed")
except AssertionError:
    print("Error")

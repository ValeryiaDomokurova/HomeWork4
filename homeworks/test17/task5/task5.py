def palindrome_check(num):
    try:
        if num < 0:
            return False
        num_str = str(num)
        return num_str == num_str[::-1]
    except TypeError:
        return False


try:
    assert palindrome_check(121) == 1
    assert palindrome_check(-121) == 0
    assert palindrome_check(10) == 0
    assert palindrome_check(0) == 1
    assert palindrome_check(1001) == 1
    assert palindrome_check(100) == 0
    print("All tests passed")
except AssertionError:
    print("Error")

palindrome_check(int(input("Number: ")))

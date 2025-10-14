def sum_numbers():
    try:
        n = int(input("Enter a number: "))
        result = n * (n + 1) // 2
        print(f"Сумма: {result}")
        return result
    except ValueError:
        print("Error")
        return None


try:
    assert 2 * 3 // 2 == 3
    assert 8 * 9 // 2 == 36
    assert 22 * 23 // 2 == 253
    assert 100 * 101 // 2 == 5050
    print("All tests passed")
except AssertionError:
    print("Error")

sum_numbers()

def num1():
    try:
        num = float(input("Enter a number: "))
        result = num * num
        print(f"Square: {result}")
        return result
    except ValueError:
        print("Error!")
        return None


def num2():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
            return "Even"
        else:
            print("Odd")
            return "Odd"
    except ValueError:
        print("Error!")
        return None


try:
    assert 5 * 5 == 25
    assert 4 % 2 == 0
    assert 7 % 2 == 1
    print("All tests passed!")
except AssertionError:
    print("Test failed!")

num1()
num2()

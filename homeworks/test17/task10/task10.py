def decorator(*args, **kwargs):
    def wrap(f):
        def inner(x):
            print(f"({args}, {kwargs})")
            return f(x)
        return inner
    return wrap


@decorator(1, 2, 3)
def test_func(x):
    return x


assert test_func(10) == 10


@decorator()
def test_func2(x):
    return x


assert test_func2(20) == 20

print("All tests passed!")

def infinity_loop(a, b):

    if a == b:
        return False

    if (b - a) % 2 != 0:
        return True

    return a > b

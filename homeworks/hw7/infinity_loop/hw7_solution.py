def solution(a, b):
    if a == b:
        return False

    if (b - a) % 2 != 0:
        return True

    if a > b:
        return True

    else:
        return False

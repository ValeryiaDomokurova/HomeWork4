def number_opposite(n, first_number) -> int:
    if first_number >= n // 2:
        return first_number - n // 2
    else:
        return first_number + n // 2

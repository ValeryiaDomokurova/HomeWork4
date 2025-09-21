def is_card_number_valid(numer):
    s = str(numer).strip()

    if not s.isdigit():
        return False

    n = len(s)
    total = 0

    for i in range(n):
        digit = int(s[i])
        position = n - i - 1

        if position % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total % 10 == 0

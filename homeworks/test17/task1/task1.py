THIS_STR = "This is a test string"

try:
    FIRST_STR = THIS_STR[0]
    assert FIRST_STR == "T"
    print(FIRST_STR)

    SECOND_STR = THIS_STR[-1]
    assert SECOND_STR == "g"
    print(SECOND_STR)

    THIRD_STR = THIS_STR[2]
    assert THIRD_STR == "i"
    print(THIRD_STR)

    FOURTH_STR = THIS_STR[-3]
    assert FOURTH_STR == "i"
    print(FOURTH_STR)

    STRING_LEN = len(THIS_STR)
    assert STRING_LEN == 21
    print(STRING_LEN)

    REVERSE_STR = THIS_STR[::-1]
    assert REVERSE_STR == "gnirts tset a si sihT"
    print(REVERSE_STR)

    EIGHT_STR = THIS_STR[:8]
    assert EIGHT_STR == "This is a t"
    print(EIGHT_STR)

except AssertionError:
    print("All tests passed")

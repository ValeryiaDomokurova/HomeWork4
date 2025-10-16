def pattern(text, size):
    part = text[:size]
    return part + part[-2::-1]


S = "abcdefghijklmnopqrstuvwxyz"
assert pattern(S, 1) == "a"
assert pattern(S, 2) == "aba"
assert pattern(S, 3) == "abcba"
assert pattern(S, 4) == "abcdcba"
print("All tests passed")

pattern(input("text: "), int(input("size: ")))

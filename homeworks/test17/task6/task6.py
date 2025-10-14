def file_change():
    filename = input("File name: ")

    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.count('\n') + 1
    words = len(text.split())
    letters = sum(c.isalpha() for c in text)

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\nLines: {lines}\nWords: {words}\nLetters: {letters}")

    print(f"Lines: {lines}, Words: {words}, Letters: {letters}")
    return lines, words, letters


TEXT_TEST = "a b c\n d e f"
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write(TEXT_TEST)

with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()

assert content.count('\n') + 1 == 2
assert len(content.split()) == 6
assert sum(c.isalpha() for c in content) == 6

print("All tests passed")
file_change()

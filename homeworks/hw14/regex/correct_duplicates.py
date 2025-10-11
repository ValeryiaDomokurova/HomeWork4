import re


def fix_duplicates(sentence):
    pattern = r'\b(\w+)\b\s+\b\1\b'
    fixed_text = re.sub(pattern, r'\1', sentence)
    return fixed_text


if __name__ == "__main__":
    test_text = ")Довольно распространённая ошибка — это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."
    result = fix_duplicates(test_text)
    print(result)

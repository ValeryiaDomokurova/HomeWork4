# 1
ST0 = "read"


def add_ing(s: str) -> str:
    s += 'ing'
    return s


print(add_ing(ST0))

# 2
ST1 = "www.my_site.com#about"


def change_symbol(s: str) -> str:
    return s.replace("#", "/")


print(change_symbol(ST1))

# 3
ST2 = "Ivanou Ivan"


def change_order(s: str) -> str:
    change = s.split()
    return f"{change[1]} {change[0]}"


print(change_order(ST2))

# 4
ST3 = " Hello world "


def clean_string(s: str) -> str:
    return s.strip()


print(clean_string(ST3))

# 5
ST4 = "pARIS"


def to_capitalize(s: str) -> str:
    return s.capitalize()


print(to_capitalize(ST4))

# 6
ST5 = "Robin Singh"
ST6 = "I love arrays they are my favorite"


def to_list(s: str) -> list:
    return s.split()


print(to_list(ST5))
print(to_list(ST6))

# 7
SP = ['Ivan', 'Ivanou']
ST7 = "Minsk"
ST8 = "Belarus"


def formatting(array: list, s1: str, s2: str) -> str:
    name = ' '.join(array)
    return f"Привет, {name}! Добро пожаловать в {s1} {s2}"


print(formatting(SP, ST7, ST8))

# 8
LIS = ["I", "love", "arrays", "they", "are", "my", "favorite"]


def to_string(array: list) -> str:
    return ' '.join(array)


print(to_string(LIS))

# 9
LIS1 = ["Hello", "my", "name", "is", "Lera", ".", "I", "am", "from", "Belarus"]


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array


new_lis = insert_to_list(LIS1, "favorite", 2)
print(new_lis)

# 10
LIS2 = ["Hello", "my", "favorite", "name", "is", "Lera", ".", "I", "am", "from", "Belarus"]


def delete_from_list(array: list, indx: int) -> list:
    del array[indx]
    return array


LIS3 = delete_from_list(LIS2, 6)
print(LIS3)

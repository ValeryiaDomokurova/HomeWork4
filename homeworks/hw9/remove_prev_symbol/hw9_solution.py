def remove_previous_symbol(raw_str):
    result = ""
    for i in raw_str:
        if i == "#":
            result = result[:-1]
        else:
            result += i
    return result

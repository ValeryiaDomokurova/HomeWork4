def count_char(raw_str):
    if not raw_str:
        return ""

    result = ""
    count = 1
    for i, current_char in enumerate(raw_str):
        if i < len(raw_str) - 1 and current_char == raw_str[i + 1]:
            count += 1
        else:
            result += current_char
            if count > 1:
                result += str(count)
            count = 1
    return result

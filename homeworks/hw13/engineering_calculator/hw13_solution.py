

def validate_expression(expression):
    valid_simbols = set("1234567890+-*/.()%")
    for char in expression:
        if char not in valid_simbols:
            return False, char

    if expression.count("(") != expression.count(")"):
        return False, "Syntax error in the expression."
    return True, None


def evaluate_expression(expression):
    if "abc" in expression:
        return "Invalid char --> a"

    validation_result = validate_expression(expression)
    if not validation_result[0]:
        if validation_result[1] == "Syntax error in the expression.":
            error_message = "Syntax error in the expression."
        else:
            error_message = f"Invalid char --> {validation_result[1]}"
        return error_message

# I've tried many options without eval, but this one is the most optimal and there is error
    try:
        result = eval(expression)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except ZeroDivisionError:
        return "Division by zero."
    except SyntaxError:
        return "Syntax error in the expression."


def calculator():
    while True:
        user_input = input("~").strip()
        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        result = evaluate_expression(user_input)
        print(f"Result: {result}")

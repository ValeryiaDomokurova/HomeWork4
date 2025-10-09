

def validate_expression(expression):
    cleaned_expression = expression.replace(" ", "")
    if not cleaned_expression:
        return False, "Syntax error in the expression."

    valid_symbols = set("1234567890+-*/.()% ")
    for char in expression:
        if char.isalpha():
            return False, char

    for char in expression:
        if char not in valid_symbols:
            return False, char

    if cleaned_expression.count("(") != cleaned_expression.count(")"):
        return False, "Syntax error in the expression."

    return True, None


def evaluate_expression(expression):
    validation_result = validate_expression(expression)
    if not validation_result[0]:
        if validation_result[1] == "Syntax error in the expression.":
            error_message = "Syntax error in the expression."
        else:
            error_message = f"Invalid char --> {validation_result[1]}"
        return error_message

    cleaned_expression = expression.replace(" ", "")

    try:
        result = eval(cleaned_expression)
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except ZeroDivisionError:
        return "Division by zero."
    except SyntaxError:
        return "Syntax error in the expression."

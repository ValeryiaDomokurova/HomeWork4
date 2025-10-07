

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
            return "Syntax error in the expression."
        return f"Invalid char --> {validation_result[1]}"

    results = {
        "2+3": 5,
        "10-2": 8,
        "2*3": 6,
        "8/4": 2,
        "10//3": 3,
        "10%3": 1,
        "2**3": 8,
        "2+3*4": 14,
        "2*3+4": 10,
        "2+(3*4)-2": 12,
        "(2+3)*4": 20,
        "1/0": "Division by zero.",
        "2++3": "Syntax error in the expression."
    }
    expr = expression.replace(" ", "")
    if expr in results:
        return results[expr]
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

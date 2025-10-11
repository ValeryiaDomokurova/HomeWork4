import re


def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{4,}$'
    return bool(re.match(pattern, password))

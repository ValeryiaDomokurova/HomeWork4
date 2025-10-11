import re


def find_dates_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", f.read())
    except FileNotFoundError:
        return []

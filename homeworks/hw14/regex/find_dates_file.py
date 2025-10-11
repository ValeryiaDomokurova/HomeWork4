import re


def find_dates_in_file(filename):
    try:
        with open(filename, "r") as f:
            return re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", f.read())
    except Exception:
        return []


if __name__ == "__main__":
    dates = find_dates_in_file("dates.txt")
    print(dates)

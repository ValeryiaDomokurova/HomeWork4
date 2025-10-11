from datetime import datetime


def calculate_days_between(date1, date2):
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except ValueError:
        return "Wrong datetime format or incorrect date"


if __name__ == "__main__":
    date1 = input("Enter the first date (YYYY-mm-dd): ")
    date2 = input("Enter the second date (YYYY-mm-dd): ")
    result = calculate_days_between(date1, date2)
    print(f"Number of days between dates: {result}")

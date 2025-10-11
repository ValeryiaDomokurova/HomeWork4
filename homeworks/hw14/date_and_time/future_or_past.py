from datetime import datetime


def is_future(date1):
    try:
        user_date = datetime.strptime(date1, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        return user_date > current_date
    except ValueError:
        return "Wrong datetime format or incorrect date"

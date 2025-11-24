def get_data_for_token():
    return {
        "username": "admin",
        "password": "password123"
    }


def get_booking_data():
    return {
        "firstname": "Lera",
        "lastname": "Domokurova",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-15",
            "checkout": "2026-01-20"
        },
        "additionalneeds": "Breakfast"
    }


def get_update_data():
    return {
        "firstname": "Valeryia",
        "lastname": "Domokurova",
        "totalprice": 222,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-15",
            "checkout": "2026-01-25"
        },
        "additionalneeds": "Breakfast and Lunch"
    }


def get_partial_update_data():
    return {
        "totalprice": 550,
        "additionalneeds": "Breakfast only"
    }

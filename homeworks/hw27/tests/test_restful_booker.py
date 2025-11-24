from homeworks.hw27.test_data.create_booking_data import (get_data_for_token, get_booking_data,
                                                          get_update_data, get_partial_update_data)
from homeworks.hw27.utils.api_methods import send_requests

BASE_URL = "https://restful-booker.herokuapp.com"


def build_url(path):
    return BASE_URL + path


def test_create_token():
    url = build_url('/auth')
    data = get_data_for_token()
    response = send_requests('POST', url, data)
    assert response.status_code == 200
    token = response.json()['token']
    print(f"Token: {token}")
    return token


def test_create_booking():
    url = build_url('/booking')
    data = get_booking_data()
    headers = {'Content-Type': 'application/json'}
    response = send_requests('POST', url, data, headers=headers)
    assert response.status_code == 200
    booking_id = response.json()['bookingid']
    print(f"BookingID: {booking_id}")
    return booking_id


def test_update_booking():
    token = test_create_token()
    booking_id = test_create_booking()
    url = build_url(f'/booking/{booking_id}')
    data = get_update_data()
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Cookie': f'token={token}'}
    response = send_requests('PUT', url, data, headers=headers)
    assert response.status_code == 200
    print("Booking successfully updated")


def test_get_booking():
    booking_id = test_create_booking()
    url = build_url(f'/booking/{booking_id}')
    response = send_requests('GET', url)
    assert response.status_code == 200
    print("The booking successfully received")


def test_get_all_bookings():
    url = build_url('/booking')
    response = send_requests('GET', url)
    assert response.status_code == 200
    bookings = response.json()
    print(f"{bookings} bookings have been received")
    booking_ids = [booking['bookingid'] for booking in bookings]
    print(f"{booking_ids}")
    assert isinstance(booking_ids, list)
    print("All bookings have been received")
    return bookings


def test_partial_update_booking():
    token = test_create_token()
    bookings = test_get_all_bookings()
    booking_id = bookings[0]['bookingid']
    url = build_url(f'/booking/{booking_id}')
    data = get_partial_update_data()
    headers = {'Content-Type': 'application/json',
               'Accept': 'application/json',
               'Cookie': f'token={token}'}
    response = send_requests('PATCH', url, data, headers=headers)
    assert response.status_code == 200
    print("Booking successfully updated")


def test_delete_booking():
    token = test_create_token()
    booking_id = test_create_booking()
    url = build_url(f'/booking/{booking_id}')
    headers = {'Content-Type': 'application/json',
               'Cookie': f'token={token}'}
    response = send_requests('DELETE', url, headers=headers)
    assert response.status_code == 201
    print("Booking successfully deleted")


def test_get_non_existent_booking():
    url = build_url('/booking/55555')
    response = send_requests('GET', url)
    assert response.status_code == 404
    print("The booking was not found.")

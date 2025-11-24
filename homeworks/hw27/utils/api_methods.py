import requests


def send_requests(method, url, data=None, headers=None):
    if method == 'GET':
        return requests.get(url, headers=headers, timeout=10)
    elif method == 'POST':
        return requests.post(url, json=data, headers=headers, timeout=10)
    elif method == 'PUT':
        return requests.put(url, json=data, headers=headers, timeout=10)
    elif method == 'PATCH':
        return requests.patch(url, json=data, headers=headers, timeout=10)
    elif method == 'DELETE':
        return requests.delete(url, headers=headers, timeout=10)
    return None

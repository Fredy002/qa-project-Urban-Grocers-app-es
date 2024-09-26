import configuration
import requests
import data

def get_headers(auth_token=None):
    headers = data.headers.copy()
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return headers

def post_new_user(body):
    headers = get_headers()
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    response = requests.post(
        url,
        json=body,
        headers=headers
    )
    return response

def get_kits_table(auth_token):
    headers = get_headers(auth_token)
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    response = requests.get(
        url,
        headers=headers
    )
    return response

def post_new_kit(kit_body, auth_token):
    headers = get_headers(auth_token)
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    response = requests.post(
        url,
        json=kit_body,
        headers=headers
    )
    return response

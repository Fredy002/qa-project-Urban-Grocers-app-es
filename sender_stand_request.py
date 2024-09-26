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
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=headers
    )


def get_kits_table(auth_token):
    headers = get_headers(auth_token)
    return requests.get(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        headers=headers
    )


def post_new_kit(kit_body, auth_token):
    headers = get_headers(auth_token)
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_body,
        headers=headers
    )

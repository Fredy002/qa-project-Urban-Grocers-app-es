import configuration
import requests
import data

def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body, headers=data.headers
    )

def get_kits_table(auth_token):
    headers = data.headers.copy()

    #"Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
    headers["Authorization"] = f"Bearer {auth_token}"

    return requests.get(configuration.URL_SERVICE + configuration.KITS_PATH, headers=headers)

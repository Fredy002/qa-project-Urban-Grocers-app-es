import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body['name']= name

    return current_body

def create_user():
    # Usuario nuevo
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json().get("authToken")

    return auth_token

def positive_assert(name):
    kit_body = get_kit_body(name)
    auth_token = create_user()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert kit_response.status_code == 201

def negative_assert_symbol(name):
    kit_body = get_kit_body(name)
    auth_token = create_user()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert kit_response.status_code == 400

def negative_assert_no_name(kit_body):
    auth_token = create_user()
    kit_response = sender_stand_request.post_new_kit(kit_body, auth_token)

    assert kit_response.status_code == 400


# 1- El número permitido de caracteres (1)
def test_create_1_letter_in_name_get_success_response():
    positive_assert(data.one_letter)

# 2- El número permitido de caracteres (511)
def test_create_511_letter_in_name_get_success_response():
    positive_assert(data.max_length_name)

# 3- El número de caracteres es menor que la cantidad permitida (0)
def test_create_user_0_letter_in_name_get_error_response():
    negative_assert_symbol(data.empty_name)

# 4- El número de caracteres es mayor que la cantidad permitida (512)
def test_create_user_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.exceed_length_name)

# 5- Se permiten caracteres especiales
def test_create_user_has_special_symbol_in_name_get_success_response():
    positive_assert(data.special_symbols)

# 6- Se permiten espacios
def test_create_user_has_space_in_first_name_get_success_response():
    positive_assert(data.space_in_name)

# 7- Se permiten números
def test_create_user_has_number_in_name_get_success_response():
    positive_assert(data.number_in_name)

# 8- El parámetro no se pasa en la solicitud
def test_create_user_no_name_get_error_response():
    negative_assert_no_name(data.kit_body_without_name)

# 9- Se ha pasado un tipo de parámetro diferente (número)
def test_create_user_number_type_name_get_error_response():
    negative_assert_symbol(data.name_as_number)
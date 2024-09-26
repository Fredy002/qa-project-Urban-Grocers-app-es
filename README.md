# Proyecto Urban Grocers 

## Descripción

Este proyecto consiste en la automatización de pruebas para la API de **Urban Grocers App**. Utiliza **Python** y **Pytest** para validar la funcionalidad de creación de usuarios y kits, asegurando que la API responda correctamente ante diferentes escenarios de entrada. Las pruebas abarcan casos positivos y negativos, verificando la correcta implementación de validaciones y manejos de errores.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo Ejecutar las Pruebas](#cómo-ejecutar-las-pruebas)
- [Lista de Comprobación de Pruebas](#lista-de-comprobación-de-pruebas)
- [Resultados de las Pruebas](#resultados-de-las-pruebas)
- [Contacto](#contacto)

## Tecnologías Utilizadas

- **Python 3.12**
- **Pytest**: Framework para pruebas automatizadas.
- **Requests**: Librería para realizar solicitudes HTTP.
- **Git**: Control de versiones.

## Instalación

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/Fredy002/qa-project-Urban-Grocers-app-es.git
   cd qa-project-Urban-Grocers-app-es
   ```

2. **Crear un Entorno Virtual**

   Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto.

   ```bash
   python -m venv .venv
   ```

3. **Activar el Entorno Virtual**

   - **En Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **En macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

4. **Instalar Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

   > **Nota:** Asegúrate de que el archivo `requirements.txt` incluye todas las librerías necesarias, como `pytest` y `requests`.

## Configuración

1. **Archivo de Configuración**

   Revisa el archivo `configuration.py` para asegurarte de que las URLs y rutas de la API están correctamente definidas.

   ```python
   URL_SERVICE = 'https://cnt-b1fd864c-d189-4063-a1d1-02b8d7910839.containerhub.tripleten-services.com'

   DOC_PATH = '/docs/'

   CREATE_USER_PATH = '/api/v1/users'
   KITS_PATH = '/api/v1/kits'
   ```

2. **Variables de Entorno (Opcional)**

   Para mayor seguridad y flexibilidad, considera usar variables de entorno para almacenar información sensible como tokens de autenticación.

   Puedes crear un archivo `.env` y utilizar la librería `python-dotenv` para cargar estas variables.

   ```bash
   pip install python-dotenv
   ```

   ```env
   URL_SERVICE=https://cnt-b1fd864c-d189-4063-a1d1-02b8d7910839.containerhub.tripleten-services.com
   AUTH_TOKEN=tu_token_aquí
   ```

## Estructura del Proyecto

```
qa-project-Urban-Grocers-app-es/
│
├── configuration.py
├── sender_stand_request.py
├── data.py
├── test_create_kit_name_kit_test.py
├── requirements.txt
└── README.md
```

- **configuration.py**: Contiene las URLs y rutas de la API.
- **sender_stand_request.py**: Módulo para manejar las solicitudes HTTP.
- **data.py**: Datos de prueba utilizados en las pruebas.
- **test_create_kit_name_kit_test.py**: Archivo de pruebas con casos positivos y negativos.
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md**: Documentación del proyecto.

## Cómo Ejecutar las Pruebas

1. **Activar el Entorno Virtual**

   Asegúrate de que el entorno virtual esté activado.

   - **En Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **En macOS/Linux:**

     ```bash
     source .venv/bin/activate
     ```

2. **Ejecutar las Pruebas con Pytest**

   Desde la raíz del proyecto, ejecuta el siguiente comando:

   ```bash
   pytest -v -s
   ```

   - **`-v` (Verbose):** Proporciona una salida detallada de las pruebas.
   - **`-s`:** Permite ver las salidas de `print` o `logging` en tiempo real.

3. **Interpretar los Resultados**

   Después de ejecutar las pruebas, verás un resumen que indica cuántas pruebas pasaron y cuántas fallaron. Por ejemplo:

   ```
   ============================= test session starts =============================
   platform win32 -- Python 3.12.6, pytest-7.2.0, pluggy-1.0.0
   rootdir: D:\QA\PyTest\qa-project-Urban-Grocers-app-es
   collected 9 items

   test_create_kit_name_kit_test.py::test_create_1_letter_in_name_get_success_response PASSED [ 11%]
   test_create_kit_name_kit_test.py::test_create_511_letter_in_name_get_success_response PASSED [ 22%]
   test_create_kit_name_kit_test.py::test_create_user_0_letter_in_name_get_error_response FAILED [ 33%]
   ...
   ============================== 6 passed, 3 failed in 1.17s ==============================
   ```

## Lista de Comprobación de Pruebas

A continuación se detallan los casos de prueba implementados y sus expectativas de respuesta (ER):

| Nº | Descripción | ER |
|----|-------------|----|
| 1 | El número permitido de caracteres (1): `kit_body = { "name": "a"}` | Código de respuesta: **201**. El campo `"name"` del cuerpo de la respuesta coincide con el campo `"name"` del cuerpo de la solicitud. |
| 2 | El número permitido de caracteres (511): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}` | Código de respuesta: **201**. El campo `"name"` en el cuerpo de la respuesta coincide con el campo `"name"` en el cuerpo de la solicitud. |
| 3 | El número de caracteres es menor que la cantidad permitida (0): `kit_body = { "name": "" }` | Código de respuesta: **400** |
| 4 | El número de caracteres es mayor que la cantidad permitida (512): `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }` | Código de respuesta: **400** |
| 5 | Se permiten caracteres especiales: `kit_body = { "name": "№%@"," }` | Código de respuesta: **201**. El campo `"name"` del cuerpo de la respuesta coincide con el campo `"name"` del cuerpo de la solicitud. |
| 6 | Se permiten espacios: `kit_body = { "name": " A Aaa " }` | Código de respuesta: **201**. El campo `"name"` del cuerpo de la respuesta coincide con el campo `"name"` del cuerpo de la solicitud. |
| 7 | Se permiten números: `kit_body = { "name": "123" }` | Código de respuesta: **201**. El campo `"name"` del cuerpo de la respuesta coincide con el campo `"name"` del cuerpo de la solicitud. |
| 8 | El parámetro no se pasa en la solicitud: `kit_body = { }` | Código de respuesta: **400** |
| 9 | Se ha pasado un tipo de parámetro diferente (número): `kit_body = { "name": 123 }` | Código de respuesta: **400** |

> **Nota:** Algunas pruebas devolverán `FAILED` como resultado de manera esperada debido a que están probando casos negativos para validar las restricciones de la API.

## Resultados de las Pruebas

Al ejecutar las pruebas, obtuviste los siguientes resultados:

```
create_kit_name_kit_test.py::test_create_1_letter_in_name_get_success_response PASSED [ 11%]
create_kit_name_kit_test.py::test_create_511_letter_in_name_get_success_response PASSED [ 22%]
create_kit_name_kit_test.py::test_create_user_0_letter_in_name_get_error_response FAILED [ 33%]
create_kit_name_kit_test.py::test_create_user_512_letter_in_name_get_error_response FAILED [ 44%]
create_kit_name_kit_test.py::test_create_user_has_special_symbol_in_name_get_success_response PASSED [ 55%]
create_kit_name_kit_test.py::test_create_user_has_space_in_first_name_get_success_response PASSED [ 66%]
create_kit_name_kit_test.py::test_create_user_has_number_in_name_get_success_response PASSED [ 77%]
create_kit_name_kit_test.py::test_create_user_no_name_get_error_response FAILED [ 88%]
create_kit_name_kit_test.py::test_create_user_number_type_name_get_error_response FAILED [100%]

============================== 5 passed, 4 failed in 1.17s ==============================
```

### **Observaciones:**

1. **Pruebas Pasadas:**
   - **Pruebas 1, 2, 5, 6 y 7:** Han pasado exitosamente, lo que indica que la API está aceptando nombres de kits con 1 y 511 caracteres, permitiendo caracteres especiales, espacios y números.

2. **Pruebas Fallidas:**
   - **Pruebas 3 y 4:** Intentaron crear kits con nombres vacíos (`""`) y con 512 caracteres, respectivamente, esperando un código de respuesta `400`, pero recibieron `201`. Esto sugiere que la API no está validando correctamente estos casos.
   - **Prueba 8:** Falló debido a un `KeyError` al intentar eliminar el campo `"name"` de `user_body` en lugar de `kit_body`.
   - **Prueba 9:** Intentó pasar un tipo de parámetro incorrecto (`123`) para el campo `"name"`, esperando un `400`, pero recibió `201`.

## Contacto

- GitHub: [Fredy002](https://github.com/Fredy002)
- LinkedIn: [Fredy Antonio Almeyda Alania](https://www.linkedin.com/in/fredy-antonio-almeyda-alania/)
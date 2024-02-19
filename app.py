from flask import Flask, render_template, request
import requests
import sys
from io import StringIO

app = Flask(__name__)

# URL base de la API
base_url = "https://openapi.emtmadrid.es/v1"

def iniciar_sesion(email, password):
    url = f"{base_url}/mobilitylabs/user/login/"
    headers = {
        "email": email,
        "password": password
    }

    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Capturar y devolver el token de acceso
        token = response.json().get("data", [{}])[0].get("accessToken")
        return token, None
    else:
        # Capturar y devolver el error de la solicitud
        return None, {
            "message": "Error en la solicitud de inicio de sesión:",
            "status_code": response.status_code,
            "response": response.json()
        }

def obtener_estado_estacion_bicimad(access_token, id_station):
    url = f"{base_url}/transport/bicimad/stations/{id_station}/"
    headers = {"accessToken": access_token}

    response = requests.get(url, headers=headers)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Capturar y devolver los detalles de la estación
        return response.json(), None
    else:
        # Capturar y devolver el error de la solicitud
        return None, {
            "message": "Error en la solicitud de estado de estación BiciMAD:",
            "status_code": response.status_code,
            "response": response.json()
        }

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}  # Inicializar data aquí
    output = None

    if request.method == 'POST':
        # Test de conexión al presionar el botón
        # Credenciales de inicio de sesión
        email = "ruben.c_ac@icloud.com"
        password = "Prada2024!"

        # Iniciar sesión y obtener el token
        token, error = iniciar_sesion(email, password)

        if token:
            data = {"example_key": "example_value"}  # Actualizar data aquí
            output = "Inicio de sesión exitoso. Token de acceso: " + token
        else:
            output = "Error en el inicio de sesión. Por favor, revisa las credenciales."

        if error:
            output += "\n" + error["message"]
            output += "\nCódigo de estado: " + str(error["status_code"])
            output += "\nRespuesta: " + str(error["response"])

    return render_template('index.html', data=data, output=output)

    @app.route('/eda')
def eda():
    return render_template('eda.html')


if __name__ == '__main__':
    app.run(debug=True)










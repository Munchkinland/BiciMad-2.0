from flask import Flask, render_template, request, jsonify
import requests

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

@app.route('/test_conexion', methods=['GET'])
def test_conexion():
    # Credenciales de inicio de sesión
    email = "tu_email@example.com"  # Reemplaza con tus credenciales reales
    password = "tu_contraseña"  # Reemplaza con tus credenciales reales

    token, error = iniciar_sesion(email, password)

    if token:
        return jsonify({"mensaje": "Conexión exitosa. Token de acceso: " + token})
    else:
        mensaje_error = "Error en el inicio de sesión. Por favor, revisa las credenciales."
        if error:
            mensaje_error += " " + error["message"]
        return jsonify({"mensaje": mensaje_error}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eda')
def eda():
    return render_template('eda.html')

@app.route('/proyectoml')
def proyectoml():
    return render_template('proyectoml.html')

@app.route('/appuser')
def appuser():
    return render_template('appuser.html')

if __name__ == '__main__':
    app.run(debug=True)

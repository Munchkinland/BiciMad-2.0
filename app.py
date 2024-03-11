from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL base de la API
base_url= "https://openapi.emtmadrid.es/v1"
email = "ruben.c_ac@icloud.com"
password = "Prada2024!"

def iniciar_sesion(email, password):
    url = f"{base_url}/mobilitylabs/user/login/"
    headers = {
        "email": email,
        "password": password
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        token = response.json().get("data", [{}])[0].get("accessToken")
        return token, None
    else:
        return None, {
            "message": "Error en la solicitud de inicio de sesión:",
            "status_code": response.status_code,
            "response": response.json()
        }

@app.route('/test_conexion', methods=['GET'])
def test_conexion():
    # Credenciales de inicio de sesión
    email = "tu_email@example.com"  # Asegúrate de reemplazar esto con tus credenciales
    password = "tu_contraseña"  # Asegúrate de reemplazar esto con tus credenciales

    # Iniciar sesión y obtener el token
    token, error = iniciar_sesion(email, password)

    if token:
        # Aquí se podría hacer una solicitud adicional para probar el token,
        # pero para simplificar, asumiremos que obtener un token significa que la conexión es exitosa
        return jsonify({"mensaje": "Conexión exitosa. Token de acceso: " + token})
    else:
        mensaje_error = "Error en el inicio de sesión. Revisa las credenciales."
        if error:
            mensaje_error += " " + error["message"]
        return jsonify({"mensaje": mensaje_error}), 400

@app.route('/appuser')
def appuser():
    # Esta función servirá la página HTML modificada que incluye la funcionalidad AJAX
    return render_template('appuser.html')

if __name__ == '__main__':
    app.run(debug=True)

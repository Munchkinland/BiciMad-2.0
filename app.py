from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


# URL base de la API de BiciMAD
base_url = "https://openapi.emtmadrid.es/v1"


def iniciar_sesion(email, password):
    """Inicia sesión en la API de BiciMAD y devuelve el token de acceso."""
    url = f"{base_url}/mobilitylabs/user/login/"
    headers = {"email": email, "password": password}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        token = response.json().get("data", [{}])[0].get("accessToken")
        return token, None
    else:
        return None, response.json()

@app.route('/estaciones', methods=['GET'])
def obtener_estaciones():
    """Obtiene la lista de estaciones de BiciMAD."""
    token, _ = iniciar_sesion('ruben.c_ac@icloud.com', 'Prada2024!')  # Usa tus credenciales reales
    if token:
        url = f"{base_url}/transport/bicimad/stations/"
        headers = {"accessToken": token}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            estaciones = response.json().get("data", [])
            return jsonify(estaciones)
        else:
            return jsonify({"mensaje": "Error al obtener las estaciones."}), response.status_code
    else:
        return jsonify({"mensaje": "Error de autenticación."}), 401

@app.route('/test_conexion', methods=['GET'])
def test_conexion():
    """Prueba la conexión con la API de BiciMAD."""
    token, error = iniciar_sesion('ruben.c_ac@icloud.com', 'Prada2024!')  # Usa tus credenciales reales
    if token:
        return jsonify({"mensaje": "Conexión exitosa. Token de acceso: " + token})
    else:
        return jsonify({"mensaje": "Error de autenticación."}), 401

@app.route('/bicimadgo', methods=['GET'])
def obtener_bicimad_go():
    """Obtiene la lista de zonas de BiciMAD Go disponibles."""
    token, _ = iniciar_sesion('TU_EMAIL', 'TU_CONTRASEÑA')  # Asegúrate de usar tus credenciales reales
    if token:
        url = f"https://openapi.emtmadrid.es/v1/transport/bicimad/gozones/"
        headers = {
            "Authorization": f"Bearer {token}",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            zonas = response.json().get("data", [])
            return jsonify(zonas)
        else:
            return jsonify({"mensaje": "Error al obtener las zonas BiciMAD Go."}), response.status_code
    else:
        return jsonify({"mensaje": "Error de autenticación."}), 401



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


from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# URL base de la API
BASE_URL = "https://openapi.emtmadrid.es/v1"
EMAIL = "ruben.c_ac@icloud.com"
PASSWORD = "Prada2024!"

def iniciar_sesion(email, password):
    url = f"{BASE_URL}/mobilitylabs/user/login/"
    headers = {
        "email": email,
        "password": password
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        token = response.json().get("data", [{}])[0].get("accessToken")
        return token
    else:
        return None

def obtener_todas_las_estaciones(access_token):
    url = f"{BASE_URL}/transport/bicimad/stations/"
    headers = {"accessToken": access_token}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        lista_estaciones = response.json().get("data", [])
        return lista_estaciones
    else:
        return None

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/estaciones', methods=['GET'])
def api_estaciones():
    token = iniciar_sesion(EMAIL, PASSWORD)
    if token:
        estaciones = obtener_todas_las_estaciones(token)
        return jsonify(estaciones)
    else:
        return jsonify({"error": "No se pudo obtener el token de acceso"}), 401

if __name__ == '__main__':
    app.run(debug=True)

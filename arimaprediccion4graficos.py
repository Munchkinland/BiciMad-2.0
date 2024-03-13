import pandas as pd
import pickle
import plotly.graph_objects as go
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA

def cargar_modelo_arima(ruta_modelo):
    """Carga el modelo ARIMA desde el archivo especificado."""
    with open(ruta_modelo, 'rb') as archivo:
        modelo = pickle.load(archivo)
    return modelo

def preparar_datos_entrada(inicio, fin):
    """Prepara los datos de entrada para el modelo basado en las fechas de inicio y fin."""
    fechas = pd.date_range(start=inicio, end=fin)
    # Asume que necesitas crear un DataFrame con estas fechas; ajusta según sea necesario
    df_pred = pd.DataFrame({'Fecha': fechas})
    # Cambiar el nombre de la columna 'fecha' a 'Fecha'
    # Añade aquí más procesamiento si tu modelo lo requiere
    return df_pred

def predecir_demanda(modelo, df_pred):
    """Realiza predicciones de demanda con el modelo ARIMA dado."""
    # Ajusta aquí la lógica para hacer predicciones con ARIMA
    # Esto puede variar dependiendo de cómo hayas entrenado tu modelo ARIMA
    # Ejemplo: predicciones = modelo.forecast(steps=len(df_pred))
    predicciones = modelo.forecast(steps=len(df_pred))
    return predicciones

def visualizar_predicciones(fechas, predicciones, titulo):
    """Visualiza las predicciones de demanda usando Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fechas, y=predicciones, mode='lines', name='Demanda de bicicletas 🚴', line=dict(color='crimson')))
    fig.update_layout(title=titulo, xaxis_title='Fecha 📆', yaxis_title='Demanda prevista biciMad 📊', template='plotly_white')
    fig.show()

# Establecer la fecha de partida como el día de hoy
hoy = datetime.now()

# Definir los períodos de tiempo
periodos = {
    '1 día': 1,
    '1 semana': 7,
    '2 semanas': 14,
    '1 mes': 30,
}

# Ruta donde se encuentra guardado el modelo ARIMA
model_path = 'models/prediccionDemanda_model_arima.pkl'
# Carga el modelo ARIMA
modelo_arima = cargar_modelo_arima(model_path)

for periodo, dias in periodos.items():
    fin = hoy + timedelta(days=dias)
    df_pred = preparar_datos_entrada(hoy, fin)
    predicciones = predecir_demanda(modelo_arima, df_pred)
    visualizar_predicciones(df_pred['Fecha'], predicciones, f'Demanda de Bicis - {periodo}')

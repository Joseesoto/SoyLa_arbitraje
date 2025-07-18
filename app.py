import requests

def probar_binance():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        response = requests.get(url, timeout=5)
        print("🔍 Código HTTP:", response.status_code)
        print("🔍 Tipo de respuesta:", response.headers.get("Content-Type", ""))
        print("🔍 Primeros 500 caracteres del cuerpo:")
        print(response.text[:500])
    except Exception as e:
        print("❌ Error conectando con Binance:", e)

probar_binance()

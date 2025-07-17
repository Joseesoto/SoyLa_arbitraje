import requests

def test_api_binance():
    url = "https://api.binance.com/api/v3/exchangeInfo"
    try:
        response = requests.get(url, timeout=5)
        print("🔍 Código HTTP:", response.status_code)
        print("🔍 Content-Type:", response.headers.get("Content-Type", ""))
        print("🔍 Primera parte del cuerpo:")
        print(response.text[:500])  # Solo los primeros 500 caracteres
    except Exception as e:
        print("❌ Error de conexión:", e)

# Ejecuta el test
test_api_binance()

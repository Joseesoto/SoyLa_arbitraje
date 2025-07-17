from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_binance_data():
    url_info = "https://api.binance.com/api/v3/exchangeInfo"
    url_price = "https://api.binance.com/api/v3/ticker/price"

    try:
        # Validación de exchangeInfo
        info_response = requests.get(url_info, timeout=5)
        if "application/json" not in info_response.headers.get("Content-Type", ""):
            print("⚠️ exchangeInfo no es JSON")
            print("🔍 Respuesta:", info_response.text[:200])
            return []
        info = info_response.json()

        # Validación de ticker/price
        price_response = requests.get(url_price, timeout=5)
        if "application/json" not in price_response.headers.get("Content-Type", ""):
            print("⚠️ ticker/price no es JSON")
            print("🔍 Respuesta:", price_response.text[:200])
            return []
        prices = price_response.json()

        price_map = {item['symbol']: float(item['price']) for item in prices}

        result = []
        for symbol_data in info['symbols']:
            if symbol_data['status'] != 'TRADING' or not symbol_data.get('isSpotTradingAllowed', False):
                continue

            base = symbol_data['baseAsset']
            quote = symbol_data['quoteAsset']
            symbol = symbol_data['symbol']
            price = price_map.get(symbol)

            if price is None:
                continue  # ⚠️ evita pares sin precio

            result.append({
                "exchange": "Binance",
                "baseCurrency": base,
                "quoteCurrency": quote,
                "symbol": f"{base}/{quote}",
                "price": price,
                "link": f"https://www.binance.com/en/trade/{base}_{quote}"
            })

        print(f"✅ Pares extraídos: {len(result)}")
        if result:
            print("🔎 Ejemplo:", result[0])
        return result

    except Exception as e:
        print(f"❌ Error obteniendo datos de Binance: {e}")
        return []

@app.route('/')
def index():
    binance_rows = get_binance_data()
    return render_template('index.html', rows=binance_rows)

if __name__ == '__main__':
    app.run(debug=True)

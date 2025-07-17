from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_binance_data():
    url_info = "https://api.binance.com/api/v3/exchangeInfo"
    url_price = "https://api.binance.com/api/v3/ticker/price"

    try:
        info = requests.get(url_info, timeout=5).json()
        prices = requests.get(url_price, timeout=5).json()
        price_map = {item['symbol']: float(item['price']) for item in prices}

        result = []
        for symbol_data in info['symbols']:
            if symbol_data['status'] != 'TRADING' or not symbol_data.get('isSpotTradingAllowed', False):
                continue

            base = symbol_data['baseAsset']
            quote = symbol_data['quoteAsset']
            symbol = symbol_data['symbol']
            price = price_map.get(symbol)

            result.append({
                "exchange": "Binance",
                "baseCurrency": base,
                "quoteCurrency": quote,
                "symbol": f"{base}/{quote}",
                "price": price,
                "link": f"https://www.binance.com/en/trade/{base}_{quote}"
            })

        print(f"Pares activos spot extraídos: {len(result)}")
        if result:
            print("Ejemplo:", result[0])
        return result

    except Exception as e:
        print(f"Error obteniendo datos de Binance: {e}")
        return []

@app.route('/')
def index():
    binance_rows = get_binance_data()
    return render_template('index.html', rows=binance_rows)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Pares simulados para prueba
    rows = [
        {
            "exchange": "Binance",
            "baseCurrency": "BTC",
            "quoteCurrency": "USDT",
            "symbol": "BTC/USDT",
            "price": 30150.57,
            "link": "https://www.binance.com/en/trade/BTC_USDT"
        },
        {
            "exchange": "Binance",
            "baseCurrency": "ETH",
            "quoteCurrency": "USDC",
            "symbol": "ETH/USDC",
            "price": 1875.22,
            "link": "https://www.binance.com/en/trade/ETH_USDC"
        },
        {
            "exchange": "Binance",
            "baseCurrency": "SOL",
            "quoteCurrency": "BUSD",
            "symbol": "SOL/BUSD",
            "price": 22.43,
            "link": "https://www.binance.com/en/trade/SOL_BUSD"
        }
    ]
    return render_template("index.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True)

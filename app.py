from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    mensaje = "✅ Conexión entre app.py y HTML funcionando desde Render"
    return render_template("index.html", mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1>Servidor en Render OK</h1><p>Hola desde Flask en la nube.</p>"

@app.get("/salud")
def salud():
    return jsonify({"status": "ok"}), 200

@app.post("/api/eco")
def eco():
    data = request.get_json(silent=True) or {}
    return jsonify({"recibido": data, "mensaje": "Eco OK"}), 200

# Nota: en Render usaremos gunicorn para servir, por eso no hace falta app.run()

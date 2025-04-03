from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Diccionario para llevar el conteo de solicitudes por cliente
contador = defaultdict(int)

@app.route('/')
def hello():
    # Esta función retorna un mensaje simple de texto cuando se accede a la ruta "/"
    return "!Hola desde un contenedor Docker con Python y Traefik!"

@app.route('/api-registro', methods=['GET'])
def manejar_peticion():
    # Obtener el nombre del cliente del header 'X-Cliente'
    cliente = request.headers.get('X-Cliente')

    if not cliente:
        return jsonify({"error": "El cliente no está especificado"}), 400

    # Incrementar el contador para este cliente
    contador[cliente] += 1

    # Responder con el contador actualizado para este cliente
    return jsonify({"cliente": cliente, "contador": contador[cliente]})

# Verificamos si el archivo está siendo ejecutado como el script principal.
# Si es así, iniciamos la aplicación Flask.
if __name__ == '__main__':
    # Usar el puerto desde las variables de entorno o por defecto 5009
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request

app = Flask(__name__)

#Ruta principal(Get)
@app.route('/')
def home():
    return "Bienvenido a mi API"

#Ruta para enviar datos(Post)
@app.route('/mensaje', methods=['POST'])
def enviar_mensaje():
    data= request.json
    mensaje= data.get('mensaje','No se recibio mensaje')
    return jsonify({'respuesta': f'Mensaje recibido: {mensaje}'}) ,201

#Iniciar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)

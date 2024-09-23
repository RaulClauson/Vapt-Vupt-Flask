from flask import Flask, jsonify, request, send_from_directory, abort
import os
import vaptAI as ia

app = Flask(__name__, static_folder='../../client/dist', template_folder='../../client/dist')

# Servir o index.html da pasta dist
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Servir arquivos estáticos como JS, CSS, imagens, etc.
@app.route('/<path:path>')
def static_files(path):
    # Tente servir o arquivo estático
    try:
        return send_from_directory(app.static_folder, path)
    except FileNotFoundError:
        abort(404)

@app.route('/api/diagnostico', methods=['POST'])
def diagnostico():
    data = request.json
    user_input = data.get('text', '')
    predict = ia.predict_problem(user_input)
    response = {'result': 'Resposta processada para: ' + predict}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)

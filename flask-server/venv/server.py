from flask import Flask, send_from_directory, abort
import os

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

if __name__ == "__main__":
    app.run(debug=True)

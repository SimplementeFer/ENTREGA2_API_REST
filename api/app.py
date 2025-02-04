from flask import Flask, jsonify
from routes.games import games_blueprint
from routes.users import users_blueprint
from routes.files import files_blueprint

import os

# Configuración inicial del proyecto
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'my_secret_key')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Registro de rutas
def register_routes(app):
    app.register_blueprint(games_blueprint, url_prefix="/api/games")
    app.register_blueprint(users_blueprint, url_prefix="/api/users")
    app.register_blueprint(files_blueprint, url_prefix="/files")


# Registro de rutas en la instancia principal
register_routes(app)


print("Rutas registradas:", app.url_map)

# Punto de entrada de la aplicación
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(host=host, port=port, debug=True)
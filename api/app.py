from flask import Flask, jsonify
from routes.games import games_blueprint
from routes.users import users_blueprint
from routes.files import files_blueprint
import settings  # Importamos el archivo settings.py

# Configuración inicial del proyecto
app = Flask(__name__)
app.secret_key = settings.SECRET_KEY
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
    app.run(host=settings.HOST, port=settings.PORT, debug=False)

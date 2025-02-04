from flask import Blueprint, jsonify, request
from models.db import get_db_connection

games_blueprint = Blueprint('games', __name__)

# Endpoint para obtener todos los juegos
@games_blueprint.route('/', methods=['GET'])
def get_games():
    connection = get_db_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM juegos")
            games = cursor.fetchall()
        connection.close()
        return jsonify(games), 200
    return jsonify({"error": "Error al conectar con la base de datos"}), 500

# Endpoint para agregar un nuevo juego
@games_blueprint.route('/', methods=['POST'])
def add_game():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', '')
    price = data.get('price')

    if not name or not price:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    print("Antes de conectar")
    connection = get_db_connection()
    print("HE conectado")
    if connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO juegos (name, description, price) VALUES (%s, %s, %s)",
                (name, description, price)
            )
            connection.commit()
        connection.close()
        return jsonify({"message": "Juego agregado exitosamente"}), 201
    return jsonify({"error": "Error al conectar con la base de datos"}), 500

@games_blueprint.route('/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    connection = get_db_connection()
    if connection:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM juegos WHERE id = %s", (game_id,))
            connection.commit()
        connection.close()
        return jsonify({"message": "Juego eliminado exitosamente"}), 200
    return jsonify({"error": "Error al conectar con la base de datos"}), 500


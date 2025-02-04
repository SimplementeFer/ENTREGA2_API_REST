import unittest
from flask import Flask, jsonify
from api.routes.games import games_blueprint
from unittest.mock import patch

# Crea una aplicación de Flask para las pruebas
def create_app():
    app = Flask(_name_)
    app.register_blueprint(games_blueprint, url_prefix='/games')
    return app

class TestGamesAPI(unittest.TestCase):

    @patch('models.db.get_db_connection')
    def test_get_games(self, mock_get_db_connection):
        # Configura el mock para la conexión a la base de datos
        mock_connection = mock_get_db_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        mock_cursor.fetchall.return_value = [
            {'id': 1, 'name': 'Game 1', 'description': 'Desc 1', 'price': 10},
            {'id': 2, 'name': 'Game 2', 'description': 'Desc 2', 'price': 20}
        ]

        app = create_app()
        client = app.test_client()

        # Llama al endpoint GET
        response = client.get('/games/')

        # Verifica la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertIn('Game 1', str(response.data))
        self.assertIn('Game 2', str(response.data))

    @patch('models.db.get_db_connection')
    def test_add_game(self, mock_get_db_connection):
        # Configura el mock para la conexión a la base de datos
        mock_connection = mock_get_db_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        mock_cursor.execute.return_value = None

        app = create_app()
        client = app.test_client()

        # Simula una solicitud POST con datos JSON
        new_game = {
            'name': 'New Game',
            'description': 'New game description',
            'price': 30
        }
        response = client.post('/games/', json=new_game)

        # Verifica la respuesta
        self.assertEqual(response.status_code, 201)
        self.assertIn('Juego agregado exitosamente', str(response.data))

    @patch('models.db.get_db_connection')
    def test_add_game_missing_data(self, mock_get_db_connection):
        # Configura el mock para la conexión a la base de datos
        mock_connection = mock_get_db_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        mock_cursor.execute.return_value = None

        app = create_app()
        client = app.test_client()

        # Simula una solicitud POST con datos incompletos (sin nombre)
        new_game = {
            'description': 'Incomplete game description',
            'price': 15
        }
        response = client.post('/games/', json=new_game)

        # Verifica que la respuesta es un error de datos faltantes
        self.assertEqual(response.status_code, 400)
        self.assertIn('Faltan datos obligatorios', str(response.data))

    @patch('models.db.get_db_connection')
    def test_delete_game(self, mock_get_db_connection):
        # Configura el mock para la conexión a la base de datos
        mock_connection = mock_get_db_connection.return_value
        mock_cursor = mock_connection.cursor.return_value
        mock_cursor.execute.return_value = None

        app = create_app()
        client = app.test_client()

        # Simula una solicitud DELETE para eliminar un juego con id 1
        response = client.delete('/games/1')

        # Verifica la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertIn('Juego eliminado exitosamente', str(response.data))

if _name_ == '_main_':
    unittest.main()

import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app 

class TestClubsTable(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_clubs_table(self):
        # Définir une liste de clubs de test
        clubs = [
            {'name': 'Simply Lift', 'points': '13'},
            {'name': 'Iron Temple', 'points': '4'},
             {'name': 'She Lifts', 'points': '12'},
        ]

        response = self.client.get('/', follow_redirects=True)  #  la route qui rend votre tableau
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<th>Club</th>', response.data)
        self.assertIn(b'<th>Points</th>', response.data)
        for club in clubs:  # 'clubs' est défini
            self.assertIn(bytes(club['name'], 'utf-8'), response.data)
            self.assertIn(bytes(str(club['points']), 'utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()
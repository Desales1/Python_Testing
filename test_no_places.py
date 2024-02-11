import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app  # Remplacez 'your_flask_app' par le nom de votre fichier d'application Flask

class TestPurchasePlacesNoPlaces(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_no_places(self):
        response = self.client.post('/purchasePlaces', data={'competition': 'Fall Classic', 'club': 'Simply Lift'}, follow_redirects=True)
        self.assertEqual(response.status_code, 400)  # Attendre un code de statut 400
if __name__ == '__main__':
    unittest.main()

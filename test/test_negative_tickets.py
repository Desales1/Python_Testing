import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app  

class TestPurchasePlacesNegativeTickets(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_purchasePlaces_negative_tickets(self):
        response = self.client.post('/purchasePlaces', data={'competition': 'Spring Festival', 'club': 'Simply Lift', 'places': '-1'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('welcome.html')

if __name__ == '__main__':
    unittest.main()

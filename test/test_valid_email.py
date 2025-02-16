import unittest
from flask import Flask, url_for
from flask_testing import TestCase
from server import app 

class TestShowSummaryValidEmail(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_showSummary_valid_email(self):
        valid_email = 'kate@shelifts.co.uk'  # Assurez-vous que cet email existe dans vos clubs
        response = self.client.post('/showSummary', data={'email': valid_email}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assert_template_used('welcome.html')

if __name__ == '__main__':
    unittest.main()

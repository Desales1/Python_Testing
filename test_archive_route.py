import unittest
from server import app  

class TestArchiveRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_archive_route(self):
        response = self.app.get('/archive')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

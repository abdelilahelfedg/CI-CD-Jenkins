import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask CI/CD Demo using Jenkins', response.data)

    def test_hello_with_name(self):
        response = self.client.post('/hello', data={'username': 'Amine'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello Amine', response.data)

    def test_hello_without_name(self):
        response = self.client.post('/hello', data={'username': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello there', response.data)

    def test_sum_valid(self):
        response = self.client.post('/sum', data={'a': '5', 'b': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'8.0', response.data)

    def test_sum_invalid_input(self):
        response = self.client.post('/sum', data={'a': 'abc', 'b': '3'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input', response.data)

if __name__ == "__main__":
    unittest.main()

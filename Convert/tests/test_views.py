from django.test import TestCase

class TestViews(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weight(self):
        response = self.client.get('/weight/')
        self.assertEqual(response.status_code, 200)

    def test_temperature(self):
        response = self.client.get('/temperature/')
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        response = self.client.get('/result/')
        self.assertEqual(response.status_code, 200)

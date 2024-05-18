import unittest
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_edit_route_get(self):
        response = self.app.get('/edit')
        self.assertEqual(response.status_code, 200)

    def test_edit_route_post(self):
        response = self.app.post('/edit', data={'favorite_pizzas': ['1', '2']})
        self.assertEqual(response.status_code, 302)  # Redirect status code

    def test_choose_route_post(self):
        response = self.app.post('/choose', data={'pizza_count': '3'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_pizza_count(self):
        response = self.app.post('/choose', data={'pizza_count': 'invalid'})
        self.assertEqual(response.status_code, 200)  # It should still return a valid response

    def test_negative_pizza_count(self):
        response = self.app.post('/choose', data={'pizza_count': '-5'})
        self.assertEqual(response.status_code, 200)  # It should still return a valid response

    # def test_chosen_pizza(self):
    #     response = self.app.post('/choose', data={'pizza_count': '1'})
    #     # Assuming chosen_pizzas template renders the chosen pizzas, you can check if the pizza names are in the
    #     # response
    #     self.assertIn(b'Cassa', response.data)


if __name__ == '__main__':
    unittest.main()

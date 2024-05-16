import unittest
from unittest.mock import patch
from main import choose_pizza, get_pizza_count


class TestPizzaDecider(unittest.TestCase):

    def setUp(self):
        # Define some sample data for testing
        self.available_pizzas = {1: 'Margherita', 2: 'Pepperoni', 3: 'Vegetarian'}
        self.favorite_pizzas = ['Margherita', 'Pepperoni']

    def test_choose_pizza(self):
        # Test that the chosen pizza is in the available pizzas list
        chosen_pizza_number, chosen_pizza = choose_pizza(self.available_pizzas, self.favorite_pizzas)
        self.assertTrue(chosen_pizza_number in self.available_pizzas)

    @patch('builtins.input', side_effect=['3'])  # Mocking user input
    def test_get_pizza_count(self, mock_input):
        # Test that get_pizza_count returns the expected count
        pizza_count = get_pizza_count()
        self.assertEqual(pizza_count, 3)

    @patch('builtins.input', side_effect=['a', '2'])  # Mocking user input with non-integer first input
    def test_get_pizza_count_non_integer(self, mock_input):
        # Test that get_pizza_count handles non-integer input
        pizza_count = get_pizza_count()
        self.assertEqual(pizza_count, 2)

    @patch('builtins.input', side_effect=['0', '2'])  # Mocking user input with zero count
    def test_get_pizza_count_zero(self, mock_input):
        # Test that get_pizza_count handles zero input count
        pizza_count = get_pizza_count()
        self.assertEqual(pizza_count, 2)

    @patch('builtins.input', side_effect=['-2', '2'])  # Mocking user input with negative count
    def test_get_pizza_count_negative(self, mock_input):
        # Test that get_pizza_count handles negative input count
        pizza_count = get_pizza_count()
        self.assertEqual(pizza_count, 2)

    @patch('builtins.input', side_effect=['5'])  # Mocking user input with count greater than available pizzas
    def test_get_pizza_count_greater_than_available(self, mock_input):
        # Test that get_pizza_count handles count greater than available pizzas
        pizza_count = get_pizza_count()
        self.assertEqual(pizza_count, 5)


if __name__ == '__main__':
    unittest.main()

import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like 'Nairobi, Kenya' work?"""
        formatted_name = get_city_country('Nairobi', 'Kenya')
        self.assertEqual(formatted_name, 'Nairobi, Kenya')

    def test_city_country_population(self):
        """Do names like 'Nairobi, Kenya-Population:5000000' work?"""
        formatted_name = get_city_country('Nairobi', 'Kenya', 5000000)
        self.assertEqual(formatted_name, 'Nairobi, Kenya-Population:5000000')


if __name__ == '__main__':
    unittest.main()
from models.city import City
import datetime
import unittest


class CityCase(unittest.TestCase):
    city = City()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

        # BaseModel Attributes
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

        # BaseModel Attributes
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

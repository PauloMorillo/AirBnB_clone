from models.amenity import Amenity
import datetime
import unittest


class AmenityCase(unittest.TestCase):
    amenitiy = Amenity()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.amenitiy, "name"))

        # BaseModel Attributes
        self.assertTrue(hasattr(self.amenitiy, "id"))
        self.assertTrue(hasattr(self.amenitiy, "created_at"))
        self.assertTrue(hasattr(self.amenitiy, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.amenitiy.name, str)

        # BaseModel Attributes
        self.assertIsInstance(self.amenitiy.id, str)
        self.assertIsInstance(self.amenitiy.created_at, datetime.datetime)
        self.assertIsInstance(self.amenitiy.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

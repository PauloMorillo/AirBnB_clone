from models.state import State
import datetime
import unittest


class StateCase(unittest.TestCase):
    state = State()

    def test_hasattr(self):
        self.assertTrue(hasattr(self.state, "name"))

        # BaseModel Attributes
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))

    def test_types(self):
        self.assertIsInstance(self.state.name, str)

        # BaseModel Attributes
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()

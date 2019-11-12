from models.base_model import BaseModel
import datetime
import unittest


class BaseModelCase(unittest.TestCase):
    dict_obj = "[BaseModel] (1234-5678-9012) {'id': '1234-5678-9012', " \
               "'created_at': datetime.datetime(2019, 11, 12, 8, 31, 23, " \
               "541848), 'updated_at': datetime.datetime(2019, 11, 12, 8, " \
               "31, 23, 541852)}"
    base = BaseModel()

    base.created_at = datetime.datetime(2019, 11, 12, 8, 31, 23, 541848)
    base.updated_at = datetime.datetime(2019, 11, 12, 8, 31, 23, 541852)
    base.id = "1234-5678-9012"

    def test_hasattr(self):
        # BaseModel Attributes
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

        self.assertTrue(hasattr(self.base, "save"))
        self.assertTrue(hasattr(self.base, "to_dict"))

    def test_types(self):
        # BaseModel Attributes
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

    def test_str_method(self):
        self.base.id = "1234-5678-9012"
        self.assertEqual(str(self.base), self.dict_obj)

    def test_repr_method(self):
        self.assertEqual(repr(self.base), self.dict_obj)

    def test_to_dict_method(self):
        cre_at_iso = self.base.created_at.isoformat()
        upd_at_iso = self.base.updated_at.isoformat()
        datetimes = " '{}', 'updated_at': '{}'".format(cre_at_iso, upd_at_iso)

        self.assertEqual(str(self.base.to_dict()), "{'id': '1234-5678-9012', "
                                                   "'created_at':" +
                         datetimes + ", '__class__': 'BaseModel'}")


if __name__ == '__main__':
    unittest.main()

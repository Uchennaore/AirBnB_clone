#!/usr/bin/python3
"""
module to test city
"""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cty = City()
        cls.cty.name = "SF"
        cls.cty.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        del cls.cty
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.cty.__class__, BaseModel), True)

    def test_functions(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attr(self):
        self.assertTrue('id' in self.cty.__dict__)
        self.assertTrue('created_at' in self.cty.__dict__)
        self.assertTrue('updated_at' in self.cty.__dict__)
        self.assertTrue('state_id' in self.cty.__dict__)
        self.assertTrue('name' in self.cty.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.cty.name), str)
        self.assertEqual(type(self.cty.state_id), str)

    def test_save(self):
        self.cty.save()
        self.assertNotEqual(self.cty.created_at, self.cty.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.cty), True)


if __name__ == "__main__":
    unittest.main()

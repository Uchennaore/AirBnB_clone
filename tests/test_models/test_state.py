#!/usr/bin/python3
"""
module contains test
for state
"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.st = State()
        cls.st.name = "Uttarakhand"

    @classmethod
    def tearDownClass(cls):
        del cls.st
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.st.__class__, BaseModel), True)

    def test_functions(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attr(self):
        self.assertTrue('id' in self.st.__dict__)
        self.assertTrue('created_at' in self.st.__dict__)
        self.assertTrue('updated_at' in self.st.__dict__)
        self.assertTrue('name' in self.st.__dict__)

    def test__strings(self):
        self.assertEqual(type(self.st.name), str)

    def test_save(self):
        self.st.save()
        self.assertNotEqual(self.st.created_at, self.st.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.st), True)


if __name__ == "__main__":
    unittest.main()

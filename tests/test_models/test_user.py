#!/usr/bin/python3

import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.usr = User()
        cls.usr.first_name = "Tessa"
        cls.usr.last_name = "Uberville"
        cls.usr.email = "tesst@gmail.com"
        cls.usr.password = "blue"

    @classmethod
    def tearDownClass(cls):
        del cls.usr
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_subclass(self):
        self.assertTrue(issubclass(self.usr.__class__, BaseModel), True)

    def test_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_attr(self):
        self.assertTrue('email' in self.usr.__dict__)
        self.assertTrue('id' in self.usr.__dict__)
        self.assertTrue('created_at' in self.usr.__dict__)
        self.assertTrue('updated_at' in self.usr.__dict__)
        self.assertTrue('password' in self.usr.__dict__)
        self.assertTrue('first_name' in self.usr.__dict__)
        self.assertTrue('last_name' in self.usr.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.usr.email), str)
        self.assertEqual(type(self.usr.password), str)
        self.assertEqual(type(self.usr.first_name), str)
        self.assertEqual(type(self.usr.first_name), str)

    def test_save(self):
        self.usr.save()
        self.assertNotEqual(self.usr.created_at, self.usr.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.usr), True)


if __name__ == "__main__":
    unittest.main()

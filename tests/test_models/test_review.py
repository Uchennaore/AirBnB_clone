#!/usr/bin/python3
"""
Unitesting for review
"""
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Mitali = Review()
        cls.Mitali.place_id = "SF"
        cls.Mitali.user_id = "Test"
        cls.Mitali.text = "Blue"

    @classmethod
    def tearDownClass(cls):
        del cls.Mitali
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_sub(self):
        self.assertTrue(issubclass(self.Mitali.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attr(self):
        self.assertTrue('id' in self.Mitali.__dict__)
        self.assertTrue('created_at' in self.Mitali.__dict__)
        self.assertTrue('updated_at' in self.Mitali.__dict__)
        self.assertTrue('place_id' in self.Mitali.__dict__)
        self.assertTrue('text' in self.Mitali.__dict__)
        self.assertTrue('user_id' in self.Mitali.__dict__)

    def test_strings(self):
        self.assertEqual(type(self.Mitali.text), str)
        self.assertEqual(type(self.Mitali.place_id), str)
        self.assertEqual(type(self.Mitali.user_id), str)

    def test_save(self):
        self.Mitali.save()
        self.assertNotEqual(self.Mitali.created_at, self.Mitali.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.Mitali), True)


if __name__ == "__main__":
    unittest.main()

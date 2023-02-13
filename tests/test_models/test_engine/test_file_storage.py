#!/usr/bin/python3
"""
Unittest to test FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    testing file storage
    """

    @classmethod
    def setUpClass(cls):
        cls.usr = User()
        cls.usr.first_name = "Tay"
        cls.usr.last_name = "lor"
        cls.usr.email = "taylor@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        del cls.usr

    def teardown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_style_check(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """
        Tests method: all (returns dic <class>.<id> : <obj instance>)
        """
        fstorage = FileStorage()
        instances_dic = fstorage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, fstorage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves object into dictionary)
        """
        n_storage = FileStorage()
        dic = n_storage.all()
        rev = User()
        rev.id = 999999
        rev.name = "Tassadar"
        n_storage.new(rev)
        key = rev.__class__.__name__ + "." + str(rev.id)
        self.assertIsNotNone(dic[key])

    def test_reload(self):
        """
        reloading (reloads objects from string file)
        """
        self.storage.save()
        pth = os.path.dirname(os.path.abspath("console.py"))
        pt = os.path.join(pth, "file.json")
        with open(pt, 'r') as f:
            lines = f.readlines()

        try:
            os.remove(pt)
        except BaseException:
            pass

        self.storage.save()

        with open(pt, 'r') as f:
            lines2 = f.readlines()

        self.assertEqual(lines, lines2)

        try:
            os.remove(pt)
        except BaseException:
            pass

        with open(pt, "w") as f:
            f.write("{}")
        with open(pt, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

if __name__ == "__main__":
    unittest.main()

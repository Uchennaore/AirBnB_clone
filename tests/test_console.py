#!/usr/bin/python3
"""
module test for console
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    testing the console
    """

    @classmethod
    def setUpClass(cls):
        """
        setup for the test
        """
        cls.cnsl = HBNBCommand()

    @classmethod
    def teardown(cls):
        """
        at the end of the test this will tear it down
        """
        del cls.cnsl

    def tearDown(self):
        """
        Remove temporary file (file.json) created as a result
        """
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')

    def test_docstrings(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_empty(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """test quit command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.cnsl.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """Test create command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("create User")
            self.cnsl.onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("all User")
            self.assertEqual(
                "[[User]", f.getvalue()[:7])

    def test_show(self):
        """Test cmd output: show"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("show")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("show asdfsdrfs")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("show BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("show City abcd-123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_destroy(self):
        """Test cmd output: destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("destroy")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("destroy Galaxy")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("destroy User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("destroy BaseModel 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())

    def test_all(self):
        """Test all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """Test cmd output: update"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update sldkfjsl")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update User")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update User 12345")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())

    def test_classes_with_all(self):
        """
        Passing arguments to classes.all()
        """
        pth = os.path.dirname(os.path.abspath("console.py"))
        pt = os.path.join(pth, "file.json")
        with patch('sys.stdout', new=StringIO()) as f:
            self.cnsl.onecmd("BaseModel.all()")
            with open(pt, 'r') as rf:
                self.assertEqual("[[BaseModel]", f.getvalue()[:12])

    def test_classes_with_count(self):
        """
        Passing arguments to classes.count()
        """
        p = os.path.dirname(os.path.abspath("console.py"))
        pat = os.path.join(p, "file.json")
        with path('sys.stdout', new=StringIO()) as fl:
            self.cnsl.onecmd("BaseModel.count()")
            with open(p, 'r') as rfl:
                self.assertEqula("1", f.getvalue())

    def test_classes_with_show(self):
        """
        Passing arguments to classes.show(id)
        """
        p = os.path.dirname(os.path.abspath("console.py"))
        pat = os.path.join(p, "file.json")
        with path('sys.stdout', new=StringIO()) as fl:
            self.cnsl.onecmd("BaseModel.show()")
            self.assertEqual("** id is missing **\n",
                             f.getvalue())

    def test_classes_with_destroy(self):
        """
        Passing arguments to classes.destroy(id)
        """
        p = os.path.dirname(os.path.abspath("console.py"))
        pat = os.path.join(p, "file.json")
        with path('sys.stdout', new=StringIO()) as fl:
            self.cnsl.onecmd("BaseModel.destroy()")
            self.assertEqual("** id is missing **\n",
                             f.getvalue())

    def test_classes_with_update(self):
        """
        Passing arguments to classes.destroy(id)
        """
        p = os.path.dirname(os.path.abspath("console.py"))
        pat = os.path.join(p, "file.json")
        with path('sys.stdout', new=StringIO()) as fl:
            self.cnsl.onecmd("BaseModel.update()")
            self.assertEqual("** id is missing **\n",
                             f.getvalue())


if __name__ == "__main__":
    unittest.main()

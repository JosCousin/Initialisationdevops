import unittest

from app import ajouter_tache

class TestStringMethods(unittest.TestCase):

    def test_liste(self):
        self.assertEqual(ajouter_tache("hello"), "c'est good mon gars")
        self.assertEqual(ajouter_tache("123464"), "facho")

if __name__ == '__main__':
    unittest.main()
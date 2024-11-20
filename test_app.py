"""
Tests unitaires pour les fonctions du module app.py.
"""

import unittest
from app import ajouter_tache_test

class TestAppMethods(unittest.TestCase):
    """
    Classe de tests pour les fonctions du module app.py.
    """

    def test_ajouter_tache_test(self):
        """
        Test de la fonction ajouter_tache_test.
        """
        self.assertEqual(ajouter_tache_test("hello"), "c'est good mon gars")
        self.assertEqual(ajouter_tache_test("123464"), "facho")

if __name__ == '__main__':
    unittest.main()

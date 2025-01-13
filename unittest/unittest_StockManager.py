import unittest
import pandas as pd
import os
import shutil
from Script.StockManager import StockManager  # Remplacez par le chemin de votre module si besoin


class TestStockManager(unittest.TestCase):
    def setUp(self):
        # Configuration initiale
        self.manager = StockManager()
        self.test_folder = "test_data"
        self.test_output_folder = "test_output"
        os.makedirs(self.test_folder, exist_ok=True)
        os.makedirs(self.test_output_folder, exist_ok=True)

        # Création de fichiers CSV de test
        data1 = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})
        data2 = pd.DataFrame({"id": [4, 5, 6], "name": ["Dave", "Eve", "Frank"]})

        data1.to_csv(os.path.join(self.test_folder, "file1.csv"), index=False)
        data2.to_csv(os.path.join(self.test_folder, "file2.csv"), index=False)

    def tearDown(self):
        # Nettoyage des fichiers et dossiers de test
        shutil.rmtree(self.test_folder)
        shutil.rmtree(self.test_output_folder)

    def test_load_files(self):
        # Test de la méthode load_files
        self.manager.load_files(self.test_folder)
        self.assertEqual(len(self.manager.data), 6)  # Vérifie que 6 lignes sont chargées

    def test_search(self):
        # Test de la méthode search
        self.manager.load_files(self.test_folder)
        results = self.manager.search("name", "Alice")
        self.assertEqual(len(results), 1)  # Vérifie qu'un seul résultat est trouvé
        self.assertEqual(results.iloc[0]["name"], "Alice")  # Vérifie que le nom correspond

    def test_search_invalid_column(self):
        # Test de recherche dans une colonne inexistante
        self.manager.load_files(self.test_folder)
        results = self.manager.search("unknown_column", "Alice")
        self.assertIsNone(results)  # Vérifie que la méthode retourne None

    def test_generate_report(self):
        # Test de la méthode generate_report
        self.manager.load_files(self.test_folder)
        output_file = os.path.join(self.test_output_folder, "report.csv")
        self.manager.generate_report(output_file)

        self.assertTrue(os.path.exists(output_file))  # Vérifie que le fichier est créé
        output_data = pd.read_csv(output_file)
        self.assertEqual(len(output_data), 6)  # Vérifie que le rapport contient 6 lignes

    def test_generate_report_empty(self):
        # Test de la génération de rapport avec des données vides
        output_file = os.path.join(self.test_output_folder, "empty_report.csv")
        self.manager.generate_report(output_file)
        self.assertFalse(os.path.exists(output_file))  # Vérifie que le fichier n'est pas créé


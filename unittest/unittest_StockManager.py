import unittest
import os
import pandas as pd
from Script.StockManager import StockManager  # Assure-toi que le chemin d'import est correct


class TestStockManager(unittest.TestCase):

    def setUp(self):
        """Configuration avant chaque test : Création d'un environnement temporaire et d'un StockManager."""
        self.manager = StockManager()

        # Création d'un dossier temporaire avec des fichiers CSV pour les tests
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)

        # Fichier 1
        with open(os.path.join(self.test_dir, "stock1.csv"), "w") as f:
            f.write("Produit,Catégorie,Quantité,Prix\n")
            f.write("Chaise,Meubles,10,49.99\n")
            f.write("Table,Meubles,5,89.99\n")

        # Fichier 2
        with open(os.path.join(self.test_dir, "stock2.csv"), "w") as f:
            f.write("Produit,Catégorie,Quantité,Prix\n")
            f.write("Canapé,Meubles,2,399.99\n")
            f.write("Lit,Meubles,3,299.99\n")

        # Chemin du rapport temporaire
        self.report_file = "test_report.csv"

    def tearDown(self):
        """Nettoyage après chaque test : Suppression des fichiers temporaires."""
        # Supprimer les fichiers de test
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_load_files(self):
        """Test pour vérifier que les fichiers CSV sont chargés correctement."""
        self.manager.load_files(self.test_dir)
        self.assertIsNotNone(self.manager.data, "Les données ne devraient pas être vides après le chargement.")
        self.assertEqual(len(self.manager.data), 4, "Le nombre total de lignes consolidées devrait être 4.")
        self.assertListEqual(
            list(self.manager.data.columns),
            ["Produit", "Catégorie", "Quantité", "Prix"],
            "Les colonnes chargées ne correspondent pas."
        )

    def test_search_valid_column(self):
        """Test de recherche dans une colonne existante."""
        self.manager.load_files(self.test_dir)
        results = self.manager.search("Produit", "Chaise")
        self.assertIsNotNone(results, "Les résultats ne devraient pas être vides.")
        self.assertEqual(len(results), 1, "La recherche devrait retourner exactement une ligne.")
        self.assertEqual(results.iloc[0]["Produit"], "Chaise", "Le résultat devrait contenir 'Chaise'.")

    def test_search_invalid_column(self):
        """Test de recherche dans une colonne inexistante."""
        self.manager.load_files(self.test_dir)
        results = self.manager.search("Inexistant", "Valeur")
        self.assertIsNone(results, "La recherche dans une colonne inexistante devrait retourner None.")

    def test_generate_report(self):
        """Test pour vérifier que le rapport est généré correctement."""
        self.manager.load_files(self.test_dir)

        # Assurer que les données sont présentes
        self.assertFalse(self.manager.data.empty,
                         "Les données ne devraient pas être vides avant la génération du rapport.")

        # Appeler la méthode de génération du rapport
        self.manager.generate_report(self.report_file)

        # Vérifier que le fichier a été créé
        self.assertTrue(os.path.exists(self.report_file), "Le fichier de rapport devrait être créé.")

    def test_generate_report_without_data(self):
        """Test de génération de rapport sans données chargées."""
        self.manager.generate_report(self.report_file)
        self.assertFalse(os.path.exists(self.report_file),
                         "Le fichier de rapport ne devrait pas être créé si aucune donnée n'est chargée.")

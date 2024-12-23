import unittest
import os
import io
from unittest_StockManager.mock import patch
import pandas as pd

# Importez votre classe StockManager
from main import StockManager


class TestStockManager(unittest.TestCase):
    def setUp(self):
        """Initialisation avant chaque test"""
        self.manager = StockManager()

    def test_init(self):
        """Test de l'initialisation de la classe"""
        self.assertIsInstance(self.manager.data, pd.DataFrame)
        self.assertTrue(hasattr(self.manager, 'logger'))

    def test_load_files(self):
        """Test de la méthode load_files"""
        # Créez un dossier temporaire avec des fichiers CSV de test
        import tempfile
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Créez un fichier CSV de test
            test_df = pd.DataFrame({
                'Produit': ['A', 'B'],
                'Quantité': [10, 20],
                'Prix Unitaire': [100, 200]
            })
            test_df.to_csv(os.path.join(tmpdirname, 'test.csv'), index=False)

            # Chargez les fichiers
            self.manager.load_files(tmpdirname)

            # Vérifiez que les données ont été chargées
            self.assertFalse(self.manager.data.empty)
            self.assertEqual(len(self.manager.data), 2)

    def test_search(self):
        """Test de la méthode search"""
        # Créez un DataFrame de test
        test_df = pd.DataFrame({
            'Produit': ['Pomme', 'Banane', 'Orange'],
            'Catégorie': ['Fruit', 'Fruit', 'Fruit']
        })
        self.manager.data = test_df

        # Testez la recherche
        results = self.manager.search('Produit', 'Pomme')
        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]['Produit'], 'Pomme')

    def test_generate_report(self):
        """Test de la méthode generate_report"""
        # Créez un DataFrame de test
        test_df = pd.DataFrame({
            'Catégorie': ['Fruit', 'Fruit', 'Légume'],
            'Quantité': [10, 20, 15],
            'Prix Unitaire': [100, 200, 50]
        })
        self.manager.data = test_df

        # Utilisez un fichier temporaire pour le rapport
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.csv', delete=False) as temp_file:
            temp_path = temp_file.name

        # Générez le rapport
        self.manager.generate_report(temp_path)

        # Vérifiez que le fichier a été créé
        self.assertTrue(os.path.exists(temp_path))

        # Lisez le rapport généré
        report_df = pd.read_csv(temp_path)
        self.assertEqual(len(report_df), 2)  # Deux catégories

        # Nettoyez le fichier temporaire
        os.unlink(temp_path)

    def test_main_menu_interaction(self):
        """Test de l'interaction avec le menu principal"""
        # Simulez les entrées utilisateur et la sortie
        user_inputs = [
            "1",  # Charger les fichiers
            "/chemin/exemple",  # Chemin du dossier
            "4"  # Quitter
        ]

        # Utilisez patch pour simuler input() et sys.exit()
        with patch('builtins.input', side_effect=user_inputs), \
                patch('sys.exit') as mock_exit, \
                patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:

            # Appelez la fonction main
            try:
                # Vous devrez peut-être adapter cette ligne selon votre implémentation exacte
                from __main__ import __name__, main
                main()
            except SystemExit:
                pass

            # Vérifiez que le menu s'affiche et que l'utilisateur peut quitter
            output = mock_stdout.getvalue()
            self.assertIn("Options :", output)
            self.assertIn("1. Charger les fichiers CSV depuis un dossier", output)
            self.assertIn("4. Quitter", output)

    def test_search_with_valid_column(self):
        # Créez un DataFrame de test
        test_df = pd.DataFrame({
            'Produit': ['Pomme', 'Banane', 'Orange'],
            'Catégorie': ['Fruit', 'Fruit', 'Fruit']
        })
        self.manager.data = test_df

        # Testez la recherche avec une colonne valide
        results = self.manager.search('Produit', 'Pomme')
        self.assertEqual(len(results), 1)
        self.assertEqual(results.iloc[0]['Produit'], 'Pomme')

        # Testez la recherche avec une valeur qui ne produit pas de résultats
        results = self.manager.search('Produit', 'Kiwi')
        self.assertTrue(results.empty)

if __name__ == '__main__':
    unittest.main()
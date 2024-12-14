import os
import pandas as pd
import logging

class StockManager:
    def __init__(self):
        self.data = pd.DataFrame()
        logging.basicConfig(level=logging.INFO)  # Configuration de base du logger
        self.logger = logging.getLogger(__name__)  # Création d'un logger

    def load_files(self, folder_path):
        try:
            all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
            dataframes = [pd.read_csv(file) for file in all_files]
            self.data = pd.concat(dataframes, ignore_index=True)
            print("Tous les fichiers ont été consolidés avec succès.")
        except Exception as e:
            print(f"Erreur lors du chargement des fichiers : {e}")

    def search(self, column, value):
        try:
            results = self.data[self.data[column].astype(str).str.contains(value, case=False, na=False)]
            self.logger.info(f"Résultats trouvés : \n{results}")
            return results  # Retourne les résultats
        except KeyError:
            self.logger.error(f"La colonne '{column}' n'existe pas dans les données.")
        except Exception as e:
            self.logger.error(f"Erreur lors de la recherche : {e}")
        return None  # Retourne None en cas d'erreur

    def generate_report(self, output_path):
        try:
            summary = self.data.groupby('Catégorie').agg({
                'Quantité': 'sum',
                'Prix Unitaire': 'mean'
            }).reset_index()
            summary.to_csv(output_path, index=False)
            print(f"Rapport généré : {output_path}")
        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")

def main():
    manager = StockManager()

    while True:
        print("\nOptions :")
        print("1. Charger les fichiers CSV depuis un dossier")
        print("2. Rechercher dans les stocks")
        print("3. Générer un rapport")
        print("4. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            dossier = input("Entrez le chemin du dossier contenant les fichiers CSV : ")
            manager.load_files(dossier)
        elif choix == "2":
            colonne = input("Entrez le nom de la colonne pour la recherche (ex: Produit, Catégorie) : ")
            valeur = input("Entrez la valeur recherchée : ")
            manager.search(colonne, valeur)
        elif choix == "3":
            chemin_sortie = input("Entrez le chemin du fichier de sortie pour le rapport : ")
            manager.generate_report(chemin_sortie)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
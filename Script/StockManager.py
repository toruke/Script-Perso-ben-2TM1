import pandas as pd
import logging
import os

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

    def generate_report(self, output_file):
        try:
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                print(f"Création du dossier de sortie : {output_dir}")
                os.makedirs(output_dir)

            if self.data.empty:
                print("Erreur : Aucune donnée à écrire dans le rapport.")
                return

            print(f"Écriture du rapport dans le fichier : {output_file}")
            self.data.to_csv(output_file, index=False)
            print("Rapport généré avec succès.")
        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")
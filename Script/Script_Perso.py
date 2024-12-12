import os
import pandas as pd

class StockManager:
    def __init__(self):
        """Initialise un gestionnaire de stocks.

            PRE: Aucune.
            POST: Initialise un objet `StockManager` avec un attribut `data` sous forme d'un DataFrame vide.
            """
        self.data = pd.DataFrame()

    def load_files(self, folder_path):
        """Charge tous les fichiers CSV d'un dossier dans une seule base de données.

    PRE:
        - `folder_path` est une chaîne de caractères représentant un chemin valide vers un dossier contenant des fichiers CSV.
        - Les fichiers CSV doivent avoir un format correct (colonnes compatibles).

    POST:
        - Les fichiers CSV sont concaténés en un seul DataFrame stocké dans `self.data`.
        - Un message de succès est affiché.
        - En cas d'erreur (dossier inexistant, fichiers absents ou illisibles), une exception est levée et un message d'erreur est affiché.
        """
        try:
            all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
            dataframes = [pd.read_csv(file) for file in all_files]
            self.data = pd.concat(dataframes, ignore_index=True)
            print("Tous les fichiers ont été consolidés avec succès.")
        except Exception as e:
            print(f"Erreur lors du chargement des fichiers : {e}")

    def search(self, column, value):
        """Recherche dans les données consolidées.

        PRE:
            - `column` est une chaîne correspondant au nom d'une colonne existante dans `self.data`.
            - `value` est une chaîne représentant la valeur à rechercher dans la colonne.

        POST:
            - Affiche les lignes du DataFrame `self.data` où la valeur recherchée est présente (sans respecter la casse).
            - Si la colonne n'existe pas, un message d'erreur est affiché.
            - Si aucune correspondance n'est trouvée, un DataFrame vide est affiché.
        """
        try:
            results = self.data[self.data[column].astype(str).str.contains(value, case=False, na=False)]
            print(results)
        except KeyError:
            print(f"La colonne '{column}' n'existe pas dans les données.")
        except Exception as e:
            print(f"Erreur lors de la recherche : {e}")

    def generate_report(self, output_path):
        """Génère un rapport récapitulatif sous forme de fichier CSV.

        PRE:
            - `self.data` doit contenir des colonnes nommées 'Catégorie', 'Quantité', et 'Prix Unitaire'.
            - `output_path` est une chaîne représentant le chemin complet (avec extension `.csv`) où le fichier sera sauvegardé.

        POST:
            - Crée un fichier CSV contenant un rapport regroupé par 'Catégorie' avec la somme des quantités et la moyenne des prix unitaires.
            - Enregistre le fichier au chemin spécifié dans `output_path`.
            - En cas d'erreur (colonnes manquantes ou problème d'écriture), une exception est levée et un message d'erreur est affiché.
        """
        try:
            summary = self.data.groupby('Catégorie').agg({
                'Quantité': 'sum',
                'Prix Unitaire': 'mean'
            }).reset_index()
            summary.to_csv(output_path, index=False)
            print(f"Rapport généré : {output_path}")
        except Exception as e:
            print(f"Erreur lors de la génération du rapport : {e}")

if __name__ == "__main__":
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

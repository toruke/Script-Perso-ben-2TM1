import Script.StockManager as StockManager

def main():
    manager = StockManager.StockManager()

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
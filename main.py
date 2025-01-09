import Script.StockManager as StockManager
import argparse as arg


def main():
    parser = arg.ArgumentParser(description="Gestionnaire de stock à partir de fichiers CSV.")

    # Ajout des arguments
    parser.add_argument('-l', '--load', type=str, help="Chemin du dossier contenant les fichiers CSV à charger.")
    parser.add_argument('-s', '--search', nargs=2, metavar=('COLONNE', 'VALEUR'),
                        help="Rechercher dans les stocks. Exemple : -s Produit 'Chaise'")
    parser.add_argument('-r', '--report', type=str, help="Chemin du fichier de sortie pour générer le rapport.")
    parser.add_argument('--shell', action='store_true',
                        help="Lancer l'application en mode interactif (shell).")

    args = parser.parse_args()

    # Instancier le gestionnaire de stock
    manager = StockManager.StockManager()

    # Vérifier si des fichiers ont été chargés
    data_loaded = False
    if args.load:
        manager.load_files(args.load)
        print(f"Fichiers CSV chargés depuis le dossier : {args.load}")
        data_loaded = True

    # Vérification pour les autres options
    if args.search:
        if not data_loaded:
            print("Erreur : Vous devez d'abord charger des fichiers avec '--load' avant d'effectuer une recherche.")
            return
        colonne, valeur = args.search
        manager.search(colonne, valeur)
        print(f"Recherche effectuée dans la colonne '{colonne}' pour la valeur '{valeur}'.")

    if args.report:
        if not data_loaded:
            print("Erreur : Vous devez d'abord charger des fichiers avec '--load' avant de générer un rapport.")
            return
        manager.generate_report(args.report)
        print(f"Rapport généré dans le fichier : {args.report}")

    if args.shell:
        shell(manager)

def shell(manager):

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
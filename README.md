# Stock Manager

## Description
Le **Stock Manager** est une application Python conçue pour gérer et analyser des données de stock issues de fichiers CSV. Elle permet :
- De charger plusieurs fichiers CSV depuis un dossier et les consolider en une base de données unique.
- De rechercher des informations dans les données consolidées.
- De générer un rapport récapitulatif basé sur les catégories, les quantités totales et les prix moyens.

## Fonctionnalités

1. **Chargement des fichiers CSV** :
   - Consolide tous les fichiers CSV d'un dossier donné en un seul tableau de données.
   - Gère les erreurs en cas de fichiers illisibles ou de format incorrect.

2. **Recherche** :
   - Permet de rechercher une valeur spécifique dans une colonne des données consolidées.
   - Affiche les résultats directement.

3. **Génération de rapport** :
   - Crée un fichier CSV récapitulatif regroupé par catégorie.
   - Calcule la somme des quantités et la moyenne des prix unitaires pour chaque catégorie.

## Prérequis

- **Python** 3.7 ou version ultérieure.
- Bibliothèques Python nécessaires :
  - `pandas`

## Installation

1. Clonez le dépôt ou téléchargez les fichiers sources :
   ```bash
   git clone https://github.com/toruke/Script-Perso-ben-2TM1
   cd Dev2/Script
   ```

2. Installez les dépendances requises avec `pip` :
   ```bash
   pip install pandas
   ```

## Utilisation

1. Lancez le programme :
   ```bash
   python stock_manager.py
   ```

2. Suivez les options affichées dans le menu principal :

   - **Option 1** : Charger les fichiers CSV depuis un dossier.
     - Saisissez le chemin du dossier contenant les fichiers CSV.
     - Exemple : `/chemin/vers/dossier`

   - **Option 2** : Rechercher dans les stocks.
     - Saisissez le nom de la colonne à rechercher (ex. : `Produit`, `Catégorie`).
     - Entrez la valeur à rechercher (insensible à la casse).

   - **Option 3** : Générer un rapport.
     - Saisissez le chemin complet (y compris le nom du fichier) pour enregistrer le rapport.
     - Exemple : `rapport.csv` ou `/chemin/vers/rapport.csv`.

   - **Option 4** : Quitter le programme.

## Exemple d'utilisation

### Fichiers CSV initiaux

Contenu de `stocks1.csv` :
```csv
Catégorie,Produit,Quantité,Prix Unitaire
Fruits,Pomme,10,2.5
Fruits,Banane,20,1.8
```

Contenu de `stocks2.csv` :
```csv
Catégorie,Produit,Quantité,Prix Unitaire
Légumes,Carotte,15,0.9
Fruits,Mangue,5,3.2
```

### Étapes dans le programme

1. **Charger les fichiers** :
   - Dossier : `/chemin/vers/fichiers`
   - Résultat consolidé :
     ```
     Catégorie  Produit  Quantité  Prix Unitaire
     Fruits     Pomme    10        2.5
     Fruits     Banane   20        1.8
     Légumes    Carotte  15        0.9
     Fruits     Mangue   5         3.2
     ```

2. **Rechercher** :
   - Colonne : `Produit`
   - Valeur : `Banane`
   - Résultat :
     ```
     Catégorie  Produit  Quantité  Prix Unitaire
     Fruits     Banane   20        1.8
     ```

3. **Générer un rapport** :
   - Chemin de sortie : `rapport.csv`
   - Contenu généré :
     ```csv
     Catégorie,Quantité,Prix Unitaire
     Fruits,35,2.5
     Légumes,15,0.9
     ```

## Gestion des erreurs

- Si le dossier spécifié n'existe pas ou ne contient pas de fichiers CSV valides, un message d'erreur sera affiché.
- Si une colonne saisie pour la recherche n'existe pas, le programme affichera un message approprié.
- En cas de problème lors de la génération du rapport (par exemple, colonnes manquantes), un message d'erreur décrira le problème.

## Structure du projet

```plaintext
Dev2/
├── Script/
│   ├── stock_manager.py  # Code source principal
│   └── Data/           # Dossier contenant les fichiers CSV
├── unittest/
│   └──unittest_stock_manager.py #test unitaire du Code source principal
└── README.md         # Documentation (ce fichier)

```

## Auteur
Ce programme a été développé pour vous aider à gérer efficacement vos stocks. Pour toute question, n'hésitez pas à me contacter !

---

Merci d'utiliser **Stock Manager** !

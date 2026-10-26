import sqlite3
from config import BASE_DONNEES


## Créer la table
def creer_table():

    connexion = sqlite3.connect(BASE_DONNEES)

    connexion.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prix TEXT,
            note TEXT,
            url TEXT UNIQUE,
            image TEXT
        )
    """)

    connexion.commit()
    connexion.close()


## Enregistrer un produit
def ajouter_produit(nom, prix, note, url, image):

    connexion = sqlite3.connect(BASE_DONNEES)

    connexion.execute("""
        INSERT OR IGNORE INTO produits
        (nom, prix, note, url, image)
        VALUES (?, ?, ?, ?, ?)
    """, (nom, prix, note, url, image))

    connexion.commit()
    connexion.close()


## Lire les produits enregistrés
def lire_produits():

    connexion = sqlite3.connect(BASE_DONNEES)
    connexion.row_factory = sqlite3.Row

    produits = connexion.execute(
        "SELECT * FROM produits ORDER BY id DESC"
    ).fetchall()

    connexion.close()

    return produits
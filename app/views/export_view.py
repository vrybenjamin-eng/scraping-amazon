import os
import csv
from config import DOSSIER_EXPORTS
from app.models.depot import lire_produits


# Exporter les produits dans un fichier CSV
def exporter_produits():

    produits = lire_produits()

    chemin = os.path.join(DOSSIER_EXPORTS, "produits.csv")

    with open(chemin, "w", newline="", encoding="utf-8-sig") as fichier:

        colonnes = ["nom", "prix", "note", "url", "image"]

        ecrivain = csv.writer(fichier)

        ecrivain.writerow(colonnes)

        for produit in produits:

            ecrivain.writerow([
                produit["nom"],
                produit["prix"],
                produit["note"],
                produit["url"],
                produit["image"]
            ])

    return chemin
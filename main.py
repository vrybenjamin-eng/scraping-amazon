from app.models.depot import creer_table
from app.controllers.scraping_controller import demarrer_scraping
from app.views.console_view import afficher_produit

# Préparer la base de données
creer_table()

# Menu principal
while True:

    print("\n===== AMAZON SCRAPER =====")
    print("1. Collecter des produits")
    print("2. Afficher les produits")
    print("3. Quitter")

    choix = input("Ton choix : ")

    if choix == "1":

        url = input(
            "Adresse de la page autorisée à consulter : "
        )

        resultat = demarrer_scraping(url)

        print("\n", resultat)

    elif choix == "2":

        afficher_produit()

    elif choix == "3":

        print("Au revoir !")
        break

    else:

        print("Choix invalide.")
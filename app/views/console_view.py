from app.models.depot import lire_produits


# Afficher les produits
def afficher_produits():

    produits = lire_produits()

    print("\n===== MES PRODUITS =====\n")

    if not produits:
        print("Aucun produit enregistré.")
        return

    for produit in produits:

        print("Nom :", produit["nom"])
        print("Prix :", produit["prix"])
        print("Note :", produit["note"])
        print("Image :", produit["image"])
        print("URL :", produit["url"])

        print("-" * 40)
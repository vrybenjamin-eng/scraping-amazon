import os
import time
import hashlib
import requests
from config import DOSSIER_IMAGES
from app.scraper.driver import ouvrir_navigateur
from app.scraper.parsing import recuperer_produits
from app.models.depot import ajouter_produit


## Télécharger une image
def telecharger_image(image_url, url_produit):

    if not image_url.startswith("https://"):
        return ""

    nom_fichier = hashlib.md5(
        url_produit.encode()
    ).hexdigest() + ".jpg"

    chemin = os.path.join(
        DOSSIER_IMAGES,
        nom_fichier
    )

    if os.path.exists(chemin):
        return chemin

    try:
        reponse = requests.get(
            image_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )

        reponse.raise_for_status()

        if not reponse.headers.get(
            "Content-Type", ""
        ).startswith("image/"):
            return ""

        with open(chemin, "wb") as fichier:
            fichier.write(reponse.content)

        return chemin

    except requests.RequestException:
        return ""


## Récupérer et enregistrer les produits
def lancer_scraping(url):

    navigateur = ouvrir_navigateur()

    nombre = 0

    try:
        navigateur.get(url)

        time.sleep(3)
        navigateur.get(url)

        time.sleep(3)

        print("Titre de la page :", navigateur.title)
        print("URL actuelle :", navigateur.current_url)

        texte_page = navigateur.find_element(
            "tag name", "body"
        ).text.lower()

        if any(mot in texte_page for mot in [
            "captcha",
            "robot check",
            "access denied"
        ]):
            return "Accès refusé : arrête la collecte."

        # Descendre dans la page pour que les images se chargent
        for i in range(5):
            navigateur.execute_script("window.scrollBy(0, 1000);")
            time.sleep(1)

        produits = recuperer_produits(navigateur)

        for produit in produits:

            image = telecharger_image(
                produit["image_url"],
                produit["url"]
            )

            ajouter_produit(
                produit["nom"],
                produit["prix"],
                produit["note"],
                produit["url"],
                image
            )

            print("Produit :", produit["nom"])
            print("Prix :", produit["prix"])
            print("Note :", produit["note"])
            print("Image :", image or "Non téléchargée")
            print("-" * 30)

            nombre += 1

        return f"Collecte terminée : {nombre} produit(s) traité(s)."

    finally:
        navigateur.quit()

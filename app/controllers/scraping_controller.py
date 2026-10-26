from app.scraper.amazon_scraper import lancer_scraping


## Démarrer la collecte
def demarrer_scraping(url):

    try:
        resultat = lancer_scraping(url)
        return resultat

    except Exception as erreur:
        return "Une erreur est survenue : " + str(erreur)
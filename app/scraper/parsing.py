from urllib.parse import urljoin


# Lire le texte d'un élément
def lire_texte(element, selecteur):
    elements = element.find_elements("css selector", selecteur)

    if elements:
        return elements[0].text.strip()

    return ""


# Récupérer les produits de la page
def recuperer_produits(navigateur):

    cartes = navigateur.find_elements(
        "css selector",
        "[data-component-type='s-search-result']"
    )

    produits = []

    for carte in cartes:

        nom = lire_texte(carte, "h2 span")
        prix = lire_texte(carte, ".a-price .a-offscreen")
        note = lire_texte(carte, ".a-icon-alt")

        liens = carte.find_elements("css selector", "h2 a")

        url = ""

        if liens:
            url = liens[0].get_attribute("href")

        if url:
            url = urljoin(navigateur.current_url, url)

        images = carte.find_elements("css selector", "img")

        image_url = ""

        if images:
            image_url = (
                images[0].get_attribute("src")
                or images[0].get_attribute("data-src")
                or ""
            )

        if nom and url:
            produit = {
                "nom": nom,
                "prix": prix,
                "note": note,
                "url": url,
                "image_url": image_url
            }

            produits.append(produit)

    return produits


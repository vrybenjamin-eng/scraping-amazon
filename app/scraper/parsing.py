from urllib.parse import urljoin


# Lire le texte d'un élément
def lire_texte(element, selecteur):
    elements = element.find_elements("css selector", selecteur)

    if elements:
        # textContent lit aussi le texte caché (prix, note)
        texte = elements[0].get_attribute("textContent")
        if texte:
            return texte.strip()

    return ""


# Récupérer les produits de la page
def recuperer_produits(navigateur):

    cartes = navigateur.find_elements(
        "css selector",
        "[data-component-type='s-search-result']"
    )
    cartes = navigateur.find_elements(
        "css selector",
        "[data-component-type='s-search-result']"
    )

    print("Nombre de cartes trouvées :", len(cartes))
    produits = []

    for carte in cartes:

        nom = lire_texte(carte, "h2 span")
        prix = lire_texte(carte, ".a-price .a-offscreen")
        note = lire_texte(carte, ".a-icon-alt")

        # On essaie plusieurs façons de trouver le lien
        url = ""

        for selecteur in [
            "h2 a",
            "a:has(h2)",
            "a.a-link-normal[href*='/dp/']"
        ]:
            liens = carte.find_elements("css selector", selecteur)

            if liens:
                url = liens[0].get_attribute("href") or ""

            if url:
                break

        if url:
            url = urljoin(navigateur.current_url, url)

            # Garder seulement la partie utile du lien
            if "/dp/" in url:
                url = url.split("?")[0].split("/ref=")[0]

        images = carte.find_elements("css selector", "img.s-image")

        if not images:
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
import os

# Définir les dossiers du projet

DOSSIER_DATA = "data"
DOSSIER_IMAGES = "data/images"
DOSSIER_EXPORTS = "exports"

# Définir le chemin de la base de données

BASE_DONNEES = "data/produits.db"

# Créer les dossiers s'ils n'existent pas

os.makedirs(DOSSIER_DATA, exist_ok=True)
os.makedirs(DOSSIER_IMAGES, exist_ok=True)
os.makedirs(DOSSIER_EXPORTS, exist_ok=True)

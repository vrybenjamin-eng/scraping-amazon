import os

## Dossier principal du projet
DOSSIER_PROJET = os.path.dirname(os.path.abspath(__file__))

## Définir les dossiers du projet

DOSSIER_DATA = os.path.join(DOSSIER_PROJET, "data")
DOSSIER_IMAGES = os.path.join(DOSSIER_PROJET, "data", "images")
DOSSIER_EXPORTS = os.path.join(DOSSIER_PROJET, "exports")

## Définir le chemin de la base de données

BASE_DONNEES = os.path.join(DOSSIER_DATA, "produits.db")

## Créer les dossiers s'ils n'existent pas

os.makedirs(DOSSIER_DATA, exist_ok=True)
os.makedirs(DOSSIER_IMAGES, exist_ok=True)
os.makedirs(DOSSIER_EXPORTS, exist_ok=True)
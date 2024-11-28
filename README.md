# Serpent Cipher Project

## Description
Ce projet implémente l'algorithme de chiffrement **Serpent**, un algorithme de chiffrement par blocs, qui était finaliste pour le standard de chiffrement avancé (AES). Ce projet offre deux versions du chiffrement : 
1. **Serpent avec texte limité** (taille de bloc fixe de 16 caractères).
2. **Serpent avec texte de longueur variable**, permettant de chiffrer et déchiffrer des textes de toute taille grâce à un mécanisme de découpage en blocs.

## Fonctionnalités
- **Chiffrement avec clé fixe** : Utilisation d'une clé statique (modifiable dans le code).
- **Chiffrement de blocs** : Implémentation de Serpent pour gérer le chiffrement de blocs de 128 bits (16 octets).
- **Gestion de padding** : Ajout et suppression du padding pour prendre en charge des textes de longueur arbitraire.
- **Texte de longueur variable** : Possibilité de chiffrer un texte de n'importe quelle longueur.

## Fichiers principaux
1. **`serpent.py`** : Version basique du programme pour chiffrer et déchiffrer des textes **limités à 16 caractères**.
2. **`serpent-long.py`** : Version améliorée pour chiffrer et déchiffrer des textes de longueur variable.

---

## Prérequis
- Python 3.6 ou supérieur.

Aucune bibliothèque externe n'est nécessaire. Le code est implémenté entièrement en Python pur.

---

## Utilisation

### 1. **Exécution de la version avec texte limité (serpent.py)**
Pour exécuter cette version :
```bash
python3 serpent.py

Exemple

Entrée :
Entrez le texte clair (16 caractères max) : bonjour1234

Sortie :
Texte clair : bonjour1234
Texte chiffré (hex) : 9c5a23f8a1b6e7c4570d8f3b4e2c6a59
Texte déchiffré : bonjour1234


2. Exécution de la version avec texte de longueur variable (serpent-long.py)

Pour exécuter cette version :
python3 serpent-long.py

Exemple

Entrée :
Entrez le texte clair : ceci est un exemple de texte avec une longueur variable

Texte clair : ceci est un exemple de texte avec une longueur variable
Texte chiffré (hex) : 84d0f4...
Texte déchiffré : ceci est un exemple de texte avec une longueur variable

```

Structure du projet
```bash
Serpent-cipher/
├── serpent.py            # Version limitée à 16 caractères
├── serpent-long.py       # Version pour textes de longueur variable
├── README.md             # Fichier d'explication du projet

```

Contributions

Ce projet a été réalisé par :

    SAHA KEUATSOP Pierre Aimé
    TAKODJOU DJOUGUELA Ulrich Carmel


Contact

Pour toute question ou suggestion, veuillez contacter :

    Pierre Aimé : aime.saha@facsciences-uy1.cm
    Ulrich Carmel : carmel.takodjou@facsciences-uy1.cm
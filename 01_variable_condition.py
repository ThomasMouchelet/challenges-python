# ========================================
# CHALLENGE 1: Variables et Conditions
# ========================================

# EXERCICE 1: Vérification d'âge
"""
Créez une fonction qui détermine la catégorie d'âge d'une personne

Règles:
- 0-12 ans : "Enfant"
- 13-17 ans : "Adolescent"
- 18-64 ans : "Adulte"
- 65+ ans : "Senior"

:param age: int - L'âge de la personne
:return: str - La catégorie d'âge
"""
def determiner_categorie_age(age: int) -> str:
    # TODO: Implémentez la logique ici avec if/elif/else
    pass


# EXERCICE 2: Calculateur de notes
"""
Créez une fonction qui convertit une note numérique en lettre

Barème:
- 90-100 : "A"
- 80-89 : "B"
- 70-79 : "C"
- 60-69 : "D"
- 0-59 : "F"

:param note: int - La note numérique (0-100)
:return: str - La note en lettre
"""
def convertir_note_en_lettre(note: int) -> str:
    # TODO: Implémentez la logique ici
    # Pensez à gérer les cas d'erreur (note < 0 ou note > 100)
    pass


# EXERCICE 3: Vérification de mot de passe
"""
Créez une fonction qui vérifie la force d'un mot de passe

Critères pour un mot de passe fort:
- Au moins 8 caractères
- Contient au moins une majuscule
- Contient au moins une minuscule
- Contient au moins un chiffre

:return: "Fort", "Moyen" ou "Faible"
"""
def verifier_mot_de_passe(mot_de_passe: str) -> str:
    # TODO: Implémentez la logique ici
    # Utilisez des conditions et des fonctions comme isupper(), islower(), isdigit()
    pass


# EXERCICE 4: Calculateur de remise
"""
Créez une fonction qui calcule le prix final avec remise

Règles de remise:
- Montant >= 1000€ : 15% de remise
- Montant >= 500€ : 10% de remise
- Montant >= 100€ : 5% de remise
- Montant < 100€ : Pas de remise

Si le client est membre, il a 5% de remise supplémentaire.

:param montant: float - Le montant initial
:param est_membre: bool - True si le client est membre
:return: float - Le prix final après remise (arrondi à 2 décimales)
"""
def calculer_prix_final(montant: float, est_membre: bool) -> float:
    # TODO: Implémentez la logique ici
    pass


# ========================================
# TESTS - Ne pas modifier
# ========================================
if __name__ == "__main__":
    # Test de la fonction determiner_categorie_age
    print("=== Tests Catégorie d'âge ===")
    print(determiner_categorie_age(10))  # "Enfant"
    print(determiner_categorie_age(15))  # "Adolescent"
    print(determiner_categorie_age(25))  # "Adulte"
    print(determiner_categorie_age(70))  # "Senior"

    # Test de la fonction convertir_note_en_lettre
    print("\n=== Tests Notes ===")
    print(convertir_note_en_lettre(95))  # "A"
    print(convertir_note_en_lettre(85))  # "B"
    print(convertir_note_en_lettre(75))  # "C"
    print(convertir_note_en_lettre(65))  # "D"
    print(convertir_note_en_lettre(50))  # "F"

    # Test de la fonction verifier_mot_de_passe
    print("\n=== Tests Mot de passe ===")
    print(verifier_mot_de_passe("MonMotDePasse123"))  # "Fort"
    print(verifier_mot_de_passe("motdepasse"))        # "Faible"
    print(verifier_mot_de_passe("MotDePasse"))        # "Moyen"

    # Test de la fonction calculer_prix_final
    print("\n=== Tests Prix final ===")
    print(calculer_prix_final(1200, False))  # 1020.0
    print(calculer_prix_final(600, True))    # 513.0
    print(calculer_prix_final(80, False))    # 80.0

# ========================================
# CHALLENGE 1 : Variables et Conditions
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


# EXERCICE 5: Frais de port
"""
Calculez les frais de port en fonction du montant et du pays.

Règles (France métropolitaine) :
- Montant < 50 € : 4.99 €
- 50 € <= Montant < 100 € : 2.99 €
- Montant >= 100 € : 0 €
Si la commande est à l'international (hors France), ajoutez +8 € au frais calculés.

:param montant: float - Montant du panier
:param est_france: bool - True si la livraison est en France, False sinon
:return: float - Frais de port (arrondi à 2 décimales)
"""
def calculer_frais_port(montant: float, est_france: bool) -> float:
    # TODO: Implémentez la logique avec if/elif/else
    pass


# EXERCICE 6: Validation simple d'e-mail
"""
Vérifiez rapidement si une adresse e-mail est plausible.

Règles :
- Doit contenir "@" et "."
- "@" ne doit pas être en première ou dernière position
- Retourne "Valide" si les conditions sont remplies,
  sinon "Invalide"

:param email: str
:return: str - "Valide" ou "Invalide"
"""
def valider_email(email: str) -> str:
    # TODO: Utilisez "in" et quelques conditions sur les index
    pass


# EXERCICE 7: Type de triangle
"""
Déterminez le type de triangle à partir des longueurs des côtés.

Règles :
- Si un côté <= 0 : "Invalide"
- Si la somme de deux côtés <= au troisième : "Invalide"
- 3 côtés égaux : "Équilatéral"
- 2 côtés égaux : "Isocèle"
- Sinon : "Scalène"

:param a: float
:param b: float
:param c: float
:return: str - Type de triangle
"""
def type_triangle(a: float, b: float, c: float) -> str:
    # TODO: Validez d'abord l'existence du triangle, puis les cas
    pass


# EXERCICE 8: Catégorisation de température
"""
Retournez une étiquette en fonction d'une température en °C.

Seuils (inclusifs à gauche) :
- temp < 0 : "Gel"
- 0 <= temp < 10 : "Froid"
- 10 <= temp < 20 : "Doux"
- 20 <= temp < 30 : "Chaud"
- temp >= 30 : "Canicule"

:param temp_c: float
:return: str
"""
def etiqueter_temperature(temp_c: float) -> str:
    # TODO: if/elif/else sur les intervalles
    pass


# ========================================
# TESTS - Ne pas modifier
# ========================================
if __name__ == "__main__":
    print("=== Tests Catégorie d'âge ===")
    print(determiner_categorie_age(10))  # "Enfant"
    print(determiner_categorie_age(15))  # "Adolescent"
    print(determiner_categorie_age(25))  # "Adulte"
    print(determiner_categorie_age(70))  # "Senior"

    print("\n=== Tests Notes ===")
    print(convertir_note_en_lettre(95))  # "A"
    print(convertir_note_en_lettre(85))  # "B"
    print(convertir_note_en_lettre(75))  # "C"
    print(convertir_note_en_lettre(65))  # "D"
    print(convertir_note_en_lettre(50))  # "F"

    print("\n=== Tests Mot de passe ===")
    print(verifier_mot_de_passe("MonMotDePasse123"))  # "Fort"
    print(verifier_mot_de_passe("motdepasse"))        # "Faible"
    print(verifier_mot_de_passe("MotDePasse"))        # "Moyen"

    print("\n=== Tests Prix final ===")
    print(calculer_prix_final(1200, False))  # 1020.0
    print(calculer_prix_final(600, True))    # 513.0
    print(calculer_prix_final(80, False))    # 80.0

    print("\n=== Tests Frais de port ===")
    print(calculer_frais_port(30, True))    # 4.99
    print(calculer_frais_port(60, True))    # 2.99
    print(calculer_frais_port(120, True))   # 0.0
    print(calculer_frais_port(120, False))  # 8.0

    print("\n=== Tests Validation e-mail ===")
    print(valider_email("contact@site.fr"))  # "Valide"
    print(valider_email("mail.site.fr"))     # "Invalide"
    print(valider_email("@site.fr"))         # "Invalide"

    print("\n=== Tests Type de triangle ===")
    print(type_triangle(3, 3, 3))    # "Équilatéral"
    print(type_triangle(3, 4, 5))    # "Scalène"
    print(type_triangle(3, 3, 5))    # "Isocèle"
    print(type_triangle(1, 2, 3))    # "Invalide"

    print("\n=== Tests Température ===")
    print(etiqueter_temperature(-5))   # "Gel"
    print(etiqueter_temperature(8))    # "Froid"
    print(etiqueter_temperature(15))   # "Doux"
    print(etiqueter_temperature(25))   # "Chaud"
    print(etiqueter_temperature(35))   # "Canicule"

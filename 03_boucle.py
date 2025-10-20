# ========================================
# CHALLENGE 3: Boucles
# ========================================

# EXERCICE 1: Table de multiplication
"""
Créez une fonction qui génère la table de multiplication d'un nombre

:param nombre: int - Le nombre pour lequel générer la table
:param limite: int - Jusqu'à quelle valeur multiplier (par défaut 10)
:return: str - La table formatée ("5 x 1 = 5\n5 x 2 = 10\n...")
"""
def generer_table_multiplication(nombre: int, limite: int = 10) -> str:
    # TODO: Utilisez une boucle for pour générer la table
    pass


# EXERCICE 2: Nombres premiers
"""
Créez une fonction qui trouve tous les nombres premiers jusqu'à n

Un nombre premier est un nombre > 1 qui n'a que deux diviseurs : 1 et lui-même

:param n: int - La limite supérieure
:return: list[int] - Tous les nombres premiers jusqu'à n
"""
def trouver_nombres_premiers(n: int) -> list[int]:
    # TODO: Utilisez des boucles imbriquées
    pass


# EXERCICE 3: Factorielle
"""
Calculez la factorielle d'un nombre
Exemple: 5! = 5 × 4 × 3 × 2 × 1 = 120

:param n: int
:return: int - La factorielle de n
"""
def calculer_factorielle(n: int) -> int:
    # TODO: Utilisez une boucle for ou while
    pass


# EXERCICE 4: Fibonacci
"""
Générez les n premiers nombres de la suite de Fibonacci
Exemple: 0, 1, 1, 2, 3, 5, 8, 13...

:param n: int
:return: list[int] - Les n premiers nombres de Fibonacci
"""
def generer_fibonacci(n: int) -> list[int]:
    # TODO: Utilisez une boucle
    pass


# EXERCICE 5: FizzBuzz
"""
Implémentez le jeu FizzBuzz

Règles:
- Multiples de 3 : "Fizz"
- Multiples de 5 : "Buzz"
- Multiples de 3 ET 5 : "FizzBuzz"
- Sinon: le nombre

:param limite: int
:return: list[str|int] - Résultats de 1 à limite
"""
def fizz_buzz(limite: int) -> list:
    # TODO: Utilisez une boucle for et des conditions
    pass


# EXERCICE 6: Somme de chiffres
"""
Calculez la somme des chiffres d'un nombre
Exemple: 1234 → 1 + 2 + 3 + 4 = 10

:param nombre: int
:return: int - La somme des chiffres
"""
def somme_chiffres(nombre: int) -> int:
    # TODO: Utilisez str() + boucle for...of ou math avec while
    pass


# EXERCICE 7: Motif d'étoiles
"""
Générez un motif d'étoiles en triangle
Exemple pour hauteur = 5:
*
**
***
****
*****

:param hauteur: int
:return: str - Motif avec retours à la ligne
"""
def generer_triangle_etoiles(hauteur: int) -> str:
    # TODO: Utilisez des boucles imbriquées
    pass


# EXERCICE 8: Vérification de mot de passe
"""
Créez une fonction qui vérifie la force d'un mot de passe

Critères pour un mot de passe fort:
- Au moins 8 caractères
- Contient au moins une majuscule
- Contient au moins une minuscule
- Contient au moins un chiffre

:param mot_de_passe: str - Le mot de passe à vérifier
:return: str - "Fort", "Moyen" ou "Faible"
"""
def verifier_mot_de_passe(mot_de_passe: str) -> str:
    # TODO: Utilisez une boucle for pour parcourir chaque caractère
    # Comptez les majuscules, minuscules et chiffres
    # Retournez "Fort" si tous les critères sont remplis, "Moyen" si partiellement, "Faible" sinon
    pass


# EXERCICE 9: Conversion en emojis
"""
Convertissez une liste de choix en emojis pour l'affichage

:param choix: list[str] - Liste des choix ("rock", "paper", "scissors")
:return: list[str] - Liste des emojis correspondants
"""
def convertir_choix_en_emojis(choix: list[str]) -> list[str]:
    # TODO: Utilisez une boucle for pour parcourir la liste
    # Retournez "🪨" pour rock, "📄" pour paper, "✂️" pour scissors
    pass


# ========================================
# TESTS - Ne pas modifier
# ========================================
if __name__ == "__main__":
    print("=== Tests Table de multiplication ===")
    print(generer_table_multiplication(5, 3))

    print("\n=== Tests Nombres premiers ===")
    print(trouver_nombres_premiers(20))  # [2, 3, 5, 7, 11, 13, 17, 19]

    print("\n=== Tests Factorielle ===")
    print(calculer_factorielle(5))  # 120
    print(calculer_factorielle(0))  # 1

    print("\n=== Tests Fibonacci ===")
    print(generer_fibonacci(8))  # [0, 1, 1, 2, 3, 5, 8, 13]

    print("\n=== Tests FizzBuzz ===")
    print(fizz_buzz(15))

    print("\n=== Tests Somme de chiffres ===")
    print(somme_chiffres(1234))  # 10
    print(somme_chiffres(9876))  # 30

    print("\n=== Tests Triangle d'étoiles ===")
    print(generer_triangle_etoiles(5))

    print("\n=== Tests Vérification mot de passe ===")
    print(verifier_mot_de_passe("MonMotDePasse123"))  # "Fort"
    print(verifier_mot_de_passe("motdepasse"))        # "Faible"
    print(verifier_mot_de_passe("MotDePasse"))        # "Moyen"
    print(verifier_mot_de_passe("12345678"))          # "Moyen"

    print("\n=== Tests Conversion emojis ===")
    print(convertir_choix_en_emojis(["rock", "paper", "scissors"]))  # ["🪨", "📄", "✂️"]
    print(convertir_choix_en_emojis(["rock", "rock", "paper"]))      # ["🪨", "🪨", "📄"]

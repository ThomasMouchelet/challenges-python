# ========================================
# CHALLENGE 5 : Rock-Paper-Scissors (Avancé)
# ========================================

# EXERCICE 1: Logique de base du jeu
"""
Créez une fonction qui détermine le gagnant d'un tour de Rock-Paper-Scissors

Règles:
- Rock bat Scissors (Pierre bat Ciseaux)
- Paper bat Rock (Papier bat Pierre)  
- Scissors bat Paper (Ciseaux bat Papier)
- Égalité si même choix

:param choix_joueur: str - "rock", "paper", ou "scissors"
:param choix_ordi: str - "rock", "paper", ou "scissors"
:return: str - "joueur", "ordi", ou "egalite"
"""
def determiner_gagnant(choix_joueur: str, choix_ordi: str) -> str:
    # TODO: Implémentez la logique avec des conditions if/elif/else
    pass


# EXERCICE 2: Génération du choix de l'ordinateur
"""
Créez une fonction qui génère un choix aléatoire pour l'ordinateur

:return: str - "rock", "paper", ou "scissors"
"""
def generer_choix_ordi() -> str:
    # TODO: Utilisez le module random pour choisir aléatoirement
    # Indice: import random puis random.choice(["rock", "paper", "scissors"])
    pass


# EXERCICE 3: Conversion en emoji
"""
Convertissez les choix en emojis pour l'affichage

:param choix: str - "rock", "paper", ou "scissors"
:return: str - L'emoji correspondant
"""
def choix_vers_emoji(choix: str) -> str:
    # TODO: Retournez "🪨" pour rock, "📄" pour paper, "✂️" pour scissors
    pass


# EXERCICE 4: Historique des parties
"""
Créez une fonction qui ajoute un tour à l'historique

:param historique: list - Liste des tours précédents
:param choix_joueur: str - Choix du joueur
:param choix_ordi: str - Choix de l'ordinateur
:param resultat: str - Résultat du tour
:return: list - Historique mis à jour
"""
def ajouter_tour_historique(historique: list, choix_joueur: str, choix_ordi: str, resultat: str) -> list:
    # TODO: Ajoutez un dictionnaire {"joueur": choix_joueur, "ordi": choix_ordi, "resultat": resultat} à l'historique
    pass


# EXERCICE 5: Statistiques de l'historique
"""
Analysez l'historique pour calculer les statistiques

:param historique: list - Historique des tours
:return: dict - Statistiques {"victoires_joueur": int, "victoires_ordi": int, "egalites": int}
"""
def calculer_statistiques(historique: list) -> dict:
    # TODO: Parcourez l'historique et comptez les victoires de chaque côté
    # Utilisez une boucle for et des conditions
    pass


# EXERCICE 6: Choix préféré du joueur
"""
Trouvez le choix le plus fréquent du joueur dans l'historique

:param historique: list - Historique des tours
:return: str - Le choix le plus fréquent ("rock", "paper", ou "scissors")
"""
def trouver_choix_prefere_joueur(historique: list) -> str:
    # TODO: Comptez les occurrences de chaque choix du joueur
    # Utilisez des boucles et des conditions pour trouver le plus fréquent
    pass


# EXERCICE 7: Stratégie intelligente
"""
Créez une stratégie qui choisit le contre du choix préféré du joueur

:param historique: list - Historique des tours
:return: str - Choix "intelligent" de l'ordinateur
"""
def strategie_intelligente(historique: list) -> str:
    # TODO: 
    # 1. Trouvez le choix préféré du joueur
    # 2. Retournez le contre (rock -> paper, paper -> scissors, scissors -> rock)
    # 3. Si pas d'historique, retournez un choix aléatoire
    pass


# EXERCICE 8: Jeu complet avec historique
"""
Créez une fonction qui gère un jeu complet avec plusieurs tours et historique

:param nb_tours: int - Nombre de tours à jouer
:return: dict - Statistiques finales
"""
def jouer_partie_complete(nb_tours: int) -> dict:
    # TODO:
    # 1. Créez une liste vide pour l'historique
    # 2. Bouclez sur le nombre de tours
    # 3. À chaque tour: demandez le choix, générez le choix ordi, déterminez le gagnant
    # 4. Ajoutez le tour à l'historique
    # 5. Affichez les résultats avec emojis
    # 6. Retournez les statistiques finales
    pass


# ========================================
# TESTS INTERACTIFS - À exécuter pour tester
# ========================================
if __name__ == "__main__":
    print("=== Test de la fonction determiner_gagnant ===")
    print("Test 1: Rock vs Scissors (devrait être 'joueur')")
    resultat1 = determiner_gagnant("rock", "scissors")
    print(f"Résultat: {resultat1}")
    
    print("\nTest 2: Paper vs Rock (devrait être 'joueur')")
    resultat2 = determiner_gagnant("paper", "rock")
    print(f"Résultat: {resultat2}")
    
    print("\nTest 3: Rock vs Rock (devrait être 'egalite')")
    resultat3 = determiner_gagnant("rock", "rock")
    print(f"Résultat: {resultat3}")
    
    print("\n=== Test de l'historique ===")
    historique_test = []
    historique_test = ajouter_tour_historique(historique_test, "rock", "scissors", "joueur")
    historique_test = ajouter_tour_historique(historique_test, "paper", "rock", "joueur")
    historique_test = ajouter_tour_historique(historique_test, "scissors", "paper", "joueur")
    print(f"Historique: {historique_test}")
    
    print("\n=== Test des statistiques ===")
    stats = calculer_statistiques(historique_test)
    print(f"Statistiques: {stats}")
    
    print("\n=== Test du choix préféré ===")
    choix_prefere = trouver_choix_prefere_joueur(historique_test)
    print(f"Choix préféré du joueur: {choix_prefere}")
    
    print("\n=== Test de la stratégie intelligente ===")
    choix_ordi = strategie_intelligente(historique_test)
    print(f"Choix intelligent de l'ordi: {choix_ordi}")
    
    print("\n=== Test du jeu complet ===")
    print("Lancement d'une partie de 3 tours...")
    stats_finales = jouer_partie_complete(3)
    print(f"Statistiques finales: {stats_finales}")
    
    print("\n=== Instructions pour tester manuellement ===")
    print("Pour tester manuellement, exécutez le fichier et suivez les instructions!")
    print("Le jeu vous demandera de choisir entre 'rock', 'paper', ou 'scissors'.")
    print("L'ordinateur utilisera une stratégie intelligente basée sur vos choix précédents!")
# ========================================
# CHALLENGE 4: Tableaux
# ========================================

# EXERCICE 1: Manipulation de base
def analyser_tableau(nombres: list[int]) -> dict:
    """
    Calcule et retourne:
    - longueur
    - somme
    - moyenne
    - minimum
    - maximum
    - premiers3 (les 3 premiers éléments)
    - derniers3 (les 3 derniers éléments)
    """
    # TODO: Votre code ici
    pass


# EXERCICE 2: Filtrage et transformation
def filtrer_et_transformer(nombres: list[int]) -> dict:
    """
    Retourne:
    - pairs: tous les nombres pairs
    - impairs: tous les nombres impairs
    - carres: le carré de chaque nombre
    - positifs: seulement les nombres > 0
    - superieursA10: les nombres > 10
    """
    # TODO: Votre code ici
    pass


# EXERCICE 3: Recherche dans un tableau
def rechercher_dans_tableau(nombres: list[int], cible: int) -> dict:
    """
    Retourne:
    - existe: bool
    - premierePosition: index de la 1ère occurrence ou -1
    - dernierePosition: index de la dernière occurrence ou -1
    - occurrences: nombre d'occurrences de la cible
    - positionsTrouvees: liste des index où la cible apparaît
    """
    # TODO: Votre code ici
    pass


# EXERCICE 4: Tri et classement
def trier_tableau(nombres: list[int]) -> dict:
    """
    Retourne:
    - croissant
    - decroissant
    - parAbsolu (ordre croissant de |x|)
    - original (copie non modifiée)
    """
    # TODO: Votre code ici
    pass


# EXERCICE 5: Opérations sur tableaux multiples
def combiner_tableaux(tableau1: list[int], tableau2: list[int]) -> dict:
    """
    Retourne:
    - concatene: tableau1 + tableau2
    - intersection: éléments de tableau1 présents dans tableau2 (garde l'ordre de tableau1)
    - union: tous les éléments uniques (préserve l'ordre de première apparition)
    - difference: éléments de tableau1 qui ne sont pas dans tableau2
    - communs: éléments en commun SANS doublons (préserve l'ordre de tableau1)
    """
    # TODO: Votre code ici
    pass


# EXERCICE 6: Tableau de mots
def analyser_mots(mots: list[str]) -> dict:
    """
    Retourne:
    - motLePlusLong
    - motLePlusCourt
    - motsCommencantParA (A/a)
    - motsTries (ordre alphabétique)
    - longueurMoyenne (float)
    - motsUniques (suppression des doublons en préservant l'ordre)
    """
    # TODO: Votre code ici
    pass


# EXERCICE 7: Matrice (tableau à 2 dimensions)
def analyser_matrice(matrice: list[list[int]]) -> dict:
    """
    Retourne:
    - sommeTotal
    - sommeLignes
    - sommeColonnes
    - elementMax
    - elementMin
    - transpose
    """
    # TODO: Votre code ici
    pass


# EXERCICE 8: Groupement de données
def grouper_nombres(nombres: list[int]) -> dict:
    """
    Groupe par:
    - parite: {pairs: [...], impairs: [...]}
    - signe: {positifs: [...], negatifs: [...], zero: [...]}
    - magnitude (via valeur absolue): {petits: [<10], moyens: [10-100], grands: [>100]}
    """
    # TODO: Votre code ici
    pass


# ========================================
# TESTS - Ne pas modifier
# ========================================
if __name__ == "__main__":
    print("=== Tests Analyse tableau ===")
    print(analyser_tableau([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print("\n=== Tests Filtrage et transformation ===")
    print(filtrer_et_transformer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print("\n=== Tests Recherche ===")
    print(rechercher_dans_tableau([1, 3, 5, 3, 7, 3, 9], 3))

    print("\n=== Tests Tri ===")
    print(trier_tableau([3, -1, 4, -2, 5, 0]))

    print("\n=== Tests Combinaison ===")
    print(combiner_tableaux([1, 2, 3, 4], [3, 4, 5, 6]))

    print("\n=== Tests Mots ===")
    print(analyser_mots(["bonjour", "au", "revoir", "hello", "aurevoir", "au"]))

    print("\n=== Tests Matrice ===")
    print(analyser_matrice([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]))

    print("\n=== Tests Groupement ===")
    print(grouper_nombres([-50, -10, 0, 5, 15, 150, -200]))

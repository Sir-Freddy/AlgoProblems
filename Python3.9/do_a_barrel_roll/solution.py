# Ecrivez une fonction qui reçoit :
# en premier paramètre un tableau d'entiers
# en second paramètre un entier k
# Votre fonction devra effectuer k rotations vers la gauche du tableau.
# Une rotation correspond au décalage d'un cran vers la gauche de chaque élément du tableau : le second élément devient le premier,
# le troisième devient le second, ..., le premier devient le dernier.


# PROTO : def do_a_barrel_roll(numbers: List[int], k: int) -> List[int]

def do_a_barrel_roll(numbers, k):
    result = [None] * len(numbers)
    for i in range(len(numbers)):
        result[i-k%len(numbers)]=numbers[i]
    return result
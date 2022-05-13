# Ecrivez une fonction qui reçoit :
# en premier paramètre un tableau d'entiers numbers
# en second paramètre un entier k, utilisable comme index dans le tableau
# Votre fonction devra déterminer si le tableau est partitionné et si l'élément à l'index k est un pivot.
# Si c'est le cas, elle devra retourner true. Si ce n'est pas le cas, elle devra retourner false.


# PROTO : def daemon(numbers: List[int], k: int) -> bool

def daemon(numbers, k):
    for i in range(k-1, -1, -1):
        if numbers[i] >= numbers[k]:
            return False
    for i in range(k,len(numbers)):
        if numbers[i] < numbers[k]:
            return False
    return True
# Ecrivez une fonction qui reçoit :
# en premier paramètre un tableau de nombres entiers
# en second paramètre un nombre entier
# Votre fonction devra déterminer si parmi les nombres entiers donnés en premier argument,
# il en existe deux qu'on peut additionner pour obtenir le nombre donné en second argument.
# Si c'est bien le cas, elle devra retourner true. Sinon, elle devra retourner false.


# PROTO :def set_et_match(numbers: List[int], n: int) -> bool

def set_et_match(numbers, n):
    tab = {}
    for value in numbers:
        try:
            tab[n-value]
            return True
        except:
            tab[value] = ''
    return False
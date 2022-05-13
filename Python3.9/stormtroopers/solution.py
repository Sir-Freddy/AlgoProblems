# Ecrivez une fonction qui reçoit en premier paramètre une liste de nombres entiers.
# Votre fonction devra renvoyer une nouvelle liste en ne conservant que les nombres qui figurent une seule fois dans la liste originale.


# PROTO : def stormtroopers(numbers: List[int]) -> List[int]

def stormtroopers(numbers):
    tab = {}
    res = []

    for n in numbers:
        try:
            tab[str(n)] +=1
        except:
            tab[str(n)] = 1

    for key, value in tab.items():
        if value == 1 :
            res.append(int(key))

    return res
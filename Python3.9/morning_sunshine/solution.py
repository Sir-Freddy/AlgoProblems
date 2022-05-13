# Ecrivez une fonction qui reçoit en premier paramètre un tableau d'entiers numbers.
# Votre fonction devra retourner un tableau contenant uniquement les éléments du tableau reçu qui sont strictement supérieurs à tous ceux situés après eux.


# PROTO : def morning_sunshine(numbers: List[int]) -> List[int]

def morning_sunshine(numbers):
    current = -1
    res = []
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] > current:
            current = numbers[i]
            res.append(numbers[i])
    res.reverse()
    return res
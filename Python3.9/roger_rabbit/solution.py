# Ecrivez une fonction qui reçoit en premier paramètre un entier naturel n.
# Votre fonction devra générer les représentations en binaire de tous les nombres compris entre 1 et n inclus.
# Ces représentations doivent être retournées sous forme d'un tableau de chaînes de caractères, dans l'ordre croissant.


# PROTO : def roger_rabbit(n: int) -> List[str]

def roger_rabbit(n):
    res = []
    for i in range(1, n+1):  
        temp = ''
        while(i>0):
            num=i%2
            temp = str(num) + temp
            i=i//2
        res.append(temp)
    return res
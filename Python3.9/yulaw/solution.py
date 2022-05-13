# Ecrivez une fonction qui reçoit en paramètre une chaîne de caractères.
# Votre fonction devra renvoyer une nouvelle chaîne correspondant à celle reçue en paramètre, en unissant chacun des doublons.


# PROTO : def yulaw(s: str) -> str

def yulaw(s):
    tab = {}
    res = []
    for letter in s:
        try:
            tab[letter]
        except:
            tab[letter] = ''
            
    for key, value in tab.items():
        res.append(key)
    
    return ''.join(res)
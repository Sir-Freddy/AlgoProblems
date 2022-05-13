# Ecrivez une fonction qui reçoit en paramètre une chaîne de caractères.
# Si la chaîne contient des doublons, votre fonction devra renvoyer true, si elle n'en contient pas, elle devra renvoyer false.


# PROTO : def playset(s: str) -> bool

def playset(s):
    a = {}
    for letter in s:
        a[letter] = ''
    return (False if len(a) == len(s) else True)
# Ecrivez une fonction qui reçoit en premier paramètre une chaîne de caractères.
# Votre fonction devra déterminer si l'une des permutations possibles de cette chaîne est un palindrome.
# Si c'est le cas, elle devra retourner true. Si ce n'est pas le cas, elle devra retourner false.


# PROTO : def falafel(s: str) -> bool

def falafel(s):
    temp = {}
    for letter in s:
        try :
            del temp[letter]
        except :
            temp[letter] = ''
    if len(s) % 2 == 0 and len(temp) == 0:
        return True
    elif len(s) % 2 == 1 and len(temp) == 1:
        return True
    return False
# Ecrivez une fonction qui reçoit en premier paramètre une chaîne de caractères contenant n'importe quelle 
# combinaison de parenthèses, de crochets ou de guillemets (simples ou doubles).
# Votre fonction devra s'assurer que chaque caractère "ouvrant" de la chaîne possède bien un caractère "fermant" 
# correspondant situé après lui dans la chaîne (et inversement : tout caractère "fermant" doit posséder un caractère "ouvrant" 
# correspondant situé avant lui).
# Si c'est bien le cas, elle devra retourner true. Sinon, elle devra retourner false.


# PROTO : def open_closed(s: str) -> bool

def open_closed(s):
    table = {'"': 0,"'": 0, '(': 0,'[': 0, '{': 0}
    open = {'"': '"',"'": "'",'(': ')','[': ']','{': '}'}
    close = {')': '(',']': '[','}': '{'}

    for letter in s:
        for key, value in table.items():
            if value < 0: return False
        if letter in open:
            table[letter] += 1
        elif letter in close:
            table[close[letter]] -= 1
    
    if table['"'] % 2 == 0 and table["'"] % 2 == 0 and table['('] == 0 and table['['] == 0 and table['{'] == 0 :
        return True
    return False
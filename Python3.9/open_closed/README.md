# 99_problems | xxxxx
Groupe : gillop_f & hadjia_i

## Code
```python
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
```

## Explication
Pour chaque caractère de la chaîne, s'il s'agit d'un caractère ouvrant, on incrémente la valeur du couple associé dans le tableau *table*, et s'il s'agit d'un caractère fermant, on décrémente cette même valeur. 

On vérifie au préalable qu'aucune valeur des couples n'est négative puisque cela indiquerait que la chaine possède un caractère fermant qui n'est pas associé à un caractère ouvrant.

On vérifie que les valeurs des caractères " et ' sont paires (puisqu'ils sont toujours considérés comme des caractères ouvrants) et si toutes les autres valeurs sont égales à 0. Si ces conditions sont respectées, on renvoie True, sinon, on renvoie False

## Complexité :
### Ligne par ligne
1) ``table = {}`` & ``open = {}`` & ``close = {}``<br>-> affectations : O(1) + O(1) + O(1)<br>= O(1)

2) ``for letter in s:``<br>-> boucle for : O(n)<br>

3) ``for key, value in table.items():``<br>-> boucle for : O(m)<br>-> .items() method : O(m)<br>où m = len(table)

4) ``if value < 0: return False``<br>-> comparaison : O(1)<br>-> return : O(1)

5) ``if letter in open: table[letter] += 1``<br>-> in operator : O(k)<br>-> set Item : O(1)<br>où k = len(open)

6) ``elif letter in close: table[close[letter]] -= 1``<br>-> in operator : O(p)<br>-> set Item : O(1)<br>où p = len(close)

7) ``if table['"'] % 2 == 0 and table["'"] % 2 == 0 and table['('] == 0 and table['['] == 0 and table['{'] == 0 :``<br>
->calculs, get Item et comparaisons : O(1)



### Calcul
= O(1) + n * ( O(2m) + O(1) + O(k) + O(p) ) + O(1)<br>
où m, k, p sont des constantes,<br>
= O(2) n * ( O(1) + O(1) + O(1) + O(1) )<br>
= O(2) + O(n)<br>
= O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
# 99_problems | xxxxx
Groupe : gillop_f & hadjia_i

## Code
```python
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
```

## Explication
Pour chaque lettre de la chaine de base, on regarde si la lettre existe dans le dictionnaire temporaire, si oui : on la retire, si non : on l'ajoute. Au final, en regardant le nombre d'élément dans l'objet temp et en prenant en compte si oui ou non la chaine de base est paire, on peut déterminer si cette dernière est un palindrome.

Si la chaine est paire, il suffit que chaque lettre soit présent un nombre pair de fois pour que l'on puisse former un palindrome.
Si la chaine est impaire, il faut que chaque lettre soit présente un nombre pair de fois PLUS que l'une d'elles soit présente un nombre impaire de fois afin de former le 'milieu' du palindrome.

Le tableau temporaire sert à déterminer si une lettre est présente un nombre pair ou impair de fois dans la chaine.

## Complexité
### Ligne par ligne
1) ``temp = {}``<br>-> affectation : O(1)

2) ``for letter in s:``<br>-> boucle for : O(n)

3) ``try : del temp[letter]``<br>-> delete Item : O(1)

4) ``except : temp[letter] = ''``<br>-> set Item : O(1)

5) ``if len(s) % 2 == 0 and len(temp) == 0: return True``<br>-> condition avec comparaisons X2 : O(2)<br>-> modulo : O(1)<br>-> get Length X2 : O(2)<br>-> return : O(1)

OU

5) ``elif len(s) % 2 == 1 and len(temp) == 1: return True``<br>-> condition avec comparaisons X2 : O(2)<br>-> modulo : O(1)<br>-> get Length X2 : O(2)<br>-> return : O(1)

OU

5) ``return False``<br>-> return : O(1)


### Calcul
= O(1) + n * O(1) + ( O(2) + O(1) + O(2) + O(1) )<br>
= O(1) + O(n) + O(6)<br>
= O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
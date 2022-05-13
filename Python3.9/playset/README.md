# 99_problems | xxxxx
Groupe : gillop_f & hadjia_i

## Code
```python
def playset(s):
    a = {}
    for letter in s:
        a[letter] = ''
    return (False if len(a) == len(s) else True)
```

## Explication
Pour chaque lettre de la chaine en paramètre on crée un couple clé valeur dans un dictionnaire.
De cette manière, la chaine 'abc' donnera {'a':'', 'b':'', 'c':''}. L'intéret est que la chaine 'abbcccc' donnera le même objet.

Ainsi, une fois l'objet généré il ne nous reste plus qu'à comparer la longueur de notre dictionnaire avec la longueur de la chaine de base puisque une différence de longueur indique forcément qu'il y avait un doublon et qu'il faut donc renvoyer True.

## Complexité
### Ligne par ligne
1) ``a = {}``<br>-> assignation : `O(1)`<br>

2) ``for letter in s:``<br> -> boucle for : `O(n)`<br>
3) ``a[letter] = ''``<br> -> set Item : O(1)<br>

4) ``return (False if len(a) == len(s) else True)``<br> -> get Length : O(1)<br> -> comparaison : O(1)

### Calcul
= O(1) + n * O(1) + O(1) + O(1)<br>
= O(1) + O(n) + O(1) + O(1)<br>
= O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
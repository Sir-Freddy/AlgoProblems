# 99_problems | yulaw
Groupe : gillop_f & hadjia_i

## Code
```python
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
```

## Explication
Pour chaque lettre du mot de base, on essaye d'accéder à tab à l'index de cette lettre, si cela échoue c'est qu'il faut créer cet index dans le objet.

De cette manière, à la fin de la boucle for, notre objet contiendra autant d'index que de lettres différents dans le mot de base.

Il ne reste donc plus qu'a récupérer ces index et à les implodes en une chaine que l'on renverra.

## Complexité
### Ligne par ligne
1) ``tab = {}`` & ``res = []``<br>-> affectations : O(1) + O(1)<br>= O(1)

2) ``for letter in s:``<br>-> boucle for : O(n)<br>

3) ``try: tab[letter]``<br>-> get Item : O(1)<br>

4) ``except: tab[letter] = ''``<br>-> set Item : O(1)<br>

5) ``for key, value in tab.items(): res.append(key)``<br>-> boucle for : O(m)<br>-> .items() method : O(m)<br>-> append method : O(1)<br>où m = len(tab)<br>

6) ``return ''.join(res)``<br>-> .join() : O(m)<br>-> return : O(1)<br>où m = len(tab)<br>

### Calcul
= O(1) + n * ( O(1) + O(1) ) + (m + m) * O(1) + m + O(1)<br>
= O(m) n * O(2) + O(2m)<br>
= O(3m) + O(n)<br>
= O(n) car 'm' n'est pas un coefficient de 'n'

L'algorithme respecte donc la contrainte de complexité de O(n)
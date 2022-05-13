# 99_problems | set_et_match
Groupe : gillop_f & hadjia_i

## Code
```python
def set_et_match(numbers, n):
    tab = {}
    for value in numbers:
        try:
            tab[n-value]
            return True
        except:
            tab[value] = ''
    return False
```

## Explication
On vérifie pour chaque nombre de numbers si le résultat de n - ce nombre est une clé existante de tab, si c'est le cas, on return True, sinon on créé une clé égale à ce nombre et on passe au nombre suivant.

Cette technique permet de chercher le résultat de la soustraction sans avoir à itérer sur tout notre objet.

## Complexité
### Ligne par ligne
1) ``tab = {}``<br>-> affectation : O(1)<br>

2) ``for value in numbers:``<br>-> boucle for : O(n)<br>

3) ``try: tab[n-value]``<br>-> soustraction : O(1)<br>-> get Item : O(1)<br>

4) ``except: tab[value] = ''``<br>-> set Item : O(1)<br>

5) ``return False`` OU ``return True``<br>-> return : O(1)<br>

### Calcul
= O(1) + n * ( O(1) + O(1) + O(1) ) O(1)<br>
= O(2) n * O(3)<br>
= O(2) + O(n)<br>
= O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
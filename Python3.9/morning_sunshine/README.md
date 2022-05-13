# 99_problems | xxxxx
Groupe : gillop_f & hadjia_i

## Code
```python
def morning_sunshine(numbers):
    current = -1
    res = []
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] > current:
            current = numbers[i]
            res.append(numbers[i])
    res.reverse()
    return res
```

## Explication
On parcours le tableau en partant de la fin et en considérant chaque nombre plus grand que les précédents parcourus comme étant la nouvelle valeur maximum et on l'ajoute à un nouveau tableau de résultat.
De ce fait, sont ajoutées seulement les valeurs pour lesquelles toutes les valeurs suivantes sont strictement inférieurs.

## Complexité :
### Ligne par ligne
1) ``current = -1`` & ``res = []``<br>-> affectations : O(1) + O(1) = O(1)

2) ``for i in range(len(numbers)-1,-1,-1):``<br>-> boucle for : O(n)<br>-> get Length : O(1)

3) ``if numbers[i] > current:``<br>-> get Item : O(1)<br>-> comparaison : O(1)

4) ``current = numbers[i]``<br>-> affectation : O(1)<br>-> get Item : O(1)

5) ``res.append(numbers[i])``<br>-> list.append : O(1)<br>-> get Item : O(1)

6) ``res.reverse()`` & ``return res``<br>-> list.reverse : O(1)<br>-> return : O(1)

### Calcul
= O(1) + O(1) + n * (2 * O(1)^2) + O(n) + O(1)<br>
= 3 * O(1) + O(n) + O(n)<br>
= 2 * O(n)<br>
= O(2n) -> O(n)

O(2n) est considéré comme linéaire et est en terme de complexité égal à 0(n) 
L'algorithme respecte donc la contrainte de complexité de O(n)

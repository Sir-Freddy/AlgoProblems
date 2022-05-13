# 99_problems | stormtroopers
Groupe : gillop_f & hadjia_i

## Code
```python
def stormtroopers(numbers):
    tab = {}
    res = []

    for n in numbers:
        try:
            tab[str(n)] +=1
        except:
            tab[str(n)] = 1

    for key, value in tab.items():
        if value == 1 :
            res.append(int(key))

    return res
```

## Explication
Pour chaque nombre 'n' de *numbers*, on incrément la valeur à l'indice 'n' dans un dictionnaire, et si cet indice n'existe pas, on le créé avec une valeur de 1.

De cette manière, on se retrouve avec un objet comprenant les chiffres de numbers en clés et leur nombre d'apparitions en valeurs.

Il ne restera plus qu'à itérer sur cet objet et n'ajouter que les indices pour lesquels les valeurs sont à 1 dans un tableau de résultat.

## Complexité
### Ligne par ligne
1) ``tab = {}`` & ``res = []``<br>-> affectations : O(1) + O(1)<br>= O(1)

2) ``for n in numbers:``<br>-> boucle for : O(n)<br>

3) ``try: tab[str(n)] +=1``<br>-> calcul : O(1)<br>-> get Item : O(1)<br>-> set Item : O(1)

4) ``except: tab[str(n)] = 1``<br>-> set Item : O(1)

5) ``for key, value in tab.items():``<br>-> boucle for : O(m)<br>-> .items() method : O(m)<br>où m = len(tab)

6) ``if value == 1 : res.append(int(key))``<br>-> comparaison : O(1)<br>-> append method : O(1)<br>-> int() : O(1)

7) ``return res``<br>-> return : O(1)

### Calcul
= O(1) + n * ( O(3) + O(1) ) + m * O(3) + O(1)<br>
= O(2) n * ( O(4) ) + O(m)<br>
= O(n) + O(m)<br>
= O(n) car 'm' n'est pas un coefficient de 'n'

L'algorithme respecte donc la contrainte de complexité de O(n)
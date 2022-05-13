# 99_problems | daemon
Groupe : gillop_f & hadjia_i

## Code
```python
def daemon(numbers, k):
    for i in range(k, -1, -1):
        if numbers[i] > numbers[k]:
            return False
    for i in range(k,len(numbers)):
        if numbers[i] < numbers[k]:
            return False
    return True
```

## Explication
On vérifie d'abord que les chiffres précédants l'index k sont strictement plus petit que `numbers[k]`, si ce n'est pas le cas : Alors il n'est pas un pivot du tableau numbers et la fonction retourne False.

On vérifie ensuite que les chiffres suivants l'index k sont plus grand ou égal que `numbers[k]`, si ce n'est pas le cas : Alors il n'est pas un pivot du tableau numbers et la fonction retourne False.

Enfin, si les deux conditions énoncées ci-dessus sont respectées : Alors le tableau numbers est bien partitionné et le chiffre à l'index k en est effectivement un pivot.

## Complexité
La présence de deux boucles `for` permet d'itérer une seule fois sur chaque élément de la liste.
La complexité de O(n) est alors respectée.
De plus, Il n'y pas d'autres boucles ou d'actions qui viendrait l'augmenter. 
# 99_problems | do_a_barrel_roll
Groupe : gillop_f & hadjia_i

## Code
```python
def do_a_barrel_roll(numbers, k):
    result = [None] * len(numbers)
    for i in range(len(numbers)):
        result[i-k%len(numbers)]=numbers[i]
    return result
```

## Explication
On créé un tableau de même taille que celui entré en paramètre puis, pour chaque nombre du premier tableau, on l'insère dans le deuxième tableau au même index - k modulo la taille du tableau (cette opération permet de simuler le fait que notre décalage puisse passer plusieurs fois sur le tableau tout en restant cohérant dans le cas où l'index k serait plus grand que la longueur du tableau), ce qui créé le décalage voulu.

## Complexité
### Ligne par ligne
1) ``result = [None] * len(numbers)``<br>-> assignation : O(1)<br> -> get Length : O(1)

2) ``for i in range(len(numbers)):``<br> -> boucle for : O(n)<br> -> get Length : O(1)

3) ``result[i-k%len(numbers)]=numbers[i]``<br> -> affectation : O(1)<br> -> calcul : O(1)<br> -> get Length : O(1)<br> -> get Item : O(1)

4) ``return result``<br> -> return : O(1)<br>

### Calcul
= O(1)^2 + O(1) * (n * O(1)^4) + O(1)<br>
= O(1) + O(n) + O(1)<br>
= O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
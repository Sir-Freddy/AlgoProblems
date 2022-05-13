# 99_problems | roger_rabbit
Groupe : gillop_f & hadjia_i

## Code
```python
def roger_rabbit(n):
    res = []
    for i in range(1, n+1):  
        temp = ''
        while(i>0):
            num=i%2
            temp = str(num) + temp
            i=i//2
        res.append(temp)
    return res
```

## Explication
on itère sur tous les chiffres de 1 à n où : pour chaque chiffre x, on boucle x fois afin de constituer une chaine de caractère composé des 0 et des 1 trouvés en calculant un modulo. 
Ensuite on ajoute à un tableau de résultat tout en inversant l'ordre de notre chaîne puisqu'on calcul un binaire de droite et gauche mais on écrit de gauche à droite. 

## Complexités
### Ligne par ligne
1) ``resultat = []``<br>-> affectation : O(1)

2) ``for i in range(1, n+1): ``<br>-> boucle for : O(n)<br>-> addition : O(1)

3) ``temp = ''``<br>-> affectation : O(1)

4) ``while(i>0):``<br>-> boucle while : O(m)

5) ``num=i%2``<br>-> modulo : O(1)<br>-> affectation : O(1)

6) ``temp = str(num) + temp``<br>-> concaténation : O(1)<br> str() function : O(log(k)**2)<br>où k = 1

7) ``i=i//2``<br>-> division : O(1)<br>-> affectation : O(1)

8) ``res.append(temp)``<br>-> append method : O(1)

9) ``return res``<br>-> return : O(1)




### Calcul
= O(1) + n * ( O(1) + O(1) + m * ( O(1) + O(log(k)**2) + O(1) ) + O(1) ) + O(1)<br>
= O(2) + n * ( O(3) + m * ( O(3) ) )<br>
= O(2) + n * ( O(3) + O(m) )
= O(n * m) -> où m correspond au nombre de 0 et de 1 dont sera composé chaque binaire. Puisque un binaire s'écrit toujours de la même manière, on peut simplifier la complexité en écrivant : O(n)

L'algorithme respecte donc la contrainte de complexité de O(n)
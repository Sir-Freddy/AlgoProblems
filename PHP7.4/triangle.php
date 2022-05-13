<?php

// Écrire une fonction dessinant un triangle de hauteur $hauteur avec le caractère '*'.
// Exemple :
//    triangle(3);
//    >>  * 
//    >> ***
//    >>***** 

function triangle($hauteur){
    $nb = 1;
    for($i=1; $i<=$hauteur; $i++){
        for($n=1; $n<=$hauteur - $i; $n++){
            echo " ";
        };
        for($j=1; $j<=$nb; $j++){
            echo "*";
        };
        $nb = $nb + 2;
        echo "\n";
    };
};


?>
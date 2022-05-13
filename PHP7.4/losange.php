<?php

// Écrire une fonction dessinant un losange de hauteur $hauteur avec le caractère '*'.
// Exemple :
//    losange(5);
//    >>  *
//    >> ***
//    >>*****
//    >> ***
//    >>  *

function losange($hauteur){
    if ($hauteur%2==0)
        return false;
    triangle($hauteur/2+0.5);
    $row = $hauteur/2-0.5;
    for($i=1; $i<=$row; $i++){
        for($j=1; $j<=$i; $j++){
            echo " ";
        }
        for($k=1; $k<=$hauteur-2; $k++){
            echo "*";
        }
        $hauteur = $hauteur -2;
        echo "\n";
    }
};


?>
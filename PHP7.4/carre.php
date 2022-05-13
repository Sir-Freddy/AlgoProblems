<?php

// Écrire une fonction dessinant un carré de hauteur $hauteur avec le caractère '*'.
// Exemple :
//    carre(3);
//    >>*** 
//    >>*** 
//    >>*** 

function carre($hauteur){
    for($i=1; $i<=$hauteur; $i++){
        for($n=1; $n<=$hauteur; $n++){
            echo "*";
        };
        echo "\n";
    };
};

?>
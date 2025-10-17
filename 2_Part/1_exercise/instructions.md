# Instructions

1. Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1et  nombre2.

2. nombre1et  nombre2sont des chaînes de caractères (str). Utilisez la méthode isnumeric  (explication de la méthode) pour vérifier que ce sont des nombres.

3. Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot cléraise:raise SystemExit("Fin du programme")

4. Sinon, convertissez les deux nombres en nombres entiers avec la fonction  int.

5. Créez une variableoperationet utilisezinputpour obtenir l'opération souhaitée par l'utilisateur.

6. Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.

7. Effectuez le calcul en fonction de la valeur deoperation(par exemple en utilisant if - elif - else) et stockez le résultat dans la variableresultat.

8. Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour quitter le programme si le deuxième nombre est 0.

9. stuce : lors de la division, utilisez la fonctionroundpour arrondir le résultat et le rendre plus lisible !

10. Affichez le resultat.
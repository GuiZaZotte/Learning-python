nombres = input("Veuillez saisir une liste de nombres séparés par des virgules: ")
liste = nombres.split(",")
liste_entiers=[]
for element in liste:
    nombre_entier=int(element)
    liste_entiers.append(nombre_entier)
print(liste_entiers)
nombre_somme = 0
for nombre in liste_entiers:
     nombre_somme += nombre
print(f"La somme des nombres est de {nombre_somme}.")
nombre_moyenne = nombre_somme
nombre_moyenne = round(nombre_moyenne/2)
print(f"La moyenne des nombres est de {nombre_moyenne}.")
nombre_superieur_moyenne = 0
for nombre in liste_entiers:
     if nombre > nombre_moyenne:
         nombre_superieur_moyenne += 1
print(f"Le nombre de nombres supérieurs à la moyenne est de {nombre_superieur_moyenne}.") 
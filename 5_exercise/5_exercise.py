fruits = {"pomme" : "rouge" ,"banane" : "jaune", "orange" : "orange"}
print(fruits)
fruits['kiwi'] = "vert"
couleur_banane = fruits.get("banane")
print(couleur_banane)
fruits['pomme'] ="vert"
del fruits["orange"]
print(fruits.keys())
print(fruits.values())
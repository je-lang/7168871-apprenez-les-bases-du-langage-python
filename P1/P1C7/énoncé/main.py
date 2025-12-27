# Écrivez votre code ici !
fruits = {"pomme" : "rouge", "banane" : "jaune", "orange" : "orange"}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
fruits.pop("banane")
print(fruits)
print(f"Couleur de la banane : {couleur_banane}")
print(f"Nombre de fruits : {len(fruits)}")

#Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
#Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies effectuées
#pour les forcer à être du bon type (nom sera un str et age un entier) 

#sans la bonne pratique
nom = input("Entrez votre nom : ")
age = input("Entrez votre age : ")
print("Votre nom est", nom, "et vous avez", age, "ans.")

#avec la bonne pratique
nom = str(input("Entrez votre nom : "))
age = int(input("Entrez votre age : "))
print("Votre nom est", nom, "et vous avez", age, "ans.")
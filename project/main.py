import pygame
# Importer la classe AB depuis le fichier AB.py
from AB import AB

# Créer l'arbre vide A1
A1 = AB()
print("A1 est vide :", A1.estVide())

# Créer l'arbre A2 avec une racine de valeur 5
A2 = AB(racine=5)
print("A2 est vide :", A2.estVide())

# Créer l'arbre A3 avec une racine de valeur 3
A3 = AB(racine=3)
print("A3 est vide :", A3.estVide())

# Modifier la partie gauche de A2 pour y placer A3
A2.set_gauche(A3)
print("A2 est vide :", A2.estVide())

# Créer les arbres avec une racine de 3, 8 et 5
arbre3 = AB(racine=3)
arbre8 = AB(racine=8)
arbre5 = AB(racine=5, gauche=arbre3, droite=arbre8)

# Créer l'arbre avec une racine de 12
arbre12 = AB(racine=12)

# Créer l'arbre avec une racine de 10 et les sous-arbres gauche et droit
aTest = AB(racine=10, gauche=arbre5, droite=arbre12)

# print(aTest.taille())

print(aTest.prefixe())
print(aTest.infixe())
print(aTest.postfixe())
print(aTest.hauteur())
print(aTest.estABR())
print(aTest.estEquilibre())

aTestRotation = aTest.rotationDroite() 

# Afficher les valeurs de l'arbre
print(aTestRotation.prefixe())
print(aTestRotation.infixe())
print(aTestRotation.postfixe())

print(True or True)


# decommenter les lignes pour afficher la partie graphique

# # Create the Pygame window
# pygame.init()
# fenetre = pygame.display.set_mode((800, 600))

# aTest.creeArbre(400, 50, 1, 50,fenetre)

# # Keep the window open and update it
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.flip()

# # Quit Pygame when finished
# pygame.quit()









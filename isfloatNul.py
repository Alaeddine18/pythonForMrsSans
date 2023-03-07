#Saisissez un flottant
# S’il est positif ou nul, affichez sa racine, sinon affichez un message d’erreur
import math

x = float(input("Saisissez un flottant : "))

if x >= 0:
    racine = math.sqrt(x)
    print("La racine de", x, "est", racine)
else:
    print("Erreur : le nombre saisi est négatif.")










import pygame

class AB:
    def __init__(self, racine=[None], gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def estVide(self):
        return self.racine == [None]

    def get_racine(self):
        return self.racine

    def set_racine(self, racine):
        self.racine = racine

    def get_gauche(self):
        return self.gauche

    def set_gauche(self, gauche):
        self.gauche = gauche

    def get_droite(self):
        return self.droite

    def set_droite(self, droite):
        self.droite = droite

    # Rajoutez ensuite dans votre classe la méthode taille() qui retourne un entier représentant la taille de l'arbre
    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + (self.gauche.taille() if self.gauche else 0) + (self.droite.taille() if self.droite else 0)

    def prefixe(self):
        result = []
        if self.estVide():
            return result
        else:
            result.append(self.racine) 
             #on range dans une liste et on verifie que les deux cotes de larbre sont abr
            if self.gauche:
                result += self.gauche.prefixe()
            if self.droite:
                result += self.droite.prefixe()
            return result

    def infixe(self):
        result = []
        if self.estVide():
            return result
        else:
            if self.gauche:
                result += self.gauche.infixe()
            result.append(self.racine)
            if self.droite:
                result += self.droite.infixe()
            return result

    def postfixe(self):
        result = []
        if self.estVide():
            return result
        else:
            if self.gauche:
                result += self.gauche.postfixe()
            if self.droite:
                result += self.droite.postfixe()
            result.append(self.racine)
            return result

    def hauteur(self):
        if self.estVide():
            return -1
        else:
            return 1 + max(self.gauche.hauteur() if self.gauche else -1, self.droite.hauteur() if self.droite else -1)

    def estABR(self):
        if self.estVide():
            return True
        else:
            infixe_list = self.infixe()
            return infixe_list == sorted(infixe_list)

    # si elle existe gauche > et si existe droite > que la racine 
    # et ensuite gauche et droite ABR ( recursif )

    # SI SOUS ARBRE ( PAR EXEMPLE 8) EST > 10. SOUCIS SUR CETTE ALGO 


    def estEquilibre(self):
        if self.estVide():
            return True # si vide alors c'est équilibré
        else:
            hauteur_gauche = self.gauche.hauteur() if self.gauche else -1
            hauteur_droite = self.droite.hauteur() if self.droite else -1
            equilibre_gauche = self.gauche.estEquilibre() if self.gauche else True
            equilibre_droite = self.droite.estEquilibre() if self.droite else True
            return abs(hauteur_gauche - hauteur_droite) <= 1 and equilibre_gauche and equilibre_droite # -1 0 ou 1 
            
   
   # C'est pas moi qui l'ai fait mais j'ai essayé 
    def creeArbre(self, x, y, niveau, espace, fenetre):
        if self:
            rayon = 30
            #position X et Y
            self.pos_x = x
            self.pos_y = y
            pygame.draw.circle(fenetre, (255, 255, 255), (x, y), rayon, 0)
            pygame.draw.circle(fenetre, (0, 0, 0), (x, y), rayon, 1)
            font = pygame.font.SysFont("Arial", 16)
            texte = font.render(str(self.racine), True, (0, 0, 0))
            text_rect = texte.get_rect(center=(x, y))
            fenetre.blit(texte, text_rect)
        if self.gauche:
            x_gauche = x - espace * 2 ** (niveau - 1)
            y_gauche = y + 80
            pygame.draw.line(fenetre, (0, 0, 0), (x, y + rayon), (x_gauche, y_gauche - rayon), 1)
            self.gauche.creeArbre(x_gauche, y_gauche, niveau + 1, espace, fenetre)
        if self.droite:
            x_droite = x + espace * 2 ** (niveau - 1) + espace / 2
            y_droite = y + 80
            pygame.draw.line(fenetre, (0, 0, 0), (x, y + rayon), (x_droite, y_droite - rayon), 1)
            self.droite.creeArbre(x_droite, y_droite, niveau + 1, espace,fenetre)


    def rotationDroite(self):
        # Si l'enfant gauche est vide, il n'y a pas de rotation possible, on retourne l'arbre tel quel
        if self.gauche is None:
            return self

        # On crée une nouvelle racine à partir du fils gauche de l'arbre courant
        nouvelle_racine = self.gauche

        # On remplace l'enfant gauche de l'arbre courant par le sous-arbre droit de la nouvelle racine
        self.gauche = nouvelle_racine.droite

        # On place l'arbre courant comme sous-arbre droit de la nouvelle racine
        nouvelle_racine.droite = self

        # On retourne la nouvelle racine qui est maintenant la racine de l'arbre
        return nouvelle_racine
    
    # meme chose que pour le droite mais avec le gauche
    def rotation_gauche(self):
        if self.droite is None:
            return self
        nouvelle_racine = self.droite
        self.droite = nouvelle_racine.gauche
        nouvelle_racine.gauche = self
        return nouvelle_racine

   
    




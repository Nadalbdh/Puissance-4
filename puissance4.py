import sys
import tkinter
import tkinter.messagebox
import pygame
import grille

                        ##### COULEURS #####

arriereplan = (230,230,250)
couleurgrille = (100,149,237)
joueur_1 =  	(233,150,122)
joueur_2 = (102,205,170)

                        ##### VARIABLE GLOBAL DE LA GRILLE #####

grille_global = grille.Grille(6,7)

                        ##### CLASSE GAME #####

class Fenetre:
    # constructeur yekhedh nombre des lignes w colonnes w taille mt3 lmourabba3 li nala3bou fih 
    def __init__(self, taille):
        self.taille = taille
        self.radius = taille // 2 - 5
        self.width = 7 * taille
        self.height = 7 * taille  
        self.offset = taille  
        self.circle_offset = taille // 2 
        self.screen = pygame.display.set_mode((self.width, self.height)) # fonction du module display qui initialise la fenetre 

    def arriere_plan(self):
        for ligne in range(grille_global.nbligne):
            for colonne in range(grille_global.nbcolonne):
                gauche = colonne * self.taille
                top = ligne * self.taille + self.offset
                # fonction taamely rectangle ( carré fl 7ala mte3y) w tekhedh les parametres hekom: screen, couleur, (position horizental w vertical w hight w width)
                pygame.draw.rect(self.screen, couleurgrille, (gauche, top, self.taille, self.taille)) 
                # nafs l7ekya amma cercle
                pygame.draw.circle(self.screen, arriereplan, (gauche + self.circle_offset, top + self.circle_offset), self.radius)
        pygame.display.update()  # fonction taamel update lil window mte3y (tzid les changements li 3amlt'hom tawa)

    def colorer_position(self):
        # fonction permettante de mettre la couleur correspondante au joueur dans la position choisie
        for ligne in range(grille_global.nbligne):
            for colonne in range(grille_global.nbcolonne):
                if grille_global.matrice[ligne, colonne] == 1:
                    couleur_du_joueur_courant = joueur_1
                elif grille_global.matrice[ligne, colonne] == 2:
                    couleur_du_joueur_courant = joueur_2
                else:
                    couleur_du_joueur_courant = arriereplan
                x_position = colonne * self.taille + self.circle_offset
                y_position = self.height - (ligne * self.taille + self.circle_offset)  
                pygame.draw.circle(self.screen, couleur_du_joueur_courant, (x_position, y_position), self.radius)
        pygame.display.update()

    def track_mouse_motion(self, x_position, couleur_du_joueur_courant):
        # fonction tkhalli la piece tabba3 souris 
        pygame.draw.rect(self.screen, arriereplan, (0, 0, self.width, self.taille)) 
        pygame.draw.circle(self.screen, couleur_du_joueur_courant, (x_position, self.circle_offset), self.radius)
        pygame.display.update()

    def mettre_piece(self, x_position, tour):
        # focntion qui permet de verifier la validité de colonne et ligne et joueur le tour si valide
        colonne = x_position // self.taille
        if grille_global.position_valide(colonne):
            row = grille_global.position_valable_suiv(colonne)
            grille_global.mettre_piece(row, colonne, tour)
            return True
        return False

    def rebelote(self):
        #nouvelle partie
        self.screen = pygame.display.set_mode((self.width, self.height))
        grille_global.rebelote()
        self.arriere_plan()
        self.colorer_position()


def popup_result(gagnant = 0):
    title = 'Game Over!'
    if gagnant != 1:
        message = f'Le joueur {gagnant} a gagné ! Souhaitez-vous recommencer ?'
    else:
        message = 'Le match était un match nul. Souhaitez-vous recommencer ?'
    return tkinter.messagebox.askyesno(title=title, message=message) # prompt box retournant des valeurs booleenes 

def main():
    pygame.init()
    pygame.display.set_caption('Puissance 4')
    fenetre = Fenetre(90)
    fenetre.arriere_plan()
    continuer = True
    tour = 1
    couleur_du_joueur_courant = joueur_1

    while continuer:
        for event in pygame.event.get(): # liste des evenements dans la file 

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEMOTION:
                fenetre.track_mouse_motion(event.pos[0], couleur_du_joueur_courant)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fenetre.mettre_piece(event.pos[0], tour): # pos est un couple x,y referençant la position du curseur
                    fenetre.colorer_position()
                    if grille_global.gagner(tour): 
                        continuer = popup_result(tour)
                        grille_global.rebelote()
                    elif grille_global.pleine():  
                        continuer = popup_result()
                        grille_global.rebelote()
                    else:  
                        if tour == 1:
                            tour = 2
                        else:
                            tour = 1

                        if tour == 1:
                            couleur_du_joueur_courant = joueur_1
                        else: 
                            couleur_du_joueur_courant = joueur_2

                        fenetre.track_mouse_motion(event.pos[0], couleur_du_joueur_courant) 


if __name__ == "__main__":
    main()
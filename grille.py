import numpy as np

        ##### CLASSE GRILLE ####
class Grille:
    def __init__(self, nbligne, nbcolonne):
        self.nbligne = nbligne
        self.nbcolonne = nbcolonne
        self.matrice = np.zeros((nbligne, nbcolonne))

    def position_valide(self, column):
        return self.matrice[self.nbligne - 1, column] == 0

    def position_valable_suiv(self, column):
        for row in range(self.nbligne):
            if self.matrice[row, column] == 0:
                return row

    def mettre_piece(self, row, column, tour):
        self.matrice[row, column] = tour

    def gagner(self, tour):
        for r in range(self.nbligne):
            for c in range(self.nbcolonne - 3):
                if self.matrice[r, c] == tour and self.matrice[r, c + 1] == tour and self.matrice[r, c + 2] == tour and self.matrice[r, c + 3] == tour:
                    return True

        for r in range(self.nbligne - 3):
            for c in range(self.nbcolonne):
                if self.matrice[r, c] == tour and self.matrice[r + 1, c] == tour and self.matrice[r + 2, c] == tour and self.matrice[r + 3, c] == tour:
                    return True

        for r in range(self.nbligne - 3):
            for c in range(self.nbcolonne - 3):
                if self.matrice[r, c] == tour and self.matrice[r + 1, c + 1] == tour and self.matrice[r + 2, c + 2] == tour and self.matrice[r + 3, c + 3] == tour:
                    return True

        for r in range(3, self.nbligne):
            for c in range(self.nbcolonne - 3):
                if self.matrice[r, c] == tour and self.matrice[r - 1, c + 1] == tour and self.matrice[r - 2, c + 2] == tour and self.matrice[r - 3, c + 3] == tour:
                    return True

        return False

    def pleine(self):
        return self.matrice.all()

    def rebelote(self):
        self.matrice = np.zeros((self.nbligne, self.nbcolonne))

    def print_matrice(self):
        print(np.flip(self.matrice, 0))
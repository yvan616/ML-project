import numpy as np

class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} démarre.")
    def arreter(self):
        print(f"La voiture {self.marque} {self.modele} s'arrête.")


matr = np.arange(12).reshape(3, 4) 
M = matr[:,-1]
M = np.zeros((3,))

print(M)
print(matr)
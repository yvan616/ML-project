class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
    def demarrer(self):
        print(f"La voiture {self.marque} {self.modele} démarre.")
    def arreter(self):
        print(f"La voiture {self.marque} {self.modele} s'arrête.")


ma_voiture = Voiture("Toyota", "Corolla", 2020)
ma_voiture.demarrer()
ma_voiture.arreter()
"""
Projection() c'est la classe qui décrit un évèenement qui soit une projection
"""
from Models.evenement import Evenement

class Projection(Evenement):
    def __init__(self, id, nom, description, date_debut, date_fin, salle, color, contexte, presentationAuteur=None, debat=None, amuses_bouches=False):
        super().__init__(id, nom, description, date_debut, date_fin, salle, color, est_projection=True)
        self.contexte = contexte
        self.presentationAuteur = presentationAuteur
        self.debat = debat
        self.amuses_bouches=amuses_bouches

    def __str__(self):
        return super().__str__() + " [projection]"
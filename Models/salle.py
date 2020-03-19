"""
Ce module contient la classe de la salle de projection (SalleProjection)
"""

class SalleProjection:
    def __init__(self, adresse=None, nbrPlaceTotal=None, typeProjection=None, responsable=None):
        self.adresse = adresse
        self.nbrPlaceTotal = nbrPlaceTotal
        self.typeProjection = typeProjection
        self.reponsable = responsable
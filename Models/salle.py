"""
Ce module contient la classe de la salle (Salle)
"""

class Salle:
    def __init__(self, 
                 id, 
                 adresse, 
                 responsable, 
                 nbr_place_standard,
                 nbr_place_premium):
        self.id = id
        self.adresse = adresse
        self.responsable = responsable
        self.nbr_place_standard = nbr_place_standard
        self.nbr_place_premium = nbr_place_premium

    def __str__(self):
        return "Salle %04d" % self.id
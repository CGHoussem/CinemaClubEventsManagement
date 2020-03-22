"""
Ce module contient la classe de la salle (Salle)
"""

class Salle:
    def __init__(self, id, adresse, responsable, nbrPlaceTotal):
        self.__id = id
        self.__adresse = adresse
        self.__nbrPlaceTotal = nbrPlaceTotal
        self.__responsable = responsable

    @property
    def id(self):
        return self.__id

    @property
    def adresse(self):
        return self.__adresse

    @property
    def nombre_places_total(self):
        return self.__nbrPlaceTotal
    
    @property
    def responsable(self):
        return self.__responsable

    def __str__(self):
        return "Salle %d (%s)" % (self.__id, self.__adresse)
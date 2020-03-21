"""
Ce module contient la classe de la salle (Salle)
"""

class Salle:
    def __init__(self, id, adresse, responsable, nbrPlaceTotal):
        self.__id = id
        self.__adresse = adresse
        self.__nbrPlaceTotal = nbrPlaceTotal
        self.__reponsable = responsable

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return "Salle %d (%s)" % (self.__id, self.__adresse)
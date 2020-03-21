from Models.utilisateur import Metier

class Debat:
    def __init__(self, id, animateur, duree, notes):
        self.__id = id
        self.animateur = animateur
        self.duree = duree
        self.notes = notes

    @property
    def id(self):
        return self.__id

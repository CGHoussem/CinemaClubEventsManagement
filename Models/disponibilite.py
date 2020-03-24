from enum import Enum
from PyQt5.QtCore import QDateTime

class Statut(Enum):
    DISPONIBLE = 0
    CONGE = 1
    MALADIE = 2
    AUTRE = 3

class Disponibilite:
    def __init__(self, id_user, statut, notes, date_debut, date_fin):
        super().__init__()
        self.__id_user = id_user
        self.__statut = Statut.DISPONIBLE
        if statut == 1:
            self.__statut = Statut.CONGE
        elif statut == 2:
            self.__statut = Statut.MALADIE
        elif statut == 3:
            self.__statut = Statut.AUTRE
        self.__notes = notes
        self.__date_debut = date_debut
        self.__date_fin = date_fin

    @property
    def id_user(self):
        return self.__id_user

    @property
    def statut(self):
        return self.__statut

    @property
    def notes(self):
        return self.__notes

    @property
    def date_debut(self):
        return self.__date_debut

    @property
    def date_fin(self):
        return self.__date_fin
    
    def __str__(self):
        if self.__statut == Statut.DISPONIBLE:
            return "Disponible".upper()
        elif self.__statut == Statut.CONGE:
            return "En congé".upper()
        elif self.__statut == Statut.MALADIE:
            return "Maladie".upper()
        else:
            return "Autre".upper()
            
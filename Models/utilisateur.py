from enum import Enum

class Metier(Enum):
    MEMBRE_MAIRIE = 1
    MEMBRE_CLUB = 2
    REPONSABLE_SALLE = 3
    ARTISTE = 4
    CRITIQUE = 5
    TECHNICIEN = 6
    AUTRE = 7


class Utilisateur:
    def __init__(self, id, email, mdp, nom, prenom, adresse, metier, est_admin=False):
        super().__init__()
        self.__id = id
        self.__email = email
        self.__motdepasse = mdp
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        self.__metier = Metier.MEMBRE_MAIRIE
        if metier == "Metier.MEMBRE_CLUB":
            self.__metier = Metier.MEMBRE_CLUB
        elif metier == "Metier.REPONSABLE_SALLE":
            self.__metier = Metier.REPONSABLE_SALLE    
        elif metier == "Metier.ARTISTE":
            self.__metier = Metier.ARTISTE
        elif metier == "Metier.CRITIQUE":
            self.__metier = Metier.CRITIQUE
        elif metier == "Metier.TECHNICIEN":
            self.__metier = Metier.TECHNICIEN
        self.__est_admin = est_admin

    @property
    def id(self):
        return self.__id

    @property
    def metier(self):
        return self.__metier
    
    @property
    def nom(self):
        return self.__nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    def __str__(self):
        return self.__nom.upper() + " " + self.__prenom
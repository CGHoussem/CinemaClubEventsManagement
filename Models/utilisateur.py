from enum import Enum

class Metier(Enum):
    MEMBRE_MAIRIE = 1
    MEMBRE_CLUB = 2
    ARTISTE = 3
    CRITIQUE = 4
    TECHNICIEN = 5


class Utilisateur:
    def __init__(self, *args, est_admin=False):
        super().__init__()
        self.__email = args['email']
        self.__motdepasse = args['motdepasse']
        self.__nom = args['nom']
        self.__prenom = args['prenom']
        self.__adresse = args['adresse']
        self.__metier = args['metier']
        self.__est_admin = est_admin

    @property
    def metier(self):
        return self.metier
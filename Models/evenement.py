from Models.utilisateur import Metier
from PyQt5.QtGui import QColor

class Evenement:
    def __init__(self, id, nom, description, date_debut, date_fin, salle, color, est_projection=False):
        self.__id = id
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsables = []
        self.salle = salle
        self.color = color
        self.est_projection = est_projection

    @property
    def id(self):
        return self.__id

    def ajouterResponsable(self, membre):
        """
        Cette fonction permet d'ajouter un membre responsable de l'évèvenement

            Parameters:
                membre (Membre): Le membre à ajouter
        """
        if membre.metier in [Metier.MEMBRE_MAIRIE, Metier.MEMBRE_CLUB]:
            self.responsables.append(membre)
        else:
            raise TypeError("Il faut que le responsable a ajouté soit un membre de la mairie ou le club")

    def __str__(self):
        return "%s - %s" % (self.nom, self.description)
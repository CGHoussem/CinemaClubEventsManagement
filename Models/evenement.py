from Models.utilisateur import Metier
from PyQt5.QtGui import QColor

from enum import Enum

class Etat(Enum):
    EN_ATTENTE = 0
    EN_COURS = 1
    TERMINE = 2

class Evenement:
    def __init__(self, id, nom, description, date_debut, date_fin, salle, color, est_projection=False, etat=Etat.EN_ATTENTE, salle_reservee=False, disponibilite_invites=False):
        self.id = id
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.responsables = []
        self.salle = salle
        self.color = color
        self.est_projection = est_projection
        self.etat = etat
        self.salle_reservee = salle_reservee
        self.disponibilite_invites = disponibilite_invites
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
        etat = "En attente"
        if self.etat == Etat.EN_COURS:
            etat = "En cours"
        elif self.etat == Etat.TERMINE:
            etat = "Termine"
        return "%s (%s)" % (self.nom, etat.upper())
from Models.utilisateur import Metier
from PyQt5.QtGui import QColor

class Evenement:
        
    def __init__(self, nom, description, date_debut, date_fin, salle, color, est_projection):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.membres = []
        self.salle = salle
        self.color = color
        self.est_projection = est_projection

    def ajouterMembre(self, membre):
        """
        Cette fonction permet d'ajouter un membre

            Parameters:
                membre (Membre): Le membre que vous voulez ajouter
        """
        if membre.metier == Metier.MEMBRE_MAIRIE:
            self.membres.append(membre)
        else:
            raise TypeError("Il faut que le membre a ajouté soit un membre de la mairie")

    def __str__(self):
        return "%s - %s" % (self.nom, self.description)

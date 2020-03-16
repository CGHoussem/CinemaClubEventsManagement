class Personne:
    def __init__(self, nom, prenom, adresse, email, tel):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.tel = tel

class MembreClub(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class MembreMairie(Personne):
    def __init__(self, nom, prenom, adresse, email, tel, mairie):
        super().__init__(nom, prenom, adresse, email, tel)
        self.mairie = mairie

class Artiste(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class Critique(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class Technicien(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class SalleProjection:
    def __init__(self, adresse=None, nbrPlaceTotal=None, typeProjection=None, responsable=None):
        self.adresse = adresse
        self.nbrPlaceTotal = nbrPlaceTotal
        self.typeProjection = typeProjection
        self.reponsable = responsable

class Evenement:
    def __init__(self, date_debut=None, date_fin=None, membres=list(), description=None):
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.membres = membres
        self.description = description

    def ajouterMembre(self, membre):
        """
            Cette fonction permettera d'ajouter un membre

            Parameters:
                membre (Membre): Le membre que vous voulez ajouter
        """
        if type(membre) in [MembreMairie]:
            self.membres.append(membre)
        else:
            raise TypeError("L'argument donné n'est pas de type artiste, critique, technicien ou un membre du club associatif!")

class Projection(Evenement):
    def __init__(self, date_debut=None, date_fin=None, membres=None, description=None, presentationAuteur=None, contexte=None, debat=None):
        super().__init__(date_debut, date_fin, membres, description)
        self.presentationAuteur = presentationAuteur
        self.contexte = contexte
        self.debat = debat

class PresentationAuteur:
    def __init__(self, auteur=None, duree=None):
        self.auteur = auteur
        self.duree = duree

class Debat:
    def __init__(self, animateur=None, duree=None):
        self.animateur = animateur
        self.duree = duree

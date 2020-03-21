
class Projection(Evenement):
    def __init__(self, date_debut=None, date_fin=None, membres=None, description=None, presentationAuteur=None, contexte=None, debat=None):
        super().__init__(date_debut, date_fin, membres, description)
        self.presentationAuteur = presentationAuteur
        self.contexte = contexte
        self.debat = debat
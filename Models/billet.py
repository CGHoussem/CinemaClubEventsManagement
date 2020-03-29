
class Place:
    def __init__(self, num, type_place):
        self.num = num
        self.type_place = type_place

class Billet:
    def __init__(self, id, event, place, nom, prenom, tel):
        self.id = id
        self.event = event
        self.place = place
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
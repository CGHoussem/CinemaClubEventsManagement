"""
Ce module contient la classe de la salle (Salle)
"""

class Salle:
    def __init__(self, id, adresse, responsable, nbrPlaceTotal):
        self.__id = id
        self.__adresse = adresse
        self.__nbrPlaceTotal = nbrPlaceTotal
        self.__responsable = responsable

    @property
    def id(self):
        return self.__id

    @property
    def adresse(self):
        return self.__adresse

    @property
    def nombre_places_total(self):
        return self.__nbrPlaceTotal
    
    @property
    def responsable(self):
        return self.__responsable

    def est_reserver(self, datetime_debut, datetime_fin):
        from DAO.DAOs import SalleReservationDAO
        
        if self.__id == None:
            return False
        
        reserver = False
        temp = SalleReservationDAO.get_by_salle(self)
        for r in temp:
            if datetime_debut >= r.debut_datetime or datetime_debut <= r.fin_datetime or \
                datetime_fin >= r.debut_datetime or datetime_fin <= r.fin_datetime:
                reserver = True
                break
        return reserver

    def __str__(self):
        return "Salle %d (%s)" % (self.__id, self.__adresse)
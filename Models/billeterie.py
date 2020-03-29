
class Billeterie:
    def __init__(self, 
                 event, 
                 billets = [], 
                 nbr_place_standard_disponible=0, 
                 nbr_place_premium_disponible=0, 
                 nbr_place_reservee=0, 
                 prix_place_standard=10, 
                 prix_place_premium=15):
        self.event = event
        self.billets = billets
        self.nbr_place_standard_disponible = nbr_place_standard_disponible
        self.nbr_place_premium_disponible = nbr_place_premium_disponible
        self.nbr_place_reservee = nbr_place_reservee
        self.prix_place_standard = prix_place_standard
        self.prix_place_premium = prix_place_premium
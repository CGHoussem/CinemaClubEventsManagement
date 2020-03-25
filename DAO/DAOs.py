r"""
Ce module permet de gérer les tables dans la base de donnée appropriés à les models

La liste des DAO:
    - UtilisateurDAO
    - EvenementDAO
    - SalleDAO
"""

import sqlite3

from db import DBConnexion
from Models.disponibilite import Disponibilite
from Models.utilisateur import Utilisateur, Metier
from Models.evenement import Evenement, Etat
from Models.salle import Salle
from Models.reservation_salle import ReservationSalle

from PyQt5.QtCore import QDate, QDateTime, QTime, QTimeZone

def format_date(datetime):
    return "%02d/%02d/%d %02d:%02d" % (datetime.date().day(), datetime.date().month(), datetime.date().year(), datetime.time().hour(), datetime.time().minute())

def data_to_datetime(data):
    if data == None:
        return None
    date_fin = QDate(int(data[6:10]), int(data[3:5]), int(data[:2]))
    time_fin = QTime(int(data[11:13]), int(data[15:17]))
    return QDateTime(date_fin, time_fin)

class DisponibiliteDAO:
    @staticmethod
    def get_by_user_id(user_id):
        """
        Cette fonction permet de renvoyer la disponbilité de l'utilsateur 'user_id'
        
            Parameters:
                user_id: L'identifiant de l'utilisateur
            Return:
                Un objet de type Disponibilite()
        """
        dispo = None
        if user_id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `USER_DISPONIBILITE` WHERE `ID_USER` = ?"
            cursor.execute(query, [user_id])

            dispo_data = cursor.fetchone()
            if dispo_data != None:
                date_debut = QDateTime(QDateTime.currentDateTime())
                dispo = Disponibilite(user_id, dispo_data[1], dispo_data[2], format_date(date_debut), data_to_datetime(dispo_data[4]))
            conn.close()
        return dispo

class UtilisateurDAO:
   
    @staticmethod
    def get_all():
        """
        Cette fonction permet de renvoyer une liste des utilisateurs
        
            Return:
                Une liste de Utilisateur()
        """
        liste = []
        conn = DBConnexion().Instance
        cursor = conn.cursor()
        query = "SELECT * FROM `USER`"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            user_id = int(row[0]) 
            dispo = DisponibiliteDAO.get_by_user_id(user_id)
            u = Utilisateur(user_id, row[1], row[2], row[3], row[4], row[5], row[6], dispo, int(row[8])==1)
            liste.append(u)
        
        conn.close()
        return liste

    @staticmethod
    def get_by_id(id):
        """
        Cette fonction permet de renvoyer l'utilisateur d'identifiant 'id'
        
            Parameters:
                id: l'identifiant de l'utilisateur voulu
            Return:
                Un objet de type Utilisateur()
        """
        user = None
        if id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `USER` WHERE `ID` = ?"
            cursor.execute(query, [id])
            
            user_data = cursor.fetchone()
            user = Utilisateur(id, user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], int(user_data[7]), int(user_data[8])==1)
            conn.close()
        return user
    
    @staticmethod
    def get_all_admins():
        """
        Cette fonction permet de renvoyer une liste des utilisateurs ayant status ADMIN
        
            Return:
                Une liste d'objets de type Utilisateur()
        """
        liste = []
        conn = DBConnexion().Instance
        cursor = conn.cursor()
        query = "SELECT * FROM `USER` WHERE `EST_ADMIN`=1"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            u = Utilisateur(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], int(row[7]), True)
            liste.append(u)
        
        conn.close()
        return liste

class EvenementDAO:
       
    @staticmethod
    def get_all():
        """
        Cette fonction permet d'obtenir tout les évènements dans la base de donnée 
        
            Return:
                Liste de Evenement()
        """
        liste = []
        conn = DBConnexion().Instance
        cursor = conn.cursor()
        query = "SELECT * FROM `EVENT`"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            # Récuperer la salle
            salle_id = int(row[5])
            salle = SalleDAO.get_by_id(salle_id)
            etat = Etat.EN_ATTENTE
            if row[8] == 1:
                etat = Etat.EN_COURS
            elif row[8] == 2:
                etat = Etat.FINI
            e = Evenement(int(row[0]), row[1], row[2], data_to_datetime(row[3]), data_to_datetime(row[4]), salle, row[6], row[7], etat)
            # Récuperer la liste des responsables
            query = "SELECT `ID_USER` FROM `EVENT_RESPONSABLE` WHERE `ID_EVENT`=?"
            cursor.execute(query, [int(row[0])])
            
            rows_event_responsable = cursor.fetchall()
            for row_event_responsable in rows_event_responsable:
                id_user = int(row_event_responsable[0])
                # Récuperer le responsable ayant comme id 'id_user'
                responsable = UtilisateurDAO.get_by_id(id_user)
                e.ajouterResponsable(responsable)
            
            liste.append(e)
        
        conn.close()
        return liste

    @staticmethod
    def add_event(new_event):
        """
        Cette fonction permet d'ajouter un évènement dans la base de donnée 
        
            Parameters:
                new_event: L'évènement a ajouté
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()

            # Ajouter l'évènement
            print("Attempt add event")
            query_add_event = "INSERT INTO `EVENT` VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, 0)"
            cursor.execute(query_add_event, (new_event.nom, 
                                             new_event.description, 
                                             format_date(new_event.date_debut), 
                                             format_date(new_event.date_fin), 
                                             new_event.salle.id, 
                                             new_event.color.name(), 
                                             int(new_event.est_projection)))
            event_id = cursor.lastrowid
            
            # Ajouter les responsables
            query_add_responsable = "INSERT INTO `EVENT_RESPONSABLE` VALUES (?, ?)"
            responsables_data = []
            for r in new_event.responsables:
                # Ajouter la liaison du responsable avec l'évèenement à la base de donnée 
                responsables_data.append((event_id, r.id))
            print("Attempt add responsables")
            cursor.executemany(query_add_responsable, responsables_data)
            
            # Si l'évènement est une projection alors ajouter la projection à la base de donéee
            if new_event.est_projection:
                debat_id = None
                if new_event.debat != None:
                    # Ajouter le débat
                    ## Ajouter un animateur à la base de donnée
                    query_add_animateur = "INSERT INTO `USER` VALUES (NULL, ?, NULL, ?, ?, ?, ?, 0)"
                    cursor.execute(query_add_animateur, (new_event.debat.animateur.email, new_event.debat.animateur.nom, new_event.debat.animateur.prenom, new_event.debat.animateur.adresse, new_event.debat.animateur.metier))
                    
                    ## Récupérer son ID
                    animateur_id = cursor.lastrowid
                    
                    ## Ajoute le débat à la base de donnée
                    query_add_debat = "INSERT INTO `DEBAT` VALUES (NULL, ?, ?, ?)"
                    cursor.execute(query_add_debat, (animateur_id, new_event.debat.duree, new_event.debat.notes))
                    
                    ## Récupérer son ID
                    debat_id = cursor.lastrowid
                
                # Ajouter la projection
                query_add_projection = "INSERT INTO `PROJECTION` VALUES (NULL, ?, ?, ?, ?, ?)"
                auteur = None
                duree = None
                if new_event.presentationAuteur != None:
                    auteur = new_event.presentationAuteur.auteur
                if new_event.presentationAuteur != None:
                    duree = new_event.presentationAuteur.duree
                cursor.execute(query_add_projection, (event_id, auteur, duree, new_event.contexte, debat_id))

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error:", str(e))

    @staticmethod
    def update_state(event):
        """
        Cette fonction permet de mettre à jour l'etat un evenement
        
            Parameters:
                event: L'évènement à MAJ
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "UPDATE `EVENT` SET `ETAT` = ? WHERE `ID` = ?"
            etat = 0
            if event.etat == Etat.EN_COURS:
                etat = 1
            elif event.etat == Etat.TERMINE:
                etat = 2
            cursor.execute(query, (etat, event.id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error ", e)

class SalleDAO:
       
    @staticmethod
    def get_all():
        """
        Cette fonction permet de renvoyer une liste de toutes les salles
        
            Return:
                Une liste de Salle()
        """
        liste = []
        conn = DBConnexion().Instance
        cursor = conn.cursor()
        query = "SELECT * FROM `SALLE`"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            responsable_id = int(row[2])
            responsable = UtilisateurDAO.get_by_id(responsable_id)
            s = Salle(int(row[0]), row[1], responsable, int(row[3]))
            liste.append(s)
        
        conn.close()
        return liste

    @staticmethod
    def get_by_id(id):
        """
        Cette fonction permet de renvoyer la salle d'identifiant 'id'
        
            Parameters:
                id: L'identifiant de la salle
            Return:
                Un objet de type Salle()
        """
        salle = None
        if id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `SALLE` WHERE `ID` = ?"
            cursor.execute(query, [id])
            
            salle_data = cursor.fetchone()
            responsable_id = int(salle_data[2])
            responsable = UtilisateurDAO.get_by_id(responsable_id)
            salle = Salle(id, salle_data[1], responsable, int(salle_data[3]))
            
            conn.close()
        return salle

class SalleReservationDAO:
    
    @staticmethod
    def get_by_event(event):
        """
        Cette fonction permet de renvoyer la reservation de la salle de l'évènement 'event'
        
            Parameters:
                event: L'évènement
            Return:
                Un objet de type ReservationSalle()
        """
        reservation = None
        if event != None and event.id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `RESERVATION_SALLE` WHERE `EVENT_ID` = ?"
            cursor.execute(query, [event.id])
            
            reservation_data = cursor.fetchone()
            if reservation_data != None:
                reservation_id = int(reservation_data[0])
                salle = SalleDAO.get_by_id(int(reservation_data[2]))
                debut_datetime = data_to_datetime(reservation_data[3])
                fin_datetime = data_to_datetime(reservation_data[4])
                reservation = ReservationSalle(reservation_id, event, salle, debut_datetime, fin_datetime)
                
            conn.close()
        return reservation

    @staticmethod
    def get_by_salle(salle):
        """
        Cette fonction permet de renvoyer la reservation de la salle 'salle'
        
            Parameters:
                salle: La salle
            Return:
                Un objet de type ReservationSalle()
        """
        reservations = []
        if salle.id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `RESERVATION_SALLE` WHERE `SALLE_ID` = ?"
            cursor.execute(query, [salle.id])
            
            reservation_datas = cursor.fetchall()
            for reservation_data in reservation_datas:
                reservation_id = int(reservation_data[0])
                debut_datetime = data_to_datetime(reservation_data[3])
                fin_datetime = data_to_datetime(reservation_data[4])
                reservation = ReservationSalle(reservation_id, None, salle, debut_datetime, fin_datetime)
                reservations.append(reservation)
                
            conn.close()
        return reservations
    
    @staticmethod
    def est_event_salle_reserve(event):
        """
        Cette fonction permet de renvoyer si la salle de l'évènement est réserver ou pas
        
            Parameters:
                event: L'évènement
            Return:
                une valeur booléene
        """
        est_resever = False
        if event != None and event.id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `RESERVATION_SALLE` WHERE `EVENT_ID` = ?"
            cursor.execute(query, [event.id])
            
            existe = cursor.fetchone()
            est_reserver = (existe != None)
                
            conn.close()
        return est_reserver
    
    @staticmethod
    def add_reservation(reservation):
        """
        Cette fonction permet d'ajouter une réservation d'une salle dans la base de donnée 
        
            Parameters:
                reservation: La réservation a ajoutée
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()

            # Ajouter l'évènement
            query_add_event = "INSERT INTO `RESERVATION_SALLE` VALUES (NULL, ?, ?, ?, ?)"
            cursor.execute(query_add_event, (reservation.event.id,
                                             reservation.salle.id,
                                             format_date(reservation.debut_datetime),
                                             format_date(reservation.fin_datetime)))
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error:", str(e))



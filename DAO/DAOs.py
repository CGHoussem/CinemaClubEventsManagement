r"""
Ce module permet de gérer les tables dans la base de donnée appropriés à les models

La liste des DAO:
    - UtilisateurDAO
    - EvenementDAO
    - SalleDAO
"""

from db import DBConnexion
import sqlite3

from Models.utilisateur import Utilisateur, Metier
from Models.evenement import Evenement
from Models.salle import Salle
from PyQt5.QtCore import QDate, QDateTime, QTime, QTimeZone


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
            u = Utilisateur(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], int(row[7])==1)
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
            user = Utilisateur(id, user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], int(user_data[7])==1)
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
            u = Utilisateur(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], int(row[7])==1)
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
            date_debut = QDate(int(row[3][6:10]), int(row[3][3:5]), int(row[3][:2]))
            date_fin = QDate(int(row[4][6:10]), int(row[4][3:5]), int(row[4][:2]))
            time_debut = QTime(int(row[3][11:13]), int(row[3][15:17]))
            time_fin = QTime(int(row[4][11:13]), int(row[4][15:17]))
            
            # Récuperer la salle
            salle_id = int(row[5])
            salle = SalleDAO.get_by_id(salle_id)
            
            e = Evenement(int(row[0]), row[1], row[2], QDateTime(date_debut, time_debut), QDateTime(date_fin, time_fin), salle, row[6], row[7])
            # Récuperer la liste des responsables
            query = "SELECT `ID_USER` FROM `EVENT_RESPONSABLE` WHERE `ID_EVENT`=?"
            cursor.execute(query, [int(row[0])])
            
            rows_event_responsable = cursor.fetchall()
            for row_event_responsable in rows_event_responsable:
                id_user = int(row_event_responsable[0])
                # Récuperer le responsable d'id 'id_user'
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
        def format_date(datetime):
            return "%02d/%02d/%d %02d:%02d" % (datetime.date().day(), datetime.date().month(), datetime.date().year(), datetime.time().hour(), datetime.time().minute())
            
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()

            # Ajouter l'évènement
            query_add_event = "INSERT INTO `EVENT` VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)"
            print("attempt adding event", str(new_event))
            cursor.execute(query_add_event, (new_event.nom, new_event.description, format_date(new_event.date_debut), format_date(new_event.date_fin), new_event.salle.id, new_event.color.name(), 0))
            event_id = cursor.lastrowid
            
            # Ajouter les responsables
            query_add_responsable = "INSERT INTO `EVENT_RESPONSABLE` VALUES (?, ?)"
            responsables_data = []
            for r in new_event.responsables:
                # Ajouter la liaison du responsable avec l'évèenement à la base de donnée 
                responsables_data.append((event_id, r.id))
            
            print("attempt adding responsables", responsables_data)
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
                cursor.execute(query_add_projection, (event_id, new_event.presentationAuteur.auteur, new_event.presentationAuteur.duree, new_event.contexte, debat_id))

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error:", str(e))

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
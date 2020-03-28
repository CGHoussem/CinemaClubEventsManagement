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
from Models.projection import Projection
from Models.debat import Debat
from Models.presentation import PresentationAuteur

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
    def add_disponibilite(user_id, conn=None):
        """
        Cette fonction permet d'ajouter la disponbilité de l'utilsateur 'user_id'
        
            Parameters:
                user_id: L'identifiant de l'utilisateur
            Return:
                Un booléen: ajout avec succée ou pas
        """
        close = False
        try:
            if conn == None:
                conn = DBConnexion().Instance
                close = True
            cursor = conn.cursor()
                
            query = "INSERT INTO `USER_DISPONIBILITE` VALUES (?, 0, NULL, NULL, NULL)"
            cursor.execute(query, [user_id])
            
            if close:
                conn.commit()
                conn.close()
            return (True, None)
        except sqlite3.Error as e:
            print("add_disponibilite error:", e)
            return (False, e)
    
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
                dispo = Disponibilite(id_user=user_id, 
                                      statut=int(dispo_data[1]), 
                                      notes=dispo_data[2], 
                                      date_debut=data_to_datetime(dispo_data[3]), 
                                      date_fin=data_to_datetime(dispo_data[4]))
            conn.close()
        return dispo

class UtilisateurDAO:
   
    @staticmethod
    def add_user(user):
        """
        Cette fonction permet d'ajouter un utilisateur dans la base de donnée 
        
            Parameters:
                user: L'utilisateur a ajouter
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()

            print(user.metier)
            return
            # Ajouter l'utilisateur
            query_add_event = "INSERT INTO `USER` VALUES (NULL, ?, ?, ?, ?, ?, ?, 1, 0)"
            cursor.execute(query_add_event, (user.email, 
                                             user.password, 
                                             user.nom, 
                                             user.prenom, 
                                             user.adresse, 
                                             str(user.metier)))
            
            if user.metier in [Metier.MEMBRE_CLUB, Metier.MEMBRE_MAIRIE]:
                user_id = cursor.lastrowid
                (r, ex) = DisponibiliteDAO.add_disponibilite(user_id, conn=conn)
                if not r:
                    raise(ex)

            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print("add_user error:", str(e))
        return False
   
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
            dispo = DisponibiliteDAO.get_by_user_id(id)
            user = Utilisateur(id, user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], dispo, int(user_data[8])==1)
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

class DebatDAO:
    @staticmethod
    def get_by_id(debat_id):
        """
        Cette fonction permet de renvoyer le debat d'identifiant 'debat_id'
        
            Parameters:
                debat_id: l'identifiant du debat
            Return:
                Un objet de type Debat()
        """
        debat = None
        if debat_id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `DEBAT` WHERE `ID` = ?"
            cursor.execute(query, [debat_id])
            
            debat_data = cursor.fetchone()
            
            animateur_id = int(debat_data[1])
            animateur = UtilisateurDAO.get_by_id(animateur_id)
            duree = debat_data[2]
            notes = debat_data[3]
            
            debat = Debat(debat_id, animateur, duree, notes)
            
            conn.close()
        return debat

class ProjectionDAO:
    
    @staticmethod
    def add_projection(projection, event_id, debat_id, conn=None):
        """
        Cette fonction permet d'ajouter une projection dans la base de donnée 
        
            Parameters:
                - projection: La projection a ajoutée
                - event_id: L'identifiant de l'évenement
                - debat_id: L'identifiant du debat
        """
        close = False
        try:
            if conn == None:
                conn = DBConnexion().Instance
                close = True
            cursor = conn.cursor()
            query_add_projection = "INSERT INTO `PROJECTION` VALUES (NULL, ?, ?, ?, ?, ?)"
            
            auteur = None
            duree = None
            if projection.presentationAuteur != None:
                auteur = projection.presentationAuteur.auteur
            if projection.presentationAuteur != None:
                duree = projection.presentationAuteur.duree

            cursor.execute(query_add_projection, (event_id, auteur, duree, projection.contexte, debat_id))

            if close:
                conn.commit()
                conn.close()
        except sqlite3.Error as e:
            print("Error:", str(e))
    
    @staticmethod
    def get_by_id(event_id, event_data, salle):
        """
        Cette fonction permet de renvoyer la projection d'identifiant 'event_id'
        
            Parameters:
                event_id: l'identifiant de le l'évènement (projection)
            Return:
                Un objet de type Projection()
        """
        projection = None
        if event_id != None:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = "SELECT * FROM `PROJECTION` WHERE `EVENT_ID` = ?"
            cursor.execute(query, [event_id])
            projection_data = cursor.fetchone()
            
            projection_auteur = None
            if projection_data[2] != None:
                projection_auteur = PresentationAuteur(projection_data[2], projection_data[3])

            debat = None
            if projection_data[5] != None:
                debat_id = int(projection_data[5])
                debat = DebatDAO.get_by_id(debat_id)

            projection = Projection(event_id, 
                                    nom=event_data[1], 
                                    description=event_data[2], 
                                    date_debut=data_to_datetime(event_data[3]), 
                                    date_fin=data_to_datetime(event_data[4]), 
                                    salle=salle, 
                                    color=event_data[6],
                                    contexte=projection_data[4], 
                                    presentationAuteur=projection_auteur,
                                    debat=debat,
                                    amuses_bouches=int(projection_data[6])==1)
            projection.salle_reservee = int(event_data[9])==1
            projection.disponibilite_invites = int(event_data[10])==1

            conn.close()
        return projection

    @staticmethod
    def update_projection(projection):
        """
        Cette fonction permet de mettre à jour une projection
        
            Parameters:
                projection: La projection à MAJ
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = """UPDATE `PROJECTION` SET 
                `AUTEUR`=?,
                `DUREE_PRESENTATION_AUTEUR`=?,
                `CONTEXTE`=?,
                `AMUSES_BOUCHES`=? WHERE `ID` = ?"""
            
            auteur = None
            duree = None
            amuses_bouches = 0
            if projection.presentationAuteur != None:
                auteur = projection.presentationAuteur.auteur
            if projection.presentationAuteur != None:
                duree = projection.presentationAuteur.duree
            if projection.amuses_bouches:
                amuses_bouches = 1

            cursor.execute(query, (auteur, 
                                   duree,
                                   projection.contexte,
                                   amuses_bouches,
                                   projection.id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("update_projection Error ", e)

class EvenementDAO:
    @staticmethod
    def get_all():
        """
        Cette fonction permet d'obtenir tout les évènements dans la base de donnée 
        
            Return:
                Liste de Evenement() / Projection()
        """
        liste = []
        conn = DBConnexion().Instance
        cursor = conn.cursor()
        query = "SELECT * FROM `EVENT`"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for row in rows:
            event_id = int(row[0])
            # Récuperer la salle
            salle_id = int(row[5])
            salle = SalleDAO.get_by_id(salle_id)
            etat = Etat.EN_ATTENTE
            if int(row[8]) == 1:
                etat = Etat.EN_COURS
            elif int(row[8]) == 2:
                etat = Etat.TERMINE
            if int(row[7]) == 1:
                # creer une projection
                e = ProjectionDAO.get_by_id(event_id, row, salle)
                e.etat = etat
            else:
                # creer une evenement
                e = Evenement(event_id, row[1], row[2], data_to_datetime(row[3]), data_to_datetime(row[4]), salle, row[6], int(row[7])==1, etat, int(row[9])==1, int(row[10])==1)
                
            # Récuperer la liste des responsables
            query = "SELECT `ID_USER` FROM `EVENT_RESPONSABLE` WHERE `ID_EVENT`=?"
            cursor.execute(query, [event_id])
            
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
                ProjectionDAO.add_projection(new_event, event_id, debat_id, conn=conn)

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("add_event Error:", str(e))

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

    @staticmethod
    def update_evenement(event):
        """
        Cette fonction permet de mettre à jour un evenement
        
            Parameters:
                event: L'évènement à MAJ
        """
        try:
            conn = DBConnexion().Instance
            cursor = conn.cursor()
            query = """UPDATE `EVENT` SET 
                `NOM`=?,
                `DESCRIPTION`=?,
                `DATE_DEBUT`=?,
                `DATE_FIN`=?,
                `SALLE`=?,
                `COLOR`=?,
                `EST_PROJECTION`=?,
                `ETAT`=?,
                `RESERVATION_SALLE`=?,
                `DISPONIBILITE_INVITES`=? WHERE `ID` = ?"""
            
            etat = 0
            if event.etat == Etat.EN_COURS:
                etat = 1
            elif event.etat == Etat.TERMINE:
                etat = 2
            
            est_projection = 0
            if event.est_projection:
                est_projection = 1
            salle_reservee = 0
            if event.salle_reservee:
                salle_reservee = 1
            disponibilite_invites = 0
            if event.disponibilite_invites:
                disponibilite_invites = 1
            cursor.execute(query, (event.nom, 
                                   event.description,
                                   format_date(event.date_debut),
                                   format_date(event.date_fin),
                                   event.salle.id,
                                   event.color,
                                   est_projection,
                                   etat,
                                   salle_reservee,
                                   disponibilite_invites,
                                   event.id))
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

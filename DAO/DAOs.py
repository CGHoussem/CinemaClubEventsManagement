"""
Ce module contient les DAO de toutes les models
"""

from db import DBConnexion

from Models.utilisateur import Utilisateur
from Models.evenement import Evenement
from PyQt5.QtCore import QDate

DB_NAME = "miniprojet.db"

class UtilisateurDAO:
   
    @staticmethod
    def get_all_users():
        """
        Cette fonction permet 
        
            Return:
                Une liste de Utilisateur()

        """
        pass

class EvenementDAO:
       
    @staticmethod
    def get_all_events():
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
            date_debut = QDate(int(row[3][6:]), int(row[3][3:5]), int(row[3][:2]))
            date_fin = QDate(int(row[4][6:]), int(row[4][3:5]), int(row[4][:2]))
            e = Evenement(row[1], row[2], date_debut, date_fin, row[5], row[6], row[7])
            liste.append(e)
        
        conn.close()
        
        return liste
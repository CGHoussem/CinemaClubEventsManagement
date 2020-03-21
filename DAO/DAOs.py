"""
Ce module contient les DAO de toutes les models
"""

from db import DBConnexion

from Models.utilisateur import Utilisateur, Metier
from Models.evenement import Evenement
from Models.salle import Salle
from PyQt5.QtCore import QDate

DB_NAME = "miniprojet.db"

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
            date_debut = QDate(int(row[3][6:]), int(row[3][3:5]), int(row[3][:2]))
            date_fin = QDate(int(row[4][6:]), int(row[4][3:5]), int(row[4][:2]))
            e = Evenement(int(row[0]), row[1], row[2], date_debut, date_fin, row[5], row[6], row[7])
            liste.append(e)
        
        conn.close()
        return liste

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
            s = Salle(int(row[0]), row[1], row[2], int(row[3]))
            liste.append(s)
        
        conn.close()
        return liste
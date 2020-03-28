"""
Ce module permet de gérer la connexion à une base de donnée
"""
import sys
import sqlite3

DB_NAME = "base.db"

class DBConnexion(object):
    def __init__(self):
        try:
            self.__instance = sqlite3.connect(DB_NAME)
            #self.__create_tables()
        except sqlite3.Error as e:
            print("SQLITE ERROR: " + str(e), file=sys.stderr)

    @property
    def Instance(self):
        if self.__instance == None:
            self.__instance = sqlite3.connect(DB_NAME)
        return self.__instance

    def __create_tables(self):
        """
        Cette fonction permet de créer toutes les tables de la base de donnée
        """
        with self.__instance:
            query = """CREATE TABLE IF NOT EXISTS `USER` (
                `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `EMAIL`	TEXT NOT NULL UNIQUE,
                `MOTDEPASSE`	TEXT NOT NULL,
                `NOM`	TEXT,
                `PRENOM`	TEXT,
                `ADRESSE`	TEXT,
                `METIER`	TEXT,
                `EST_ADMIN`	INTEGER NOT NULL DEFAULT 0);"""
            self.__instance.execute(query)
            query = """CREATE TABLE `SALLE` (
                `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `ADRESSE`	INTEGER NOT NULL UNIQUE,
                `RESPONSABLE`	INTEGER NOT NULL,
                `NBR_PLACE`	INTEGER NOT NULL,
                FOREIGN KEY(`RESPONSABLE`) REFERENCES `USER`(`ID`));"""
            self.__instance.execute(query)
            query = """CREATE TABLE IF NOT EXISTS `EVENT` (
                `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `NOM`	TEXT NOT NULL UNIQUE,
                `DESCRIPTION`	TEXT,
                `DATE_DEBUT`	TEXT NOT NULL,
                `DATE_FIN`	TEXT NOT NULL,
                `SALLE`	INTEGER NOT NULL,
                `EST_PROJECTION`	INTEGER NOT NULL DEFAULT 0,
                FOREIGN KEY(`SALLE`) REFERENCES `SALLE`(`ID`));"""
            self.__instance.execute(query)
            query = """CREATE TABLE IF NOT EXISTS `EVENT_RESPONSABLE` (
                `ID_EVENT`	INTEGER,
                `ID_USER`	INTEGER,
                PRIMARY KEY(`ID_EVENT`,`ID_USER`),
                FOREIGN KEY(`ID_EVENT`) REFERENCES `EVENT`(`ID`),
                FOREIGN KEY(`ID_USER`) REFERENCES `USER`);"""
            self.__instance.execute(query)
            query = """CREATE TABLE IF NOT EXISTS `DEBAT` (
                `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `ANIMATEUR`	INTEGER NOT NULL,
                `DUREE`	TEXT,
                `NOTES`	TEXT,
                FOREIGN KEY(`ANIMATEUR`) REFERENCES `USER`(`ID`));"""
            self.__instance.execute(query)
            query = """CREATE TABLE IF NOT EXISTS `PROJECTION` (
                `ID`	INTEGER PRIMARY KEY AUTOINCREMENT,
                `EVENT_ID`	INTEGER NOT NULL,
                `AUTEUR`	TEXT,
                `DUREE_PRESENTATION_AUTEUR`	TEXT,
                `CONTEXTE`	TEXT,
                `DEBAT_ID`	INTEGER NOT NULL,
                FOREIGN KEY(`DEBAT_ID`) REFERENCES `DEBAT`(`ID`));"""
            self.__instance.execute(query)


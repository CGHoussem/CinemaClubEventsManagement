# -*- coding: utf-8 -*-

import os
import random
import string

from pathlib import Path
from PIL import Image, ImageOps

from PyQt5.QtCore import QCoreApplication, QDate, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, pyqtSlot
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI.add_event_dialog import Ui_add_event_dialog
from UI.info_event_dialog import Ui_info_event_dialog

from DAO.DAOs import EvenementDAO, UtilisateurDAO

from Models.evenement import Etat
from Models.utilisateur import Utilisateur,Metier
from Models.disponibilite import Statut
from UI.info_user_dialog import Ui_info_user_dialog
import hashlib

class PicButton(QAbstractButton):
    def __init__(self, normal_pixmap=None, hovered_pixmap=None, parent=None):
        super(PicButton, self).__init__(parent)
        self.hovered_pixmap = hovered_pixmap
        self.normal_pixmap = normal_pixmap
        self.__pixmap = normal_pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.__pixmap)
        self.__pixmap = self.normal_pixmap

    def enterEvent(self, event):
        self.__pixmap = self.hovered_pixmap
        return super().enterEvent(event)

    def sizeHint(self):
        return self.__pixmap.size()

class Scheduler(QCalendarWidget):
    def __init__(self, parent=None, events=[]):
        super().__init__(parent)
        self.setGridVisible(True)
        self.__events = events

    def update_events(self, new_events):
        self.__all_events = new_events

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        for event in self.__events:   
            if date >= event.date_debut.date() and date <= event.date_fin.date():
                painter.setBrush(QColor(event.color))
                painter.drawRect(rect)
                painter.drawText(rect, Qt.AlignCenter, str(date.day()))

class Ui_AdminWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags(), admin=None):
        super().__init__(parent=parent, flags=flags)
        
        # Initializing variables
        self.__parent = parent
        self.__admin = admin
        self.__all_events = EvenementDAO.get_all()
        self.__all_users = UtilisateurDAO.get_all()
        self.__tree_items = []
        
        self.__setupUi()
        
        # Initialiazing members
        self.__generate_password()
        self.filtre_date_edit.setDate(QDate.currentDate())
        self.__afficher_all_evenements()
        self.__afficher_all_users()

        # connect signals
        self.disconnect_btn.clicked.connect(self.__disconnect)
        self.profile_btn.clicked.connect(self.__open_profile_dialog)
        self.members_tree.itemDoubleClicked.connect(self.__on_membre_item_click)
        self.addEventBtn.clicked.connect(self.__ouvrir_ajout_evenement_dialog)
        self.eventsListWidget.itemDoubleClicked.connect(self.__ouvrir_evenement_dialog)
        self.reset_filtre_btn.clicked.connect(self.__reset_filter)
        self.filter_btn.clicked.connect(self.__filter_events)
        # Add User Signals
        self.user_password_generate_btn.clicked.connect(self.__generate_password)
        self.add_user_btn.clicked.connect(self.__add_user_form)

    @pyqtSlot()
    def __open_profile_dialog(self):
        """
        Cette fonction permet d'ouvrir la dialog du profile de l'utilisateur
        """
        Ui_info_user_dialog(self, self.__admin).show()

    @pyqtSlot()
    def __disconnect(self):
        """
        Cette fonction permet de mettre l'utilisateur hors connexion
        """
        self.close()
        self.__parent.show()

    @pyqtSlot(QTreeWidgetItem, int)
    def __on_membre_item_click(self, item, column):
        for user, tree_item in self.__tree_items:
            if tree_item == item:
                Ui_info_user_dialog(self, user).show()

    @pyqtSlot()
    def __reset_filter(self):
        self.filtre_date_edit.setDate(QDate.currentDate())
        self.__afficher_all_evenements()
        
    @pyqtSlot()
    def __ouvrir_evenement_dialog(self):
        """
        Cette fonction permet d'ouvrir une fenêtre qui affiche les détails d'un évènement
        """
        indexes = self.eventsListWidget.selectedIndexes()
        if len(indexes) > 0:
            dialog = Ui_info_event_dialog(self, self.__all_events[indexes[0].row()])
            dialog.exec_()

            self.__afficher_all_evenements()

    @pyqtSlot()
    def __ouvrir_ajout_evenement_dialog(self):
        """
        Cette fonction permet d'ouvrir une fenêtre qui permet l'ajout d'un évènement
        """       
        dialog = Ui_add_event_dialog(self)
        ret = dialog.exec_()
        
        if ret == 1:
            if dialog.potential_new_event != None:
                if EvenementDAO.add_event(dialog.potential_new_event):
                    self.__afficher_all_evenements()
                    self.scheduler.update_events(self.__all_events)
                    self.scheduler.updateCells()
                    QMessageBox.information(self, "Ajout d'un évènement", "L'évènement a été ajouté avec succée!")
                else:
                    QMessageBox.warning(self, "Ajout d'un évènement", "Erreur lors de l'ajout de l'évènement!")
            else:
                # error (unknown error)
                QMessageBox.critical(self, "Erreur!", "Erreur inconnue, veuillez réessayer!")
    
    @pyqtSlot()
    def __filter_events(self):
        """
        Cette fonction permet de filtrer les évènements par date
        """
        wanted_date = self.filtre_date_edit.date()
        self.__afficher_evenements(wanted_date.year(), wanted_date.month())

    #region AddUserSignals
    @pyqtSlot()
    def __add_user_form(self):
        """
        Cette fonction permet de vérifer les champs de la forumlaire d'ajout de l'utilisateur et l'ajouté si valide
        """
        nom = self.user_name_edit.text()
        prenom = self.user_fname_edit.text()
        adresse = self.user_adresse_edit.toPlainText()
        email = self.user_email_edit.text()
        password = hashlib.sha256(self.user_password_edit.text().encode()).hexdigest()
        metiers = []
        for m in Metier:
            metiers.append(m)
        metier = metiers[self.user_metier_combox.currentIndex()]
    
        if len(nom) == 0 or len(prenom) == 0 or len(adresse) == 0 or len(email) == 0:
            QMessageBox.warning(self, "Insertion de l'utilisateur", "Vérifier les champs de la formulaire!")
        else:
            user = Utilisateur(None, email, password, nom, prenom, adresse, metier)
            if UtilisateurDAO.add_user(user):
                QMessageBox.information(self, "Insertion de l'utilisateur", "L'utilisateur a été bien ajouter à la base de donnée")
                # clear attributes
                self.user_name_edit.clear()
                self.user_fname_edit.clear()
                self.user_adresse_edit.clear()
                self.user_email_edit.clear()
                self.user_password_edit.clear()
                self.user_metier_combox.setCurrentIndex(0)
                # refresh tree widget
                self.__afficher_all_users()
            else:
                QMessageBox.warning(self, "Insertion de l'utilisateur", "Erreur lors de l'ajout de l'utilisateur à la base de donnée")
        
    @pyqtSlot()
    def __generate_password(self):
        """ 
        Cette fonction permet de générer un mot de passe et l'affecter au champ mot de passe de la formulaire
        """
        def generateOTP(size):
            """ 
            Cette fonction permet de générer un mot de passe 
            """
            OTP = ''.join([random.choice(string.ascii_uppercase+
                                         string.ascii_lowercase+
                                         string.digits)
                                        for n in range(size)])
            return OTP
        self.user_password_edit.setText(generateOTP(8))
    #endregion

    def __afficher_all_users(self):
        """
        Cette fonction permet d'afficher tout les utilisateurs
        """
        def stylize_item(statut, item):
            if statut == Statut.DISPONIBLE:
                item.setBackground(1, QColor(18, 209, 28))
            else:
                item.setBackground(1, QColor(255, 205, 66))
        self.__all_users = UtilisateurDAO.get_all()
        self.members_tree.clear()
        membres_mairie = QTreeWidgetItem(self.members_tree, ['Membres de la mairie'])
        membres_club = QTreeWidgetItem(self.members_tree, ['Membres du club'])
        artistes = None
        critiques = None
        techniciens = None
        responsables_salle = None
        autres = None
        for i, user in enumerate(self.__all_users):
            if user.metier == Metier.MEMBRE_MAIRIE:
                item = QTreeWidgetItem(membres_mairie, [str(user), str(user.disponibilite)])
                stylize_item(user.disponibilite.statut, item)
            elif user.metier == Metier.MEMBRE_CLUB:
                item = QTreeWidgetItem(membres_club, [str(user), str(user.disponibilite)])
                stylize_item(user.disponibilite.statut, item)
            elif user.metier == Metier.REPONSABLE_SALLE:
                if responsables_salle == None:
                    responsables_salle = QTreeWidgetItem(self.members_tree, ['Responsable d\'une salle'])
                item = QTreeWidgetItem(responsables_salle, [str(user), ""])
            elif user.metier == Metier.ARTISTE:
                if artistes == None:
                    artistes = QTreeWidgetItem(self.members_tree, ['Artistes'])
                item = QTreeWidgetItem(artistes, [str(user), ""])
            elif user.metier == Metier.CRITIQUE:
                if critiques == None:
                    critiques = QTreeWidgetItem(self.members_tree, ['Critiques'])
                item = QTreeWidgetItem(critiques, [str(user), ""])
            elif user.metier == Metier.TECHNICIEN:
                if techniciens == None:
                    techniciens = QTreeWidgetItem(self.members_tree, ['Techniciens'])
                item = QTreeWidgetItem(techniciens, [str(user), ""])
            elif user.metier == Metier.AUTRE:
                if autres == None:
                    autres = QTreeWidgetItem(self.members_tree, ['Autres'])
                item = QTreeWidgetItem(autres, [str(user), ""])
            self.__tree_items.append((user, item))

    def __afficher_all_evenements(self):
        """
        Cette fonction permet d'afficher toutes les évènements
        """
        self.__all_events = EvenementDAO.get_all()
        self.eventsListWidget.clear()
        for e in self.__all_events:
            Path("UI/events_icons").mkdir(parents=True, exist_ok=True)
            icon_name = "UI/events_icons/event_%d.png" % e.id
            self.__draw_image(icon_name, (10, 10), e.color)
            icon = QIcon(icon_name)

            item = QListWidgetItem(icon, str(e))
            if e.etat == Etat.EN_ATTENTE:
                item.setBackground(QColor("#FF4B3C"))
            if e.etat == Etat.EN_COURS:
                item.setBackground(QColor("#FFCD42"))
            if e.etat == Etat.TERMINE:
                item.setBackground(QColor("#12D11C"))
            self.eventsListWidget.addItem(item)

    def __afficher_evenements(self, year, month):
        """
        Cette fonction permet d'afficher les évènements de l'année et le mois souhaité
        """
        self.__all_events = EvenementDAO.get_all()
        
        self.eventsListWidget.clear()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for i, e in enumerate(self.__all_events):
            if e.date_debut.date().year() == year and e.date_debut.date().month() == month:
                icon_name = dir_path+"/events_icons/event%d.png" % i
                self.__draw_image(icon_name, (10, 10), e.color)
                icon = QIcon(icon_name)
                
                item = QListWidgetItem(icon, str(e))
                if e.etat == Etat.EN_ATTENTE:
                    item.setBackground(QColor("#FF4B3C"))
                if e.etat == Etat.EN_COURS:
                    item.setBackground(QColor("#FFCD42"))
                if e.etat == Etat.TERMINE:
                    item.setBackground(QColor("#12D11C"))
                self.eventsListWidget.addItem(item)

    def __draw_image(self, file_path, dimension, color):
        if not Path(file_path).exists():
            if isinstance(dimension, tuple):
                img = Image.new('RGB', dimension, color=color)
                img.save(file_path)
                self.__add_border(file_path, file_path, 1)
            else:
                raise RuntimeError('dimension is not a tuple!')

    def __add_border(self, input_image, output_image, border):
        img = Image.open(input_image)
        
        if isinstance(border, int) or isinstance(border, tuple):
            bimg = ImageOps.expand(img, border=border)
        else:
            raise RuntimeError('Border is not an integer or tuple!')
        
        bimg.save(output_image)
    
    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"AdminWindow")
        self.resize(530, 570)
        self.setStyleSheet(open("UI/styles/base_style.css", "r").read())
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.container = QVBoxLayout()
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(5, 5, 5, 5)
        self.header_container = QWidget(self.centralwidget)
        self.header_container.setObjectName(u"header_container")
        self.gridLayout_3 = QGridLayout(self.header_container)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.titre = QLabel(self.header_container)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.titre, 0, 0, 1, 1)

        self.header_buttons_widget = QWidget(self.header_container)
        self.header_buttons_widget.setObjectName(u"header_buttons_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.header_buttons_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.profile_btn = PicButton(QPixmap("UI/pics/profile_btn_normal.png"), QPixmap("UI/pics/profile_btn_hovered.png"), self.header_buttons_widget)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setMouseTracking(True)
        self.profile_btn.setMaximumSize(25, 25)

        self.horizontalLayout_2.addWidget(self.profile_btn, 0, Qt.AlignRight|Qt.AlignTop)

        self.disconnect_btn = QPushButton(self.header_buttons_widget)
        self.disconnect_btn.setObjectName(u"disconnect_btn")

        self.horizontalLayout_2.addWidget(self.disconnect_btn, 0, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout_3.addWidget(self.header_buttons_widget, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.container.addWidget(self.header_container)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.container.addWidget(self.line)

        self.form_grid = QGridLayout()
        self.form_grid.setObjectName(u"form_grid")
        self.form_grid.setSizeConstraint(QLayout.SetFixedSize)
        self.form_grid.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.events_tab = QWidget()
        self.events_tab.setObjectName(u"events_tab")
        self.gridLayout_2 = QGridLayout(self.events_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scheduler = Scheduler(self.events_tab, self.__all_events)
        self.scheduler.setObjectName(u"scheduler")

        self.gridLayout_2.addWidget(self.scheduler, 0, 0, 1, 2)

        self.eventsListWidget = QListWidget(self.events_tab)
        self.eventsListWidget.setObjectName(u"eventsListWidget")

        self.gridLayout_2.addWidget(self.eventsListWidget, 2, 0, 1, 2)

        self.addEventBtn = QPushButton(self.events_tab)
        self.addEventBtn.setObjectName(u"addEventBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addEventBtn.sizePolicy().hasHeightForWidth())
        self.addEventBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.addEventBtn, 1, 1, 1, 1)

        self.filter_widget = QWidget(self.events_tab)
        self.filter_widget.setObjectName(u"filter_widget")
        self.gridLayout_5 = QGridLayout(self.filter_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.filtre_date_label = QLabel(self.filter_widget)
        self.filtre_date_label.setObjectName(u"filtre_date_label")

        self.gridLayout_5.addWidget(self.filtre_date_label, 0, 0, 1, 1)

        self.filtre_date_edit = QDateEdit(self.filter_widget)
        self.filtre_date_edit.setObjectName(u"filtre_date_edit")
        self.filtre_date_edit.setCalendarPopup(True)

        self.gridLayout_5.addWidget(self.filtre_date_edit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.filter_widget, 3, 0, 1, 1)

        self.filter_buttons_container = QWidget(self.events_tab)
        self.filter_buttons_container.setObjectName(u"filter_buttons_container")
        self.horizontalLayout = QHBoxLayout(self.filter_buttons_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset_filtre_btn = QPushButton(self.filter_buttons_container)
        self.reset_filtre_btn.setObjectName(u"reset_filtre_btn")

        self.horizontalLayout.addWidget(self.reset_filtre_btn)

        self.filter_btn = QPushButton(self.filter_buttons_container)
        self.filter_btn.setObjectName(u"filter_btn")

        self.horizontalLayout.addWidget(self.filter_btn)


        self.gridLayout_2.addWidget(self.filter_buttons_container, 3, 1, 1, 1)

        self.tabWidget.addTab(self.events_tab, "")
        self.staff_tab = QWidget()
        self.staff_tab.setObjectName(u"staff_tab")
        self.gridLayout = QGridLayout(self.staff_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(self.staff_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -140, 449, 499))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.liste_membres_label = QLabel(self.scrollAreaWidgetContents)
        self.liste_membres_label.setObjectName(u"liste_membres_label")

        self.verticalLayout.addWidget(self.liste_membres_label, 0, Qt.AlignTop)

        self.members_tree = QTreeWidget(self.scrollAreaWidgetContents)
        self.members_tree.setObjectName(u"members_tree")
        self.members_tree.setAnimated(True)
        self.members_tree.setHeaderHidden(False)
        self.members_tree.setColumnCount(2)
        self.members_tree.setHeaderLabels(['Utilisateur', 'Disponibilité'])
        self.members_tree.header().setCascadingSectionResizes(False)
        self.members_tree.header().setMinimumSectionSize(150)
        self.members_tree.header().setDefaultSectionSize(200)
        self.members_tree.header().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.members_tree)

        self.add_user_groupbox = QGroupBox(self.scrollAreaWidgetContents)
        self.add_user_groupbox.setObjectName(u"add_user_groupbox")
        sizePolicy3.setHeightForWidth(self.add_user_groupbox.sizePolicy().hasHeightForWidth())
        self.add_user_groupbox.setSizePolicy(sizePolicy3)
        self.add_user_groupbox.setMinimumSize(QSize(0, 100))
        self.gridLayout_3 = QGridLayout(self.add_user_groupbox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.add_user_btn = QPushButton(self.add_user_groupbox)
        self.add_user_btn.setObjectName(u"add_user_btn")
        sizePolicy2.setHeightForWidth(self.add_user_btn.sizePolicy().hasHeightForWidth())
        self.add_user_btn.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.add_user_btn, 5, 0, 1, 3, Qt.AlignRight)

        self.user_password_label = QLabel(self.add_user_groupbox)
        self.user_password_label.setObjectName(u"user_password_label")

        self.gridLayout_3.addWidget(self.user_password_label, 3, 0, 1, 1)

        self.user_password_generate_btn = QPushButton(self.add_user_groupbox)
        self.user_password_generate_btn.setObjectName(u"user_password_generate_btn")

        self.gridLayout_3.addWidget(self.user_password_generate_btn, 3, 2, 1, 1)

        self.user_email_edit = QLineEdit(self.add_user_groupbox)
        self.user_email_edit.setObjectName(u"user_email_edit")

        self.gridLayout_3.addWidget(self.user_email_edit, 2, 1, 1, 1)

        self.user_password_edit = QLineEdit(self.add_user_groupbox)
        self.user_password_edit.setObjectName(u"user_password_edit")
        self.user_password_edit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.user_password_edit, 3, 1, 1, 1)

        self.user_adresse_edit = QPlainTextEdit(self.add_user_groupbox)
        self.user_adresse_edit.setObjectName(u"user_adresse_edit")
        sizePolicy1.setHeightForWidth(self.user_adresse_edit.sizePolicy().hasHeightForWidth())
        self.user_adresse_edit.setSizePolicy(sizePolicy1)
        self.user_adresse_edit.setMaximumSize(QSize(16777215, 75))

        self.gridLayout_3.addWidget(self.user_adresse_edit, 1, 1, 1, 1)

        self.user_email_label = QLabel(self.add_user_groupbox)
        self.user_email_label.setObjectName(u"user_email_label")

        self.gridLayout_3.addWidget(self.user_email_label, 2, 0, 1, 1)

        self.user_metier_combox = QComboBox(self.add_user_groupbox)
        self.user_metier_combox.addItem("")
        self.user_metier_combox.addItem("")
        self.user_metier_combox.addItem("")
        self.user_metier_combox.addItem("")
        self.user_metier_combox.addItem("")
        self.user_metier_combox.addItem("")
        self.user_metier_combox.setObjectName(u"user_metier_combox")

        self.gridLayout_3.addWidget(self.user_metier_combox, 4, 1, 1, 1)

        self.user_fname_lname_layout = QHBoxLayout()
        self.user_fname_lname_layout.setObjectName(u"user_fname_lname_layout")
        self.user_name_label = QLabel(self.add_user_groupbox)
        self.user_name_label.setObjectName(u"user_name_label")

        self.user_fname_lname_layout.addWidget(self.user_name_label)

        self.user_name_edit = QLineEdit(self.add_user_groupbox)
        self.user_name_edit.setObjectName(u"user_name_edit")

        self.user_fname_lname_layout.addWidget(self.user_name_edit)

        self.user_fname_label = QLabel(self.add_user_groupbox)
        self.user_fname_label.setObjectName(u"user_fname_label")

        self.user_fname_lname_layout.addWidget(self.user_fname_label)

        self.user_fname_edit = QLineEdit(self.add_user_groupbox)
        self.user_fname_edit.setObjectName(u"user_fname_edit")

        self.user_fname_lname_layout.addWidget(self.user_fname_edit)


        self.gridLayout_3.addLayout(self.user_fname_lname_layout, 0, 0, 1, 3)

        self.user_adresse_label = QLabel(self.add_user_groupbox)
        self.user_adresse_label.setObjectName(u"user_adresse_label")

        self.gridLayout_3.addWidget(self.user_adresse_label, 1, 0, 1, 1, Qt.AlignTop)

        self.user_metier_label = QLabel(self.add_user_groupbox)
        self.user_metier_label.setObjectName(u"user_metier_label")

        self.gridLayout_3.addWidget(self.user_metier_label, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.add_user_groupbox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.staff_tab, "")
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.tabWidget.addTab(self.history_tab, "")

        self.form_grid.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.container.addLayout(self.form_grid)

        self.container.setStretch(0, 1)
        self.container.setStretch(2, 2)

        self.gridLayout_4.addLayout(self.container, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        #if QT_CONFIG(shortcut)
        self.filtre_date_label.setBuddy(self.filtre_date_edit)
        self.liste_membres_label.setBuddy(self.members_tree)
        self.user_password_label.setBuddy(self.user_password_edit)
        self.user_email_label.setBuddy(self.user_email_edit)
        self.user_name_label.setBuddy(self.user_name_edit)
        self.user_fname_label.setBuddy(self.user_fname_edit)
        self.user_adresse_label.setBuddy(self.user_adresse_edit)
        self.user_metier_label.setBuddy(self.user_metier_combox)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.scheduler)
        QWidget.setTabOrder(self.scheduler, self.addEventBtn)
        QWidget.setTabOrder(self.addEventBtn, self.eventsListWidget)
        QWidget.setTabOrder(self.eventsListWidget, self.filtre_date_edit)
        QWidget.setTabOrder(self.filtre_date_edit, self.filter_btn)
        QWidget.setTabOrder(self.filter_btn, self.reset_filtre_btn)
        QWidget.setTabOrder(self.reset_filtre_btn, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.members_tree)
        QWidget.setTabOrder(self.members_tree, self.user_name_edit)
        QWidget.setTabOrder(self.user_name_edit, self.user_fname_edit)
        QWidget.setTabOrder(self.user_fname_edit, self.user_adresse_edit)
        QWidget.setTabOrder(self.user_adresse_edit, self.user_email_edit)
        QWidget.setTabOrder(self.user_email_edit, self.user_password_edit)
        QWidget.setTabOrder(self.user_password_edit, self.user_password_generate_btn)
        QWidget.setTabOrder(self.user_password_generate_btn, self.user_metier_combox)
        QWidget.setTabOrder(self.user_metier_combox, self.add_user_btn)

        self.__retranslateUi()

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Tableau de board d'administrateur", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MemberWindow", u"Se D\u00e9connecter", None))
        self.titre.setText(QCoreApplication.translate("AdminWindow", u"Cin\u00e9-Club", None))
        self.addEventBtn.setText(QCoreApplication.translate("AdminWindow", u"Ajouter un \u00e9v\u00e8nement", None))
        self.filtre_date_label.setText(QCoreApplication.translate("AdminWindow", u"Filtrer par date", None))
        self.reset_filtre_btn.setText(QCoreApplication.translate("AdminWindow", u"R\u00e9tablir", None))
        self.filter_btn.setText(QCoreApplication.translate("AdminWindow", u"Filtrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events_tab), QCoreApplication.translate("AdminWindow", u"\u00c9v\u00e8nements", None))
        self.liste_membres_label.setText(QCoreApplication.translate("AdminWindow", u"Liste des users", None))
        self.add_user_groupbox.setTitle(QCoreApplication.translate("AdminWindow", u"Ajout d'un user", None))
        self.add_user_btn.setText(QCoreApplication.translate("AdminWindow", u"Ajouter l'utilisateur", None))
        self.user_password_label.setText(QCoreApplication.translate("AdminWindow", u"Mot de passe", None))
        self.user_password_generate_btn.setText(QCoreApplication.translate("AdminWindow", u"G\u00e9nerer", None))
        self.user_email_edit.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Entrez l'adresse email", None))
        self.user_password_edit.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"G\u00e9n\u00e9rer un mot de passe", None))
        self.user_adresse_edit.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Entrez l'adresse postale", None))
        self.user_email_label.setText(QCoreApplication.translate("AdminWindow", u"Adresse e-mail", None))
        self.user_metier_combox.setItemText(0, QCoreApplication.translate("AdminWindow", u"Membre de la mairie", None))
        self.user_metier_combox.setItemText(1, QCoreApplication.translate("AdminWindow", u"Membre du club", None))
        self.user_metier_combox.setItemText(2, QCoreApplication.translate("AdminWindow", u"Responsable d'une salle", None))
        self.user_metier_combox.setItemText(3, QCoreApplication.translate("AdminWindow", u"Artiste", None))
        self.user_metier_combox.setItemText(4, QCoreApplication.translate("AdminWindow", u"Critique", None))
        self.user_metier_combox.setItemText(5, QCoreApplication.translate("AdminWindow", u"Technicien", None))
        self.user_metier_combox.setItemText(6, QCoreApplication.translate("AdminWindow", u"Autre", None))

        self.user_name_label.setText(QCoreApplication.translate("AdminWindow", u"Nom", None))
        self.user_name_edit.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Entrez le nom", None))
        self.user_fname_label.setText(QCoreApplication.translate("AdminWindow", u"Pr\u00e9nom", None))
        self.user_fname_edit.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Entrez le pr\u00e9nom", None))
        self.user_adresse_label.setText(QCoreApplication.translate("AdminWindow", u"Adresse", None))
        self.user_metier_label.setText(QCoreApplication.translate("AdminWindow", u"M\u00e9tier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.staff_tab), QCoreApplication.translate("AdminWindow", u"Membres", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("AdminWindow", u"Historique", None))
    # retranslateUi
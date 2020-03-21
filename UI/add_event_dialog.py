# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'self.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
from DAO.DAOs import UtilisateurDAO, SalleDAO
from Models.utilisateur import Metier
from Models.presentation import PresentationAuteur
from Models.projection import Projection
from Models.debat import Debat
from Models.salle import Salle
from Models.evenement import Evenement

from PyQt5.QtCore import QCoreApplication, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, pyqtSlot
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI.add_animateur_dialog import Ui_add_animateur_dialog

class Ui_add_event_dialog(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.__potential_new_event = None
        self.__event_color = None
        self.__list_potential_responsables = []
        self.__list_responsables = []
        self.__list_salles = SalleDAO.get_all()
        self.__animateur = None
        
        self.__setupUi()
        
        # connect signals
        # checkboxes
        self.est_projection_checkbox.clicked.connect(lambda e: self.projection_groupbox.setEnabled(self.est_projection_checkbox.isChecked()))
        self.presentation_checkbox.clicked.connect(lambda e: self.presentation_groupbox.setEnabled(self.presentation_checkbox.isChecked()))
        self.debat_checkbox.clicked.connect(lambda e: self.debat_groupbox.setEnabled(self.debat_checkbox.isChecked()))
        # buttons
        self.enlever_repsonsable_btn.clicked.connect(self.__delete_responsable)
        self.ajouter_responsable_btn.clicked.connect(self.__add_responsable)
        self.event_color_btn.clicked.connect(self.__choose_color)
        self.ajout_animateur_btn.clicked.connect(self.__add_animateur)
        
        # initilazing members
        users = UtilisateurDAO.get_all()
        for u in users:
            if u.metier in [Metier.MEMBRE_MAIRIE, Metier.MEMBRE_CLUB]:
                self.__list_potential_responsables.append(u)
                self.responsable_combo.addItem(str(u))
        
        self.date_debut_edit.setDateTime(QDateTime.currentDateTime())
        self.date_fin_edit.setDateTime(QDateTime.currentDateTime())
        
        for s in self.__list_salles:
            self.salle_projection_combo.addItem(str(s))
    
    @property
    def potential_new_event(self):
        return self.__potential_new_event
    
    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"AddEventDialog")
        self.setWindowModality(Qt.WindowModal)
        self.resize(500, 600)
        self.setMinimumSize(QSize(500, 600))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f = open(dir_path+"/base_style.css", "r")
        self.setStyleSheet(f.read())
        f.close()
        self.setSizeGripEnabled(True)
        self.setModal(True)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titre = QLabel(self)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.titre)

        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 463, 872))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.projection_groupbox = QGroupBox(self.scrollAreaWidgetContents)
        self.projection_groupbox.setObjectName(u"projection_groupbox")
        self.projection_groupbox.setEnabled(False)
        self.est_projection_layout = QGridLayout(self.projection_groupbox)
        self.est_projection_layout.setObjectName(u"est_projection_layout")
        self.presentation_groupbox = QGroupBox(self.projection_groupbox)
        self.presentation_groupbox.setObjectName(u"presentation_groupbox")
        self.presentation_groupbox.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.presentation_groupbox.sizePolicy().hasHeightForWidth())
        self.presentation_groupbox.setSizePolicy(sizePolicy2)
        self.presentation_auteur_layout = QGridLayout(self.presentation_groupbox)
        self.presentation_auteur_layout.setObjectName(u"presentation_auteur_layout")
        self.duree_presentation_edit = QLineEdit(self.presentation_groupbox)
        self.duree_presentation_edit.setObjectName(u"duree_presentation_edit")

        self.presentation_auteur_layout.addWidget(self.duree_presentation_edit, 1, 1, 1, 1)

        self.duree_presentation_label = QLabel(self.presentation_groupbox)
        self.duree_presentation_label.setObjectName(u"duree_presentation_label")

        self.presentation_auteur_layout.addWidget(self.duree_presentation_label, 1, 0, 1, 1)

        self.nom_auteur_label = QLabel(self.presentation_groupbox)
        self.nom_auteur_label.setObjectName(u"nom_auteur_label")

        self.presentation_auteur_layout.addWidget(self.nom_auteur_label, 0, 0, 1, 1)

        self.nom_auteur_edit = QLineEdit(self.presentation_groupbox)
        self.nom_auteur_edit.setObjectName(u"nom_auteur_edit")

        self.presentation_auteur_layout.addWidget(self.nom_auteur_edit, 0, 1, 1, 1)


        self.est_projection_layout.addWidget(self.presentation_groupbox, 5, 1, 1, 1)

        self.debat_groupbox = QGroupBox(self.projection_groupbox)
        self.debat_groupbox.setObjectName(u"debat_groupbox")
        self.debat_groupbox.setEnabled(False)
        self.debat_layout = QGridLayout(self.debat_groupbox)
        self.debat_layout.setObjectName(u"debat_layout")
        self.debat_notes_label = QLabel(self.debat_groupbox)
        self.debat_notes_label.setObjectName(u"debat_notes_label")

        self.debat_layout.addWidget(self.debat_notes_label, 4, 0, 1, 1, Qt.AlignTop)

        self.duree_debat_edit = QLineEdit(self.debat_groupbox)
        self.duree_debat_edit.setObjectName(u"duree_debat_edit")

        self.debat_layout.addWidget(self.duree_debat_edit, 3, 1, 1, 1)

        self.animateur_list = QListWidget(self.debat_groupbox)
        self.animateur_list.setObjectName(u"animateur_list")
        self.animateur_list.setMovement(QListView.Free)

        self.debat_layout.addWidget(self.animateur_list, 0, 1, 1, 1)

        self.debat_animateur_label = QLabel(self.debat_groupbox)
        self.debat_animateur_label.setObjectName(u"debat_animateur_label")

        self.debat_layout.addWidget(self.debat_animateur_label, 0, 0, 1, 1, Qt.AlignTop)

        self.debat_notes__edit = QTextEdit(self.debat_groupbox)
        self.debat_notes__edit.setObjectName(u"debat_notes__edit")

        self.debat_layout.addWidget(self.debat_notes__edit, 4, 1, 1, 1)

        self.debat_duree_label = QLabel(self.debat_groupbox)
        self.debat_duree_label.setObjectName(u"debat_duree_label")

        self.debat_layout.addWidget(self.debat_duree_label, 3, 0, 1, 1)

        self.ajout_animateur_btn = QPushButton(self.debat_groupbox)
        self.ajout_animateur_btn.setObjectName(u"ajout_animateur_btn")

        self.debat_layout.addWidget(self.ajout_animateur_btn, 2, 1, 1, 1)


        self.est_projection_layout.addWidget(self.debat_groupbox, 7, 1, 1, 1)

        self.context_tournage_edit = QTextEdit(self.projection_groupbox)
        self.context_tournage_edit.setObjectName(u"context_tournage_edit")

        self.est_projection_layout.addWidget(self.context_tournage_edit, 3, 1, 1, 1)

        self.presentation_checkbox = QCheckBox(self.projection_groupbox)
        self.presentation_checkbox.setObjectName(u"presentation_checkbox")

        self.est_projection_layout.addWidget(self.presentation_checkbox, 4, 0, 1, 1)

        self.contexte_label = QLabel(self.projection_groupbox)
        self.contexte_label.setObjectName(u"contexte_label")

        self.est_projection_layout.addWidget(self.contexte_label, 3, 0, 1, 1, Qt.AlignTop)

        self.debat_checkbox = QCheckBox(self.projection_groupbox)
        self.debat_checkbox.setObjectName(u"debat_checkbox")

        self.est_projection_layout.addWidget(self.debat_checkbox, 6, 0, 1, 1)


        self.gridLayout_4.addWidget(self.projection_groupbox, 2, 0, 1, 1)

        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.responsable_combo = QComboBox(self.scrollAreaWidgetContents)
        self.responsable_combo.setObjectName(u"responsable_combo")

        self.add_event_layout.addWidget(self.responsable_combo, 1, 1, 1, 1)

        self.description_evenement_edit = QTextEdit(self.scrollAreaWidgetContents)
        self.description_evenement_edit.setObjectName(u"description_evenement_edit")

        self.add_event_layout.addWidget(self.description_evenement_edit, 3, 1, 1, 2)

        self.ajouter_responsable_btn = QPushButton(self.scrollAreaWidgetContents)
        self.ajouter_responsable_btn.setObjectName(u"ajouter_responsable_btn")

        self.add_event_layout.addWidget(self.ajouter_responsable_btn, 1, 2, 1, 1)

        self.date_fin_label = QLabel(self.scrollAreaWidgetContents)
        self.date_fin_label.setObjectName(u"date_fin_label")

        self.add_event_layout.addWidget(self.date_fin_label, 5, 0, 1, 1)

        self.date_debut_edit = QDateTimeEdit(self.scrollAreaWidgetContents)
        self.date_debut_edit.setObjectName(u"date_debut_edit")
        self.date_debut_edit.setCalendarPopup(True)

        self.add_event_layout.addWidget(self.date_debut_edit, 4, 1, 1, 2)

        self.event_color_label = QLabel(self.scrollAreaWidgetContents)
        self.event_color_label.setObjectName(u"event_color_label")

        self.add_event_layout.addWidget(self.event_color_label, 7, 0, 1, 1)

        self.date_fin_edit = QDateTimeEdit(self.scrollAreaWidgetContents)
        self.date_fin_edit.setObjectName(u"date_fin_edit")
        self.date_fin_edit.setCalendarPopup(True)

        self.add_event_layout.addWidget(self.date_fin_edit, 5, 1, 1, 2)

        self.salle_projection_label = QLabel(self.scrollAreaWidgetContents)
        self.salle_projection_label.setObjectName(u"salle_projection_label")

        self.add_event_layout.addWidget(self.salle_projection_label, 6, 0, 1, 1)

        self.nom_evenement_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.nom_evenement_edit.setObjectName(u"nom_evenement_edit")

        self.add_event_layout.addWidget(self.nom_evenement_edit, 2, 1, 1, 2)

        self.responsable_list = QListWidget(self.scrollAreaWidgetContents)
        self.responsable_list.setObjectName(u"responsable_list")

        self.add_event_layout.addWidget(self.responsable_list, 0, 1, 1, 1)

        self.est_projection_checkbox = QCheckBox(self.scrollAreaWidgetContents)
        self.est_projection_checkbox.setObjectName(u"est_projection_checkbox")

        self.add_event_layout.addWidget(self.est_projection_checkbox, 8, 0, 1, 1)

        self.description_label = QLabel(self.scrollAreaWidgetContents)
        self.description_label.setObjectName(u"description_label")

        self.add_event_layout.addWidget(self.description_label, 3, 0, 1, 1, Qt.AlignTop)

        self.responsables_label = QLabel(self.scrollAreaWidgetContents)
        self.responsables_label.setObjectName(u"responsables_label")

        self.add_event_layout.addWidget(self.responsables_label, 0, 0, 1, 1, Qt.AlignTop)

        self.nom_evenement_label = QLabel(self.scrollAreaWidgetContents)
        self.nom_evenement_label.setObjectName(u"nom_evenement_label")

        self.add_event_layout.addWidget(self.nom_evenement_label, 2, 0, 1, 1)

        self.salle_projection_combo = QComboBox(self.scrollAreaWidgetContents)
        self.salle_projection_combo.setObjectName(u"salle_projection_combo")

        self.add_event_layout.addWidget(self.salle_projection_combo, 6, 1, 1, 2)

        self.enlever_repsonsable_btn = QPushButton(self.scrollAreaWidgetContents)
        self.enlever_repsonsable_btn.setObjectName(u"enlever_repsonsable_btn")

        self.add_event_layout.addWidget(self.enlever_repsonsable_btn, 0, 2, 1, 1, Qt.AlignBottom)

        self.date_debut_label = QLabel(self.scrollAreaWidgetContents)
        self.date_debut_label.setObjectName(u"date_debut_label")

        self.add_event_layout.addWidget(self.date_debut_label, 4, 0, 1, 1)

        self.event_color_btn = QPushButton(self.scrollAreaWidgetContents)
        self.event_color_btn.setObjectName(u"event_color_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.event_color_btn.sizePolicy().hasHeightForWidth())
        self.event_color_btn.setSizePolicy(sizePolicy3)

        self.add_event_layout.addWidget(self.event_color_btn, 7, 1, 1, 2)


        self.gridLayout_4.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)

        #if QT_CONFIG(shortcut)
        self.duree_presentation_label.setBuddy(self.duree_presentation_edit)
        self.nom_auteur_label.setBuddy(self.nom_auteur_edit)
        self.debat_notes_label.setBuddy(self.debat_notes__edit)
        self.debat_animateur_label.setBuddy(self.animateur_list)
        self.debat_duree_label.setBuddy(self.duree_debat_edit)
        self.contexte_label.setBuddy(self.context_tournage_edit)
        self.date_fin_label.setBuddy(self.date_fin_edit)
        self.event_color_label.setBuddy(self.event_color_btn)
        self.salle_projection_label.setBuddy(self.salle_projection_combo)
        self.description_label.setBuddy(self.description_evenement_edit)
        self.responsables_label.setBuddy(self.responsable_list)
        self.nom_evenement_label.setBuddy(self.nom_evenement_edit)
        self.date_debut_label.setBuddy(self.date_debut_edit)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.responsable_list)
        QWidget.setTabOrder(self.responsable_list, self.enlever_repsonsable_btn)
        QWidget.setTabOrder(self.enlever_repsonsable_btn, self.responsable_combo)
        QWidget.setTabOrder(self.responsable_combo, self.ajouter_responsable_btn)
        QWidget.setTabOrder(self.ajouter_responsable_btn, self.nom_evenement_edit)
        QWidget.setTabOrder(self.nom_evenement_edit, self.description_evenement_edit)
        QWidget.setTabOrder(self.description_evenement_edit, self.date_debut_edit)
        QWidget.setTabOrder(self.date_debut_edit, self.date_fin_edit)
        QWidget.setTabOrder(self.date_fin_edit, self.salle_projection_combo)
        QWidget.setTabOrder(self.salle_projection_combo, self.event_color_btn)
        QWidget.setTabOrder(self.event_color_btn, self.est_projection_checkbox)
        QWidget.setTabOrder(self.est_projection_checkbox, self.context_tournage_edit)
        QWidget.setTabOrder(self.context_tournage_edit, self.presentation_checkbox)
        QWidget.setTabOrder(self.presentation_checkbox, self.nom_auteur_edit)
        QWidget.setTabOrder(self.nom_auteur_edit, self.duree_presentation_edit)
        QWidget.setTabOrder(self.duree_presentation_edit, self.debat_checkbox)
        QWidget.setTabOrder(self.debat_checkbox, self.animateur_list)
        QWidget.setTabOrder(self.animateur_list, self.ajout_animateur_btn)
        QWidget.setTabOrder(self.ajout_animateur_btn, self.duree_debat_edit)
        QWidget.setTabOrder(self.duree_debat_edit, self.debat_notes__edit)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.__local_save_event)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("AddEventDialog", u"Ajout d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("AddEventDialog", u"Cin\u00e9-Club", None))
        self.est_projection_checkbox.setText(QCoreApplication.translate("AddEventDialog", u"Est Projection?", None))
        self.enlever_repsonsable_btn.setText(QCoreApplication.translate("AddEventDialog", u"Enlever", None))
        self.nom_evenement_label.setText(QCoreApplication.translate("AddEventDialog", u"Nom de l'\u00e9v\u00e8nement", None))
        self.ajouter_responsable_btn.setText(QCoreApplication.translate("AddEventDialog", u"Ajouter", None))
        self.date_debut_label.setText(QCoreApplication.translate("AddEventDialog", u"Date de d\u00e9but", None))
        self.description_label.setText(QCoreApplication.translate("AddEventDialog", u"Description", None))
        self.responsables_label.setText(QCoreApplication.translate("AddEventDialog", u"Reponsables", None))
        self.nom_evenement_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez le nom de l'\u00e9v\u00e8nement", None))
        self.description_evenement_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez la description de l'\u00e9v\u00e8nement", None))
        self.date_fin_label.setText(QCoreApplication.translate("AddEventDialog", u"Date de fin", None))
        self.context_tournage_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez le contexte du trounage", None))
        self.presentation_checkbox.setText(QCoreApplication.translate("AddEventDialog", u"Pr\u00e9sentation de l'auteur?", None))
        self.ajout_animateur_btn.setText(QCoreApplication.translate("add_event_dialog", u"Ajouter un animateur", None))
        self.duree_debat_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez la dur\u00e9e du d\u00e9bat", None))
        self.debat_duree_label.setText(QCoreApplication.translate("AddEventDialog", u"Dur\u00e9e", None))
        self.debat_animateur_label.setText(QCoreApplication.translate("AddEventDialog", u"Animateur", None))
        self.debat_notes_label.setText(QCoreApplication.translate("AddEventDialog", u"Notes", None))
        self.debat_notes__edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez quelques notes sur le d\u00e9bat", None))
        self.debat_checkbox.setText(QCoreApplication.translate("AddEventDialog", u"D\u00e9bat?", None))
        self.contexte_label.setText(QCoreApplication.translate("AddEventDialog", u"Contexte du tournage", None))
        self.duree_presentation_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez la dur\u00e9e de la pr\u00e9sentation", None))
        self.nom_auteur_edit.setPlaceholderText(QCoreApplication.translate("AddEventDialog", u"Entrez le nom de l'auteur", None))
        self.duree_presentation_label.setText(QCoreApplication.translate("AddEventDialog", u"Dur\u00e9e de la pr\u00e9sentation", None))
        self.nom_auteur_label.setText(QCoreApplication.translate("AddEventDialog", u"Nom de l'auteur", None))
        self.salle_projection_label.setText(QCoreApplication.translate("add_event_dialog", u"Salle de projection", None))
        self.event_color_label.setText(QCoreApplication.translate("add_event_dialog", u"Couleur", None))
        #if QT_CONFIG(tooltip)
        self.event_color_btn.setToolTip(QCoreApplication.translate("add_event_dialog", u"<html><head/><body><p>La couleur de l'\u00e9v\u00e8nement sur la calendrier</p></body></html>", None))
        #endif // QT_CONFIG(tooltip)
        self.event_color_btn.setText(QCoreApplication.translate("add_event_dialog", u"Choisir une couleur", None))
    # retranslateUi

    @pyqtSlot()
    def __delete_responsable(self):
        selected_indexes = []
        for selected_item in  self.responsable_list.selectedIndexes():
            selected_indexes.append(selected_item.row())
        
        for index in selected_indexes:
            self.__list_responsables.pop(index)
            self.responsable_list.takeItem(index)

    @pyqtSlot()
    def __add_responsable(self):
        index = self.responsable_combo.currentIndex()
        responsable = self.__list_potential_responsables[index]
        
        if not responsable in self.__list_responsables:
            self.__list_responsables.append(responsable)
            self.responsable_list.addItem(str(responsable))
    
    @pyqtSlot()
    def __add_animateur(self):
        potential_new_animateur = None
        dialog = Ui_add_animateur_dialog(self)
        ret = dialog.exec_()
        
        if ret == 1:
            if self.__animateur != None or (not self.__animateur.nom+self.____animateur.prenom == dialog.potential_new_animateur.nom+dialog.potential_new_animateur.prenom):
                print("Add", dialog.potential_new_animateur)
                self.__animateur = dialog.potential_new_animateur
                self.animateur_list.addItem(str(self.__animateur))
            else:
                print("DO NOTHING", ret)
        else:
            print("DO NOTHING", ret)
    
    @pyqtSlot()
    def __choose_color(self):
        dialog = QColorDialog(self) 
        
        if dialog.exec_() == 1:    
            color = dialog.currentColor()
            if color.isValid():
                p = QPalette()
                p.setColor(p.Foreground, color)
                self.event_color_label.setPalette(p)
                self.__event_color = color
    
    # TODO save event
    def __local_save_event(self):
        nom = self.nom_evenement_edit.text()
        description = self.description_evenement_edit.toPlainText()
        date_debut = self.date_debut_edit.dateTime()
        date_fin = self.date_fin_edit.dateTime()
        
        salle = self.__list_salles[self.salle_projection_combo.currentIndex()]
        color = self.__event_color
        
        est_projection = self.est_projection_checkbox.isChecked()
        if est_projection:
            presentation = None
            debat = None
            contexte = self.context_tournage_edit.toPlainText()
            existe_presentation = self.presentation_checkbox.isChecked()
            existe_debat = self.debat_checkbox.isChecked()
            if existe_presentation:
                auteur = self.nom_auteur_edit.text()
                duree_presentation = self.duree_presentation_edit.text()
                if len(auteur) != 0 and len(duree_presentation) != 0:
                    presentation = PresentationAuteur(auteur, duree_presentation)
                else:
                    # error presentation
                    QMessageBox.warning(self, "Informations manquantes!", "Il faut saisir toutes les informations de la présentation.")
                    return
            if existe_debat:
                duree_debat = self.duree_debat_edit.text()
                notes = self.debat_notes__edit.text()
                if self.__animateur != None:
                    debat = Debat(None, self.__animateur, duree_debat, notes)
                else:
                    # error debat
                    QMessageBox.warning(self, "Informations manquantes!", "Vous devrez assigner un animateur.")
                    return
            
            if len(nom) != 0 and len(description) != 0 and len(contexte) != 0 and date_debut < date_fin and color != None and salle != None:
                projection = Projection(None, nom, description, date_debut, date_fin, salle, color, contexte, presentation, debat)
                if len(self.__list_responsables) != 0:
                    for r in self.__list_responsables:
                        projection.ajouterResponsable(r)
                    self.__potential_new_event = projection
                else:
                    # error projection (aucun responsable)
                    QMessageBox.warning(self, "Informations manquantes!", "Vous devez ajouter, au moins, un responsable.")
                    return
            else:
                # error projection (autres)
                QMessageBox.warning(self, "Informations manquantes!", "Vérifier les informations générale de l'évènement!")
                return
        else:
            if len(nom) != 0 and len(description) != 0  and date_debut < date_fin and color != None and salle != None:
                evenement = Evenement(None, nom, description, date_debut, date_fin, salle, color)
                if len(self.__list_responsables) != 0:
                    for r in self.__list_responsables:
                        evenement.ajouterResponsable(r)
                    self.__potential_new_event = evenement
                else:
                    # error projection (aucun responsable)
                    QMessageBox.warning(self, "Informations manquantes!", "Vous devez ajouter, au moins, un responsable.")
                    return
            else:
                # error projection (autres)
                QMessageBox.warning(self, "Informations manquantes!", "Vérifier les informations générale de l'évènement!")
                return
        self.accept()
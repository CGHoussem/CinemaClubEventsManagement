# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_animateur_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from Models.utilisateur import Metier, Utilisateur


class Ui_add_animateur_dialog(QDialog):
    
    def __init__(self, parent=None, flags=Qt.WindowFlags(), potential_new_animateur=None):
        super().__init__(parent=parent, flags=flags)
        self.__potential_new_animateur = None
        
        self.__setupUi()
    
    @property
    def potential_new_animateur(self):
        return self.__potential_new_animateur
    
    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"add_event_dialog")
        self.setWindowModality(Qt.WindowModal)
        self.resize(500, 461)
        self.setMinimumSize(QSize(500, 0))
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
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.email_animateur_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.email_animateur_edit.setObjectName(u"email_animateur_edit")

        self.add_event_layout.addWidget(self.email_animateur_edit, 2, 1, 1, 2)

        self.prenom_animateur = QLabel(self.scrollAreaWidgetContents)
        self.prenom_animateur.setObjectName(u"prenom_animateur")

        self.add_event_layout.addWidget(self.prenom_animateur, 1, 0, 1, 1)

        self.prenom_animateur_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.prenom_animateur_edit.setObjectName(u"prenom_animateur_edit")

        self.add_event_layout.addWidget(self.prenom_animateur_edit, 1, 1, 1, 2)

        self.metier_animateur_combo = QComboBox(self.scrollAreaWidgetContents)
        self.metier_animateur_combo.addItem("Membre du club")
        self.metier_animateur_combo.addItem("Artiste")
        self.metier_animateur_combo.addItem("Critique")
        self.metier_animateur_combo.addItem("Technicien")
        self.metier_animateur_combo.addItem("Autre..")
        self.metier_animateur_combo.setObjectName(u"metier_animateur_combo")

        self.add_event_layout.addWidget(self.metier_animateur_combo, 4, 1, 2, 2)

        self.adresse_animateur_edit = QTextEdit(self.scrollAreaWidgetContents)
        self.adresse_animateur_edit.setObjectName(u"adresse_animateur_edit")

        self.add_event_layout.addWidget(self.adresse_animateur_edit, 3, 1, 1, 2)

        self.nom_animateur_label = QLabel(self.scrollAreaWidgetContents)
        self.nom_animateur_label.setObjectName(u"nom_animateur_label")

        self.add_event_layout.addWidget(self.nom_animateur_label, 0, 0, 1, 1)

        self.email_animateur_label = QLabel(self.scrollAreaWidgetContents)
        self.email_animateur_label.setObjectName(u"email_animateur_label")

        self.add_event_layout.addWidget(self.email_animateur_label, 2, 0, 1, 1)

        self.metier_animateur_label = QLabel(self.scrollAreaWidgetContents)
        self.metier_animateur_label.setObjectName(u"metier_animateur_label")

        self.add_event_layout.addWidget(self.metier_animateur_label, 4, 0, 2, 1)

        self.adresse_animateur_label = QLabel(self.scrollAreaWidgetContents)
        self.adresse_animateur_label.setObjectName(u"adresse_animateur_label")

        self.add_event_layout.addWidget(self.adresse_animateur_label, 3, 0, 1, 1, Qt.AlignTop)

        self.nom_animateur_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.nom_animateur_edit.setObjectName(u"nom_animateur_edit")

        self.add_event_layout.addWidget(self.nom_animateur_edit, 0, 1, 1, 2)


        self.gridLayout_4.addLayout(self.add_event_layout, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.__local_save_animateur)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("add_event_dialog", u"Ajout d'un animateur", None))
        self.titre.setText(QCoreApplication.translate("add_event_dialog", u"Cin\u00e9-Club", None))
        self.email_animateur_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez l'adresse email de l'animateur", None))
        self.prenom_animateur.setText(QCoreApplication.translate("add_event_dialog", u"Pr\u00e9nom", None))
        self.prenom_animateur_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez le pr\u00e9nom de l'animateur", None))
        self.metier_animateur_combo.setItemText(0, QCoreApplication.translate("add_event_dialog", u"Membre du club", None))
        self.metier_animateur_combo.setItemText(1, QCoreApplication.translate("add_event_dialog", u"Artiste", None))
        self.metier_animateur_combo.setItemText(2, QCoreApplication.translate("add_event_dialog", u"Critique", None))
        self.metier_animateur_combo.setItemText(3, QCoreApplication.translate("add_event_dialog", u"Technicien", None))
        self.metier_animateur_combo.setItemText(4, QCoreApplication.translate("add_event_dialog", u"Autre", None))

        self.adresse_animateur_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez l'adresse de l'animateur", None))
        self.nom_animateur_label.setText(QCoreApplication.translate("add_event_dialog", u"Nom", None))
        self.email_animateur_label.setText(QCoreApplication.translate("add_event_dialog", u"Email", None))
        self.metier_animateur_label.setText(QCoreApplication.translate("add_event_dialog", u"M\u00e9tier", None))
        self.adresse_animateur_label.setText(QCoreApplication.translate("add_event_dialog", u"Adresse", None))
        self.nom_animateur_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez le nom de l'animateur", None))
    # retranslateUi

    def __local_save_animateur(self):
        email = self.email_animateur_edit.text()
        nom = self.nom_animateur_edit.text()
        prenom = self.prenom_animateur_edit.text()
        adresse = self.adresse_animateur_edit.toPlainText()
        
        if email == "" or nom == "" or prenom == "" or adresse == "":
            self.reject()
        else:
            metier = Metier.AUTRE
            if self.metier_animateur_combo.currentText() == "Membre du club":
                metier = Metier.MEMBRE_CLUB
            elif self.metier_animateur_combo.currentText() == "Artiste":
                metier = Metier.ARTISTE
            elif self.metier_animateur_combo.currentText() == "Critique":
                metier = Metier.CRITIQUE
            elif self.metier_animateur_combo.currentText() == "Technicien":
                metier = Metier.TECHNICIEN
            self.__potential_new_animateur = Utilisateur(None, email, None, nom, prenom, adresse, metier)
            self.accept()

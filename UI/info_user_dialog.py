# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from Models.disponibilite import Statut


class Ui_info_user_dialog(QDialog):
    
    def __init__(self, parent=None, user=None):
        super().__init__(parent, Qt.WindowFlags())
        self.__user = user
        self.__setupUi()
        self.__inject()
        
    def __inject(self):
        if self.__user == None:
            self.close()
        else:
            self.identifiant_user_value.setText("Utilisateur #%04d" % self.__user.id)
            self.nom_prenom_user_value.setText(str(self.__user))
            self.adresse_user_value.setText(self.__user.adresse)
            self.email_user_value.setText(self.__user.email)
            self.metier_user_value.setText(self.__user.metier_str)
            if self.__user.disponibilite != None:
                if self.__user.disponibilite.statut == Statut.DISPONIBLE:
                    self.disponibilite_user_value.setStyleSheet("color: #12D11C")
                else:
                    self.disponibilite_user_value.setStyleSheet("color: #FFCD42")
                self.disponibilite_user_value.setText(str(self.__user.disponibilite))
            else:
                self.disponibilite_user_label.hide()
                self.disponibilite_user_value.hide()

    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_user_dialog")
        self.setMinimumSize(QSize(300, 300))
        self.setStyleSheet(open("UI/styles/base_style.css").read())
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 499, 460))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.identifiant_user_value = QLabel(self.scrollAreaWidgetContents)
        self.identifiant_user_value.setObjectName(u"identifiant_user_value")
        self.identifiant_user_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.identifiant_user_value, 0, 0, 2, 2)

        self.nom_prenom_user_label = QLabel(self.scrollAreaWidgetContents)
        self.nom_prenom_user_label.setObjectName(u"nom_prenom_user_label")
        self.nom_prenom_user_label.setMinimumSize(QSize(100, 0))
        self.nom_prenom_user_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.nom_prenom_user_label, 2, 0, 1, 1)

        self.metier_user_label = QLabel(self.scrollAreaWidgetContents)
        self.metier_user_label.setObjectName(u"metier_user_label")
        self.metier_user_label.setMinimumSize(QSize(100, 0))
        self.metier_user_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.metier_user_label, 5, 0, 1, 1)

        self.email_user_label = QLabel(self.scrollAreaWidgetContents)
        self.email_user_label.setObjectName(u"email_user_label")
        self.email_user_label.setMinimumSize(QSize(100, 0))
        self.email_user_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.email_user_label, 3, 0, 1, 1)

        self.disponibilite_user_label = QLabel(self.scrollAreaWidgetContents)
        self.disponibilite_user_label.setObjectName(u"disponibilite_user_label")
        self.disponibilite_user_label.setMinimumSize(QSize(100, 0))
        self.disponibilite_user_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.disponibilite_user_label, 6, 0, 1, 1)

        self.nom_prenom_user_value = QLabel(self.scrollAreaWidgetContents)
        self.nom_prenom_user_value.setObjectName(u"nom_prenom_user_value")

        self.add_event_layout.addWidget(self.nom_prenom_user_value, 2, 1, 1, 1)

        self.email_user_value = QLabel(self.scrollAreaWidgetContents)
        self.email_user_value.setObjectName(u"email_user_value")

        self.add_event_layout.addWidget(self.email_user_value, 3, 1, 1, 1)

        self.adresse_user_value = QLabel(self.scrollAreaWidgetContents)
        self.adresse_user_value.setObjectName(u"adresse_user_value")

        self.add_event_layout.addWidget(self.adresse_user_value, 4, 1, 1, 1)

        self.metier_user_value = QLabel(self.scrollAreaWidgetContents)
        self.metier_user_value.setObjectName(u"metier_user_value")

        self.add_event_layout.addWidget(self.metier_user_value, 5, 1, 1, 1)

        self.disponibilite_user_value = QLabel(self.scrollAreaWidgetContents)
        self.disponibilite_user_value.setObjectName(u"disponibilite_user_value")

        self.add_event_layout.addWidget(self.disponibilite_user_value, 6, 1, 1, 1)

        self.adresse_user_label = QLabel(self.scrollAreaWidgetContents)
        self.adresse_user_label.setObjectName(u"adresse_user_label")
        self.adresse_user_label.setMinimumSize(QSize(100, 0))
        self.adresse_user_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.adresse_user_label, 4, 0, 1, 1)

        self.add_event_layout.setRowStretch(1, 1)
        self.add_event_layout.setRowStretch(2, 1)
        self.add_event_layout.setRowStretch(3, 1)
        self.add_event_layout.setRowStretch(4, 1)
        self.add_event_layout.setRowStretch(5, 1)
        self.add_event_layout.setRowStretch(6, 1)
        self.add_event_layout.setRowMinimumHeight(0, 5)

        self.gridLayout_4.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_user_dialog", u"D\u00e9tails d'un utilisateur", None))
        self.titre.setText(QCoreApplication.translate("info_user_dialog", u"Cin\u00e9-Club", None))
        self.identifiant_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.nom_prenom_user_label.setText(QCoreApplication.translate("info_user_dialog", u"Nom / Pr\u00e9nom", None))
        self.metier_user_label.setText(QCoreApplication.translate("info_user_dialog", u"Metier", None))
        self.email_user_label.setText(QCoreApplication.translate("info_user_dialog", u"Email", None))
        self.disponibilite_user_label.setText(QCoreApplication.translate("info_user_dialog", u"Disponibilit\u00e9", None))
        self.nom_prenom_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.email_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.adresse_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.metier_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.disponibilite_user_value.setText(QCoreApplication.translate("info_user_dialog", u"TextLabel", None))
        self.adresse_user_label.setText(QCoreApplication.translate("info_user_dialog", u"Adresse", None))
    # retranslateUi


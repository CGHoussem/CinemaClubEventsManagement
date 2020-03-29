# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billeterie_event_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from DAO.DAOs import BilleterieDAO

from UI.info_salle_dialog import Ui_info_salle_dialog
from UI.vendre_reserver_billet_dialog import Ui_vendre_reserver_billet_dialog
from UI.rembourser_billet_dialog import Ui_rembourser_billet_dialog
class Ui_billeterie_event_dialog(QDialog):
    def __init__(self, parent=None, evenement=None):
        super().__init__(parent, Qt.WindowFlags())
        self.__evenement = evenement
        self.__billeterie = BilleterieDAO.get_by_event_id(self.__evenement)
        
        self.setupUi()
        self.inject()
        self.signals()
    
    @pyqtSlot()
    def __ouvrir_salle_dialog(self):
        """
        Cette fonction permet d'ouvrir la dialog de la salle
        """
        Ui_info_salle_dialog(self, Qt.WindowFlags(), self.__evenement.salle).show()

    @pyqtSlot()
    def __ouvrir_vendre_reservee_dialog(self, t):
        if t == 1:
            # Vendre
            d = Ui_vendre_reserver_billet_dialog(self, False, self.__evenement, self.__billeterie)
        else:
            # Reserver
            d = Ui_vendre_reserver_billet_dialog(self, True, self.__evenement, self.__billeterie)
        d.exec_()
        
        self.__billeterie = BilleterieDAO.get_by_event_id(self.__evenement)
        self.inject()
        
    @pyqtSlot()
    def __ouvrir_rembourser_dialog(self):
        d = Ui_rembourser_billet_dialog(self, self.__billeterie)
        d.exec_()
        self.__billeterie = BilleterieDAO.get_by_event_id(self.__evenement)
        self.inject()

    def signals(self):
        """
        Cette fonction permet d'établir les signaux des boutons
        """
        self.evenement_salle_btn.clicked.connect(self.__ouvrir_salle_dialog)
        self.vendre_ticket_btn.clicked.connect(lambda: self.__ouvrir_vendre_reservee_dialog(1))
        self.reserver_place_btn.clicked.connect(lambda: self.__ouvrir_vendre_reservee_dialog(2))
        self.rembourser_ticket_btn.clicked.connect(self.__ouvrir_rembourser_dialog)
    
    def inject(self):
        """
        Cette fonction permet de remplir les attributs de l'interface graphique
        """
        self.evenement_identifiant_value.setText(self.__evenement.nom)
        self.evenement_place_standard_value.setText(str(self.__billeterie.nbr_place_standard_disponible))
        self.evenement_place_premium_value.setText(str(self.__billeterie.nbr_place_premium_disponible))
        places_vendues =\
            (self.__evenement.salle.nbr_place_standard+self.__evenement.salle.nbr_place_premium)-\
                (self.__billeterie.nbr_place_standard_disponible+self.__billeterie.nbr_place_premium_disponible)
        self.evenement_place_vendues_value.setText(str(places_vendues))
        self.evenement_place_reservees_value.setText(str(self.__billeterie.nbr_place_reservee))
        self.evenement_place_standard_prix.setText("%.2f €" % self.__billeterie.prix_place_standard)
        self.evenement_place_premium_prix.setText("%.2f €" % self.__billeterie.prix_place_premium)
        self.evenement_salle_identifiant_value.setText(str(self.__evenement.salle))
    
    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_projection_dialog")
        self.resize(500, 600)
        self.setMinimumSize(QSize(500, 600))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 523))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.evenement_place_premium_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_premium_value.setObjectName(u"evenement_place_premium_value")

        self.add_event_layout.addWidget(self.evenement_place_premium_value, 3, 2, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label_13, 9, 1, 1, 1)

        self.evenement_salle_btn = QPushButton(self.scrollAreaWidgetContents)
        self.evenement_salle_btn.setObjectName(u"evenement_salle_btn")

        self.add_event_layout.addWidget(self.evenement_salle_btn, 12, 2, 1, 1)

        self.evenement_place_reservees_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_reservees_value.setObjectName(u"evenement_place_reservees_value")

        self.add_event_layout.addWidget(self.evenement_place_reservees_value, 5, 2, 1, 1)

        self.evenement_place_premium_prix = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_premium_prix.setObjectName(u"evenement_place_premium_prix")

        self.add_event_layout.addWidget(self.evenement_place_premium_prix, 8, 2, 1, 1)

        self.evenement_identifiant_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_identifiant_value.setObjectName(u"evenement_identifiant_value")
        self.evenement_identifiant_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.evenement_identifiant_value, 0, 0, 1, 3)

        self.evenement_place_standard_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_standard_value.setObjectName(u"evenement_place_standard_value")

        self.add_event_layout.addWidget(self.evenement_place_standard_value, 2, 2, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label_12, 8, 1, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 10))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.add_event_layout.addWidget(self.line_4, 1, 0, 1, 3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label_4, 3, 1, 1, 1)

        self.evenement_place_standard_prix = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_standard_prix.setObjectName(u"evenement_place_standard_prix")

        self.add_event_layout.addWidget(self.evenement_place_standard_prix, 9, 2, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(0, 10))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.add_event_layout.addWidget(self.line_2, 6, 0, 1, 3)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")

        self.add_event_layout.addWidget(self.label_7, 4, 0, 1, 2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.add_event_layout.addWidget(self.label_2, 2, 0, 2, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.add_event_layout.addWidget(self.label_11, 7, 0, 1, 2)

        self.evenement_salle_identifiant_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_salle_identifiant_value.setObjectName(u"evenement_salle_identifiant_value")

        self.add_event_layout.addWidget(self.evenement_salle_identifiant_value, 12, 1, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.add_event_layout.addWidget(self.label_16, 11, 0, 1, 2)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")

        self.add_event_layout.addWidget(self.label_9, 5, 0, 1, 2)

        self.evenement_place_vendues_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_place_vendues_value.setObjectName(u"evenement_place_vendues_value")

        self.add_event_layout.addWidget(self.evenement_place_vendues_value, 4, 2, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 10))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.add_event_layout.addWidget(self.line_3, 10, 0, 1, 3)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vendre_ticket_btn = QPushButton(self.widget)
        self.vendre_ticket_btn.setObjectName(u"vendre_ticket_btn")

        self.verticalLayout_2.addWidget(self.vendre_ticket_btn)

        self.reserver_place_btn = QPushButton(self.widget)
        self.reserver_place_btn.setObjectName(u"reserver_place_btn")

        self.verticalLayout_2.addWidget(self.reserver_place_btn)

        self.rembourser_ticket_btn = QPushButton(self.widget)
        self.rembourser_ticket_btn.setObjectName(u"rembourser_ticket_btn")

        self.verticalLayout_2.addWidget(self.rembourser_ticket_btn)


        self.add_event_layout.addWidget(self.widget, 14, 0, 1, 3)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label_3, 2, 1, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 10))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.add_event_layout.addWidget(self.line_5, 13, 0, 1, 3)


        self.gridLayout_4.addLayout(self.add_event_layout, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_projection_dialog", u"D\u00e9tails de la projection", None))
        self.titre.setText(QCoreApplication.translate("info_projection_dialog", u"Cin\u00e9-Club", None))
        self.evenement_place_premium_value.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("info_projection_dialog", u"Place Standard", None))
        self.evenement_salle_btn.setText(QCoreApplication.translate("info_projection_dialog", u"Savoir Plus", None))
        self.evenement_place_reservees_value.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.evenement_place_premium_prix.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.evenement_identifiant_value.setText(QCoreApplication.translate("info_projection_dialog", u"\u00c9v\u00e8nement #0002", None))
        self.evenement_place_standard_value.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("info_projection_dialog", u"Place Premium", None))
        self.label_4.setText(QCoreApplication.translate("info_projection_dialog", u"Premium", None))
        self.evenement_place_standard_prix.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("info_projection_dialog", u"Nombre de places vendues", None))
        self.label_2.setText(QCoreApplication.translate("info_projection_dialog", u"Nombre de places disponbiles", None))
        self.label_11.setText(QCoreApplication.translate("info_projection_dialog", u"Les prix des places", None))
        self.evenement_salle_identifiant_value.setText(QCoreApplication.translate("info_projection_dialog", u"Salle #0005", None))
        self.label_16.setText(QCoreApplication.translate("info_projection_dialog", u"La salle de l'\u00e9v\u00e8nement", None))
        self.label_9.setText(QCoreApplication.translate("info_projection_dialog", u"Nombre de places r\u00e9serv\u00e9es", None))
        self.evenement_place_vendues_value.setText(QCoreApplication.translate("info_projection_dialog", u"TextLabel", None))
        self.vendre_ticket_btn.setText(QCoreApplication.translate("info_projection_dialog", u"Vendre un ticket", None))
        self.reserver_place_btn.setText(QCoreApplication.translate("info_projection_dialog", u"R\u00e9server une place", None))
        self.rembourser_ticket_btn.setText(QCoreApplication.translate("info_projection_dialog", u"Rembourser un ticket", None))
        self.label_3.setText(QCoreApplication.translate("info_projection_dialog", u"Standard", None))
    # retranslateUi


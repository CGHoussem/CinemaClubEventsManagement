# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from DAO.DAOs import BilletDAO


class Ui_rembourser_billet_dialog(QDialog):
    def __init__(self, parent=None, billeterie=None):
        super().__init__(parent=parent,flags=Qt.WindowFlags())
        
        self.__billeterie= billeterie
        self.__personnes = []
        self.__index_billet = 0
        for b in self.__billeterie.billets:
            self.__personnes.append("%s %s" % (b.nom.upper(), b.prenom))
        
        self.setupUi()
        self.__signals()
        self.__inject()

    @pyqtSlot(int)
    def __update_ui(self, index):
        personne = self.__personnes[index]
        billet = self.__billeterie.billets[index]
        self.__index_billet = index
        
        if billet != None:
            # Réference Ticket
            self.ref_ticket_value.setText("#%04d" % billet.id)
            # La place
            if billet.place.type_place==1:
                self.place_value.setText("#%02d (Standard)" % billet.place.num)
            else:
                self.place_value.setText("#%02d (Premium)" % billet.place.num)

    @pyqtSlot()
    def __rembourser_billet(self):
        """
        Cette fonction permet de rembourser un ticket/billet
        """
        billet = self.__billeterie.billets[self.__index_billet]
        if BilletDAO.rembourser_billet(billet, self.__billeterie):
            QMessageBox.information(self, "Remboursement d'un ticket", "Le ticket a été rembourser avec succée!")
            self.close()
        else:
            QMessageBox.warning(self, "Remboursement d'un ticket", "Erreur lors du remboursement du ticket!")
        
    def __inject(self):
        self.personne_combobox.addItems(self.__personnes)
        # Réference Ticket
        self.ref_ticket_value.setText("#%04d" % self.__billeterie.billets[0].id)
        # La place
        if self.__billeterie.billets[0].place.type_place==1:
            self.place_value.setText("#%02d (Standard)" % self.__billeterie.billets[0].place.num)
        else:
            self.place_value.setText("#%02d (Premium)" % self.__billeterie.billets[0].place.num)
        
    def __signals(self):
        self.rembourser_btn.clicked.connect(self.__rembourser_billet)
        self.personne_combobox.currentIndexChanged.connect(self.__update_ui)
    
    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"rembourser_billet_dialog")
        self.setWindowModality(Qt.WindowModal)
        self.resize(538, 287)
        self.setStyleSheet(u"")
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 518, 233))
        self._2 = QGridLayout(self.scrollAreaWidgetContents)
        self._2.setObjectName(u"_2")
        self._3 = QGridLayout()
        self._3.setObjectName(u"_3")
        self.evenement_nom_value = QLabel(self.scrollAreaWidgetContents)
        self.evenement_nom_value.setObjectName(u"evenement_nom_value")
        self.evenement_nom_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self._3.addWidget(self.evenement_nom_value, 0, 0, 2, 2)

        self.vendre_reserver_groupbox = QGroupBox(self.scrollAreaWidgetContents)
        self.vendre_reserver_groupbox.setObjectName(u"vendre_reserver_groupbox")
        self.formLayout = QFormLayout(self.vendre_reserver_groupbox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.vendre_reserver_groupbox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_4 = QLabel(self.vendre_reserver_groupbox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.rembourser_btn = QPushButton(self.vendre_reserver_groupbox)
        self.rembourser_btn.setObjectName(u"rembourser_btn")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.rembourser_btn)

        self.personne_combobox = QComboBox(self.vendre_reserver_groupbox)
        self.personne_combobox.setObjectName(u"personne_combobox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.personne_combobox)

        self.label_2 = QLabel(self.vendre_reserver_groupbox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.place_value = QLabel(self.vendre_reserver_groupbox)
        self.place_value.setObjectName(u"place_value")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.place_value)

        self.ref_ticket_value = QLabel(self.vendre_reserver_groupbox)
        self.ref_ticket_value.setObjectName(u"ref_ticket_value")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ref_ticket_value)


        self._3.addWidget(self.vendre_reserver_groupbox, 2, 0, 1, 2)

        self._3.setRowStretch(1, 1)
        self._3.setRowStretch(2, 2)

        self._2.addLayout(self._3, 0, 0, 1, 1)

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
        self.setWindowTitle(QCoreApplication.translate("rembourser_billet_dialog", u"Rembourser un ticket", None))
        self.titre.setText(QCoreApplication.translate("rembourser_billet_dialog", u"Cin\u00e9-Club", None))
        self.evenement_nom_value.setText(QCoreApplication.translate("rembourser_billet_dialog", u"TextLabel", None))
        self.vendre_reserver_groupbox.setTitle(QCoreApplication.translate("rembourser_billet_dialog", u"Remboursement d'un ticket", None))
        self.label.setText(QCoreApplication.translate("rembourser_billet_dialog", u"Personne", None))
        self.label_4.setText(QCoreApplication.translate("rembourser_billet_dialog", u"REF Ticket", None))
        self.rembourser_btn.setText(QCoreApplication.translate("rembourser_billet_dialog", u"Rembourser", None))
        self.label_2.setText(QCoreApplication.translate("rembourser_billet_dialog", u"Place", None))
        self.place_value.setText(QCoreApplication.translate("rembourser_billet_dialog", u"TextLabel", None))
        self.ref_ticket_value.setText(QCoreApplication.translate("rembourser_billet_dialog", u"TextLabel", None))
    # retranslateUi


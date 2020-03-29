# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from DAO.DAOs import BilletDAO
from Models.billet import Billet, Place


class Ui_vendre_reserver_billet_dialog(QDialog):
    
    def __init__(self, parent=None, reserve=False, event=None, billeterie=None):
        super().__init__(parent, Qt.WindowFlags())
        self.__event = event
        self.__billeterie = billeterie
        self.setupUi()
        self.inject(reserve)
        self.signals(reserve)

    def verif_champs(self):
        nom = self.personne_nom_edit.text()
        prenom = self.personne_prenom_edit.text()
        tel = self.personne_tel_edit.text()
        type_place = self.type_place_combobox.currentIndex() + 1
        
        if len(nom)==0 or len(prenom)==0 or len(tel) == 0:
            QMessageBox.warning(self, "Erreur dans la formulaire", "Erreur! Il faut saisir tout les champs")
            return None
        
        return (nom, prenom, tel, type_place)

    @pyqtSlot()
    def __reserver_place(self):
        """
        Cette fonction permet de réserver une place
        """
        ret = self.verif_champs()
        if ret != None:
            (nom, prenom, tel, type_place) = ret
            place = Place(len(self.__billeterie.billets), type_place)
            billet = Billet(None, self.__event, place, nom, prenom, tel)
            if BilletDAO.reserver_billet(billet, self.__billeterie):
                QMessageBox.information(self, "Réservation d'une place", "La réservation a été établit avec succée!")
                self.close()
            else:
                QMessageBox.warning(self, "Réservation d'une place", "Erreur de la réservation de la place!")
            

    @pyqtSlot()
    def __vendre_billet(self):
        """
        Cette fonction permet de vendre un billet
        """
        ret = self.verif_champs()
        if ret != None:
            (nom, prenom, tel, type_place) = ret
            place = Place(len(self.__billeterie.billets), type_place)
            billet = Billet(None, self.__event, place, nom, prenom, tel)
            if BilletDAO.add_billet(billet, self.__billeterie):
                QMessageBox.information(self, "Vente d'un billet", "La vente du billet a été faite avec succée!")
                self.close()
            else:
                QMessageBox.warning(self, "Vente d'un billet", "Erreur de la vente du billet!")
    def signals(self, reserve):
        if reserve:
            self.vendre_reserver_btn.clicked.connect(self.__reserver_place)
        else:
            self.vendre_reserver_btn.clicked.connect(self.__vendre_billet)

    def inject(self, reserve):
        if not reserve:
            # Vendre
            self.setWindowTitle("Vente d'un ticket")
            self.vendre_reserver_btn.setText("Vendre")
            self.vendre_reserver_groupbox.setTitle("Vente d'un ticket")

    def setupUi(self):
        if self.objectName():
            self.setObjectName(u"vendre_reserver_billet_dialog")
        self.setWindowModality(Qt.WindowModal)
        self.resize(538, 410)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 518, 333))
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
        self.label_4 = QLabel(self.vendre_reserver_groupbox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.type_place_combobox = QComboBox(self.vendre_reserver_groupbox)
        self.type_place_combobox.addItem("")
        self.type_place_combobox.addItem("")
        self.type_place_combobox.setObjectName(u"type_place_combobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.type_place_combobox.sizePolicy().hasHeightForWidth())
        self.type_place_combobox.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.type_place_combobox)

        self.groupBox_2 = QGroupBox(self.vendre_reserver_groupbox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.personne_nom_edit = QLineEdit(self.groupBox_2)
        self.personne_nom_edit.setObjectName(u"personne_nom_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.personne_nom_edit.sizePolicy().hasHeightForWidth())
        self.personne_nom_edit.setSizePolicy(sizePolicy3)
        self.personne_nom_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.personne_nom_edit, 0, 1, 1, 1)

        self.personne_prenom_edit = QLineEdit(self.groupBox_2)
        self.personne_prenom_edit.setObjectName(u"personne_prenom_edit")
        sizePolicy3.setHeightForWidth(self.personne_prenom_edit.sizePolicy().hasHeightForWidth())
        self.personne_prenom_edit.setSizePolicy(sizePolicy3)
        self.personne_prenom_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.personne_prenom_edit, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.personne_tel_edit = QLineEdit(self.groupBox_2)
        self.personne_tel_edit.setObjectName(u"personne_tel_edit")
        sizePolicy3.setHeightForWidth(self.personne_tel_edit.sizePolicy().hasHeightForWidth())
        self.personne_tel_edit.setSizePolicy(sizePolicy3)
        self.personne_tel_edit.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.personne_tel_edit, 2, 1, 1, 1)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.groupBox_2)

        self.vendre_reserver_btn = QPushButton(self.vendre_reserver_groupbox)
        self.vendre_reserver_btn.setObjectName(u"vendre_reserver_btn")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.vendre_reserver_btn)


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
        self.setWindowTitle(QCoreApplication.translate("vendre_reserver_billet_dialog", u"R\u00e9servation d'une place", None))
        self.titre.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Cin\u00e9-Club", None))
        self.evenement_nom_value.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"TextLabel", None))
        self.vendre_reserver_groupbox.setTitle(QCoreApplication.translate("vendre_reserver_billet_dialog", u"R\u00e9servation d'une place", None))
        self.label_4.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Type de place", None))
        self.type_place_combobox.setItemText(0, QCoreApplication.translate("vendre_reserver_billet_dialog", u"Standard", None))
        self.type_place_combobox.setItemText(1, QCoreApplication.translate("vendre_reserver_billet_dialog", u"Premium", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Informations de la personne", None))
        self.label_2.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Pr\u00e9nom", None))
        self.label.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Nom", None))
        self.label_3.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"Num\u00e9ro de tel", None))
        self.vendre_reserver_btn.setText(QCoreApplication.translate("vendre_reserver_billet_dialog", u"R\u00e9server", None))
    # retranslateUi


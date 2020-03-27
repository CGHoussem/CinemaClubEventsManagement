# -*- coding: utf-8 -*-

from PyQt5.QtCore import QCoreApplication, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, pyqtSlot
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from Models.evenement import Etat

from UI.info_salle_dialog import Ui_info_salle_dialog
from UI.info_projection_dialog import Ui_info_projection_dialog

from DAO.DAOs import EvenementDAO, ProjectionDAO
from UI.info_user_dialog import Ui_info_user_dialog

class Ui_info_event_dialog(QDialog):
    def __init__(self, parent, evenement=None):
        super().__init__(parent, Qt.WindowFlags())
        self.__evenement = evenement
       
        self.__reservation_salle = self.__evenement.salle_reservee
        self.__disponibilite_invites = self.__evenement.disponibilite_invites
        self.__amuses_bouches_debat = True
        if self.__evenement.est_projection:
            if self.__evenement.debat != None:
                self.__amuses_bouches_debat = self.__evenement.amuses_bouches

        self.__setupUi()
        self.__setup_signals()
        self.__check_and_design_validation_button()
        self.__inject() 

    def __setup_signals(self):
        """
        Cette fonction permet de définir les fonctions de signaux des bouttons
        """
        if self.__evenement.etat == Etat.EN_ATTENTE:
            self.prendre_charge_btn.clicked.connect(lambda: self.__change_etat_evenement(Etat.EN_COURS))
        elif self.__evenement.etat == Etat.EN_COURS:
            self.prendre_charge_btn.clicked.connect(lambda: self.__change_etat_evenement(Etat.TERMINE))
        
        self.invites_disponbile_checkbox.stateChanged.connect(self.__disponibilite_invites_state)
        self.amuses_bouches_checkbox.stateChanged.connect(self.__amuses_bouches_state)
        self.reserver_salle_checkbox.stateChanged.connect(self.__reserver_salle_state)
        self.responsable_list_widget.itemDoubleClicked.connect(self.__ouvrir_responsable_dialog)
        self.salle_info_btn.clicked.connect(self.__open_salle_dialog)
        self.projection_evenement_btn.clicked.connect(self.__ouvrir_projection_dialog)

    def __check_and_design_validation_button(self):
        """
        Cette fonction permet de colorier la boutton de validation de l'évènement
        """
        print(self.__reservation_salle, self.__disponibilite_invites, self.__amuses_bouches_debat)
        if self.__reservation_salle and self.__disponibilite_invites and self.__amuses_bouches_debat:
            self.prendre_charge_btn.setStyleSheet(open("UI/styles/success_button.css").read())
            self.prendre_charge_btn.setEnabled(True)
        elif self.__evenement.etat != Etat.EN_ATTENTE:
            self.prendre_charge_btn.setStyleSheet(open("UI/styles/warning_button.css").read())
            self.prendre_charge_btn.setEnabled(False)

    @pyqtSlot()
    def __reserver_salle_state(self):
        """
        Cette fonction est une fonction de signal qui permet l'attribution de la variable self.__reserver_salle_state
        """
        state = self.reserver_salle_checkbox.checkState()
        self.__reservation_salle=(state==Qt.Checked)
        self.__evenement.salle_reservee = self.__reservation_salle
        EvenementDAO.update_evenement(self.__evenement)
        self.__check_and_design_validation_button()
    @pyqtSlot()
    def __disponibilite_invites_state(self):
        """
        Cette fonction est une fonction de signal qui permet l'attribution de la variable self.__disponibilite_invites
        """
        state = self.invites_disponbile_checkbox.checkState()
        self.__disponibilite_invites=(state==Qt.Checked)
        self.__evenement.disponibilite_invites = self.__disponibilite_invites
        EvenementDAO.update_evenement(self.__evenement)
        self.__check_and_design_validation_button()
    @pyqtSlot()
    def __amuses_bouches_state(self):
        """
        Cette fonction est une fonction de signal qui permet l'attribution de la variable self.__amuses_bouches_state
        """
        state = self.amuses_bouches_checkbox.checkState()
        self.__amuses_bouches_debat=(state==Qt.Checked)
        self.__evenement.amuses_bouches = self.__amuses_bouches_debat
        ProjectionDAO.update_projection(self.__evenement)
        self.__check_and_design_validation_button()
   
    @pyqtSlot()
    def __ouvrir_responsable_dialog(self):
        """
        Cette fonction permet d'ouvrir la dialog du profile de l'utilisateur
        """
        indexes = self.responsable_list_widget.selectedIndexes()
        if len(indexes) > 0:
            responsable = self.__evenement.responsables[indexes[0].row()]
            Ui_info_user_dialog(self, responsable).show()
        
    @pyqtSlot()
    def __ouvrir_projection_dialog(self):
        dialog = Ui_info_projection_dialog(self, projection=self.__evenement)
        dialog.exec_()
        self.__amuses_bouches_debat = dialog.est_debat_valider
        self.__check_and_design_validation_button()

    @pyqtSlot()
    def __change_etat_evenement(self, etat):
        """
        Cette fonction permet de changer l'etat de l'évènement
        """
        if etat == Etat.EN_COURS:
            self.__evenement.etat = etat
            EvenementDAO.update_state(self.__evenement)
            self.prendre_charge_btn.clicked.connect(lambda: self.__change_etat_evenement(Etat.TERMINE))
            self.prendre_charge_btn.setText("Valider")
            self.__check_and_design_validation_button()
        elif etat == Etat.TERMINE:
            if self.__reservation_salle and self.__disponibilite_invites and self.__amuses_bouches_debat:
                self.__evenement.etat = etat
                EvenementDAO.update_state(self.__evenement)

                self.dashboard_page.hide()

                QMessageBox.information(self, "Etat de l'évènement", "L'évènement a été valider et terminer!")

    @pyqtSlot()
    def __open_salle_dialog(self):
        dialog = Ui_info_salle_dialog(self, Qt.WindowFlags(), self.__evenement.salle)
        dialog.show()

    def __inject(self):
        if self.__evenement.etat != Etat.TERMINE:
            if self.__evenement.salle_reservee:
                self.reserver_salle_checkbox.setCheckState(Qt.Checked)
            if self.__evenement.disponibilite_invites:
                self.invites_disponbile_checkbox.setCheckState(Qt.Checked)
            if self.__evenement.est_projection and self.__evenement.amuses_bouches:
                self.amuses_bouches_checkbox.setCheckState(Qt.Checked)
            
        if self.__evenement.etat == Etat.EN_ATTENTE:
            self.prendre_charge_btn.setText("Prendre en charge")
        elif self.__evenement.etat == Etat.EN_COURS:
            self.prendre_charge_btn.setText("Valider l'évènement")
        else:
            self.dashboard_page.hide()
        
        if self.__evenement.est_projection:
            self.projection_evenement_btn.setText("Cette évènement est une projection. Savoir plus!")
            if self.__evenement.debat == None:
                self.amuses_bouches_label.hide()
                self.amuses_bouches_checkbox.hide()
                self.__amuses_bouches_debat = True
        else:
            self.projection_evenement_btn.hide()
            self.amuses_bouches_label.hide()
            self.amuses_bouches_checkbox.hide()

        self.nom_evenement_value.setText(self.__evenement.nom)
        self.description_evenement_value.setText(self.__evenement.description)
        for r in self.__evenement.responsables:
            self.responsable_list_widget.addItem(str(r))
        self.salle_label_value.setText(str(self.__evenement.salle))
        self.color_evenement_frame.setStyleSheet("background-color: %s" % self.__evenement.color)

    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_event_dialog")
        self.resize(600, 672)
        self.setMinimumSize(QSize(600, 600))
        self.setStyleSheet(open("UI/styles/base_style.css", "r").read())
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 655, 641))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.toolBox = QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName(u"toolBox")
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.info_page.setGeometry(QRect(0, 0, 637, 569))
        self.gridLayout = QGridLayout(self.info_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.date_fin_evenement_value = QLabel(self.info_page)
        self.date_fin_evenement_value.setObjectName(u"date_fin_evenement_value")

        self.add_event_layout.addWidget(self.date_fin_evenement_value, 5, 1, 1, 1)

        self.description_evenement_label = QLabel(self.info_page)
        self.description_evenement_label.setObjectName(u"description_evenement_label")

        self.add_event_layout.addWidget(self.description_evenement_label, 2, 0, 1, 1, Qt.AlignTop)

        self.date_debut_evenement_value = QLabel(self.info_page)
        self.date_debut_evenement_value.setObjectName(u"date_debut_evenement_value")

        self.add_event_layout.addWidget(self.date_debut_evenement_value, 4, 1, 1, 1)

        self.projection_evenement_btn = QPushButton(self.info_page)
        self.projection_evenement_btn.setObjectName(u"projection_evenement_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projection_evenement_btn.sizePolicy().hasHeightForWidth())
        self.projection_evenement_btn.setSizePolicy(sizePolicy2)

        self.add_event_layout.addWidget(self.projection_evenement_btn, 8, 0, 1, 2, Qt.AlignLeft)

        self.salle_label = QLabel(self.info_page)
        self.salle_label.setObjectName(u"salle_label")

        self.add_event_layout.addWidget(self.salle_label, 6, 0, 1, 1)

        self.date_fin_label = QLabel(self.info_page)
        self.date_fin_label.setObjectName(u"date_fin_label")

        self.add_event_layout.addWidget(self.date_fin_label, 5, 0, 1, 1)

        self.date_debut_label = QLabel(self.info_page)
        self.date_debut_label.setObjectName(u"date_debut_label")

        self.add_event_layout.addWidget(self.date_debut_label, 4, 0, 1, 1)

        self.responsables_label = QLabel(self.info_page)
        self.responsables_label.setObjectName(u"responsables_label")

        self.add_event_layout.addWidget(self.responsables_label, 3, 0, 1, 1)

        self.event_color_label = QLabel(self.info_page)
        self.event_color_label.setObjectName(u"event_color_label")

        self.add_event_layout.addWidget(self.event_color_label, 7, 0, 1, 1)

        self.color_evenement_frame = QFrame(self.info_page)
        self.color_evenement_frame.setObjectName(u"color_evenement_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.color_evenement_frame.sizePolicy().hasHeightForWidth())
        self.color_evenement_frame.setSizePolicy(sizePolicy3)
        self.color_evenement_frame.setMinimumSize(QSize(50, 50))
        self.color_evenement_frame.setStyleSheet(u"background-color: rgb(255, 170, 255)")
        self.color_evenement_frame.setFrameShape(QFrame.StyledPanel)
        self.color_evenement_frame.setFrameShadow(QFrame.Raised)

        self.add_event_layout.addWidget(self.color_evenement_frame, 7, 1, 1, 1)

        self.nom_evenement_value = QLabel(self.info_page)
        self.nom_evenement_value.setObjectName(u"nom_evenement_value")
        self.nom_evenement_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.nom_evenement_value, 0, 0, 2, 2)

        self.responsable_list_widget = QListWidget(self.info_page)
        self.responsable_list_widget.setObjectName(u"responsable_list_widget")
        sizePolicy1.setHeightForWidth(self.responsable_list_widget.sizePolicy().hasHeightForWidth())
        self.responsable_list_widget.setSizePolicy(sizePolicy1)
        self.responsable_list_widget.setMaximumSize(QSize(300, 100))

        self.add_event_layout.addWidget(self.responsable_list_widget, 3, 1, 1, 1)

        self.salle_container = QWidget(self.info_page)
        self.salle_container.setObjectName(u"salle_container")
        self.horizontalLayout = QHBoxLayout(self.salle_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.salle_label_value = QLabel(self.salle_container)
        self.salle_label_value.setObjectName(u"salle_label_value")
        sizePolicy3.setHeightForWidth(self.salle_label_value.sizePolicy().hasHeightForWidth())
        self.salle_label_value.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.salle_label_value)

        self.salle_info_btn = QPushButton(self.salle_container)
        self.salle_info_btn.setObjectName(u"salle_info_btn")
        sizePolicy2.setHeightForWidth(self.salle_info_btn.sizePolicy().hasHeightForWidth())
        self.salle_info_btn.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.salle_info_btn, 0, Qt.AlignLeft)

        self.horizontalLayout.setStretch(1, 1)

        self.add_event_layout.addWidget(self.salle_container, 6, 1, 1, 1, Qt.AlignLeft)

        self.description_evenement_value = QTextBrowser(self.info_page)
        self.description_evenement_value.setObjectName(u"description_evenement_value")
        sizePolicy1.setHeightForWidth(self.description_evenement_value.sizePolicy().hasHeightForWidth())
        self.description_evenement_value.setSizePolicy(sizePolicy1)
        self.description_evenement_value.setMaximumSize(QSize(16777215, 250))
        self.description_evenement_value.setReadOnly(True)

        self.add_event_layout.addWidget(self.description_evenement_value, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.toolBox.addItem(self.info_page, u"Les informations sur l'\u00e9v\u00e8nement")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.dashboard_page.setGeometry(QRect(0, 0, 637, 531))
        self.formLayout = QFormLayout(self.dashboard_page)
        self.formLayout.setObjectName(u"formLayout")
        self.reserver_salle_lable = QLabel(self.dashboard_page)
        self.reserver_salle_lable.setObjectName(u"reserver_salle_lable")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.reserver_salle_lable)

        self.reserver_salle_checkbox = QCheckBox(self.dashboard_page)
        self.reserver_salle_checkbox.setObjectName(u"reserver_salle_checkbox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.reserver_salle_checkbox)

        self.invites_label = QLabel(self.dashboard_page)
        self.invites_label.setObjectName(u"invites_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.invites_label)

        self.invites_disponbile_checkbox = QCheckBox(self.dashboard_page)
        self.invites_disponbile_checkbox.setObjectName(u"invites_disponbile_checkbox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.invites_disponbile_checkbox)

        self.amuses_bouches_label = QLabel(self.dashboard_page)
        self.amuses_bouches_label.setObjectName(u"amuses_bouches_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.amuses_bouches_label)

        self.amuses_bouches_checkbox = QCheckBox(self.dashboard_page)
        self.amuses_bouches_checkbox.setObjectName(u"amuses_bouches_checkbox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.amuses_bouches_checkbox)

        self.gerer_evenement_label = QLabel(self.dashboard_page)
        self.gerer_evenement_label.setObjectName(u"gerer_evenement_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.gerer_evenement_label)

        self.prendre_charge_btn = QPushButton(self.dashboard_page)
        self.prendre_charge_btn.setObjectName(u"prendre_charge_btn")
        sizePolicy2.setHeightForWidth(self.prendre_charge_btn.sizePolicy().hasHeightForWidth())
        self.prendre_charge_btn.setSizePolicy(sizePolicy2)
        self.prendre_charge_btn.setMinimumSize(QSize(200, 0))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.prendre_charge_btn)

        self.toolBox.addItem(self.dashboard_page, u"Les boutons de contr\u00f4le de l'\u00e9v\u00e8nement")

        self.gridLayout_4.addWidget(self.toolBox, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        #if QT_CONFIG(shortcut)
        self.description_evenement_label.setBuddy(self.description_evenement_value)
        self.salle_label.setBuddy(self.salle_info_btn)
        self.responsables_label.setBuddy(self.responsable_list_widget)
        self.salle_label_value.setBuddy(self.salle_info_btn)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.description_evenement_value)
        QWidget.setTabOrder(self.description_evenement_value, self.responsable_list_widget)
        QWidget.setTabOrder(self.responsable_list_widget, self.salle_info_btn)
        QWidget.setTabOrder(self.salle_info_btn, self.projection_evenement_btn)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_event_dialog", u"D\u00e9tails d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("info_event_dialog", u"Cin\u00e9-Club", None))
        self.date_fin_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.description_evenement_label.setText(QCoreApplication.translate("info_event_dialog", u"Description", None))
        self.date_debut_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.projection_evenement_btn.setText(QCoreApplication.translate("info_event_dialog", u"Cette \u00e9v\u00e8nement est une projection", None))
        self.salle_label.setText(QCoreApplication.translate("info_event_dialog", u"Salle", None))
        self.date_fin_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de fin", None))
        self.date_debut_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de d\u00e9but", None))
        self.responsables_label.setText(QCoreApplication.translate("info_event_dialog", u"Reponsables", None))
        self.event_color_label.setText(QCoreApplication.translate("info_event_dialog", u"Couleur", None))
        self.nom_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.salle_label_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.salle_info_btn.setText(QCoreApplication.translate("info_event_dialog", u"Plus d'infos", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.info_page), QCoreApplication.translate("info_event_dialog", u"Les informations sur l'\u00e9v\u00e8nement", None))
        self.reserver_salle_lable.setText(QCoreApplication.translate("info_event_dialog", u"R\u00e9servation de la salle", None))
        self.reserver_salle_checkbox.setText(QCoreApplication.translate("info_event_dialog", u"R\u00e9server?", None))
        self.invites_label.setText(QCoreApplication.translate("info_event_dialog", u"Les invit\u00e9s", None))
        self.invites_disponbile_checkbox.setText(QCoreApplication.translate("info_event_dialog", u"Disponible?", None))
        self.amuses_bouches_label.setText(QCoreApplication.translate("info_event_dialog", u"Amuses bouches", None))
        self.amuses_bouches_checkbox.setText(QCoreApplication.translate("info_event_dialog", u"Disponible?", None))
        self.gerer_evenement_label.setText(QCoreApplication.translate("info_event_dialog", u"G\u00e9rer l'\u00e9v\u00e8nement", None))
        self.prendre_charge_btn.setText(QCoreApplication.translate("info_event_dialog", u"Prendre en charge", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.dashboard_page), QCoreApplication.translate("info_event_dialog", u"Les boutons de contr\u00f4le de l'\u00e9v\u00e8nement", None))
    # retranslateUi

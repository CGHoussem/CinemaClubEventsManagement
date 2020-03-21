# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_event_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_add_event_dialog(object):
    def setupUi(self, add_event_dialog):
        if add_event_dialog.objectName():
            add_event_dialog.setObjectName(u"add_event_dialog")
        add_event_dialog.setWindowModality(Qt.WindowModal)
        add_event_dialog.resize(500, 635)
        add_event_dialog.setMinimumSize(QSize(500, 600))
        add_event_dialog.setStyleSheet(u"QLabel#titre{ \n"
"	font: 28pt \"Lucida Calligraphy\";\n"
"	color: rgb(255, 44, 47)\n"
"}\n"
"QLabel#authentification_label{\n"
"	font: bold\n"
"}\n"
"QPushButton {\n"
"	color: #fff;\n"
"	background-color: #007bff;\n"
"	border-style: outset;\n"
"	border-width: 1px;\n"
"	border-radius: 10px;\n"
"	border-color: #007bff;\n"
"	font: bold 12px;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #0069d9;\n"
"	border-color: #0062cc\n"
"}\n"
"QPushButton#detailsEventBtn {\n"
"	background-color: #17a2b8;\n"
"	border-color: #17a2b8;\n"
"}\n"
"QPushButton:hover#detailsEventBtn {\n"
"	background-color: #138496;\n"
"	border-color: #117a8b;\n"
"}\n"
"QLineEdit, QTextEdit, QListWidget, QComboBox {\n"
"	color: #495057;\n"
"	background-color: #fff;\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 2px;\n"
"	padding: 4 1px;\n"
"}\n"
"")
        add_event_dialog.setSizeGripEnabled(True)
        add_event_dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(add_event_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titre = QLabel(add_event_dialog)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.titre)

        self.line = QFrame(add_event_dialog)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(add_event_dialog)
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

        self.description_edit = QTextEdit(self.scrollAreaWidgetContents)
        self.description_edit.setObjectName(u"description_edit")

        self.add_event_layout.addWidget(self.description_edit, 3, 1, 1, 2)

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

        self.nom_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.nom_edit.setObjectName(u"nom_edit")

        self.add_event_layout.addWidget(self.nom_edit, 2, 1, 1, 2)

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

        self.buttonBox = QDialogButtonBox(add_event_dialog)
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
        self.description_label.setBuddy(self.description_edit)
        self.responsables_label.setBuddy(self.responsable_list)
        self.nom_evenement_label.setBuddy(self.nom_edit)
        self.date_debut_label.setBuddy(self.date_debut_edit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.responsable_list)
        QWidget.setTabOrder(self.responsable_list, self.enlever_repsonsable_btn)
        QWidget.setTabOrder(self.enlever_repsonsable_btn, self.responsable_combo)
        QWidget.setTabOrder(self.responsable_combo, self.ajouter_responsable_btn)
        QWidget.setTabOrder(self.ajouter_responsable_btn, self.nom_edit)
        QWidget.setTabOrder(self.nom_edit, self.description_edit)
        QWidget.setTabOrder(self.description_edit, self.date_debut_edit)
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

        self.retranslateUi(add_event_dialog)
        self.buttonBox.accepted.connect(add_event_dialog.accept)
        self.buttonBox.rejected.connect(add_event_dialog.reject)

        QMetaObject.connectSlotsByName(add_event_dialog)
    # setupUi

    def retranslateUi(self, add_event_dialog):
        add_event_dialog.setWindowTitle(QCoreApplication.translate("add_event_dialog", u"Ajout d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("add_event_dialog", u"Cin\u00e9-Club", None))
        self.presentation_groupbox.setTitle("")
        self.duree_presentation_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez la dur\u00e9e de la pr\u00e9sentation", None))
        self.duree_presentation_label.setText(QCoreApplication.translate("add_event_dialog", u"Dur\u00e9e de la pr\u00e9sentation", None))
        self.nom_auteur_label.setText(QCoreApplication.translate("add_event_dialog", u"Nom de l'auteur", None))
        self.nom_auteur_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez le nom de l'auteur", None))
        self.debat_notes_label.setText(QCoreApplication.translate("add_event_dialog", u"Notes", None))
        self.duree_debat_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez la dur\u00e9e du d\u00e9bat", None))
        self.debat_animateur_label.setText(QCoreApplication.translate("add_event_dialog", u"Animateur", None))
        self.debat_notes__edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez quelques notes sur le d\u00e9bat", None))
        self.debat_duree_label.setText(QCoreApplication.translate("add_event_dialog", u"Dur\u00e9e", None))
        self.ajout_animateur_btn.setText(QCoreApplication.translate("add_event_dialog", u"Ajouter un animateur", None))
        self.context_tournage_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez le contexte du trounage", None))
        self.presentation_checkbox.setText(QCoreApplication.translate("add_event_dialog", u"Pr\u00e9sentation de l'auteur", None))
        self.contexte_label.setText(QCoreApplication.translate("add_event_dialog", u"Contexte du tournage", None))
        self.debat_checkbox.setText(QCoreApplication.translate("add_event_dialog", u"D\u00e9bat?", None))
        self.description_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez la description de l'\u00e9v\u00e8nement", None))
        self.ajouter_responsable_btn.setText(QCoreApplication.translate("add_event_dialog", u"Ajouter", None))
        self.date_fin_label.setText(QCoreApplication.translate("add_event_dialog", u"Date de fin", None))
        self.event_color_label.setText(QCoreApplication.translate("add_event_dialog", u"Couleur", None))
        self.salle_projection_label.setText(QCoreApplication.translate("add_event_dialog", u"Salle de projection", None))
        self.nom_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez le nom de l'\u00e9v\u00e8nement", None))
        self.est_projection_checkbox.setText(QCoreApplication.translate("add_event_dialog", u"Est Projection?", None))
        self.description_label.setText(QCoreApplication.translate("add_event_dialog", u"Description", None))
        self.responsables_label.setText(QCoreApplication.translate("add_event_dialog", u"Reponsables", None))
        self.nom_evenement_label.setText(QCoreApplication.translate("add_event_dialog", u"Nom de l'\u00e9v\u00e8nement", None))
        self.enlever_repsonsable_btn.setText(QCoreApplication.translate("add_event_dialog", u"Enlever", None))
        self.date_debut_label.setText(QCoreApplication.translate("add_event_dialog", u"Date de d\u00e9but", None))
#if QT_CONFIG(tooltip)
        self.event_color_btn.setToolTip(QCoreApplication.translate("add_event_dialog", u"<html><head/><body><p>La couleur de l'\u00e9v\u00e8nement sur la calendrier</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.event_color_btn.setText(QCoreApplication.translate("add_event_dialog", u"Choisir une couleur", None))
    # retranslateUi


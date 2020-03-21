# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_animateur_dialog.ui'
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
        add_event_dialog.resize(500, 461)
        add_event_dialog.setMinimumSize(QSize(500, 0))
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
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.nom_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.nom_edit.setObjectName(u"nom_edit")

        self.add_event_layout.addWidget(self.nom_edit, 2, 1, 1, 2)

        self.prenom_animateur = QLabel(self.scrollAreaWidgetContents)
        self.prenom_animateur.setObjectName(u"prenom_animateur")

        self.add_event_layout.addWidget(self.prenom_animateur, 1, 0, 1, 1)

        self.prenom_animateur_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.prenom_animateur_edit.setObjectName(u"prenom_animateur_edit")

        self.add_event_layout.addWidget(self.prenom_animateur_edit, 1, 1, 1, 2)

        self.metier_animateur_combo = QComboBox(self.scrollAreaWidgetContents)
        self.metier_animateur_combo.addItem("")
        self.metier_animateur_combo.addItem("")
        self.metier_animateur_combo.addItem("")
        self.metier_animateur_combo.addItem("")
        self.metier_animateur_combo.addItem("")
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

        self.buttonBox = QDialogButtonBox(add_event_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(add_event_dialog)
        self.buttonBox.accepted.connect(add_event_dialog.accept)
        self.buttonBox.rejected.connect(add_event_dialog.reject)

        QMetaObject.connectSlotsByName(add_event_dialog)
    # setupUi

    def retranslateUi(self, add_event_dialog):
        add_event_dialog.setWindowTitle(QCoreApplication.translate("add_event_dialog", u"Ajout d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("add_event_dialog", u"Cin\u00e9-Club", None))
        self.nom_edit.setPlaceholderText(QCoreApplication.translate("add_event_dialog", u"Entrez l'adresse email de l'animateur", None))
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

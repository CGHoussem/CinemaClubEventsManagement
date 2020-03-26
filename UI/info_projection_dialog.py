# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_info_projection_dialog(QDialog):
    
    def __init__(self, parent=None, flags=Qt.WindowFlags(), projection=None):
        super().__init__(parent, flags)
        
        self.__projection = projection
        self.est_debat_valider = False
        
        self.__setupUi()
        self.__inject()
        self.__connect_signals()
    
    @pyqtSlot()
    def __valider_debat(self):
        """
        Cette fonction permet de valider le debat
        """
        self.est_debat_valider = True
        self.valider_debat_btn.hide()

    def __connect_signals(self):
        """
        Cette fonction permet de connecter les signaux des widgets
        """
        # TODO info_animateur_dialog
        self.animateur_debat_btn.clicked.connect(lambda: print("Ouvrir la dialog info_animateur"))
        self.valider_debat_btn.clicked.connect(self.__valider_debat)
    
    def __inject(self):
        """
        Cette fonction permet d'injecter les attributs d'une projection
        """
        self.contexte_projection_value.setText(self.__projection.contexte)
        if self.__projection.presentationAuteur != None:
            self.auteur_presentation_label.setText(self.__projection.presentationAuteur.auteur)
            self.duree_presentation_label.setText(self.__projection.presentationAuteur.duree)
        else:
            self.presentation_auteur_group.hide()
        if self.__projection.debat != None:
            self.animateur_debat_edit.setText(str(self.__projection.debat.animateur))
            self.duree_debat_edit.setText(self.__projection.debat.duree)
            self.notes_debat_edit.setText(self.__projection.debat.notes)
        else:
            self.debat_group.hide()

    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_projection_dialog")
        self.resize(500, 600)
        self.setMinimumSize(QSize(500, 600))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 523))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.presentation_auteur_group = QGroupBox(self.scrollAreaWidgetContents)
        self.presentation_auteur_group.setObjectName(u"presentation_auteur_group")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.presentation_auteur_group.sizePolicy().hasHeightForWidth())
        self.presentation_auteur_group.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.presentation_auteur_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.auteur_presentation_label = QLabel(self.presentation_auteur_group)
        self.auteur_presentation_label.setObjectName(u"auteur_presentation_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.auteur_presentation_label.sizePolicy().hasHeightForWidth())
        self.auteur_presentation_label.setSizePolicy(sizePolicy3)
        self.auteur_presentation_label.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.auteur_presentation_label, 0, 0, 1, 1)

        self.duree_presentation_label = QLabel(self.presentation_auteur_group)
        self.duree_presentation_label.setObjectName(u"duree_presentation_label")
        sizePolicy3.setHeightForWidth(self.duree_presentation_label.sizePolicy().hasHeightForWidth())
        self.duree_presentation_label.setSizePolicy(sizePolicy3)
        self.duree_presentation_label.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.duree_presentation_label, 1, 0, 1, 1)

        self.auteur_presentation_edit = QLineEdit(self.presentation_auteur_group)
        self.auteur_presentation_edit.setObjectName(u"auteur_presentation_edit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.auteur_presentation_edit.sizePolicy().hasHeightForWidth())
        self.auteur_presentation_edit.setSizePolicy(sizePolicy4)
        self.auteur_presentation_edit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.auteur_presentation_edit, 0, 1, 1, 1, Qt.AlignLeft)

        self.duree_presentation_edit = QLineEdit(self.presentation_auteur_group)
        self.duree_presentation_edit.setObjectName(u"duree_presentation_edit")
        sizePolicy4.setHeightForWidth(self.duree_presentation_edit.sizePolicy().hasHeightForWidth())
        self.duree_presentation_edit.setSizePolicy(sizePolicy4)
        self.duree_presentation_edit.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.duree_presentation_edit, 1, 1, 1, 1)


        self.add_event_layout.addWidget(self.presentation_auteur_group, 1, 0, 1, 2, Qt.AlignLeft)

        self.contexte_projection_value = QTextBrowser(self.scrollAreaWidgetContents)
        self.contexte_projection_value.setObjectName(u"contexte_projection_value")
        sizePolicy1.setHeightForWidth(self.contexte_projection_value.sizePolicy().hasHeightForWidth())
        self.contexte_projection_value.setSizePolicy(sizePolicy1)
        self.contexte_projection_value.setMinimumSize(QSize(0, 0))
        self.contexte_projection_value.setMaximumSize(QSize(16777215, 250))
        self.contexte_projection_value.setReadOnly(True)

        self.add_event_layout.addWidget(self.contexte_projection_value, 0, 1, 1, 1)

        self.debat_group = QGroupBox(self.scrollAreaWidgetContents)
        self.debat_group.setObjectName(u"debat_group")
        self.gridLayout_2 = QGridLayout(self.debat_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.animateur_debat_label = QLabel(self.debat_group)
        self.animateur_debat_label.setObjectName(u"animateur_debat_label")

        self.gridLayout_2.addWidget(self.animateur_debat_label, 0, 0, 1, 1)

        self.widget = QWidget(self.debat_group)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.animateur_debat_edit = QLineEdit(self.widget)
        self.animateur_debat_edit.setObjectName(u"animateur_debat_edit")

        self.horizontalLayout.addWidget(self.animateur_debat_edit)

        self.animateur_debat_btn = QPushButton(self.widget)
        self.animateur_debat_btn.setObjectName(u"animateur_debat_btn")

        self.horizontalLayout.addWidget(self.animateur_debat_btn)


        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)

        self.notes_debat_label = QLabel(self.debat_group)
        self.notes_debat_label.setObjectName(u"notes_debat_label")

        self.gridLayout_2.addWidget(self.notes_debat_label, 2, 0, 1, 1, Qt.AlignTop)

        self.duree_debat_label = QLabel(self.debat_group)
        self.duree_debat_label.setObjectName(u"duree_debat_label")

        self.gridLayout_2.addWidget(self.duree_debat_label, 1, 0, 1, 1)

        self.valider_debat_btn = QPushButton(self.debat_group)
        self.valider_debat_btn.setObjectName(u"valider_debat_btn")

        self.gridLayout_2.addWidget(self.valider_debat_btn, 3, 0, 1, 2)

        self.notes_debat_edit = QTextEdit(self.debat_group)
        self.notes_debat_edit.setObjectName(u"notes_debat_edit")
        self.notes_debat_edit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.notes_debat_edit, 2, 1, 1, 1)

        self.duree_debat_edit = QLineEdit(self.debat_group)
        self.duree_debat_edit.setObjectName(u"duree_debat_edit")

        self.gridLayout_2.addWidget(self.duree_debat_edit, 1, 1, 1, 1)


        self.add_event_layout.addWidget(self.debat_group, 2, 0, 1, 2)

        self.contexte_projection_label = QLabel(self.scrollAreaWidgetContents)
        self.contexte_projection_label.setObjectName(u"contexte_projection_label")

        self.add_event_layout.addWidget(self.contexte_projection_label, 0, 0, 1, 1, Qt.AlignTop)


        self.gridLayout_4.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        #if QT_CONFIG(shortcut)
        self.contexte_projection_label.setBuddy(self.contexte_projection_value)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.contexte_projection_value)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self    .accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_projection_dialog", u"D\u00e9tails de la projection", None))
        self.titre.setText(QCoreApplication.translate("info_projection_dialog", u"Cin\u00e9-Club", None))
        self.presentation_auteur_group.setTitle(QCoreApplication.translate("info_projection_dialog", u"Pr\u00e9sentation de l'auteur", None))
        self.auteur_presentation_label.setText(QCoreApplication.translate("info_projection_dialog", u"Auteur", None))
        self.duree_presentation_label.setText(QCoreApplication.translate("info_projection_dialog", u"Dur\u00e9e", None))
        self.debat_group.setTitle(QCoreApplication.translate("info_projection_dialog", u"D\u00e9bat", None))
        self.animateur_debat_label.setText(QCoreApplication.translate("info_projection_dialog", u"Animateur", None))
        self.animateur_debat_btn.setText(QCoreApplication.translate("info_projection_dialog", u"Plus d'infos", None))
        self.notes_debat_label.setText(QCoreApplication.translate("info_projection_dialog", u"Notes", None))
        self.duree_debat_label.setText(QCoreApplication.translate("info_projection_dialog", u"Dur\u00e9e", None))
        self.valider_debat_btn.setText(QCoreApplication.translate("info_projection_dialog", u"Valider les amuses bouches", None))
        self.contexte_projection_label.setText(QCoreApplication.translate("info_projection_dialog", u"Contexte", None))
    # retranslateUi


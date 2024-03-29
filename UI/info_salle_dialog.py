# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_salle_dialog.ui'
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

from UI.info_user_dialog import Ui_info_user_dialog

class Ui_info_salle_dialog(QDialog):
    def __init__(self, parent, f, salle):
        super().__init__(parent, f)
        self.__salle = salle

        self.__setupUi()

        # connect signals
        self.responsable_info_btn.clicked.connect(self.__ouvrir_responsable_dialog)

        self.__inject()

    @pyqtSlot()
    def __ouvrir_responsable_dialog(self):
        Ui_info_user_dialog(self, self.__salle.responsable).show()

    def __inject(self):
        self.nom_salle_value.setText("Salle %04d" % self.__salle.id)
        self.adresse_salle_value.setText(self.__salle.adresse)
        self.nbr_place_standard_value.setText(str(self.__salle.nbr_place_standard))
        self.nbr_place_premium_vaue.setText(str(self.__salle.nbr_place_premium))
        self.responsable_salle_value.setText(str(self.__salle.responsable))

    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_salle_dialog")
        self.resize(500, 384)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 518, 295))
        self._2 = QGridLayout(self.scrollAreaWidgetContents)
        self._2.setObjectName(u"_2")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label_4, 4, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.label, 5, 1, 1, 1)

        self.nombre_place_salle_label = QLabel(self.scrollAreaWidgetContents)
        self.nombre_place_salle_label.setObjectName(u"nombre_place_salle_label")
        self.nombre_place_salle_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.nombre_place_salle_label, 4, 0, 1, 1)

        self.adresse_salle_label = QLabel(self.scrollAreaWidgetContents)
        self.adresse_salle_label.setObjectName(u"adresse_salle_label")
        self.adresse_salle_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.adresse_salle_label, 2, 0, 1, 1, Qt.AlignTop)

        self.responsable_salle_label = QLabel(self.scrollAreaWidgetContents)
        self.responsable_salle_label.setObjectName(u"responsable_salle_label")
        self.responsable_salle_label.setMaximumSize(QSize(100, 16777215))

        self.add_event_layout.addWidget(self.responsable_salle_label, 3, 0, 1, 1)

        self.nbr_place_premium_vaue = QLabel(self.scrollAreaWidgetContents)
        self.nbr_place_premium_vaue.setObjectName(u"nbr_place_premium_vaue")

        self.add_event_layout.addWidget(self.nbr_place_premium_vaue, 4, 2, 1, 1)

        self.nbr_place_standard_value = QLabel(self.scrollAreaWidgetContents)
        self.nbr_place_standard_value.setObjectName(u"nbr_place_standard_value")

        self.add_event_layout.addWidget(self.nbr_place_standard_value, 5, 2, 1, 1)

        self.salle_container = QWidget(self.scrollAreaWidgetContents)
        self.salle_container.setObjectName(u"salle_container")
        self.horizontalLayout = QHBoxLayout(self.salle_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.responsable_salle_value = QLabel(self.salle_container)
        self.responsable_salle_value.setObjectName(u"responsable_salle_value")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.responsable_salle_value.sizePolicy().hasHeightForWidth())
        self.responsable_salle_value.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.responsable_salle_value)

        self.responsable_info_btn = QPushButton(self.salle_container)
        self.responsable_info_btn.setObjectName(u"responsable_info_btn")
        self.responsable_info_btn.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.responsable_info_btn)

        self.horizontalLayout.setStretch(1, 1)

        self.add_event_layout.addWidget(self.salle_container, 3, 1, 1, 2, Qt.AlignLeft)

        self.adresse_salle_value = QTextBrowser(self.scrollAreaWidgetContents)
        self.adresse_salle_value.setObjectName(u"adresse_salle_value")
        sizePolicy1.setHeightForWidth(self.adresse_salle_value.sizePolicy().hasHeightForWidth())
        self.adresse_salle_value.setSizePolicy(sizePolicy1)
        self.adresse_salle_value.setMinimumSize(QSize(0, 0))
        self.adresse_salle_value.setMaximumSize(QSize(16777215, 100))

        self.add_event_layout.addWidget(self.adresse_salle_value, 2, 1, 1, 2)

        self.nom_salle_value = QLabel(self.scrollAreaWidgetContents)
        self.nom_salle_value.setObjectName(u"nom_salle_value")
        self.nom_salle_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.nom_salle_value, 0, 0, 2, 3)


        self._2.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        #if QT_CONFIG(shortcut)
        self.adresse_salle_label.setBuddy(self.adresse_salle_value)
        self.responsable_salle_value.setBuddy(self.responsable_info_btn)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.adresse_salle_value)
        QWidget.setTabOrder(self.adresse_salle_value, self.responsable_info_btn)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_salle_dialog", u"D\u00e9tails d'une salle", None))
        self.titre.setText(QCoreApplication.translate("info_salle_dialog", u"Cin\u00e9-Club", None))
        self.label_4.setText(QCoreApplication.translate("info_salle_dialog", u"Premium", None))
        self.label.setText(QCoreApplication.translate("info_salle_dialog", u"Standard", None))
        self.nombre_place_salle_label.setText(QCoreApplication.translate("info_salle_dialog", u"Nombre de places", None))
        self.adresse_salle_label.setText(QCoreApplication.translate("info_salle_dialog", u"Adresse", None))
        self.responsable_salle_label.setText(QCoreApplication.translate("info_salle_dialog", u"Reponsable", None))
        self.nbr_place_premium_vaue.setText(QCoreApplication.translate("info_salle_dialog", u"TextLabel", None))
        self.nbr_place_standard_value.setText(QCoreApplication.translate("info_salle_dialog", u"TextLabel", None))
        self.responsable_salle_value.setText(QCoreApplication.translate("info_salle_dialog", u"TextLabel", None))
        self.responsable_info_btn.setText(QCoreApplication.translate("info_salle_dialog", u"Plus d'infos", None))
        self.nom_salle_value.setText(QCoreApplication.translate("info_salle_dialog", u"TextLabel", None))
    # retranslateUi


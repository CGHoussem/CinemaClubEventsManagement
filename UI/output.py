# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_event_dialog.ui'
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


class Ui_info_event_dialog(object):
    def setupUi(self, info_event_dialog):
        if info_event_dialog.objectName():
            info_event_dialog.setObjectName(u"info_event_dialog")
        info_event_dialog.resize(500, 672)
        info_event_dialog.setMinimumSize(QSize(500, 600))
        info_event_dialog.setStyleSheet(u"QLabel#titre{ \n"
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
        info_event_dialog.setSizeGripEnabled(True)
        info_event_dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(info_event_dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titre = QLabel(info_event_dialog)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.titre)

        self.line = QFrame(info_event_dialog)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.scrollArea = QScrollArea(info_event_dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 557))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.responsables_label = QLabel(self.scrollAreaWidgetContents)
        self.responsables_label.setObjectName(u"responsables_label")

        self.add_event_layout.addWidget(self.responsables_label, 3, 0, 1, 1)

        self.responsable_list_widget = QListWidget(self.scrollAreaWidgetContents)
        self.responsable_list_widget.setObjectName(u"responsable_list_widget")
        sizePolicy1.setHeightForWidth(self.responsable_list_widget.sizePolicy().hasHeightForWidth())
        self.responsable_list_widget.setSizePolicy(sizePolicy1)
        self.responsable_list_widget.setMaximumSize(QSize(16777215, 300))

        self.add_event_layout.addWidget(self.responsable_list_widget, 3, 1, 1, 1)

        self.date_fin_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.date_fin_evenement_value.setObjectName(u"date_fin_evenement_value")

        self.add_event_layout.addWidget(self.date_fin_evenement_value, 5, 1, 1, 1)

        self.event_color_label = QLabel(self.scrollAreaWidgetContents)
        self.event_color_label.setObjectName(u"event_color_label")

        self.add_event_layout.addWidget(self.event_color_label, 7, 0, 1, 1)

        self.projection_evenement_btn = QPushButton(self.scrollAreaWidgetContents)
        self.projection_evenement_btn.setObjectName(u"projection_evenement_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projection_evenement_btn.sizePolicy().hasHeightForWidth())
        self.projection_evenement_btn.setSizePolicy(sizePolicy2)

        self.add_event_layout.addWidget(self.projection_evenement_btn, 8, 0, 1, 2, Qt.AlignHCenter)

        self.description_evenement_value = QTextBrowser(self.scrollAreaWidgetContents)
        self.description_evenement_value.setObjectName(u"description_evenement_value")
        sizePolicy1.setHeightForWidth(self.description_evenement_value.sizePolicy().hasHeightForWidth())
        self.description_evenement_value.setSizePolicy(sizePolicy1)
        self.description_evenement_value.setMinimumSize(QSize(0, 0))
        self.description_evenement_value.setMaximumSize(QSize(16777215, 100))

        self.add_event_layout.addWidget(self.description_evenement_value, 2, 1, 1, 1)

        self.color_evenement_frame = QFrame(self.scrollAreaWidgetContents)
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

        self.description_evenement_label = QLabel(self.scrollAreaWidgetContents)
        self.description_evenement_label.setObjectName(u"description_evenement_label")

        self.add_event_layout.addWidget(self.description_evenement_label, 2, 0, 1, 1, Qt.AlignTop)

        self.date_debut_label = QLabel(self.scrollAreaWidgetContents)
        self.date_debut_label.setObjectName(u"date_debut_label")

        self.add_event_layout.addWidget(self.date_debut_label, 4, 0, 1, 1)

        self.salle_container = QWidget(self.scrollAreaWidgetContents)
        self.salle_container.setObjectName(u"salle_container")
        self.horizontalLayout = QHBoxLayout(self.salle_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.salle_label_value = QLabel(self.salle_container)
        self.salle_label_value.setObjectName(u"salle_label_value")

        self.horizontalLayout.addWidget(self.salle_label_value)

        self.salle_info_btn = QPushButton(self.salle_container)
        self.salle_info_btn.setObjectName(u"salle_info_btn")

        self.horizontalLayout.addWidget(self.salle_info_btn)

        self.horizontalLayout.setStretch(1, 1)

        self.add_event_layout.addWidget(self.salle_container, 6, 1, 1, 1)

        self.date_debut_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.date_debut_evenement_value.setObjectName(u"date_debut_evenement_value")

        self.add_event_layout.addWidget(self.date_debut_evenement_value, 4, 1, 1, 1)

        self.date_fin_label = QLabel(self.scrollAreaWidgetContents)
        self.date_fin_label.setObjectName(u"date_fin_label")

        self.add_event_layout.addWidget(self.date_fin_label, 5, 0, 1, 1)

        self.salle_label = QLabel(self.scrollAreaWidgetContents)
        self.salle_label.setObjectName(u"salle_label")

        self.add_event_layout.addWidget(self.salle_label, 6, 0, 1, 1)

        self.nom_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.nom_evenement_value.setObjectName(u"nom_evenement_value")
        self.nom_evenement_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.nom_evenement_value, 0, 0, 2, 2)


        self.gridLayout_4.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(info_event_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

#if QT_CONFIG(shortcut)
        self.responsables_label.setBuddy(self.responsable_list_widget)
        self.description_evenement_label.setBuddy(self.description_evenement_value)
        self.salle_label_value.setBuddy(self.salle_info_btn)
        self.salle_label.setBuddy(self.salle_info_btn)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.description_evenement_value)
        QWidget.setTabOrder(self.description_evenement_value, self.responsable_list_widget)
        QWidget.setTabOrder(self.responsable_list_widget, self.salle_info_btn)
        QWidget.setTabOrder(self.salle_info_btn, self.projection_evenement_btn)

        self.retranslateUi(info_event_dialog)
        self.buttonBox.accepted.connect(info_event_dialog.accept)
        self.buttonBox.rejected.connect(info_event_dialog.reject)

        QMetaObject.connectSlotsByName(info_event_dialog)
    # setupUi

    def retranslateUi(self, info_event_dialog):
        info_event_dialog.setWindowTitle(QCoreApplication.translate("info_event_dialog", u"D\u00e9tails d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("info_event_dialog", u"Cin\u00e9-Club", None))
        self.responsables_label.setText(QCoreApplication.translate("info_event_dialog", u"Reponsables", None))
        self.date_fin_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.event_color_label.setText(QCoreApplication.translate("info_event_dialog", u"Couleur", None))
        self.projection_evenement_btn.setText(QCoreApplication.translate("info_event_dialog", u"Cette \u00e9v\u00e8nement est une projection", None))
        self.description_evenement_label.setText(QCoreApplication.translate("info_event_dialog", u"Description", None))
        self.date_debut_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de d\u00e9but", None))
        self.salle_label_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.salle_info_btn.setText(QCoreApplication.translate("info_event_dialog", u"Plus d'infos", None))
        self.date_debut_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.date_fin_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de fin", None))
        self.salle_label.setText(QCoreApplication.translate("info_event_dialog", u"Salle", None))
        self.nom_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
    # retranslateUi


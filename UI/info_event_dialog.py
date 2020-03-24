# -*- coding: utf-8 -*-

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI.info_salle_dialog import Ui_info_salle_dialog

class Ui_info_event_dialog(QDialog):
    def __init__(self, parent, f=Qt.WindowFlags(), evenement=None):
        super().__init__(parent, f)
        self.__setupUi()
        
        self.__evenement = evenement

        self.projection_evenement_btn.setEnabled(self.__evenement.est_projection)
        if self.__evenement.est_projection:
            self.projection_evenement_btn.setText("Cette évènement est une projection. Savoir plus!")
        else:
            self.projection_evenement_btn.setText("Cette évènement n'est pas une projection!")
            self.projection_evenement_btn.setStyleSheet(open("UI/styles/secondary_button.css").read())

        # setup signals
        self.responsable_list_widget.itemDoubleClicked.connect(lambda e: print("Ouvrir le dialog du responsable"))
        self.salle_info_btn.clicked.connect(self.__open_salle_dialog)
        self.projection_evenement_btn.clicked.connect(lambda e: print("Ouvrir le dialog de la projection"))
    
        self.__inject()
  
    @pyqtSlot()
    def __open_salle_dialog(self):
        dialog = Ui_info_salle_dialog(self, Qt.WindowFlags(), self.__evenement.salle)
        dialog.show()
  
    def __inject(self):
        def format_date(datetime):
            return "%02d/%02d/%d %02d:%02d" % (datetime.date().day(), datetime.date().month(), datetime.date().year(), datetime.time().hour(), datetime.time().minute())
        
        self.nom_evenement_value.setText(self.__evenement.nom)
        self.description_evenement_value.setText(self.__evenement.description)
        for r in self.__evenement.responsables:
            self.responsable_list_widget.addItem(str(r))
        self.date_debut_evenement_value.setText(format_date(self.__evenement.date_debut))
        self.date_fin_evenement_value.setText(format_date(self.__evenement.date_fin))
        self.salle_label_value.setText(str(self.__evenement.salle))
        self.color_evenement_frame.setStyleSheet("background-color: %s" % self.__evenement.color)
  
    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"info_event_dialog")
        self.resize(500, 672)
        self.setMinimumSize(QSize(500, 600))
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 557))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_event_layout = QGridLayout()
        self.add_event_layout.setObjectName(u"add_event_layout")
        self.add_event_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.date_debut_label = QLabel(self.scrollAreaWidgetContents)
        self.date_debut_label.setObjectName(u"date_debut_label")

        self.add_event_layout.addWidget(self.date_debut_label, 5, 0, 1, 1)

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

        self.add_event_layout.addWidget(self.salle_container, 7, 1, 1, 1)

        self.projection_evenement_btn = QPushButton(self.scrollAreaWidgetContents)
        self.projection_evenement_btn.setObjectName(u"projection_evenement_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.projection_evenement_btn.sizePolicy().hasHeightForWidth())
        self.projection_evenement_btn.setSizePolicy(sizePolicy2)

        self.add_event_layout.addWidget(self.projection_evenement_btn, 9, 0, 1, 2, Qt.AlignHCenter)

        self.description_evenement_label = QLabel(self.scrollAreaWidgetContents)
        self.description_evenement_label.setObjectName(u"description_evenement_label")

        self.add_event_layout.addWidget(self.description_evenement_label, 3, 0, 1, 1, Qt.AlignTop)

        self.date_fin_label = QLabel(self.scrollAreaWidgetContents)
        self.date_fin_label.setObjectName(u"date_fin_label")

        self.add_event_layout.addWidget(self.date_fin_label, 6, 0, 1, 1)

        self.event_color_label = QLabel(self.scrollAreaWidgetContents)
        self.event_color_label.setObjectName(u"event_color_label")

        self.add_event_layout.addWidget(self.event_color_label, 8, 0, 1, 1)

        self.description_evenement_value = QTextBrowser(self.scrollAreaWidgetContents)
        self.description_evenement_value.setObjectName(u"description_evenement_value")
        sizePolicy1.setHeightForWidth(self.description_evenement_value.sizePolicy().hasHeightForWidth())
        self.description_evenement_value.setSizePolicy(sizePolicy1)
        self.description_evenement_value.setMinimumSize(QSize(0, 0))
        self.description_evenement_value.setMaximumSize(QSize(16777215, 100))

        self.add_event_layout.addWidget(self.description_evenement_value, 3, 1, 1, 1)

        self.date_debut_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.date_debut_evenement_value.setObjectName(u"date_debut_evenement_value")

        self.add_event_layout.addWidget(self.date_debut_evenement_value, 5, 1, 1, 1)

        self.date_fin_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.date_fin_evenement_value.setObjectName(u"date_fin_evenement_value")

        self.add_event_layout.addWidget(self.date_fin_evenement_value, 6, 1, 1, 1)

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

        self.add_event_layout.addWidget(self.color_evenement_frame, 8, 1, 1, 1)

        self.salle_label = QLabel(self.scrollAreaWidgetContents)
        self.salle_label.setObjectName(u"salle_label")

        self.add_event_layout.addWidget(self.salle_label, 7, 0, 1, 1)

        self.responsables_label = QLabel(self.scrollAreaWidgetContents)
        self.responsables_label.setObjectName(u"responsables_label")

        self.add_event_layout.addWidget(self.responsables_label, 4, 0, 1, 1)

        self.responsable_list_widget = QListWidget(self.scrollAreaWidgetContents)
        self.responsable_list_widget.setObjectName(u"responsable_list_widget")
        sizePolicy1.setHeightForWidth(self.responsable_list_widget.sizePolicy().hasHeightForWidth())
        self.responsable_list_widget.setSizePolicy(sizePolicy1)
        self.responsable_list_widget.setMaximumSize(QSize(16777215, 300))

        self.add_event_layout.addWidget(self.responsable_list_widget, 4, 1, 1, 1)

        self.nom_evenement_value = QLabel(self.scrollAreaWidgetContents)
        self.nom_evenement_value.setObjectName(u"nom_evenement_value")
        self.nom_evenement_value.setStyleSheet(u"font: 14pt \"Arial\";")

        self.add_event_layout.addWidget(self.nom_evenement_value, 0, 0, 2, 2)


        self.gridLayout_4.addLayout(self.add_event_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)

        #if QT_CONFIG(shortcut)
        self.salle_label_value.setBuddy(self.salle_info_btn)
        self.description_evenement_label.setBuddy(self.description_evenement_value)
        self.salle_label.setBuddy(self.salle_info_btn)
        self.responsables_label.setBuddy(self.responsable_list_widget)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.scrollArea, self.description_evenement_value)
        QWidget.setTabOrder(self.description_evenement_value, self.responsable_list_widget)
        QWidget.setTabOrder(self.responsable_list_widget, self.salle_info_btn)
        QWidget.setTabOrder(self.salle_info_btn, self.projection_evenement_btn)

        self.__retranslateUi()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("info_event_dialog", u"D\u00e9tails d'un \u00e9v\u00e8nement", None))
        self.titre.setText(QCoreApplication.translate("info_event_dialog", u"Cin\u00e9-Club", None))
        self.date_debut_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de d\u00e9but", None))
        self.salle_label_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.salle_info_btn.setText(QCoreApplication.translate("info_event_dialog", u"Plus d'infos", None))
        self.projection_evenement_btn.setText(QCoreApplication.translate("info_event_dialog", u"Cette \u00e9v\u00e8nement est une projection", None))
        self.description_evenement_label.setText(QCoreApplication.translate("info_event_dialog", u"Description", None))
        self.date_fin_label.setText(QCoreApplication.translate("info_event_dialog", u"Date de fin", None))
        self.event_color_label.setText(QCoreApplication.translate("info_event_dialog", u"Couleur", None))
        self.date_debut_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.date_fin_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
        self.salle_label.setText(QCoreApplication.translate("info_event_dialog", u"Salle", None))
        self.responsables_label.setText(QCoreApplication.translate("info_event_dialog", u"Reponsables", None))
        self.nom_evenement_value.setText(QCoreApplication.translate("info_event_dialog", u"TextLabel", None))
    # retranslateUi

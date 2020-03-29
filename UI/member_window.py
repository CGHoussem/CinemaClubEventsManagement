# -*- coding: utf-8 -*-

from pathlib import Path

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI.info_event_dialog import Ui_info_event_dialog
from UI.info_user_dialog import Ui_info_user_dialog
from UI.billeterie_event_dialog import Ui_billeterie_event_dialog

from DAO.DAOs import EvenementDAO
from Models.disponibilite import Statut
from Models.evenement import Etat
from PIL import Image, ImageOps

import re

class PicButton(QAbstractButton):
    def __init__(self, normal_pixmap=None, hovered_pixmap=None, parent=None):
        super(PicButton, self).__init__(parent)
        self.hovered_pixmap = hovered_pixmap
        self.normal_pixmap = normal_pixmap
        self.__pixmap = normal_pixmap

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.__pixmap)
        self.__pixmap = self.normal_pixmap

    def enterEvent(self, event):
        self.__pixmap = self.hovered_pixmap
        return super().enterEvent(event)

    def sizeHint(self):
        return self.__pixmap.size()

class Ui_MemberWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags(), member=None):
        super().__init__(parent=parent, flags=flags)
        self.__parent = parent
        self.__member = member
        self.__member_events = []
        
        self.__events = EvenementDAO.get_all()
        for e in self.__events:
            for r in e.responsables:
                if r.id == self.__member.id:
                    self.__member_events.append(e)
        
        self.__setupUi()
        
        # Connect signals
        self.profile_btn.clicked.connect(self.__open_profile_dialog)
        self.disconnect_btn.clicked.connect(self.__disconnect)
        self.events_list_widget.itemDoubleClicked.connect(self.__open_event_dialog)
        self.billeterie_event_name_edit.textChanged.connect(self.__filter_list_widget)
        self.billeterie_filter_btn.clicked.connect(lambda: self.__filter_list_widget(self.billeterie_event_name_edit.text()))
        self.billeterie_list_widget.itemDoubleClicked.connect(self.__open_billeterie_event_dialog)
        self.billeterie_event_btn.clicked.connect(self.__open_event_dialog)
        
        self.__inject()
    
    def __refresh_list(self):
        self.__member_events.clear()
        self.__events = EvenementDAO.get_all()
        for e in self.__events:
            for r in e.responsables:
                if r.id == self.__member.id:
                    self.__member_events.append(e)

        self.events_list_widget.clear()
        for e in self.__member_events:
            self.events_list_widget.addItem(self.__get_item(e))
    
    @pyqtSlot(str)
    def __filter_list_widget(self, text):
        """
        Cette fonction permet de filtrer la liste des évènement par une formule regex
        
            Parameters:
                text: le text a chercher 
        """
        self.billeterie_list_widget.clear()
    
        for e in self.__events:
            match = True
            if len(text) != 0:
                match = re.match(r"^.*%s.*$" % text, e.nom, re.IGNORECASE)
            if match and e.etat == Etat.TERMINE:
                self.billeterie_list_widget.addItem(self.__get_item(e))

    @pyqtSlot()
    def __open_event_dialog(self):
        """
        Cette fonction permet d'ouvrir le dialog d'un évènement
        """
        indexes = self.events_list_widget.selectedIndexes()
        if len(indexes) > 0:
            dialog = Ui_info_event_dialog(self, self.__member_events[indexes[0].row()])
            dialog.exec_()
            self.__refresh_list()
    
    @pyqtSlot(QListWidgetItem)
    def __open_billeterie_event_dialog(self, item):
        """
        Cette fonction permet d'ouvrir le dialog de la billeterie d'un évènement
        """
        indexes = self.billeterie_list_widget.selectedIndexes()
        if len(indexes) > 0:
            Ui_billeterie_event_dialog(self, self.__events[indexes[0].row()]).show()
    
    @pyqtSlot()
    def __open_profile_dialog(self):
        """
        Cette fonction permet d'ouvrir la dialog du profile de l'utilisateur
        """
        Ui_info_user_dialog(self, self.__member).show()
    
    @pyqtSlot()
    def __disconnect(self):
        """
        Cette fonction permet de mettre l'utilisateur hors connexion
        """
        self.close()
        self.__parent.show()
    
    def __inject(self):
        """
        Cette fonction permet d'injecter les attributs de l'utilisateur à l'interface graphique
        """
        self.billeterie_event_name_edit.setPlaceholderText("Entrez votre expression")
        self.nom_prenom_value.setText(self.__member.nom.upper() + " "+ self.__member.prenom)
        
        if self.__member.disponibilite.statut == Statut.DISPONIBLE:
            self.status_value.setStyleSheet("color: #12D11C")
        else:
            self.status_value.setStyleSheet("color: #FFCD42")
        self.status_value.setText(str(self.__member.disponibilite))

        # Get all events related to the user
        self.events_list_widget.clear()
        for e in self.__member_events:
            self.events_list_widget.addItem(self.__get_item(e))
        
        # populate all events in billeterie list
        for e in self.__events:
            if e.etat == Etat.TERMINE:
                self.billeterie_list_widget.addItem(self.__get_item(e))

    def __get_item(self, event):
        """
        Cette fonction permet de créer une item pour la liste
        
            Parameters:
                event: L'évènement à ajouté dans la liste
            Return:
                Un objet de QListWidgetItem()
        """
        Path("UI/events_icons/member_%d" % self.__member.id).mkdir(parents=True, exist_ok=True)
        icon_name ="UI/events_icons/member_%d/event_%d.png" % (self.__member.id, event.id)
        self.__draw_image(icon_name, (10, 10), event.color)
        icon = QIcon(icon_name)

        item = QListWidgetItem(icon, str(event))
        if event.etat == Etat.EN_ATTENTE:
            item.setBackground(QColor("#FF4B3C"))
        if event.etat == Etat.EN_COURS:
            item.setBackground(QColor("#FFCD42"))
        if event.etat == Etat.TERMINE:
            item.setBackground(QColor("#12D11C"))
        return item
    
    def __draw_image(self, file_path, dimension, color):
        if not Path(file_path).exists():
            if isinstance(dimension, tuple):
                img = Image.new('RGB', dimension, color=color)
                img.save(file_path)
                self.__add_border(file_path, file_path, 1)
            else:
                raise RuntimeError('dimension is not a tuple!')

    def __add_border(self, input_image, output_image, border):
        img = Image.open(input_image)
        
        if isinstance(border, int) or isinstance(border, tuple):
            bimg = ImageOps.expand(img, border=border)
        else:
            raise RuntimeError('Border is not an integer or tuple!')
        
        bimg.save(output_image)
    
    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"MemberWindow")
        self.resize(530, 570)
        self.setStyleSheet(open("UI/styles/base_style.css", "r").read())
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.container = QVBoxLayout()
        self.container.setObjectName(u"container")
        self.container.setContentsMargins(5, 5, 5, 5)
        self.header_container = QWidget(self.centralwidget)
        self.header_container.setObjectName(u"header_container")
        self.gridLayout_3 = QGridLayout(self.header_container)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.titre = QLabel(self.header_container)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.titre, 0, 0, 1, 1)

        self.header_buttons_widget = QWidget(self.header_container)
        self.header_buttons_widget.setObjectName(u"header_buttons_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.header_buttons_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.profile_btn = PicButton(QPixmap("UI/pics/profile_btn_normal.png"), QPixmap("UI/pics/profile_btn_hovered.png"), self.header_buttons_widget)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setMouseTracking(True)
        self.profile_btn.setMaximumSize(25, 25)

        self.horizontalLayout_2.addWidget(self.profile_btn, 0, Qt.AlignRight|Qt.AlignTop)

        self.disconnect_btn = QPushButton(self.header_buttons_widget)
        self.disconnect_btn.setObjectName(u"disconnect_btn")

        self.horizontalLayout_2.addWidget(self.disconnect_btn, 0, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout_3.addWidget(self.header_buttons_widget, 0, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.container.addWidget(self.header_container)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.container.addWidget(self.line)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.form_grid = QGridLayout()
        self.form_grid.setObjectName(u"form_grid")
        self.form_grid.setContentsMargins(5, 5, 5, 5)
        self.status_label = QLabel(self.tab)
        self.status_label.setObjectName(u"status_label")

        self.form_grid.addWidget(self.status_label, 1, 0, 1, 1)

        self.events_list_widget = QListWidget(self.tab)
        self.events_list_widget.setObjectName(u"events_list_widget")

        self.form_grid.addWidget(self.events_list_widget, 3, 0, 1, 2)

        self.nom_prenom_label = QLabel(self.tab)
        self.nom_prenom_label.setObjectName(u"nom_prenom_label")

        self.form_grid.addWidget(self.nom_prenom_label, 0, 0, 1, 1)

        self.evenements_label = QLabel(self.tab)
        self.evenements_label.setObjectName(u"evenements_label")

        self.form_grid.addWidget(self.evenements_label, 2, 0, 1, 1)

        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.status_value = QLabel(self.widget)
        self.status_value.setObjectName(u"status_value")

        self.horizontalLayout.addWidget(self.status_value)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.form_grid.addWidget(self.widget, 1, 1, 1, 1)

        self.nom_prenom_value = QLabel(self.tab)
        self.nom_prenom_value.setObjectName(u"nom_prenom_value")

        self.form_grid.addWidget(self.nom_prenom_value, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.form_grid, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.billeterieTab = QWidget()
        self.billeterieTab.setObjectName(u"billeterieTab")
        self.verticalLayout = QVBoxLayout(self.billeterieTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.billeterieTab)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.billeterie_event_name_edit = QLineEdit(self.widget_2)
        self.billeterie_event_name_edit.setObjectName(u"billeterie_event_name_edit")

        self.horizontalLayout_3.addWidget(self.billeterie_event_name_edit)

        self.billeterie_filter_btn = QPushButton(self.widget_2)
        self.billeterie_filter_btn.setObjectName(u"billeterie_filter_btn")

        self.horizontalLayout_3.addWidget(self.billeterie_filter_btn)


        self.verticalLayout.addWidget(self.widget_2)

        self.billeterie_list_widget = QListWidget(self.billeterieTab)
        self.billeterie_list_widget.setObjectName(u"billeterie_list_widget")

        self.verticalLayout.addWidget(self.billeterie_list_widget)

        self.billeterie_event_btn = QPushButton(self.billeterieTab)
        self.billeterie_event_btn.setObjectName(u"billeterie_event_btn")

        self.verticalLayout.addWidget(self.billeterie_event_btn, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.billeterieTab, "")

        self.container.addWidget(self.tabWidget)

        self.container.setStretch(0, 1)
        self.container.setStretch(2, 2)

        self.gridLayout_4.addLayout(self.container, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 545, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        #if QT_CONFIG(shortcut)
        self.evenements_label.setBuddy(self.events_list_widget)
        self.status_value.setBuddy(self.pushButton)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.profile_btn, self.disconnect_btn)
        QWidget.setTabOrder(self.disconnect_btn, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.events_list_widget)

        self.__retranslateUi()

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MemberWindow", u"Cin\u00e9-Club", None))
        self.titre.setText(QCoreApplication.translate("MemberWindow", u"Cin\u00e9-Club", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MemberWindow", u"Se D\u00e9connecter", None))
        self.status_label.setText(QCoreApplication.translate("MemberWindow", u"Status :", None))
        self.nom_prenom_label.setText(QCoreApplication.translate("MemberWindow", u"Membre de la mairie / du club :", None))
        self.evenements_label.setText(QCoreApplication.translate("MemberWindow", u"\u00c9v\u00e8nements associ\u00e9s :", None))
        self.status_value.setText(QCoreApplication.translate("MemberWindow", u"Status", None))
        self.pushButton.setText(QCoreApplication.translate("MemberWindow", u"Plus d'infos", None))
        self.nom_prenom_value.setText(QCoreApplication.translate("MemberWindow", u"Nom et Pr\u00e9nom", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MemberWindow", u"G\u00e9n\u00e9rale", None))
        self.billeterie_filter_btn.setText(QCoreApplication.translate("MainWinMemberWindowdow", u"Filtrer", None))
        self.billeterie_event_btn.setText(QCoreApplication.translate("MemberWindow", u"Gestion de billeterie sur l'\u00e9v\u00e8nement", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.billeterieTab), QCoreApplication.translate("MemberWindow", u"Billeterie", None))
    # retranslateUi


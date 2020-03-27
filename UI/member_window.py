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

from DAO.DAOs import EvenementDAO
from Models.disponibilite import Statut
from Models.evenement import Etat
from PIL import Image, ImageOps


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
        
        events = EvenementDAO.get_all()
        for e in events:
            for r in e.responsables:
                if r.id == self.__member.id:
                    self.__member_events.append(e)
        
        self.__setupUi()
        
        # Connect signals
        self.profile_btn.clicked.connect(self.__open_profile_dialog)
        self.disconnect_btn.clicked.connect(self.__disconnect)
        self.events_list_widget.itemDoubleClicked.connect(self.__open_event_dialog)
        
        self.__inject()
    
    def __refresh_list(self):
        self.__member_events.clear()
        events = EvenementDAO.get_all()
        for e in events:
            for r in e.responsables:
                if r.id == self.__member.id:
                    self.__member_events.append(e)

        self.events_list_widget.clear()
        for e in self.__member_events:
            self.events_list_widget.addItem(self.__get_item(e))
    
    @pyqtSlot()
    def __open_event_dialog(self):
        indexes = self.events_list_widget.selectedIndexes()
        if len(indexes) > 0:
            dialog = Ui_info_event_dialog(self, self.__member_events[indexes[0].row()])
            dialog.exec_()
            self.__refresh_list()
    
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
        self.resize(432, 400)
        self.setStyleSheet(open("UI/styles/base_style.css", "r").read())
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"")
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

        self.form_grid = QGridLayout()
        self.form_grid.setObjectName(u"form_grid")
        self.form_grid.setContentsMargins(5, 5, 5, 5)
        self.nom_prenom_label = QLabel(self.centralwidget)
        self.nom_prenom_label.setObjectName(u"nom_prenom_label")

        self.form_grid.addWidget(self.nom_prenom_label, 0, 0, 1, 1)

        self.evenements_label = QLabel(self.centralwidget)
        self.evenements_label.setObjectName(u"evenements_label")

        self.form_grid.addWidget(self.evenements_label, 2, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.status_value = QLabel(self.widget)
        self.status_value.setObjectName(u"status_value")

        self.horizontalLayout.addWidget(self.status_value)

        self.form_grid.addWidget(self.widget, 1, 1, 1, 1)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")

        self.form_grid.addWidget(self.status_label, 1, 0, 1, 1)

        self.nom_prenom_value = QLabel(self.centralwidget)
        self.nom_prenom_value.setObjectName(u"nom_prenom_value")

        self.form_grid.addWidget(self.nom_prenom_value, 0, 1, 1, 1)

        self.events_list_widget = QListWidget(self.centralwidget)
        self.events_list_widget.setObjectName(u"events_list_widget")

        self.form_grid.addWidget(self.events_list_widget, 3, 0, 1, 2)


        self.container.addLayout(self.form_grid)

        self.container.setStretch(0, 1)
        self.container.setStretch(2, 2)

        self.gridLayout_4.addLayout(self.container, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        #if QT_CONFIG(shortcut)
        self.evenements_label.setBuddy(self.events_list_widget)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.profile_btn, self.disconnect_btn)
        QWidget.setTabOrder(self.disconnect_btn, self.events_list_widget)

        self.__retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MemberWindow", u"Cin\u00e9-Club", None))
        self.titre.setText(QCoreApplication.translate("MemberWindow", u"Cin\u00e9-Club", None))
        self.disconnect_btn.setText(QCoreApplication.translate("MemberWindow", u"Se D\u00e9connecter", None))
        self.nom_prenom_label.setText(QCoreApplication.translate("MemberWindow", u"Membre de la mairie / du club :", None))
        self.evenements_label.setText(QCoreApplication.translate("MemberWindow", u"\u00c9v\u00e8nements associ\u00e9s :", None))
        self.status_value.setText(QCoreApplication.translate("MemberWindow", u"Status", None))
        self.status_label.setText(QCoreApplication.translate("MemberWindow", u"Status :", None))
        self.nom_prenom_value.setText(QCoreApplication.translate("MemberWindow", u"Nom et Pr\u00e9nom", None))
    # retranslateUi


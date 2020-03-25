# -*- coding: utf-8 -*-

import os
from DAO.DAOs import EvenementDAO

from PyQt5.QtCore import QCoreApplication, QDate, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, pyqtSlot
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from UI.add_event_dialog import Ui_add_event_dialog
from UI.info_event_dialog import Ui_info_event_dialog

from pathlib import Path
from PIL import Image, ImageOps

from Models.evenement import Etat

class Scheduler(QCalendarWidget):
    def __init__(self, parent=None, events=[]):
        super().__init__(parent)
        self.setGridVisible(True)
        self.__events = events

    def update_events(self, new_events):
        self.__all_events = new_events

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        for event in self.__events:   
            if date == event.date_debut.date():
                painter.setBrush(QColor(event.color))
                painter.drawEllipse(rect.center(), 10, 10)
                painter.drawText(rect, Qt.AlignCenter, str(date.day()))

class Ui_AdminWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        
        # Initializing variables
        self.__all_events = EvenementDAO.get_all()
        self.__setupUi()
        
        # Initialiazing members
        self.filtre_date_edit.setDate(QDate.currentDate())
        
        self.__afficher_all_evenements()
        
        # connect signals
        self.addEventBtn.clicked.connect(self.__ouvrir_ajout_evenement_dialog)
        #self.scheduler.currentPageChanged.connect(self.__afficher_evenements)
        self.eventsListWidget.itemDoubleClicked.connect(self.__ouvrir_evenement_dialog)
        self.reset_filtre_btn.clicked.connect(self.__reset_filter)
        self.filter_btn.clicked.connect(self.__filter_events)

    @pyqtSlot()
    def __reset_filter(self):
        self.filtre_date_edit.setDate(QDate.currentDate())
        self.__afficher_all_evenements()
        
    @pyqtSlot()
    def __ouvrir_evenement_dialog(self):
        """
        Cette fonction permet d'ouvrir une fenêtre qui affiche les détails d'un évènement
        """
        indexes = self.eventsListWidget.selectedIndexes()
        if len(indexes) > 0:
            dialog = Ui_info_event_dialog(self, Qt.WindowFlags(), self.__all_events[indexes[0].row()])
            dialog.show()

    @pyqtSlot()
    def __ouvrir_ajout_evenement_dialog(self):
        """
        Cette fonction permet d'ouvrir une fenêtre qui permet l'ajout d'un évènement
        """       
        dialog = Ui_add_event_dialog(self)
        ret = dialog.exec_()
        
        if ret == 1:
            if dialog.potential_new_event != None:
                EvenementDAO.add_event(dialog.potential_new_event)
                self.__all_events.append(dialog.potential_new_event)
                self.scheduler.update_events(self.__all_events)
                self.scheduler.updateCells()
            else:
                # error (unknown error)
                QMessageBox.critical(self, "Erreur!", "Error inconnue, veuillez réessayer!")
        else:
            print("L'ajout de l'évènement a été annuler!")
    
    @pyqtSlot()
    def __filter_events(self):
        """
        Cette fonction permet de filtrer les évènements par date
        """
        wanted_date = self.filtre_date_edit.date()
        self.__afficher_evenements(wanted_date.year(), wanted_date.month())

    def __afficher_all_evenements(self):
        """
        Cette fonction permet d'afficher toutes les évènements
        """
        self.eventsListWidget.clear()
        for e in self.__all_events:
            Path("UI/events_icons").mkdir(parents=True, exist_ok=True)
            icon_name = "UI/events_icons/event_%d.png" % e.id
            self.__draw_image(icon_name, (10, 10), e.color)
            icon = QIcon(icon_name)

            item = QListWidgetItem(icon, str(e))
            if e.etat == Etat.EN_ATTENTE:
                item.setBackground(QColor("#FF4B3C"))
            if e.etat == Etat.EN_COURS:
                item.setBackground(QColor("#FFCD42"))
            if e.etat == Etat.TERMINE:
                item.setBackground(QColor("#12D11C"))
            self.eventsListWidget.addItem(item)

    def __afficher_evenements(self, year, month):
        """
        Cette fonction permet d'afficher les évènements de l'année et le mois souhaité
        """
        self.__all_events = EvenementDAO.get_all()
        
        self.eventsListWidget.clear()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for i, e in enumerate(self.__all_events):
            if e.date_debut.date().year() == year and e.date_debut.date().month() == month:
                icon_name = dir_path+"/events_icons/event%d.png" % i
                self.__draw_image(icon_name, (10, 10), e.color)
                icon = QIcon(icon_name)
                
                item = QListWidgetItem(icon, str(e))
                self.eventsListWidget.addItem(item)

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
            self.setObjectName(u"AdminWindow")
        self.resize(530, 569)
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
        self.titre = QLabel(self.centralwidget)
        self.titre.setObjectName(u"titre")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titre.sizePolicy().hasHeightForWidth())
        self.titre.setSizePolicy(sizePolicy)

        self.container.addWidget(self.titre)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setFrameShape(QFrame.HLine)

        self.container.addWidget(self.line)

        self.form_grid = QGridLayout()
        self.form_grid.setObjectName(u"form_grid")
        self.form_grid.setSizeConstraint(QLayout.SetFixedSize)
        self.form_grid.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.events_tab = QWidget()
        self.events_tab.setObjectName(u"events_tab")
        self.gridLayout_2 = QGridLayout(self.events_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scheduler = Scheduler(self.events_tab, self.__all_events)
        self.scheduler.setObjectName(u"scheduler")

        self.gridLayout_2.addWidget(self.scheduler, 0, 0, 1, 2)

        self.eventsListWidget = QListWidget(self.events_tab)
        self.eventsListWidget.setObjectName(u"eventsListWidget")

        self.gridLayout_2.addWidget(self.eventsListWidget, 2, 0, 1, 2)

        self.addEventBtn = QPushButton(self.events_tab)
        self.addEventBtn.setObjectName(u"addEventBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addEventBtn.sizePolicy().hasHeightForWidth())
        self.addEventBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.addEventBtn, 1, 1, 1, 1)

        self.filter_widget = QWidget(self.events_tab)
        self.filter_widget.setObjectName(u"filter_widget")
        self.gridLayout_5 = QGridLayout(self.filter_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.filtre_date_label = QLabel(self.filter_widget)
        self.filtre_date_label.setObjectName(u"filtre_date_label")

        self.gridLayout_5.addWidget(self.filtre_date_label, 0, 0, 1, 1)

        self.filtre_date_edit = QDateEdit(self.filter_widget)
        self.filtre_date_edit.setObjectName(u"filtre_date_edit")
        self.filtre_date_edit.setCalendarPopup(True)

        self.gridLayout_5.addWidget(self.filtre_date_edit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.filter_widget, 3, 0, 1, 1)

        self.filter_buttons_container = QWidget(self.events_tab)
        self.filter_buttons_container.setObjectName(u"filter_buttons_container")
        self.horizontalLayout = QHBoxLayout(self.filter_buttons_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reset_filtre_btn = QPushButton(self.filter_buttons_container)
        self.reset_filtre_btn.setObjectName(u"reset_filtre_btn")

        self.horizontalLayout.addWidget(self.reset_filtre_btn)

        self.filter_btn = QPushButton(self.filter_buttons_container)
        self.filter_btn.setObjectName(u"filter_btn")

        self.horizontalLayout.addWidget(self.filter_btn)


        self.gridLayout_2.addWidget(self.filter_buttons_container, 3, 1, 1, 1)

        self.tabWidget.addTab(self.events_tab, "")
        self.staff_tab = QWidget()
        self.staff_tab.setObjectName(u"staff_tab")
        self.gridLayout = QGridLayout(self.staff_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.staff_tab)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.staff_tab, "")
        self.history_tab = QWidget()
        self.history_tab.setObjectName(u"history_tab")
        self.tabWidget.addTab(self.history_tab, "")

        self.form_grid.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.container.addLayout(self.form_grid)

        self.container.setStretch(0, 1)
        self.container.setStretch(2, 2)

        self.gridLayout_4.addLayout(self.container, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)
        #if QT_CONFIG(shortcut)
        self.filtre_date_label.setBuddy(self.filtre_date_edit)
        #endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.scheduler)
        QWidget.setTabOrder(self.scheduler, self.addEventBtn)
        QWidget.setTabOrder(self.addEventBtn, self.eventsListWidget)
        QWidget.setTabOrder(self.eventsListWidget, self.filtre_date_edit)
        QWidget.setTabOrder(self.filtre_date_edit, self.filter_btn)
        QWidget.setTabOrder(self.filter_btn, self.reset_filtre_btn)
        QWidget.setTabOrder(self.reset_filtre_btn, self.tableWidget)

        self.__retranslateUi()

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(self)     
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Tableau de bord", None))
        self.titre.setText(QCoreApplication.translate("AdminWindow", u"Cin\u00e9-Club", None))
        self.addEventBtn.setText(QCoreApplication.translate("AdminWindow", u"Ajouter un \u00e9v\u00e8nement", None))
        self.filtre_date_label.setText(QCoreApplication.translate("AdminWindow", u"Filtrer par date", None))
        self.reset_filtre_btn.setText(QCoreApplication.translate("AdminWindow", u"R\u00e9tablir", None))
        self.filter_btn.setText(QCoreApplication.translate("AdminWindow", u"Filtrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events_tab), QCoreApplication.translate("AdminWindow", u"\u00c9v\u00e8nements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.staff_tab), QCoreApplication.translate("AdminWindow", u"Membres de la Mairie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("AdminWindow", u"Historique", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 569)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        f = open(dir_path+"/base_style.css", "r")
        self.centralwidget.setStyleSheet(f.read())
        f.close()
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
        self.addEventBtn = QPushButton(self.events_tab)
        self.addEventBtn.setObjectName(u"addEventBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.addEventBtn.sizePolicy().hasHeightForWidth())
        self.addEventBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.addEventBtn, 3, 1, 1, 1)

        self.calendarWidget = QCalendarWidget(self.events_tab)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 2)

        self.eventsListWidget = QListWidget(self.events_tab)
        self.eventsListWidget.setObjectName(u"eventsListWidget")

        self.gridLayout_2.addWidget(self.eventsListWidget, 1, 0, 1, 1)

        self.detailsEventBtn = QPushButton(self.events_tab)
        self.detailsEventBtn.setObjectName(u"detailsEventBtn")
        sizePolicy2.setHeightForWidth(self.detailsEventBtn.sizePolicy().hasHeightForWidth())
        self.detailsEventBtn.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.detailsEventBtn, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titre.setText(QCoreApplication.translate("MainWindow", u"Cin\u00e9-Club", None))
        self.addEventBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter un \u00e9v\u00e8nement", None))
        self.detailsEventBtn.setText(QCoreApplication.translate("MainWindow", u"Plus d'infos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events_tab), QCoreApplication.translate("MainWindow", u"\u00c9v\u00e8nements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.staff_tab), QCoreApplication.translate("MainWindow", u"Membres de la Mairie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"Historique", None))
    # retranslateUi


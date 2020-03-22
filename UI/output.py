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
        MainWindow.setStyleSheet(u"QLabel#titre{ \n"
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
"QLineEdit {\n"
"	color: #495057;\n"
"	background-color: #fff;\n"
"	border: 1px solid #ced4da;\n"
"	border-radius: 2px;\n"
"	padding: 4 1px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
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
        self.calendarWidget = QCalendarWidget(self.events_tab)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 2)

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

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.filtre_date_label.setBuddy(self.filtre_date_edit)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.tabWidget, self.calendarWidget)
        QWidget.setTabOrder(self.calendarWidget, self.addEventBtn)
        QWidget.setTabOrder(self.addEventBtn, self.eventsListWidget)
        QWidget.setTabOrder(self.eventsListWidget, self.filtre_date_edit)
        QWidget.setTabOrder(self.filtre_date_edit, self.filter_btn)
        QWidget.setTabOrder(self.filter_btn, self.reset_filtre_btn)
        QWidget.setTabOrder(self.reset_filtre_btn, self.tableWidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titre.setText(QCoreApplication.translate("MainWindow", u"Cin\u00e9-Club", None))
        self.addEventBtn.setText(QCoreApplication.translate("MainWindow", u"Ajouter un \u00e9v\u00e8nement", None))
        self.filtre_date_label.setText(QCoreApplication.translate("MainWindow", u"Filtrer par date", None))
        self.reset_filtre_btn.setText(QCoreApplication.translate("MainWindow", u"R\u00e9tablir", None))
        self.filter_btn.setText(QCoreApplication.translate("MainWindow", u"Filtrer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.events_tab), QCoreApplication.translate("MainWindow", u"\u00c9v\u00e8nements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.staff_tab), QCoreApplication.translate("MainWindow", u"Membres de la Mairie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), QCoreApplication.translate("MainWindow", u"Historique", None))
    # retranslateUi


# -*- coding: utf-8 -*-

import os
import re
import hashlib

from DAO.DAOs import UtilisateurDAO

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, Qt, QUrl, pyqtSlot)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPainter,
                         QPalette, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

from UI.admin_window import Ui_AdminWindow
from UI.member_window import Ui_MemberWindow

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.__setupUi()
        
        # setup signals
        self.connect_btn.clicked.connect(self.__connecter)
    
    @pyqtSlot()
    def __connecter(self):
        email = self.email_input.text()
        password = ""
        if self.pass_input.text() != "":
            password = hashlib.sha256(self.pass_input.text().encode()).hexdigest()
        if len(email) == 0:
            self.error_text.setText("Il faut saisir votre email adresse!")
        else:
            check_format = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
            if check_format != None:
                users = UtilisateurDAO.get_all()
                for u in users:
                    if u.email == email:
                        if u.admin:
                            # Check password
                            if u.password == password:
                                self.hide()
                                window = Ui_AdminWindow(self)
                                window.show()
                            else:
                                self.error_text.setText("Le mot de passe est incorrect!")
                        else:
                            # Check password
                            if u.password == password:
                                self.hide()
                                window = Ui_MemberWindow(parent=self, member=u)
                                window.show()
                            else:
                                self.error_text.setText("Le mot de passe est incorrect!")
                        break
                else:
                    self.error_text.setText("L'adresse email ou mot de passe non valide!")
            else:
                self.error_text.setText("Format d'adresse email non valide!")

    def showEvent(self, event):
        self.pass_input.setText("")
        return super().showEvent(event)

    def __setupUi(self):
        if self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(555, 445)
        self.setStyleSheet(open("UI/styles/base_style.css", "r").read())
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
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

        self.authentification_label = QLabel(self.centralwidget)
        self.authentification_label.setObjectName(u"authentification_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.authentification_label.sizePolicy().hasHeightForWidth())
        self.authentification_label.setSizePolicy(sizePolicy2)
        self.authentification_label.setTextFormat(Qt.PlainText)

        self.container.addWidget(self.authentification_label)

        self.form_grid = QGridLayout()
        self.form_grid.setObjectName(u"form_grid")
        self.form_grid.setSizeConstraint(QLayout.SetFixedSize)
        self.form_grid.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.form_grid.addWidget(self.label, 2, 0, 1, 1)

        self.email_input = QLineEdit(self.centralwidget)
        self.email_input.setObjectName(u"email_input")

        self.form_grid.addWidget(self.email_input, 2, 1, 1, 1)

        self.pass_input = QLineEdit(self.centralwidget)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.form_grid.addWidget(self.pass_input, 3, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.form_grid.addWidget(self.label_2, 3, 0, 1, 1)

        self.connect_btn = QPushButton(self.centralwidget)
        self.connect_btn.setObjectName(u"connect_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy3)
        self.connect_btn.setMinimumSize(QSize(100, 0))
        self.connect_btn.setBaseSize(QSize(150, 0))

        self.form_grid.addWidget(self.connect_btn, 4, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)

        self.error_text = QLabel(self.centralwidget)
        self.error_text.setObjectName(u"error_text")
        sizePolicy2.setHeightForWidth(self.error_text.sizePolicy().hasHeightForWidth())
        self.error_text.setSizePolicy(sizePolicy2)
        self.error_text.setLayoutDirection(Qt.LeftToRight)
        self.error_text.setStyleSheet(open("UI/styles/error.css").read())

        self.form_grid.addWidget(self.error_text, 1, 1, 1, 1, Qt.AlignRight)

        self.form_grid.setColumnStretch(0, 1)
        self.form_grid.setColumnStretch(1, 2)

        self.container.addLayout(self.form_grid)

        self.container.setStretch(0, 1)
        self.container.setStretch(2, 1)
        self.container.setStretch(3, 2)

        self.gridLayout_4.addLayout(self.container, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 21))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.__retranslateUi()
        
        QMetaObject.connectSlotsByName(self)
    # setupUi

    def __retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titre.setText(QCoreApplication.translate("MainWindow", u"Cin\u00e9-Club", None))
        self.authentification_label.setText(QCoreApplication.translate("MainWindow", u"Authentification", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Adresse Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"Se Connecter", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre adresse email", None))
        self.pass_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Entrez votre mot de passe", None))
    # retranslateUi

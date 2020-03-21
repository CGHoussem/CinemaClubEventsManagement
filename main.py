"""
La boucle principale de l'application

    Écrit par: BEN MABROUK Houssem
    Email: cjhoussem@gmail.com
    Tel: +33 7 66 21 59 63
    Date: 2019-2020
"""

from UI.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Ui_MainWindow()
    main.show()
    sys.exit(app.exec_())

"""
La boucle principale de l'application

    Écrit par: BEN MABROUK Houssem
    Email: cjhoussem@gmail.com
    Tel: +33 7 66 21 59 63
    Date: 2019-2020
"""

from graphique import *

if __name__ == "__main__":
    root = Tk()
    s = ttk.Style(root)
    s.theme_use('clam')

    app = Application(master=root)
    app.master.title("Mini Projet")
    app.master.minsize(600, 400)
    app.master.maxsize(600, 400)

    app.mainloop()

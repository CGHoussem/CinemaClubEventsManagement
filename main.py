import tkinter as tk
import webview


class Personne:
    def __init__(self, nom, prenom, adresse, email, tel):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.email = email
        self.tel = tel

class MembreClub(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class MembreMairie(Personne):
    def __init__(self, nom, prenom, adresse, email, tel, mairie):
        super().__init__(nom, prenom, adresse, email, tel)
        self.mairie = mairie

class Artiste(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class Critique(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class Technicien(Personne):
    def __init__(self, nom, prenom, adresse, email, tel):
        super().__init__(nom, prenom, adresse, email, tel)

class SalleProjection:
    def __init__(self, adresse, nbrPlaceTotal, typeProjection, responsable):
        self.adresse = adresse
        self.nbrPlaceTotal = nbrPlaceTotal
        self.typeProjection = typeProjection
        self.reponsable = responsable

class Evenement:
    def __init__(self, date=None, membres=list()):
        self.date = date
        self.membres = membres

    def ajouterMembre(self, membre):
        """
            Cette fonction permettera d'ajouter un membre 

            Parameters:
                membre (Membre): Le membre que vous voulez ajouter
        """
        if type(membre) in [Artiste, Critique, Technicien, MembreClub]:
            self.membres.append(membre)
        else:
            raise TypeError("L'argument donné n'est pas de type artiste, critique, technicien ou un membre du club associatif!")

class Projection(Evenement):
    def __init__(self, date=None, membres=None, presentationAuteur=None, contexte=None, debat=None):
        super().__init__(date, membres)
        self.presentationAuteur = presentationAuteur
        self.contexte = contexte
        self.debat = debat

class Debat:
    def __init__(self, animateur, duree):
        self.animateur = animateur
        self.duree = duree

# Classes des interfaces graphiques

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.creer_interface()

    def creer_interface(self):
        self.titre = tk.Label(self, text="Gestion des évènements", font=('Times', '32'))
        self.titre.pack(side="top")

        self.label_lst_evenements = tk.Label(self, text="Liste des évènements")
        self.label_lst_evenements.pack()
        
        self.lst_evenements = tk.Listbox(self)
        self.lst_evenements.pack()

        self.ajouter_evt_btn = tk.Button(self, text="Ajouter un évènement", command=self.ajouter_evt)
        self.ajouter_evt_btn.pack()

    def ajouter_evt(self):
        self.temp = Projection()
        dialog = AjouterEvenement(parent=self)


class AjouterEvenement(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.transient(parent)
        self.parent = parent
        self.body = tk.Frame(self)
        self.body.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        self.minsize(500, 300)

        self.creer_interface()
        self.grab_set()

    def creer_interface(self):
        titre = tk.Label(self.body, text="Ajouter un évènement", font=('Times', '18'))
        titre.pack(side="top")

        evenement_label_frame = tk.LabelFrame(self.body, text="Détails sur l'évènement")
        evenement_label_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(evenement_label_frame, text="Date de début:").grid(row=0, column=0)
        date_debut = tk.Entry(evenement_label_frame).grid(row=0, column=1)

        tk.Button(evenement_label_frame, text="Ajouter un membre", command=self.ajouter_membre).grid(row=1, column=0)
        lst_membres = tk.Listbox(evenement_label_frame).grid(row=1, column=1)

        projection_label_frame = tk.LabelFrame(self.body, text="Détails sur la projection")
        projection_label_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(evenement_label_frame, text="Présentation de l'auteur:").grid(row=0, column=0)
        date_debut = tk.Entry(evenement_label_frame).grid(row=0, column=1)

        tk.Label(evenement_label_frame, text="Date de début:").grid(row=1, column=0)
        date_debut = tk.Entry(evenement_label_frame).grid(row=1, column=1)

        tk.Label(evenement_label_frame, text="Date de début:").grid(row=2, column=0)
        date_debut = tk.Entry(evenement_label_frame).grid(row=2, column=1)


    def ajouter_membre(self):
        print("TODO ajouter membre")
        pass

if __name__ == "__main__":
    #root = tk.Tk()
    #app = Application(master=root)
    #app.master.title("Mini Projet")
    #app.master.minsize(600, 400)

    #app.mainloop()
    
    window = webview.create_window("ABC", html="<h1>TESTING</h1>")
    window.start()
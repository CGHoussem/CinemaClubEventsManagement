"""
Ce module prend en charge de la partie graphique, tels que: 
    - Toutes les interfaces graphiques
    - Les fonctions de toutes les boutons
    - ...
"""
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from custom_widgets.textarea import TextArea

from models import *

# Classes des interfaces graphiques
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=TRUE, padx=5, pady=5)
        self.__creer_interface()

    def __creer_interface(self):
        def afficher_evts(x):
            selected_event_ids = c.get_calevents(date=c.selection_get())
            lst_evenements.reset()

            for i, event_id in enumerate(selected_event_ids):
                text = c.calevent_cget(event_id, option='text')
                date = c.get_date()
                event_description = 'Event: %s [%s]\n' % (text, date)
                lst_evenements.insert(1.0, event_description)
                lst_evenements.T.tag_add('event', "%d.0"%(i+1), "%d.6"%(i+1))
            lst_evenements.T.tag_config('event', background='yellow')

        titre = Label(self, text="Gestion des évènements", font=('Times', '32'))

        left_panel = Frame(self)
        right_panel = Frame(self)

        c = Calendar(left_panel)
        events = []

        date = c.datetime.today() + c.timedelta(days=2)
        events.append(c.calevent_create(date, text='Projection du film 1', tags=['reminder']))
        events.append(c.calevent_create(date, text='Coupe du monde'))
        c.tag_config('reminder', background='#698535')
        c.bind("<<CalendarSelected>>", afficher_evts)
        c.pack(fill=BOTH, expand=TRUE)

        Label(left_panel, text="Liste des évènements").pack(anchor=W)
        lst_evenements = TextArea(left_panel)
        lst_evenements.pack(anchor=W)

        ttk.Button(right_panel, text="Ajouter un évènement", command=self.__ajouter_evt).pack(pady=5)
        ttk.Button(right_panel, text="Liste des membres de la mairie", command=self.__afficher_membres_mairie).pack(pady=5)

        # Packing
        titre.pack()
        right_panel.pack(side=RIGHT, padx=10)
        left_panel.pack(side=LEFT, padx=5)

    def __ajouter_evt(self):
        dialog_window = AjouterEvenement(parent=self)
        
    def __afficher_membres_mairie(self):
        print("TODO: Afficher les membres de la mairie")

class AjouterEvenement(Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.transient(parent)
        self.container = Frame(self)
        self.canvas = Canvas(self.container)
        self.scrollbar = Scrollbar(self.container, orient=VERTICAL, command=self.canvas.yview)
        self.body = Frame(self.canvas)

        self.body.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window=self.body, anchor=NW)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", self.__on_mousewheel)

        self.canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.container.pack(fill=BOTH, padx=10, pady=10, expand=TRUE)
        self.minsize(500, 400)
        self.maxsize(500, 800)

        self.__creer_interface()
        self.grab_set()

        self.__est_projection = False
        self.__projection_label_frame = None

        self.__debat_existe = False
        self.__debat_label_frame = None

    def __creer_interface(self):
        titre = Label(self.body, text="Ajouter un évènement", font=('Times', '18'))

        evenement_label_frame = LabelFrame(self.body, text="Détails sur l'évènement", height=300)
        
        ajout_btn = ttk.Button(self.body, text="Ajouter l'évènement", command=self.__ajouter_evenement)

        Label(evenement_label_frame, text="Date de début").grid(row=0, column=0, sticky=NW)
        date_debut = DateEntry(evenement_label_frame, locale='fr_FR').grid(row=0, column=1, sticky=NW)

        Label(evenement_label_frame, text="Date de fin").grid(row=0, column=2, sticky=NW)
        date_fin = DateEntry(evenement_label_frame, locale='fr_FR').grid(row=0, column=3, sticky=NW)

        Label(evenement_label_frame, text="Description").grid(row=1, column=0, sticky=NW)
        description = Text(evenement_label_frame, height=5, width=30, wrap=WORD).grid(row=1, column=1, columnspan=3, sticky=NW)

        Label(evenement_label_frame, text="Responsables").grid(row=2, column=0, sticky=NW)
        liste_membres = Listbox(evenement_label_frame, height=5, width=25).grid(row=2, column=1, columnspan=3, sticky=NW)
        ttk.Button(evenement_label_frame, text="Ajouter un responsable", command=self.__ajouter_responsable_evenement)\
            .grid(row=2, column=3, sticky=W)

        temp = IntVar()
        Checkbutton(evenement_label_frame, command=self.__show_projection, text="Est une projection?", variable=temp).grid(row=3, column=0, sticky=NW)
        
        # Packing
        titre.pack(side=TOP)
        evenement_label_frame.pack(fill=BOTH, padx=5, pady=5)
        ajout_btn.pack(side=BOTTOM, anchor=E)
       
    def __ajouter_evenement(self):
        print("Ajouter l'évènement!")

    def __show_projection(self):
        self.__est_projection = not self.__est_projection
        if self.__est_projection:
            self.__projection_label_frame = LabelFrame(self.body, text="Détails sur la projection")

            avant_projection_label_frame = LabelFrame(self.__projection_label_frame, text="Avant la projection")
            apres_projection_label_frame = LabelFrame(self.__projection_label_frame, text="Après la projection")

            # Avant la projection
            presentation_auteur_label_frame = LabelFrame(avant_projection_label_frame, text="Présentation de l'auteur")
            Label(presentation_auteur_label_frame, text="Nom de l'auteur").grid(row=0, column=0, sticky=NW)
            nom_auteur = Entry(presentation_auteur_label_frame).grid(row=0, column=1, sticky=NW)
            Label(presentation_auteur_label_frame, text="Durée de la présentation").grid(row=1, column=0, sticky=NW)
            duree_presentation_auteur = Entry(presentation_auteur_label_frame).grid(row=1, column=1, sticky=NW)

            Label(avant_projection_label_frame, text="Context").grid(row=1, column=0, sticky=NW)
            duree_presentation_auteur = Text(avant_projection_label_frame, height=5, width=30, wrap=WORD).grid(row=1, column=1, sticky=NW)

            # # Après la projection
            temp = IntVar()
            chk_btn = Checkbutton(apres_projection_label_frame, command=lambda: self.__show_debat(apres_projection_label_frame), text="Débat?", variable=temp).grid(row=0, column=0, sticky=NW)

            # Packing everything together
            presentation_auteur_label_frame.grid(row=0, column=0, columnspan=2, ipadx=5, ipady=5, padx=5, sticky=NW)
            avant_projection_label_frame.pack(fill=BOTH, expand=TRUE, padx=5, pady=5, ipadx=5, ipady=5)
            apres_projection_label_frame.pack(fill=BOTH, expand=TRUE, padx=5, pady=5, ipadx=5, ipady=5)
            self.__projection_label_frame.pack(fill=BOTH, expand=TRUE, padx=5, pady=5, ipadx=5, ipady=5)

        elif self.__projection_label_frame != None:
            self.__projection_label_frame.destroy()

    def __show_debat(self, parent):
        self.__debat_existe = not self.__debat_existe
        if self.__debat_existe:
            self.__debat_label_frame = LabelFrame(parent, text="Débat")
            self.__debat_label_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=5, sticky=NSEW)

            Label(self.__debat_label_frame, text="Animateur").grid(row=0, column=0, sticky=NW)
            lb = Listbox(self.__debat_label_frame, height=4)
            lb.grid(row=0, column=1, sticky=NW)
            ttk.Button(self.__debat_label_frame, text="Ajouter un animateur", command=self.__ajouter_animateur).grid(row=0, column=2, sticky=NW)

            Label(self.__debat_label_frame, text="Durée").grid(row=1, column=0, sticky=NW)
            duree_debat = Entry(self.__debat_label_frame).grid(row=1, column=1, sticky=NW)
        elif self.__debat_label_frame != None:
            self.__debat_label_frame.destroy()

    # Fonctions qui gére les fonctionalités graphiques
    def __on_mousewheel(self, event):
        self.canvas.yview_scroll(-1*(event.delta//120), UNITS)

    # Fonctions
    def __ajouter_responsable_evenement(self):
        print("TODO ajouter membre")
        pass

    def __ajouter_animateur(self):
        print("TODO: Ajouter un animateur")
        pass
"""
Cette classe permettera de creer une zone de texte déroulante
"""

from tkinter import Frame, Text, Scrollbar, RIGHT, LEFT, Y, END, DISABLED, NORMAL, WORD

class TextArea(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)
        S = Scrollbar(self)
        self.T = Text(self, height=4, width=50, state=DISABLED, wrap=WORD)
        S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=Y)
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)
        
    def insert(self, index, text):
        self.T['state'] = NORMAL
        self.T.insert(index, text)
        self.T['state'] = DISABLED
        
    def reset(self):
        self.T['state'] = NORMAL
        self.T.delete("1.0", END)
        self.T['state'] = DISABLED
        
    def tag_add(self, tag_name, index1, *args):
        self.T.tag_add(tag_name, index1, *args)
from customtkinter import CTk
from modules.application import Application
from modules.gui.guiManager import GUIManager

class MainApp(CTk):
    def __init__(self):
        CTk.__init__(self)

        Application.setup(self)
        GUIManager.setup(self)


root = MainApp()
root.mainloop()

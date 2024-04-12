from customtkinter import CTk
from modules.application import Application
from modules.gui.windowManager import WindowManager
from modules.gui.frames.frames import TopFrame


class MainApp(CTk):
    def __init__(self):
        CTk.__init__(self)

        Application.setup(self)
        WindowManager.setup(self)
        self.load_frames()


    def load_frames(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.topFrame = TopFrame(self)
        self.topFrame.grid(row=0, column=0, sticky="nsew")
        #self.topFrame.configure(fg_color="red")

root = MainApp()
root.mainloop()

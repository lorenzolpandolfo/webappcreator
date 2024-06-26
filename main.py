from customtkinter import CTk
from modules.application import Application
from modules.gui.windowManager import WindowManager
from modules.gui.frames.frames import TopFrame
from modules.logManager.logManager import logger


class MainApp(CTk):
    def __init__(self):
        CTk.__init__(self)
        self.topFrame = None
        logger.info("Initializing graphical user interface")
        logger.info("Application setup")
        Application.setup(self)
        logger.info("WindowManager setup")
        WindowManager.setup(self)
        logger.info("Loading frames")
        self.load_frames()

    def load_frames(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.topFrame = TopFrame(self)
        self.topFrame.grid(row=0, column=0, sticky="nsew")


root = MainApp()
root.mainloop()

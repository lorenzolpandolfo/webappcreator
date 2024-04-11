import os
from modules.application import Application

class Pathes:
    @staticmethod
    def getIconsDirectory() -> str:
        return os.path.abspath(os.path.join(os.getcwd(), "icons"))

    @staticmethod
    def loadImagesPath(title:str):
        ICONS_PATH = Pathes.getIconsDirectory()
        Application.icon_path     = os.path.join(ICONS_PATH, f"{title}.ico")
        Application.temp_png_path = os.path.join(ICONS_PATH, f"{title}.png")

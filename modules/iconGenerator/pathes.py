import os
from modules.application import Application


class Pathes:
    @staticmethod
    def get_icons_directory() -> str:
        return os.path.abspath(os.path.join(os.getcwd(), "icons"))

    @staticmethod
    def load_images_path(title: str):
        icons_path = Pathes.get_icons_directory()
        Application.icon_path     = os.path.join(icons_path, f"{title}.ico")
        Application.temp_png_path = os.path.join(icons_path, f"{title}.png")


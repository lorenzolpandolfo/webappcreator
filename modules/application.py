from dataclasses import dataclass
import os
import winshell

@dataclass
class Application:
    url: str
    title: str
    icon_path: str
    temp_png_path: str
    browser_path: str
    auto_title: bool = True
    mainapp = None
    incognito: bool = False
    shortcut_path = os.path.join(winshell.desktop())

    @staticmethod
    def setup(mainapp):
        Application.mainapp = mainapp

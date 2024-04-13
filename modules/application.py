from dataclasses import dataclass


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

    @staticmethod
    def setup(mainapp):
        Application.mainapp = mainapp

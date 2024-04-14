import os
from modules.application import Application
from pylnk3 import Lnk


class CurrentWebapps:
    @staticmethod
    def list_created_webapps():
        current_created_webapps = []
        files = os.listdir(Application.shortcut_path)
        for file in files:
            if file.endswith("lnk"):
                shortcut_path = os.path.join(Application.shortcut_path, file)
                arguments = CurrentWebapps._read_shortcut_argument_(shortcut_path)
                if Application.signature in arguments and file not in current_created_webapps:
                    current_created_webapps.append(Lnk(shortcut_path))
        return current_created_webapps

    @staticmethod
    def _read_shortcut_argument_(shortcut_path: str):
        return str(Lnk(shortcut_path).arguments)

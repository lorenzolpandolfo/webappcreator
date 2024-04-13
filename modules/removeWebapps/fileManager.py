import os
from modules.application import Application
from pylnk3 import Lnk

class FileManager:
    @staticmethod
    def check_if_webapp_exists():
        current_created_webapps = []
        files = os.listdir(Application.shortcut_path)
        print(f"lendo o diretorio {Application.shortcut_path}")
        for file in files:
            if file.endswith("lnk"):
                shortcut_path = os.path.join(Application.shortcut_path, file)
                arguments = FileManager._read_shortcut_argument_(shortcut_path)
                if Application.signature in arguments and file not in current_created_webapps:
                    current_created_webapps.append(file)

        print("webapps encontrados: ", current_created_webapps)
    
    @staticmethod
    def _check_if_id_registered_(file_id: str):
        with open(os.path.join(os.getcwd(), "ids", "ids.txt")) as file:
            lines = file.readlines()
            for line in lines:
                return file_id in line
        return False

    @staticmethod
    def _read_shortcut_argument_(shortcut_path: str):
        return str(Lnk(shortcut_path).arguments)

import os
from win32com.client import Dispatch
from modules.application import Application


class FileManager:
    @staticmethod
    def check_if_webapp_exists():
        files = os.listdir(Application.shortcut_path)
        print(f"lendo o diretorio {Application.shortcut_path}")
        for file in files:
            if file.endswith("lnk"):
                shortcut_path = os.path.join(Application.shortcut_path, file)
                arguments = FileManager._read_shortcut_argument_(shortcut_path)
                if " WEBAPPCREATORID=" not in arguments:
                    continue
                file_id = arguments.strip(" WEBAPPCREATORID="[1])
                print("o id é: ", file_id)
                return FileManager._check_if_id_registered_(file_id)
        return False

    @staticmethod
    def _check_if_id_registered_(file_id: str):
        with open(os.path.join(os.getcwd(), "ids", "ids.txt")) as file:
            lines = file.readlines()
            for line in lines:
                return file_id in line
        return False

    @staticmethod
    def _read_shortcut_argument_(shortcut_path: str):
        shell = Dispatch('WScript.Shell')
        atalho = shell.CreateShortCut(shortcut_path)
        return atalho.Targetpath

import os
import pywin32
from modules.application import Application


class FileManager:
    @staticmethod
    def check_if_webapp_exists():
        files = os.listdir(Application.shortcut_path)
        print(f"lendo o diretorio {Application.shortcut_path}")
        for file in files:
            print(file)
            if file.endswith("lnk"):
                shortcut_path = os.path.join(Application.shortcut_path, file)
                print(f"{file} termina com lnk ent é atalho")
                print("o seu path é ", shortcut_path)
                arguments = FileManager.read_shortcut_argument(shortcut_path)
                print("os argumentos sao: ", arguments)
                file_id = arguments.strip("ID:"[1])
                print("o id é: ", file_id)
                return FileManager.check_if_id_registered(file_id)
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
        shell = win32com.client.Dispatch("WScript.Shell")
        atalho = shell.CreateShortCut(shortcut_path)
        print(atalho.Arguments)
        print(atalho.Targetpath)
        return atalho.Arguments

import os
import winshell
from win32com.client import Dispatch

from modules.application import Application
from modules.iconGenerator.pathes import Pathes
from modules.titleGenerator.titleGenerator import TitleGenerator
from modules.iconGenerator.iconGenerator import IconGenerator

ICONS_PATH = Pathes.get_icons_directory()


class WebAppCreator:
    @staticmethod
    def create_web_app(url: str, browser_path: str, manual_title: str):
        if Application.auto_title:
            title = TitleGenerator.generate_title(url)
        else:
            title = manual_title if manual_title != "" else "untitled"

        Pathes.load_images_path(title)
        # temp_png_path = os.path.join(ICONS_PATH, f"{title}temp.png")
        # icone_final_path = os.path.join(ICONS_PATH, f"{title}.ico")
        # Application.icon_path = icone_final_path
        # Application.temp_png_path = temp_png_path

        # print(Application.auto_title)
        # print(Application.browser_path)
        # print(Application.icon_path)
        # print(Application.temp_png_path)
        # print(Application.url)
        # print(Application.title)

        Application.title = title
        Application.browser_path = browser_path
        Application.url = url
        IconGenerator.generate_icon(url)
        shortcut_path = os.path.join(winshell.desktop())
        WebAppCreator.create_shortcut(shortcut_path)

    @staticmethod
    def create_shortcut(shortcut_path):
        print("[-] Gerando o webapp...")
        try:
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(os.path.join(shortcut_path, f"{Application.title}.lnk"))
            shortcut.Targetpath = Application.browser_path
            shortcut.IconLocation = Application.icon_path
            shortcut.Arguments = f"--app=https://{Application.url}" if "https://" not in Application.url else f"--app={Application.url}"
            shortcut.save()
        except Exception as e:
            print(f"[x] Houve um erro ao gerar o webapp:\n{e}")
            return
        print("[!] Webapp gerado com sucesso!")

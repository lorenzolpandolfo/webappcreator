import os

from win32com.client import Dispatch

from modules.application import Application
from modules.iconGenerator.pathes import Pathes
from modules.titleGenerator.titleGenerator import TitleGenerator
from modules.iconGenerator.iconGenerator import IconGenerator
from modules.logManager.logManager import logger

ICONS_PATH = Pathes.get_icons_directory()


class WebAppCreator:
    @staticmethod
    def create_web_app(url: str, browser_path: str, manual_title: str):
        if Application.auto_title:
            title = TitleGenerator.generate_title(url)
        else:
            title = manual_title if manual_title != "" else "untitled"

        Pathes.load_images_path(title)
        Application.title = title
        Application.browser_path = browser_path
        Application.url = url
        IconGenerator.generate_icon(url)
        WebAppCreator.create_shortcut()

    @staticmethod
    def create_shortcut():
        logger.info("Initializing webapp creation")
        try:
            logger.info("No errors detected in try-except block")
            shell = Dispatch('WScript.Shell')
            final_shortcut_path = os.path.join(Application.shortcut_path, f"{Application.title}.lnk")
            shortcut = shell.CreateShortCut(final_shortcut_path)
            shortcut.Targetpath = Application.browser_path
            shortcut.IconLocation = Application.icon_path
            argument = f"--app=https://{Application.url}" if "https://" not in Application.url else f"--app={Application.url}"
            if Application.incognito:
                argument = f"--incognito {argument}"
            argument = f"{argument} {Application.signature}"
            shortcut.Arguments = argument
            shortcut.save()
            logger.info("Shortcut created successfully: %s", final_shortcut_path)

        except Exception as e:
            logger.error("An error ocurred while creating shortcut: %s", str(e))
            return
        logger.info("WebApp created sucessfully")

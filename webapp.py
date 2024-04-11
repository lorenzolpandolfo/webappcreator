import os
import winshell
from win32com.client import Dispatch

def create_shortcut(target, shortcut_name, shortcut_path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(os.path.join(shortcut_path, f"{shortcut_name}.lnk"))
    shortcut.Targetpath = target
    shortcut.Arguments = '--incognito --app=https://www.kernel.org'
    shortcut.save()

target_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
shortcut_name = "My App"
shortcut_path = os.path.join(winshell.desktop())

create_shortcut(target_path, shortcut_name, shortcut_path)

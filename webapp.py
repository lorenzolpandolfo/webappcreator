import os
import winshell
import requests
from win32com.client import Dispatch
from PIL import Image

from modules.iconGenerator.pathes import Pathes
from modules.titleGenerator.titleGenerator import TitleGenerator
from modules.application          import Application






ICONS_PATH = Pathes.getIconsDirectory()

def convert_to_ico(png_path, ico_path):
    image = Image.open(png_path)
    image.save(ico_path)


def download_icon(url, save_path) -> bool:
    response = requests.get(url)
    if not response.status_code == 200:return False
    with open(save_path, 'wb') as f:
        f.write(response.content)
        return True
    

def create_shortcut(target, shortcut_name, shortcut_path, icon_path):
    print("[-] Gerando o webapp...")
    try:
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(os.path.join(shortcut_path, f"{shortcut_name}.lnk"))
        shortcut.Targetpath = target
        shortcut.IconLocation = icon_path
        shortcut.Arguments = f"--app={site_url}"
        shortcut.save()
    except Exception as e:
        print(f"[x] Houve um erro ao gerar o webapp:\n{e}")
        return
    print("[!] Webapp gerado com sucesso!")

# URL do site
site_url = input("Link: ")
site_url = f"https://{site_url}" if "https://" not in site_url else site_url
Application.url = site_url

title = TitleGenerator.generateTitle(Application.url) if Application.auto_title else input("> Title: ")




# Caminho local onde o png do icone será salvo
temp_png_path = os.path.join(ICONS_PATH, f"{title}temp.png")
icone_final_path = os.path.join(ICONS_PATH, f"{title}.ico")
print("[-] Caminho dos ícones carregados")

print("[-] Buscando ícone online...")
# Busca o ícone do site a partir da URL
raw_url = site_url.replace("https://www.", "")
icon_url = f"https://www.google.com/s2/favicons?domain_url={raw_url}&sz=96"
print("[-] Realizando download do ícone...")

if download_icon(icon_url, temp_png_path):
    print("[-] Download realizado com sucesso.") 
    # agora o png está salvo, entao precisamos converte-lo para icone
    convert_to_ico(temp_png_path, icone_final_path)
    print("[-] Ícone convertido para .ico")
    # removendo o png temporario
    os.remove(temp_png_path)
    print("[-] Removido arquivo temporário .png")

else:
    print("[x] Erro ao fazer o download do ícone.")
    icone_final_path = "icons\\default.ico"

# Exemplo de uso
target_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Caminho para o executável do Google Chrome
shortcut_name = title
shortcut_path = os.path.join(winshell.desktop()) # o destino do atalho é a área de trabalho

# cria o atalho
create_shortcut(target_path, shortcut_name, shortcut_path, icone_final_path)

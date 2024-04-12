import requests
import os
from PIL import Image

from modules.application import Application
from modules.iconGenerator.pathes import Pathes


def download_icon(url, save_path) -> bool:
    response = requests.get(url)
    if not response.status_code == 200: return False
    with open(save_path, 'wb') as f:
        f.write(response.content)
        return True


def convert_to_ico(png_path, ico_path):
    image = Image.open(png_path)
    image.save(ico_path)


class IconGenerator:
    @staticmethod
    def generate_icon(url: str):
        icon_url = f"https://www.google.com/s2/favicons?domain_url={url}&sz=96"
        temp_png_path = Application.temp_png_path

        if download_icon(icon_url, temp_png_path):
            convert_to_ico(temp_png_path, Application.icon_path)
            os.remove(temp_png_path)
        else:
            Application.icon_path = os.path.join(Pathes.get_icons_directory(), "default.ico")

import os
import json
from dataclasses import dataclass


@dataclass
class Language:
    tab_create: str
    tab_remove: str

    label_url: str
    label_title: str
    label_browser_selector: str
    label_browser_path: str

    button_select_local_icon: str
    button_create_webapp: str

    switch_auto_title: str
    checkbox_incognito_mode: str
    auto_title_warning: str

    @classmethod
    def load_language(cls, json_data):
        return cls(**json_data)


class LanguageManager:
    @staticmethod
    def load_language(language: str):
        translation = LanguageManager.__load_language__(language)
        return Language.load_language(translation)

    @staticmethod
    def __load_language__(language: str):
        file_path = os.path.join(os.getcwd(), "modules", "languages", f"{language}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf8") as file:
                return json.load(file)

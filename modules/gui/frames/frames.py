from customtkinter import CTkFrame, CTkTabview, CTkTextbox, CTkLabel, CTkButton, CTkSwitch, StringVar, CTkComboBox, CTkCheckBox, CTkImage, CTkFont, ThemeManager
import customtkinter
from PIL import Image
import os
from pylnk3 import Lnk

from modules.browsers.defaultPathes import DefaultBrowsersPathes
from modules.application import Application
from modules.webappCreator.webappCreator import WebAppCreator
from modules.languages.languageManager import LanguageManager
from modules.logManager.logManager import logger
from modules.removeWebapps.currentWebapps import CurrentWebapps
from modules.iconGenerator.pathes import Pathes
Language = LanguageManager.setup()


class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        logger.info("Initializing TopFrame")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabview = CTkTabview(self, command=self.tabview_click_callback)
        tabview_create = self.tabview.add(Language.tab_create)
        tabview_remove = self.tabview.add(Language.tab_remove)

        self.tabview.grid(row=0, column=0, sticky="nsew")

        tabview_create.grid_columnconfigure(0, weight=1)
        tabview_remove.grid_columnconfigure(0, weight=1)
        tabview_remove.grid_rowconfigure(0, weight=1)

        self.create_tab = tabview_create
        self.remove_tab = tabview_remove

        self.create_frames()
        self.configure_frames()
        self.create_url_widgets()
        self.create_title_widgets()
        self.create_right_frame_widgets()

        self.checkbox_incognito = CTkCheckBox(self.right_frame, text=Language.checkbox_incognito_mode)
        self.checkbox_incognito.grid(row=2, column=1, padx=10, pady=10)
        self.label_browsers = CTkLabel(self.bottom_frame, text=Language.label_browser_selector)
        self.label_browsers.grid(row=0, column=0, pady=(10,0))
        self.combobox_var = StringVar(value="Google Chrome")
        self.combobox_browsers = CTkComboBox(self.bottom_frame, values=["Google Chrome", "Chromium", "Firefox"],
                                             command=self.combobox_callback, variable=self.combobox_var)
        self.combobox_browsers.grid(row=1, column=0, padx=10, pady=(0,10))

        self.label_browser_path = CTkLabel(self.bottom_frame, text=Language.label_browser_path)
        self.label_browser_path.grid(row=2, column=0)
        self.textbox_browser_path = CTkTextbox(self.bottom_frame, width=200, height=30)
        self.textbox_browser_path.grid(row=3, column=0, padx=10, pady=(0,10), columnspan=2, sticky="ew")

        self.combobox_callback("Google Chrome")

        self.create_run_button()
        logger.info("TopFrame created sucessfully")

    def tabview_click_callback(self):
        webapps_list = CurrentWebapps.list_created_webapps()
        self.delete_all_webapp_frames()
        self.create_webapp_view(webapps_list)
    
    def delete_all_webapp_frames(self):
        for webapp in Application.current_webapps:
            webapp.destroy()
        Application.current_webapps = []

    def create_right_frame_widgets(self):
        self.button_select_icon = CTkButton(self.right_frame, text=Language.button_select_local_icon)
        self.switch_auto_title_variable = StringVar(value="on")
        self.switch_auto_title = CTkSwitch(self.right_frame, text=Language.switch_auto_title, variable=self.switch_auto_title_variable, onvalue="on", offvalue="off", command=lambda:self.switch_title_widgets_visibility())
        self.button_select_icon.grid(row=0, column=1, padx=10, pady=10)
        self.switch_auto_title.grid(row=1, column=1, padx=10, pady=10)

    def create_frames(self):
        self.right_frame = CTkFrame(self.create_tab)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.left_frame = CTkFrame(self.create_tab)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.bottom_frame = CTkFrame(self.create_tab)
        self.bottom_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)
        self.final_frame = CTkFrame(self.create_tab)
        self.final_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10, columnspan=2)

        self.main_frame = CTkFrame(self.remove_tab)
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def create_webapp_view(self, webapp_list: list):
        column = 0
        aux_row = 0
        for row in range(0, len(webapp_list)):
            if (row != 0) and (row % 5) == 0:
                aux_row -= 4
                column += 1
            else:
                aux_row += 1

            webapp_instance = WebAppFrame(self.main_frame, webapp_list[row], height=60)
            webapp_instance.grid(row=aux_row, column=column, sticky="ew", padx=(5,0), pady=(5,0))
            Application.current_webapps.append(webapp_instance)

    def configure_frames(self):
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.final_frame.grid_columnconfigure(0, weight=1)

    def create_title_widgets(self):
        self.label_title = CTkLabel(self.left_frame, text=Language.label_title, state="disabled")
        self.textbox_title = CTkTextbox(self.left_frame, width=200, height=30, text_color="gray")
        self.textbox_title.insert("1.0", Language.auto_title_warning)
        self.label_title.grid(row=2, column=0, padx=10, pady=(10,0))
        self.textbox_title.grid(row=3, column=0, pady=(0,20))
        self.textbox_title.configure(state="disabled")
    
    def create_url_widgets(self):
        self.label_url = CTkLabel(self.left_frame, text=Language.label_url)
        self.label_url.grid(row=0, column=0, padx=10, pady=(10,0))
        self.textbox_url = CTkTextbox(self.left_frame, width=200, height=30)
        self.textbox_url.grid(row=1, column=0)

    def create_run_button(self):
        self.button_run = CTkButton(self.final_frame, text=Language.button_create_webapp, command=self.create_button_callback)
        self.button_run.grid(row=0, column=0, padx=10, pady=10)

    def switch_title_widgets_visibility(self):
        normal = self.label_title.cget("state") == "normal"
        Application.auto_title = normal
        if normal:
            self.label_title.configure(state="disabled")
            self.textbox_title.delete("1.0", "end")
            self.textbox_title.insert("1.0", Language.auto_title_warning)
            self.textbox_title.configure(state="disabled", text_color="gray")

        else:
            self.label_title.configure(state="normal")
            text_color = "black" if (customtkinter.get_appearance_mode() == "light") else "white"
            self.textbox_title.configure(state="normal", text_color=text_color)
            self.textbox_title.delete("1.0", "end")

    def combobox_callback(self, event):
        self.combobox_var.set(event)
        self.textbox_browser_path.delete("1.0", "end")
        self.textbox_browser_path.insert("1.0", DefaultBrowsersPathes.get_default_path(event).replace("\\\\", "/"))

    def create_button_callback(self, *args):
        url = self.textbox_url.get("1.0", "end-1c")
        browser_path = self.textbox_browser_path.get("1.0", "end-1c")
        manual_title = self.textbox_title.get("1.0", "end-1c")
        if url != "" and browser_path != "":
            Application.incognito = self.checkbox_incognito.get()
            WebAppCreator.create_web_app(url, browser_path, manual_title)
        else:
            print("a url está vazia")
            

class WebAppFrame(CTkFrame):
    def __init__(self, master, aslnk: Lnk,  *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.browser: str = None
        self.data: Lnk = aslnk
        self.title = os.path.basename(self.data.file).replace(".lnk", "")

        self.configure_grid()
        self.get_webapp_browser()
        self.create_widgets()


    def get_webapp_browser(self):
        browser_path = str(self.data.path)
        for browser in DefaultBrowsersPathes.supported_browsers:
            if browser in browser_path.lower():
                self.browser = browser.replace(".exe", "").capitalize()
                break
    
    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        icon = Image.open(self.data.icon)
        self.image_icon = CTkImage(light_image=icon, dark_image=icon, size=(30,30))

        self.frame_title = CTkFrame(self)
        self.frame_title.grid(row=0,column=0,padx=5,pady=5)

        self.frame_details = CTkFrame(self)
        self.frame_details.grid(row=1,column=0, padx=5, pady=5)

        self.label_image = CTkLabel(self.frame_title, text="", image=self.image_icon)
        self.label_image.grid(row=0, column=0)

        self.label_title = CTkLabel(self.frame_title, text=self.title, font=CTkFont(family="Roboto", size=20), anchor="w")
        self.label_title.grid(row=0, column=1, padx=5, pady=5)

        self.label_browser = CTkLabel(self.frame_details, text=self.browser)
        self.label_browser.grid(row=0, column=0)

        incognito_mode = f"({Language.incognito_mode_message})" if "--incognito" in self.data.arguments else f"({Language.keep_data_mode_message})"
        self.label_incognito = CTkLabel(self.frame_details, text=incognito_mode)
        self.label_incognito.grid(row=0, column=1, padx=5, pady=5)

        self.button_remove = CTkButton(self, text=Language.tab_remove, command=self.remove_webapp)
        self.button_remove.grid(row=1, column=1, padx=(0,7))


    def remove_webapp(self):
        os.remove(self.data.file)
        self.destroy()
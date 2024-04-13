from customtkinter import CTkFrame, CTkTabview, CTkTextbox, CTkLabel, CTkButton, CTkSwitch, StringVar, CTkComboBox, CTkCheckBox
from modules.browsers.defaultPathes import DefaultBrowsersPathes
from modules.application import Application
from modules.webappCreator.webappCreator import WebAppCreator
from modules.languages.languageManager import LanguageManager

Language = LanguageManager.load_language("eng")


class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabview = CTkTabview(self)
        tabview_create = self.tabview.add(Language.tab_create)
        tabview_remove = self.tabview.add(Language.tab_remove)

        self.tabview.grid(row=0, column=0, sticky="nsew", padx=5, pady=(0,5))

        tabview_create.grid_columnconfigure(0, weight=1)

        self.create_tab = tabview_create

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
        if (normal):
            self.label_title.configure(state="disabled")
            self.textbox_title.delete("1.0", "end")
            self.textbox_title.insert("1.0", "Título automático ativo")
            self.textbox_title.configure(state="disabled", text_color="gray")

        else:
            self.label_title.configure(state="normal")
            self.textbox_title.configure(state="normal", text_color="black")
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
            WebAppCreator.create_web_app(url, browser_path, manual_title)
        else:
            print("a url está vazia")
            

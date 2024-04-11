from customtkinter import CTkFrame, CTkTabview, CTkTextbox, CTkLabel, CTkButton, CTkSwitch, StringVar

class TopFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.tabview = CTkTabview(self)
        self.tabview.add("Create")
        self.tabview.add("Remove")
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.tabview.tab("Create").grid_columnconfigure(0, weight=1)
        self.create_tab = self.tabview.tab("Create")

        self.label_url = CTkLabel(self.create_tab, text="Insira o link")
        self.label_url.grid(row=0, column=0, padx=10, pady=10)
        self.textbox_url = CTkTextbox(self.create_tab, width=50, height=30)
        self.textbox_url.grid(row=1, column=0, sticky="nsew")
        
        self.create_title_widgets()

        self.button_select_icon = CTkButton(self.create_tab, text="Procurar ícone")
        self.switch_auto_title_variable = StringVar(value="on")
        self.switch_auto_title = CTkSwitch(self.create_tab, text="Título automático", variable=self.switch_auto_title_variable, onvalue="on", offvalue="off", command=lambda:self.switch_title_widgets_visibility())
        self.button_select_icon.grid(row=0, column=1, padx=10, pady=10)
        self.switch_auto_title.grid(row=1, column=1, padx=10, pady=10)

    def create_title_widgets(self):
        self.label_title = CTkLabel(self.create_tab, text="Insira o título do WebApp")
        self.label_title.grid(row=2, column=0, padx=10, pady=10)
        self.textbox_title = CTkTextbox(self.create_tab, width=50, height=30)
        self.textbox_title.grid(row=3, column=0, sticky="nsew")
    
    def switch_title_widgets_visibility(self):
        if self.label_title.winfo_viewable():
            self.label_title.grid_forget()
            self.textbox_title.grid_forget()
        else:
            self.label_title.grid(row=2, column=0, padx=10, pady=10)
            self.textbox_title.grid(row=3, column=0, sticky="nsew")

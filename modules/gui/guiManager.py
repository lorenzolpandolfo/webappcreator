from customtkinter import CTk

class GUIManager:
    @staticmethod
    def setup(mainapp:CTk):
        GUIManager.__set_window_resolution__(mainapp)
        GUIManager.__set_window_title__(mainapp, "WebApp Creator Tool")

    @staticmethod
    def __set_window_resolution__(mainapp):
        mainapp.geometry("600x500")

    @staticmethod
    def __set_window_title__(mainapp:CTk, title:str):
        mainapp.title(title)
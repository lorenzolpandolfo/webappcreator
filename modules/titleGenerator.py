from modules.application import Application

title = site_url.lower().replace("https://", "").replace("www", "").replace(".com", "").strip(".")[0].capitalize() if autoTitle else input("Título: ")
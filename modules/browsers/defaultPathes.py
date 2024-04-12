class DefaultBrowsersPathes:
    hash = {
        "Google Chrome" : r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "Firefox"       : r"C:\\Program Files\\Mozilla Firefox\\firefox.exe",
        "Chromium"      : r"C:\\Program Files\\Chromium\\Application\\chrome.exe"
    }

    @staticmethod
    def get_default_path(browser: str):
        path = DefaultBrowsersPathes.hash[browser]
        if path:
            return path

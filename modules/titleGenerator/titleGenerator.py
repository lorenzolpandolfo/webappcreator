
from modules.titleGenerator.sufixes  import Sufixes
from modules.titleGenerator.prefixes import Prefixes

BLANK_SPACE = ""

class TitleGenerator:
    @staticmethod
    def generateTitle(url) -> str:
        url = TitleGenerator.__cleaning_url_prefixes__(url)
        url = TitleGenerator.__cleaning_url_sufixes__(url)
        return url.capitalize()

    @staticmethod
    def __cleaning_url_sufixes__(url:str) -> str:
        for sufix in Sufixes.getAllCodes():
            if "." not in url: break
            if sufix in url:
                print(url)
                url = url.replace(sufix, BLANK_SPACE)
                print(url, sufix)
        return url
    
    @staticmethod
    def __cleaning_url_prefixes__(url:str) -> str:
        for prefix in Prefixes.getAllPrefixes():
            if "." not in url: break
            if prefix in url:
                url = url.replace(prefix, BLANK_SPACE)
        return url
    

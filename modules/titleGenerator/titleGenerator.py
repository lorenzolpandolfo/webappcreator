from modules.titleGenerator.sufixes import Sufixes
from modules.titleGenerator.prefixes import Prefixes
from modules.logManager.logManager import logger
BLANK_SPACE = ""


class TitleGenerator:
    @staticmethod
    def generate_title(url) -> str:
        logger.info("Generating title")
        url = TitleGenerator.__cleaning_url_prefixes__(url)
        url = TitleGenerator.__cleaning_url_sufixes__(url)
        title = url.capitalize()
        logger.info(f"Title generated: {title}")
        return title

    @staticmethod
    def __cleaning_url_sufixes__(url: str) -> str:
        for sufix in Sufixes.get_all_codes():
            if "." not in url: break
            if sufix in url:
                url = url.replace(sufix, BLANK_SPACE)
        return url

    @staticmethod
    def __cleaning_url_prefixes__(url: str) -> str:
        for prefix in Prefixes.get_all_prefixes():
            if "." not in url: break
            if prefix in url:
                url = url.replace(prefix, BLANK_SPACE)
        return url

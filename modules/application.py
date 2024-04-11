from dataclasses import dataclass

@dataclass
class Application:
    url           :str
    title         :str
    icon_path     :str
    browser_path  :str
    AUTO_TITLE    :bool = True

from dataclasses import dataclass


class Sufixes:
    countryCodes = [".br", ".us", ".jp", ".ca", ".au", ".de", ".uk", ".fr",
                    ".nl", ".it", ".ru", ".uk", ".nl", ".es", ".ch", ".cn",
                    ".kr", ".ar", ".co", ".cl", ".pe", ".ve", ".ec", ".kz"]
    
    genericCodes = [".org", ".net", ".com", ".edu", ".mil", ".info", ".biz",
                    ".co" , ".io" , ".me",  ".tv"]
    
    @staticmethod
    def get_all_codes():
        all_codes = Sufixes.genericCodes.copy()
        all_codes.extend(Sufixes.countryCodes)
        return all_codes

from dataclasses import dataclass

class Prefixes:
    all = ["https://", "http://"]

    @staticmethod
    def getAllPrefixes():
        return Prefixes.all
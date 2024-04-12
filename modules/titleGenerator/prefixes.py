from dataclasses import dataclass


class Prefixes:
    _all = ["https://", "http://", "www.", "web.", "chat."]

    @staticmethod
    def get_all_prefixes():
        return Prefixes._all

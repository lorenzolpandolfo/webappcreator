from dataclasses import dataclass


class Prefixes:
    _all = ["https://", "http://"]

    @staticmethod
    def get_all_prefixes():
        return Prefixes._all

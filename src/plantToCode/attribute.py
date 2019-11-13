from src.plantToCode.visibility import Visibility


class Attribute:
    def __init__(self, name: str, type_: str,
                 visibility: Visibility):
        self.name = name
        self.type_ = type_
        self.visibility = visibility

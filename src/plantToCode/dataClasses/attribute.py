from src.plantToCode.dataClasses.visibility import Visibility


class Attribute:
    def __init__(self, name: str, type_: str,
                 visibility: Visibility = Visibility.private):
        self.name = name
        self.type_ = type_
        self.visibility = visibility

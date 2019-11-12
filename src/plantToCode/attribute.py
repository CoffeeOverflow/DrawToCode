from src.plantToCode.visibility import Visibility


class Attribute:
    def __init__(self, name: str, type_: str,
                 visibility: Visibility):
        self.name = name
        self.type_ = type_
        self.visibility = visibility

    def __str__(self):
        return (f"{self.visibility.name} {self.type_}"
                f" {self.name}")

    def __repr__(self):
        return self.__str__

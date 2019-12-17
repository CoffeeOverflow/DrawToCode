from src.dataToCode.dataClasses.visibility import Visibility


class Attribute:
    def __init__(self, name: str, type_: str,
                 visibility: Visibility = Visibility.private):
        self.name = name
        self.type_ = type_
        self.visibility = visibility

    def __eq__(self, other: "Attribute"):
        cond1 = self.name == other.name
        cond2 = self.type_ == other.type_
        cond3 = self.visibility == other.visibility
        if cond1 and cond2 and cond3:
            result = True
        else:
            result = False
        return result

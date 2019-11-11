from visibility import Visibility


class Attribute:
    def __init__(self, name: str, attribute_type: str,
                 visibility: Visibility):
        self.name = name
        self.attribute_type = attribute_type
        self.visibility = visibility

    def __str__(self):
        return (f"{self.visibility.name} {self.attribute_type}"
                f" {self.name}")

    def __repr__(self):
        return self.__str__

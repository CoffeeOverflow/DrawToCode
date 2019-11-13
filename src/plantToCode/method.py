from src.plantToCode.visibility import Visibility
from src.plantToCode.modifier import Modifier
from src.plantToCode.attribute import Attribute
from typing import List


class Method:
    def __init__(self, name: str, 
                return_type: str = "void",
                parameters: List[Attribute] = [], 
                visibility: Visibility = Visibility.public,
                modifier: Modifier = Modifier.none):
                
        self.name = name
        self.return_type = return_type
        self.parameters = parameters
        self.visibility = visibility
        self.modifier = modifier

    def __str__(self):
        return (f"{self.visibility.name} "
                f"{self.__formatted_modifier()}" 
                f"{self.return_type} {self.name}"
                f"({self.__formatted_parameters()})")

    def __repr__(self):
        return self.__str__

    def __formatted_parameters(self) -> str:
        parameters = [f"{parameter.type_} {parameter.name}" 
                    for parameter in self.parameters]
        return ', '.join(parameters)

    def __formatted_modifier(self) -> str:
        return (f"{self.modifier.value}"
                f"{'' if self.modifier is Modifier.none else ' '}")

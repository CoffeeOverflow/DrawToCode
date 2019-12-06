from typing import List

from src.plantToCode.attribute import Attribute
from src.plantToCode.dataToCode.methodToCode import MethodToCode
from src.plantToCode.method import Method
from src.plantToCode.modifier import Modifier
from src.plantToCode.visibility import Visibility


class MethodToPython(MethodToCode):
    def __init__(self, methods: List[Method], is_from_interface: bool):
        self.methods = methods
        self.is_from_interface = is_from_interface

    def get_formatted_methods(self) -> str:
        methods_str_list = [f"\t{self.__convert_method(method) + self.__formatted_body()}"
                            for method in self.methods]
        return '\n\n'.join(methods_str_list)

    def __convert_method(self, method: Method) -> str:
        return (f"{self.__formatted_modifier(method)}"
                f"def {self.__formatted_visibility(method)}"
                f"{method.name}("
                f"{'self' if method.modifier is not Modifier.static else ''}"
                f"{', ' if method.parameters and method.modifier is not Modifier.static else ''}"
                f"{self.__formatted_parameters(method.parameters)}):")

    def __formatted_body(self) -> str:
        return "\n\t\tpass"

    def __formatted_parameters(self, parameters: List[Attribute]) -> str:
        parameters = [f"{parameter.name}"
                      for parameter in parameters]
        return ', '.join(parameters)

    def __formatted_visibility(self, method: Method) -> str:
        if method.visibility is Visibility.private:
            return "__"
        elif method.visibility is Visibility.protected:
            return "_"
        else:
            return ""

    def __formatted_modifier(self, method: Method) -> str:
        if method.modifier is Modifier.abstract or self.is_from_interface:
            return "@abstractmethod\n\t"
        elif method.modifier is Modifier.static:
            return "@staticmethod\n\t"
        else:
            return ""

from src.plantToCode.method import Method
from src.plantToCode.attribute import Attribute
from src.plantToCode.modifier import Modifier
from typing import List


class MethodToJava:
    def __init__(self, methods: List[Method], is_from_interface: bool = False):
        self.methods = methods
        self.is_from_interface = is_from_interface

    def __convert_method(self, method: Method) -> str:
        return (f"{method.visibility.name} "
                f"{method.modifier.value}"
                f"{'' if method.modifier is Modifier.none else ' '}"
                f"{method.return_type} {method.name}"
                f"({self.__formatted_parameters(method.parameters)})"
                f"{self.__formatted_body()}")

    def __formatted_body(self) -> str:
        if self.is_from_interface:
            return ";"
        else:
            return " {\n\t\tthrow new UnsupportedOperationException();\n\t}"

    def __formatted_parameters(self, parameters: List[Attribute]) -> str:
        parameters = [f"{parameter.type_} {parameter.name}"
                      for parameter in parameters]
        return ', '.join(parameters)

    def get_formatted_methods(self) -> str:
        methods_str_list = [f"\t{self.__convert_method(method)}"
                            for method in self.methods]
        return '\n\n'.join(methods_str_list)

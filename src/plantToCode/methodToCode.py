from src.plantToCode.method import Method
from src.plantToCode.attribute import Attribute
from src.plantToCode.modifier import Modifier
from typing import List


class MethodToCode:
    def __init__(self, methods: List[Method]):
        self.methods = methods

    def __convert_method(self, method: Method) -> str:
        return (f"{method.visibility.name} "
                f"{method.modifier.name}"
                f"{'' if method.modifier.name is Modifier.none else ' '}"
                f"{method.return_type} {method.name}"
                f"({self.__formatted_parameters(method.parameters)})")

    def __formatted_parameters(self, parameters: List[Attribute]) -> str:
        parameters = [f"{parameter.type_} {parameter.name}"
                      for parameter in parameters]
        return ', '.join(parameters)

    def get_formatted_methods(self) -> str:
        methods_str_list = [f"\t{self.__convert_method(method)};"
                            for method in self.methods]
        return '\n\n'.join(methods_str_list)
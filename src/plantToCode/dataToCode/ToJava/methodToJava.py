from src.plantToCode.dataToCode.methodToCode import MethodToCode
from src.plantToCode.method import Method
from src.plantToCode.attribute import Attribute
from src.plantToCode.modifier import Modifier
from typing import List


class MethodToJava(MethodToCode):
    def __init__(self, methods: List[Method], is_from_interface: bool):
        self.methods = methods
        self.is_from_interface = is_from_interface

    def __convert_method(self, method: Method) -> str:
        modifier_space = self.__get_modifier_space(method)
        modifier_value = self.__get_modifier_value(method)
        override_value = self.__get_override_value(method)

        return (f"{override_value}"
                f"{method.visibility.name} "
                f"{modifier_value}"
                f"{modifier_space}"
                f"{method.return_type} {method.name}"
                f"({self.__formatted_parameters(method.parameters)})")

    def __get_override_value(self, method):
        if method.modifier is Modifier.override:
            return f"@{method.modifier.value}\n\t"
        else:
            return ""

    def __get_modifier_value(self, method):
        if method.modifier is Modifier.override:
            return ''
        else:
            return method.modifier.value

    def __get_modifier_space(self, method):
        if method.modifier in [Modifier.none, Modifier.override]:
            return ''
        else:
            return " "

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
        methods_str_list = [f"\t{self.__convert_method(method) + self.__formatted_body()}"
                            for method in self.methods]
        return '\n\n'.join(methods_str_list)

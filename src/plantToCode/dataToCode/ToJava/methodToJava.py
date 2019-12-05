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
        
        if method.modifier in [Modifier.none, Modifier.override]:
            modifier_space = ''
        else:
            modifier_space = " "

        if method.modifier is Modifier.override:
            modifier_value = ''
            override_value = f"@{method.modifier.value}\n\t"
        else:
            modifier_value = method.modifier.value
            override_value = ""

        return (f"{override_value}"
                f"{method.visibility.name} "
                f"{modifier_value}"
                f"{modifier_space}"
                f"{method.return_type} {method.name}"
                f"({self.__formatted_parameters(method.parameters)})")

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

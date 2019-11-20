from src.plantToCode.classData import ClassData
from src.plantToCode.modifier import Modifier
from src.plantToCode.methodToCode import MethodToCode
from src.plantToCode.interfaceToCode import InterfaceToCode


class ClassToCode:

    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToCode(self.class_data.methods)

    def convert(self) -> str:
        return (f"{self.__formatted_class_header()}"
                f"{self.__formatted_fields()}\n\n"
                f"{self.method_to_code.get_formatted_methods()}\n"
                f"}}")

    def __formatted_class_header(self):
        return (f"{self.class_data.visibility.name} {self.class_data.modifier.value}"
                f"{'' if self.class_data.modifier is Modifier.none else ' '}"
                f"class {self.class_data.name}{self.__get_optional_inheritances()}"
                f"{InterfaceToCode.codeImplementedInterfaces(self.class_data.implementations)}"
                f" {{\n")

    def __get_optional_inheritances(self) -> str:
        if self.class_data.inheritances:
            return f" extends {self.__formatted_inheritances()}"
        else:
            return ''

    def __formatted_inheritances(self) -> str:
        inheritance_list = [f"{class_data.name}"
                            for class_data in self.class_data.inheritances]
        return ', '.join(inheritance_list)

    def __formatted_fields(self):
        class_fields = [f"\t{fields.visibility.value} {fields.type_} {fields.name};"
                        for fields in self.class_data.fields]
        return '\n'.join(class_fields)

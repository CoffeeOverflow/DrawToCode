from src.plantToCode.languages.classToCode import ClassToCode
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.modifier import Modifier
from src.plantToCode.languages.ToJava.methodToJava import MethodToJava
from src.plantToCode.languages.ToJava.interfaceToJava import InterfaceToJava
from src.plantToCode.languages.ToJava.inheritanceToJava import InheritanceToJava


class ClassToJava(ClassToCode):

    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToJava(self.class_data.methods, False)
        self.inheritance_to_code = InheritanceToJava(self.class_data.inheritances)

    def convert(self) -> str:
        return (f"import java.util.*;\n\n{self.__formatted_class_header()}\n"
                f"{self.__formatted_fields()}"
                f"{self.method_to_code.get_formatted_methods()}\n"
                f"}}")

    def __formatted_class_header(self):
        return (f"{self.class_data.visibility.name} {self.class_data.modifier.value}"
                f"{'' if self.class_data.modifier is Modifier.none else ' '}"
                f"class {self.class_data.name}{self.inheritance_to_code.get_formatted()}"
                f"{InterfaceToJava.codeImplementedInterfaces(self.class_data.implementations)}"
                f" {{\n")

    def __formatted_fields(self):
        if len(self.class_data.fields) > 0:
            class_fields = [f"\t{fields.visibility.value} {fields.type_} {fields.name};"
                        for fields in self.class_data.fields]

            return '\n'.join(class_fields) + \
                   ("\n\n" if self.class_data.methods else "")
        else:
            return ""

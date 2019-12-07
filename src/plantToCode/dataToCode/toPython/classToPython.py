from dataClasses.classData import ClassData
from dataClasses.modifier import Modifier
from dataToCode.classToCode import ClassToCode
from dataToCode.toPython.initToPython import InitToPython
from dataToCode.toPython.methodToPython import MethodToPython


class ClassToPython(ClassToCode):
    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToPython(self.class_data.methods, False)
        self.init_to_python = InitToPython(self.class_data.fields)

    def convert(self) -> str:
        return (f"{self.__formatted_imports()}"
                f"class {self.class_data.name}"
                f"({self.__formatted_inheritances()}):\n"
                f"{self.init_to_python.get_formatted()}\n"
                f"{self.method_to_code.get_formatted_methods()}\n")

    def __formatted_imports(self) -> str:
        inheritances = self.class_data.inheritances + self.class_data.implementations
        imports = [f"from {inheritance.name.lower()} import {inheritance.name}"
                   for inheritance in inheritances]
        return self.__optional_abc_import() + '\n'.join(imports) + '\n\n'

    def __optional_abc_import(self) -> str:
        for method in self.class_data.methods:
            if method.modifier is Modifier.abstract:
                return "from abc import ABC, abstractmethod\n"
        return ""

    def __formatted_inheritances(self) -> str:
        inheritances = self.class_data.inheritances + self.class_data.implementations
        inheritances_name = [f"{inheritance.name}"
                             for inheritance in inheritances]
        return ', '.join(inheritances_name)

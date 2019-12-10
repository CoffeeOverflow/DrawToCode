from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.modifier import Modifier
from src.plantToCode.dataToCode.classToCode import ClassToCode
from src.plantToCode.dataToCode.toPython.initToPython import InitToPython
from src.plantToCode.dataToCode.toPython.methodToPython import MethodToPython
from src.plantToCode.dataToCode.toPython.fileNameToPython import FileNameToPython

class ClassToPython(ClassToCode):
    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        all_methods = self.class_data.methods
        
        for implementation in self.class_data.implementations:
            for method in implementation.methods:
                if method not in all_methods:
                    all_methods.append(method)

        all_methods = list(all_methods)
        self.method_to_code = MethodToPython(all_methods, False)
        self.init_to_python = InitToPython(self.class_data.fields)

    def convert(self) -> str:
        return (f"{self.__formatted_imports()}"
                f"class {self.class_data.name}"
                f"({self.__formatted_inheritances()}):\n"
                f"\n{self.init_to_python.get_formatted()}\n"
                f"{self.method_to_code.get_formatted_methods()}\n")

    def __formatted_imports(self) -> str:
        inheritances = self.class_data.inheritances + self.class_data.implementations
        imports = [f"from {FileNameToPython(inheritance).get_file_name()[:-3]} import {inheritance.name}"
                   for inheritance in inheritances]
        space = '\n\n\n' if inheritances else ''
        return self.__optional_abc_import() + '\n'.join(imports) + space

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

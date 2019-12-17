from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.languages.interfaceToCode import InterfaceToCode
from src.dataToCode.languages.toPython.methodToPython import MethodToPython
from src.dataToCode.languages.toPython.fileNameToPython import FileNameToPython


class InterfaceToPython(InterfaceToCode):
    def __init__(self, interface: Interface):
        self.interface = interface
        self.method_to_code = MethodToPython(self.interface.methods, True)

    def convert(self) -> str:
        return (f"{self.__formatted_imports()}"
                f"class {self.interface.name}"
                f"({self.__formatted_inheritances()}):\n"
                f"\n{self.method_to_code.get_formatted_methods()}\n")

    def __formatted_imports(self) -> str:
        imports = [f"from {FileNameToPython(inheritance).get_file_name()[:-3]} import {inheritance.name}"
                   for inheritance in self.interface.interfaces]
        space = '\n\n\n' if self.interface.interfaces else '\n\n'
        return "from abc import ABC, abstractmethod\n" + '\n'.join(imports) + space

    def __formatted_inheritances(self) -> str:
        inheritances_name = [f"{interface.name}"
                             for interface in self.interface.interfaces]
        abstract_import = "ABC, " if self.interface.interfaces else "ABC"
        return abstract_import + ', '.join(inheritances_name)

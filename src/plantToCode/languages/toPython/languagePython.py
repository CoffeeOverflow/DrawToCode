from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.languages.languageInterface import LanguageInterface
from src.plantToCode.languages.toPython.classToPython import ClassToPython
from src.plantToCode.languages.toPython.interfaceToPython import InterfaceToPython
from src.plantToCode.languages.toPython.fileNameToPython import FileNameToPython
from typing import Union


class LanguagePython(LanguageInterface):

    def get_class_code(self, class_data: ClassData) -> str:
        class_python = ClassToPython(class_data)
        return class_python.convert()

    def get_interface_code(self, interface: Interface) -> str:
        interface_python = InterfaceToPython(interface)
        return interface_python.convert()

    def get_file_name(self, object_data: Union[ClassData, Interface]) -> str:
        file_name_to_python = FileNameToPython(object_data)
        return file_name_to_python.get_file_name()

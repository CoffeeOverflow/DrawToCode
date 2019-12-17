from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.languages.languageInterface import LanguageInterface
from src.plantToCode.languages.ToJava.classToJava import ClassToJava
from src.plantToCode.languages.ToJava.interfaceToJava import InterfaceToJava
from src.plantToCode.languages.ToJava.fileNameToJava import FileNameToJava
from typing import Union


class LanguageJava(LanguageInterface):

    def get_class_code(self, class_data: ClassData) -> str:
        class_java = ClassToJava(class_data)
        return class_java.convert()

    def get_interface_code(self, interface: Interface) -> str:
        interface_java = InterfaceToJava(interface)
        return interface_java.convert()

    def get_file_name(self, object_data: Union[ClassData, Interface]) -> str:
        file_name_to_java = FileNameToJava(object_data)
        return file_name_to_java.get_file_name()

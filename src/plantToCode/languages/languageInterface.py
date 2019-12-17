from abc import ABC, abstractmethod
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from typing import Union


class LanguageInterface(ABC):

    @abstractmethod
    def get_class_code(self, class_data: ClassData) -> str:
        pass

    @abstractmethod
    def get_interface_code(self, interface: Interface) -> str:
        pass

    @abstractmethod
    def get_file_name(self, object_data: Union[ClassData, Interface]) -> str:
        pass


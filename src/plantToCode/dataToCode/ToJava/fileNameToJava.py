from src.plantToCode.dataToCode.fileNameToCode import FileNameToCode
from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from typing import Union


class FileNameToJava(FileNameToCode):

    def __init__(self, object_data: Union[ClassData, Interface]):
        self.name = object_data.name

    def get_file_name(self) -> str:
        return f"{self.name}.java"

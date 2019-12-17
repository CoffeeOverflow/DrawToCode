from src.dataToCode.languages.fileNameToCode import FileNameToCode
from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from typing import Union


class FileNameToJava(FileNameToCode):

    def __init__(self, object_data: Union[ClassData, Interface]):
        self.name = object_data.name

    def get_file_name(self) -> str:
        return f"{self.name}.java"

from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.languages.fileNameToCode import FileNameToCode
from typing import Union
import re


class FileNameToPython(FileNameToCode):
    def __init__(self, data: Union[ClassData, Interface]):
        self.data = data

    def get_file_name(self) -> str:
        words = re.findall("[A-Z][^A-Z]*", self.data.name)
        formatted_name = '_'.join(words)
        return formatted_name.lower() + '.py'

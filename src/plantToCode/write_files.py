import os

from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataToCode.ToJava.languageJava import LanguageJava
from src.plantToCode.dataToCode.toPython.languagePython import LanguagePython
from src.plantToCode.dataToCode.languageInterface import LanguageInterface

from typing import List, Union


def write_files(objects: List[Union[ClassData, Interface]], 
                path: str, language: str) -> None:

    language_writer: LanguageInterface
    if language == "python":
        language_writer = LanguagePython()
    elif language == "java":
        language_writer = LanguageJava()
    else:
        raise ValueError("This language is not implemented")

    for element in objects:
        print(type(element))
        if type(element) == ClassData:
            source_code = language_writer.get_class_code(element)
        elif type(element) == Interface:
            source_code = language_writer.get_interface_code(element)
        else:
            raise ValueError(f"{type(element)} is not acceptable "
                             f"Use classData or interface")
        
        name = language_writer.get_file_name(element)
        element_file_path = os.path.join(path, name)
        
        with open(element_file_path, "w") as element_file:
            element_file.write(source_code)

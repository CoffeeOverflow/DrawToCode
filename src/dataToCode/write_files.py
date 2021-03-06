import os

from src.dataToCode.dataClasses.classData import ClassData
from src.dataToCode.dataClasses.interface import Interface
from src.dataToCode.languages.ToJava.languageJava import LanguageJava
from src.dataToCode.languages.toPython.languagePython import LanguagePython
from src.dataToCode.languages.languageInterface import LanguageInterface

from typing import List, Union


def select_language(language: str) -> LanguageInterface:
    language_writer: LanguageInterface
    if language == "python":
        language_writer = LanguagePython()
    elif language == "java":
        language_writer = LanguageJava()
    else:
        raise ValueError("This language is not implemented")
    return language_writer


def write_files(objects: List[Union[ClassData, Interface]], 
                path: str, language: str) -> None:

    print('\n')
    language_writer = select_language(language)
    for element in objects:
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

        print(f"'{name}' created")
    print('Done.')

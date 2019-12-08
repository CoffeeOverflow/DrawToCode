import os

from src.plantToCode.dataClasses.classData import ClassData
from src.plantToCode.dataClasses.interface import Interface
from src.plantToCode.dataToCode.toPython.classToPython import ClassToPython
from src.plantToCode.dataToCode.toPython.interfaceToPython import InterfaceToPython


def write_files(objects: list, path: str) -> None:
    for element in objects:
        if type(element) == ClassData:
            python_object = ClassToPython(element)
        elif type(element) == Interface:
            python_object = InterfaceToPython(element)
        else:
            raise ValueError(f"{type(python_object)} is not acceptable "
                             f"Use classData or interface")
        
        source_code = python_object.convert()
        name = element.name
        element_file_path = os.path.join(path, name)
        
        with open(element_file_path, "w") as element_file:
            element_file.write(source_code)

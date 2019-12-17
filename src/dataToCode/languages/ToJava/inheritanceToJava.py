from src.dataToCode.languages.inheritanceToCode import InheritanceToCode
from src.dataToCode.dataClasses.classData import ClassData


class InheritanceToJava(InheritanceToCode):
    def __init__(self, inheritances: [ClassData]):
        self.inheritances = inheritances

    def get_formatted(self) -> str:
        if self.inheritances:
            return f" extends {self.__formatted_names()}"
        else:
            return ''

    def __formatted_names(self) -> str:
        inheritance_list = [f"{class_data.name}"
                            for class_data in self.inheritances]
        return ', '.join(inheritance_list)

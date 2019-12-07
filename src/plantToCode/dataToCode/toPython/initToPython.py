from typing import List
from dataClasses.attribute import Attribute
from dataToCode.toPython.visibilityToPython import visibility_to_python


class InitToPython:
    def __init__(self, class_fields: List[Attribute]):
        self.class_fields = class_fields

    def get_formatted(self) -> str:
        pass_ = '\t\tpass'
        return (f"\tdef __init__(self" + self.__formatted_parameters() + "):\n"
                f"{self.__formatted_assignments() if self.class_fields else pass_}\n")

    def __formatted_parameters(self) -> str:
        fields_name = [f"{field.name}"
                       for field in self.class_fields]
        return f", {', '.join(fields_name)}" if self.class_fields else ""

    def __formatted_assignments(self) -> str:
        class_fields = [f"\t\tself.{visibility_to_python[field.visibility]}"
                        f"{field.name} = {field.name}"
                        for field in self.class_fields]
        return '\n'.join(class_fields)
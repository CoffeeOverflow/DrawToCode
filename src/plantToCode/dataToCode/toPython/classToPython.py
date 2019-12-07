from classData import ClassData
from dataToCode.classToCode import ClassToCode
from dataToCode.toPython.initToPython import InitToPython
from dataToCode.toPython.methodToPython import MethodToPython


class ClassToPython(ClassToCode):
    def __init__(self, class_data: ClassData):
        self.class_data = class_data
        self.method_to_code = MethodToPython(self.class_data.methods, False)
        self.init_to_python = InitToPython(self.class_data.fields)

    def convert(self) -> str:
        return (f"class {self.class_data.name}"
                f"({self.__formatted_inheritances()}):\n"
                f"{self.init_to_python.get_formatted()}\n"
                f"{self.method_to_code.get_formatted_methods()}")

    def __formatted_inheritances(self) -> str:
        inheritances = self.class_data.inheritances + self.class_data.implementations
        inheritances_name = [f"{inheritance.name}"
                             for inheritance in inheritances]
        return ', '.join(inheritances_name)
